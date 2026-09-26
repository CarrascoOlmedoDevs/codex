"""Build the Historical Technology Acceleration Baseline (HTAB v0).

Outputs (data/htab/results/):
  htab_domains.csv  per-series k for the historical window, full sample and
                    pre-1986 context, with SE, 80/90/95% intervals,
                    doubling/halving time, model and n
  htab_aggregate.csv  k_HTAB for fast, control and all series, with
                    bootstrap intervals
Also runs the sensitivity analyses listed in RESULTS.md.

Usage: python src/build_htab.py
"""

import csv

import numpy as np

from htab_lib import (ANALYSIS_START, HIST_END, LEVELS, N_BOOT, OUTDIR, SEED,
                      ar1_exact_se, block_bootstrap_k, doubling_time,
                      fit_window, fmt, load_raw, t_interval)


def domain_row(s, fit, window_name):
    row = dict(series_id=s.series_id, role=s.role, domain=s.domain,
               metric=s.metric, direction=s.direction, window=window_name)
    if fit is None:
        return row | dict(n_observations=0)
    row |= dict(
        historical_window=f"{fit['start']}-{fit['end']}",
        k=fmt(fit["k"]), se_k=fmt(fit["se"]),
    )
    for lv in LEVELS:
        lo, hi = t_interval(fit["k"], fit["se"], fit["df"], lv)
        row[f"ci{int(lv*100)}_low"], row[f"ci{int(lv*100)}_high"] = fmt(lo), fmt(hi)
    row["doubling_or_halving_years"] = fmt(doubling_time(fit["k"]), 2)
    se_ar1, rho = ar1_exact_se(fit)
    lo, hi = t_interval(fit["k"], se_ar1, fit["df"], 0.90)
    row["sens_ar1_se"], row["sens_ar1_ci90_low"], row["sens_ar1_ci90_high"] = fmt(se_ar1), fmt(lo), fmt(hi)
    row["residual_rho_corrected"] = fmt(rho, 3)
    row["model"] = "OLS ln X ~ year" + (
        " + level shift " + ",".join(map(str, fit["breaks_used"])) if fit["breaks_used"] else "")
    row["hac_lag"] = fit["lag"]
    row["n_observations"] = fit["n"]
    return row


def aggregate(series, fits, rng, label, ids):
    ks = np.array([fits[i]["k"] for i in ids])
    boots = np.column_stack([block_bootstrap_k(fits[i], rng) for i in ids])
    agg = boots.mean(axis=1)
    row = dict(aggregate=label, n_series=len(ids), series=";".join(ids),
               k_htab=fmt(ks.mean()))
    for lv in LEVELS:
        lo, hi = np.percentile(agg, [50 - lv * 50, 50 + lv * 50])
        row[f"ci{int(lv*100)}_low"], row[f"ci{int(lv*100)}_high"] = fmt(lo), fmt(hi)
    row["doubling_or_halving_years"] = fmt(doubling_time(ks.mean()), 2)
    return row


def write(path, rows):
    fields = []
    for r in rows:
        for k in r:
            if k not in fields:
                fields.append(k)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    series = load_raw()
    order = ["genome", "transistors", "supercomputer", "dram", "pv",
             "ag_tfp", "wheat", "us_tfp"]
    rng = np.random.default_rng(SEED)

    rows, hist = [], {}
    for sid in order:
        s = series[sid]
        start = max(ANALYSIS_START, int(s.years.min()))
        hist[sid] = fit_window(s, start, HIST_END)
        rows.append(domain_row(s, hist[sid], "historical"))
        rows.append(domain_row(s, fit_window(s, start, int(s.years.max())), "full_sample"))
        if s.years.min() < ANALYSIS_START:
            rows.append(domain_row(s, fit_window(s, int(s.years.min()), ANALYSIS_START - 1),
                                   "pre_1986_context"))
    write(OUTDIR / "htab_domains.csv", rows)

    fast = [i for i in order if series[i].role == "fast"]
    ctrl = [i for i in order if series[i].role == "control"]
    agg = [aggregate(series, hist, rng, "fast", fast),
           aggregate(series, hist, rng, "control", ctrl),
           aggregate(series, hist, rng, "all", order)]
    write(OUTDIR / "htab_aggregate.csv", agg)

    # Sensitivity: genome without the preregistered 2008 break dummy.
    s = series["genome"]
    nb = fit_window(s, int(s.years.min()), HIST_END, use_breaks=False)
    sens = [domain_row(s, nb, "historical_no_break_dummy")]
    write(OUTDIR / "htab_sensitivity.csv", sens)

    print("Per-series historical k (log units / year):")
    for r in rows:
        if r["window"] == "historical":
            print(f"  {r['series_id']:14s} {r['historical_window']:10s} k={r['k']:>8s} "
                  f"90% [{r['ci90_low']}, {r['ci90_high']}]  t2={r['doubling_or_halving_years']}y  n={r['n_observations']}")
    print("Aggregates:")
    for r in agg:
        print(f"  {r['aggregate']:8s} k_HTAB={r['k_htab']}  90% [{r['ci90_low']}, {r['ci90_high']}]")
    print("Sensitivity genome without break dummy:", sens[0]["k"], sens[0]["ci90_low"], sens[0]["ci90_high"])


if __name__ == "__main__":
    main()
