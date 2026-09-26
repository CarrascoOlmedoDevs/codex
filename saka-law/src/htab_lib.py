"""Shared estimation code for HTAB v0 (rules frozen in data/htab/UNIVERSE.md).

- Derived layer: y(t) = ln X(t), X(t) = V(t)/V(t0), inverted for lower_is_better.
- k = OLS slope of y on year (log units per year), optional level-shift dummies
  for preregistered methodology breaks.
- SE: Newey-West HAC, lag L = floor(4 (n/100)^(2/9)), minimum 1.
- Intervals: t distribution with n - p degrees of freedom.
- Bootstrap: moving-block bootstrap of residuals, block length L + 1.
"""

import csv
import math
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "htab" / "raw.csv"
OUTDIR = ROOT / "data" / "htab" / "results"

ANALYSIS_START = 1986
HIST_END = 2015
CURRENT_START = 2016
MIN_CURRENT_OBS = 5
LEVELS = (0.80, 0.90, 0.95)
N_BOOT = 10_000
SEED = 20260926


@dataclass
class Series:
    series_id: str
    role: str
    domain: str
    metric: str
    unit: str
    direction: str
    years: np.ndarray
    values: np.ndarray
    breaks: list = field(default_factory=list)

    def y(self):
        """Log of the value, signed so that improvement is positive."""
        ly = np.log(self.values)
        return -ly if self.direction == "lower_is_better" else ly

    def window(self, start, end):
        m = (self.years >= start) & (self.years <= end)
        return self.years[m], self.y()[m]


def load_raw(path=RAW):
    rows = list(csv.DictReader(open(path, newline="")))
    by_id = {}
    for r in rows:
        by_id.setdefault(r["series_id"], []).append(r)
    out = {}
    for sid, rs in by_id.items():
        rs.sort(key=lambda r: int(r["year"]))
        r0 = rs[0]
        out[sid] = Series(
            series_id=sid, role=r0["role"], domain=r0["domain"], metric=r0["metric"],
            unit=r0["unit"], direction=r0["direction"],
            years=np.array([int(r["year"]) for r in rs]),
            values=np.array([float(r["value"]) for r in rs]),
            breaks=[int(r["year"]) for r in rs if r["methodology_break"] == "1"],
        )
    return out


def hac_lag(n):
    return max(1, int(math.floor(4 * (n / 100) ** (2 / 9))))


def design(years, breaks):
    cols = [np.ones_like(years, dtype=float), years.astype(float) - years.min()]
    used = []
    for b in breaks:
        d = (years >= b).astype(float)
        if 0 < d.sum() < len(d):  # break inside the window
            cols.append(d)
            used.append(b)
    return np.column_stack(cols), used


def ols_hac(years, y, breaks=()):
    """Return dict with slope k, HAC SE, residuals, fitted, lag, df, breaks used."""
    X, used = design(years, breaks)
    n, p = X.shape
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    fitted = X @ beta
    resid = y - fitted
    L = hac_lag(n)
    XtX_inv = np.linalg.inv(X.T @ X)
    u = X * resid[:, None]
    S = u.T @ u
    for lag in range(1, L + 1):
        w = 1 - lag / (L + 1)
        G = u[lag:].T @ u[:-lag]
        S += w * (G + G.T)
    cov = XtX_inv @ S @ XtX_inv * n / max(n - p, 1)
    se = math.sqrt(max(cov[1, 1], 0.0))
    return dict(k=float(beta[1]), se=se, resid=resid, fitted=fitted, lag=L,
                df=n - p, n=n, breaks_used=used, X=X)


def t_interval(k, se, df, level):
    if df <= 0:
        return (float("nan"), float("nan"))
    q = stats.t.ppf(0.5 + level / 2, df)
    return (k - q * se, k + q * se)


def block_bootstrap_k(fit, rng, n_boot=N_BOOT):
    """Moving-block bootstrap of residuals; returns array of bootstrap slopes."""
    resid, fitted, X = fit["resid"], fit["fitted"], fit["X"]
    n = len(resid)
    b = min(fit["lag"] + 1, n)
    starts_max = n - b + 1
    n_blocks = math.ceil(n / b)
    XtX_inv_Xt = np.linalg.pinv(X)
    ks = np.empty(n_boot)
    for i in range(n_boot):
        starts = rng.integers(0, starts_max, size=n_blocks)
        e = np.concatenate([resid[s:s + b] for s in starts])[:n]
        ystar = fitted + e
        ks[i] = (XtX_inv_Xt @ ystar)[1]
    return ks


def fit_window(s, start, end, use_breaks=True):
    yrs, y = s.window(start, end)
    if len(yrs) < 3:
        return None
    fit = ols_hac(yrs, y, s.breaks if use_breaks else ())
    fit["start"], fit["end"] = int(yrs.min()), int(yrs.max())
    return fit


def doubling_time(k):
    return math.log(2) / abs(k) if k != 0 else float("inf")


def ar1_exact_se(fit):
    """Sensitivity SE (not preregistered): exact OLS slope variance under AR(1)
    errors, with the residual autocorrelation bias-corrected by (2 + 4 rho)/n.
    Added after simulations showed that Newey-West intervals under-cover badly
    in windows of 6-30 observations (see RESULTS.md)."""
    X, r = fit["X"], fit["resid"]
    n = len(r)
    P = np.linalg.pinv(X)
    rho = float(np.dot(r[1:], r[:-1]) / np.dot(r, r))
    rho = float(np.clip(rho + (2 + 4 * rho) / n, -0.9, 0.97))
    s2 = float(np.dot(r, r) / max(n - X.shape[1], 1))
    i = np.arange(n)
    S = s2 * rho ** np.abs(i[:, None] - i[None, :])
    return math.sqrt(max((P @ S @ P.T)[1, 1], 0.0)), rho


def fmt(x, nd=4):
    if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))):
        return ""
    return f"{x:.{nd}f}"
