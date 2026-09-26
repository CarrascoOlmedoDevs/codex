"""Technology Acceleration Ratio (TAR) and Δk for HTAB v0.

For each series with at least MIN_CURRENT_OBS observations in the current
window (2016 onward):
  TAR_i = k_current / k_historical   (only if the 90% interval of k_historical
                                      excludes 0; otherwise undefined)
  Δk_i  = k_current - k_historical   (always reported)
Intervals: moving-block bootstrap, windows resampled independently.
Aggregate TAR = mean k_current / mean k_historical over series with defined
TAR, equal weights, bootstrap interval.

Usage: python src/calculate_tar.py
"""

import numpy as np
from scipy import stats

from build_htab import write
from htab_lib import (ANALYSIS_START, CURRENT_START, HIST_END, LEVELS,
                      MIN_CURRENT_OBS, OUTDIR, SEED, ar1_exact_se,
                      block_bootstrap_k, fit_window, fmt, load_raw, t_interval)


def pct(a, lv):
    return np.percentile(a, [50 - lv * 50, 50 + lv * 50])


def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    series = load_raw()
    order = ["genome", "transistors", "supercomputer", "dram", "pv",
             "ag_tfp", "wheat", "us_tfp"]
    rng = np.random.default_rng(SEED + 1)

    rows, boot_h, boot_c, defined = [], {}, {}, []
    for sid in order:
        s = series[sid]
        start = max(ANALYSIS_START, int(s.years.min()))
        h = fit_window(s, start, HIST_END)
        c = fit_window(s, CURRENT_START, int(s.years.max()))
        row = dict(series_id=sid, role=s.role,
                   historical_window=f"{h['start']}-{h['end']}",
                   k_historical=fmt(h["k"]))
        if c is None or c["n"] < MIN_CURRENT_OBS:
            n_c = 0 if c is None else c["n"]
            row |= dict(current_window="", n_current=n_c,
                        note=f"not computed: {n_c} current observations (< {MIN_CURRENT_OBS})")
            rows.append(row)
            continue
        bh, bc = block_bootstrap_k(h, rng), block_bootstrap_k(c, rng)
        boot_h[sid], boot_c[sid] = bh, bc
        lo90, hi90 = t_interval(h["k"], h["se"], h["df"], 0.90)
        tar_defined = lo90 > 0 or hi90 < 0
        dk = c["k"] - h["k"]
        row |= dict(current_window=f"{c['start']}-{c['end']}", n_current=c["n"],
                    k_current=fmt(c["k"]), delta_k=fmt(dk))
        dkb = bc - bh
        for lv in LEVELS:
            lo, hi = pct(dkb, lv)
            row[f"delta_k_ci{int(lv*100)}_low"], row[f"delta_k_ci{int(lv*100)}_high"] = fmt(lo), fmt(hi)
        if tar_defined:
            defined.append(sid)
            row["tar"] = fmt(c["k"] / h["k"], 3)
            tb = bc / bh
            for lv in LEVELS:
                lo, hi = pct(tb, lv)
                row[f"tar_ci{int(lv*100)}_low"], row[f"tar_ci{int(lv*100)}_high"] = fmt(lo, 3), fmt(hi, 3)
        else:
            row["tar"] = "undefined"
        lo90d, hi90d = pct(dkb, 0.90)
        row["reading_90"] = ("acceleration" if lo90d > 0 else
                             "deceleration" if hi90d < 0 else "no clear change")
        # Sensitivity (not preregistered): AR(1)-exact SEs, windows independent.
        seh, _ = ar1_exact_se(h)
        sec, _ = ar1_exact_se(c)
        se_dk = (seh ** 2 + sec ** 2) ** 0.5
        q = stats.t.ppf(0.95, min(h["df"], c["df"]))
        row["sens_ar1_delta_k_ci90_low"] = fmt(dk - q * se_dk)
        row["sens_ar1_delta_k_ci90_high"] = fmt(dk + q * se_dk)
        row["sens_ar1_reading_90"] = ("acceleration" if dk - q * se_dk > 0 else
                                      "deceleration" if dk + q * se_dk < 0 else "no clear change")
        lo_h, hi_h = t_interval(h["k"], seh, h["df"], 0.90)
        row["sens_ar1_tar_defined"] = int(lo_h > 0 or hi_h < 0)
        row["robust_reading"] = (row["reading_90"] if row["reading_90"] == row["sens_ar1_reading_90"]
                                 else "not robust")
        rows.append(row)
    write(OUTDIR / "tar_domains.csv", rows)

    kh = np.mean([fit_window(series[i], max(ANALYSIS_START, int(series[i].years.min())), HIST_END)["k"] for i in defined])
    kc = np.mean([fit_window(series[i], CURRENT_START, int(series[i].years.max()))["k"] for i in defined])
    bh = np.column_stack([boot_h[i] for i in defined]).mean(axis=1)
    bc = np.column_stack([boot_c[i] for i in defined]).mean(axis=1)
    agg = dict(aggregate="fast series with defined TAR", series=";".join(defined),
               k_historical=fmt(kh), k_current=fmt(kc), tar=fmt(kc / kh, 3),
               delta_k=fmt(kc - kh))
    for lv in LEVELS:
        lo, hi = pct(bc / bh, lv)
        agg[f"tar_ci{int(lv*100)}_low"], agg[f"tar_ci{int(lv*100)}_high"] = fmt(lo, 3), fmt(hi, 3)
        lo, hi = pct(bc - bh, lv)
        agg[f"delta_k_ci{int(lv*100)}_low"], agg[f"delta_k_ci{int(lv*100)}_high"] = fmt(lo), fmt(hi)
    write(OUTDIR / "tar_aggregate.csv", [agg])

    print("Per-series TAR and Δk:")
    for r in rows:
        if "k_current" in r:
            print(f"  {r['series_id']:14s} hist {r['historical_window']} k={r['k_historical']:>7s} | "
                  f"cur {r['current_window']} k={r['k_current']:>7s} | Δk={r['delta_k']:>7s} "
                  f"90% [{r['delta_k_ci90_low']}, {r['delta_k_ci90_high']}] | TAR={r['tar']} "
                  f"[{r.get('tar_ci90_low','')}, {r.get('tar_ci90_high','')}] -> {r['reading_90']} "
                  f"| AR1 [{r['sens_ar1_delta_k_ci90_low']}, {r['sens_ar1_delta_k_ci90_high']}] -> {r['sens_ar1_reading_90']} "
                  f"| robust: {r['robust_reading']}")
        else:
            print(f"  {r['series_id']:14s} {r['note']}")
    print(f"Aggregate TAR ({agg['series']}): {agg['tar']} 90% [{agg['tar_ci90_low']}, {agg['tar_ci90_high']}]; "
          f"Δk={agg['delta_k']} 90% [{agg['delta_k_ci90_low']}, {agg['delta_k_ci90_high']}]")


if __name__ == "__main__":
    main()
