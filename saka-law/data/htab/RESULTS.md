# HTAB v0 — first results

Date: 26 September 2026. Universe, windows and estimation rules were frozen in `UNIVERSE.md` (commit `8f613fc`) before the data were retrieved. This is a pilot, not the preregistration of paper §17.

Reproduce:

```
python src/build_raw.py      # snapshots -> raw.csv + verification.txt
python src/build_htab.py     # results/htab_domains.csv, htab_aggregate.csv, htab_sensitivity.csv
python src/calculate_tar.py  # results/tar_domains.csv, tar_aggregate.csv
python src/coverage_check.py # interval coverage simulation
```

Requires Python 3 with numpy and scipy.

## Headline

**In the five fast domains, the current rate of progress (2016 onward) is not faster than the historical baseline. It is slower.**

- Aggregate TAR over the five fast series = **0.53** (bootstrap 90%: 0.48–0.59); $\Delta k$ = −0.20 per year (90%: −0.23 to −0.17).
- Three series decelerated clearly (genome sequencing cost, fastest supercomputer, DRAM price). Two show no clear change (transistors per chip, solar PV module cost).
- No series shows acceleration.

The decelerations survive every check below, including doubling the width of the sensitivity intervals.

This is **not** evidence against the recursive-acceleration hypothesis as stated in the paper, for the reasons in "How to read this". It is evidence that the classic frontier technologies that usually illustrate "exponential progress" were not in an accelerating regime in 2016–2025.

## Per-domain baseline (historical window)

$k$ in log units per year; for costs, positive $k$ means falling cost. Interval method: Newey–West HAC t interval (preregistered). "AR(1) 90%" is the sensitivity interval described under "Uncertainty".

| Series | Role | Window | n | k | 90% (NW) | AR(1) 90% | Doubling / halving |
|---|---|---|---|---|---|---|---|
| genome | fast | 2001–2015 | 15 | 0.599 | 0.487–0.712 | 0.483–0.716 | 1.2 y |
| transistors | fast | 1986–2014 | 27 | 0.374 | 0.360–0.389 | 0.356–0.393 | 1.9 y |
| supercomputer | fast | 1993–2015 | 23 | 0.630 | 0.604–0.655 | 0.605–0.654 | 1.1 y |
| dram | fast | 1986–2015 | 30 | 0.457 | 0.427–0.487 | 0.407–0.507 | 1.5 y |
| pv | fast | 1986–2015 | 30 | 0.089 | 0.063–0.115 | 0.064–0.113 | 7.8 y |
| ag_tfp | control | 1986–2015 | 30 | 0.016 | 0.015–0.016 | 0.015–0.017 | 44 y |
| wheat | control | 1986–2014 | 29 | 0.012 | 0.011–0.013 | 0.011–0.013 | 59 y |
| us_tfp | control | 1986–2015 | 30 | 0.013 | 0.012–0.014 | 0.011–0.014 | 55 y |

Aggregates (equal weights, block bootstrap):

| Aggregate | $k_{HTAB}$ | 90% | Doubling / halving |
|---|---|---|---|
| fast (5) | 0.430 | 0.407–0.452 | 1.6 y |
| control (3) | 0.013 | 0.013–0.014 | 52 y |
| all (8) | 0.274 | 0.259–0.288 | 2.5 y |

The fast and control groups differ by a factor of about 30. An "all-technology" baseline is therefore mostly a statement about which series were chosen; the per-domain table is the meaningful output, as expected.

Sanity checks against well-known figures: transistors doubling every ~1.9 years is Moore's law; the TOP500 #1 system grew ~1.9× per year until the mid-2010s; control productivity grew 1.2–1.6% per year.

## TAR and Δk (current window 2016 → last year)

| Series | Current window | n | $k_{current}$ | $\Delta k$ | $\Delta k$ 90% (bootstrap) | $\Delta k$ 90% (AR(1)) | TAR | TAR 90% | Reading |
|---|---|---|---|---|---|---|---|---|---|
| genome | 2016–2022 | 7 | 0.175 | −0.424 | −0.547 to −0.301 | −0.581 to −0.267 | 0.29 | 0.19–0.41 | deceleration |
| transistors | 2016–2021 | 6 | 0.363 | −0.011 | −0.064 to 0.038 | −0.109 to 0.087 | 0.97 | 0.83–1.10 | no clear change |
| supercomputer | 2016–2025 | 10 | 0.387 | −0.243 | −0.291 to −0.197 | −0.300 to −0.186 | 0.61 | 0.54–0.69 | deceleration |
| dram | 2016–2023 | 8 | 0.115 | −0.342 | −0.395 to −0.292 | −0.446 to −0.239 | 0.25 | 0.15–0.34 | deceleration |
| pv | 2016–2024 | 9 | 0.108 | +0.020 | −0.003 to 0.044 | −0.017 to 0.057 | 1.22 | 0.97–1.60 | no clear change |

The three controls have no current-window data (their archived sources end in 2014–2019), so they contribute to the baseline only.

"Reading" is identical under both interval methods for every series.

## Uncertainty: a problem found in the preregistered method

A simulation (`src/coverage_check.py`, results in `results/coverage_check.csv`) tested the preregistered Newey–West intervals on synthetic trends with AR(1) noise and a known slope. They are **too narrow** at these sample sizes:

| n | Autocorrelation | Coverage of nominal 90%: Newey–West | Coverage: AR(1)-exact |
|---|---|---|---|
| 7 | 0.0 | 73% | 85% |
| 7 | 0.5 | 57% | 71% |
| 10 | 0.5 | 61% | 75% |
| 30 | 0.0 | 81% | 90% |
| 30 | 0.5 | 71% | 85% |
| 30 | 0.8 | 53% | 73% |

The implementation was checked against statsmodels and gives identical standard errors, so this is a property of the method in short samples, not a bug. The moving-block bootstrap used for aggregates has similar under-coverage.

Response, declared as a deviation from `UNIVERSE.md`:

1. The preregistered method remains the primary analysis and is reported unchanged.
2. A sensitivity interval was added *after* seeing this simulation (but the coverage test uses synthetic data only): the exact OLS slope variance under AR(1) errors, with the residual autocorrelation bias-corrected by $(2+4\rho)/n$. It is better calibrated but still too narrow when autocorrelation is high.
3. A reading counts as robust only if both methods agree. They agree for all five series.
4. **Stress test:** even if the AR(1) intervals are doubled in width, the three decelerations still exclude zero (genome ≈ −0.74 to −0.11; supercomputer ≈ −0.36 to −0.13; DRAM ≈ −0.55 to −0.14). The two "no clear change" readings are unaffected.

All intervals in this file, especially the narrow aggregate intervals, should be read as optimistic. For v1, inference should use longer windows, fixed-b critical values or a hierarchical model across series.

## Other sensitivity checks

- **Genome break dummy.** Without the preregistered 2008 level shift, historical $k$ is 0.90 (90%: 0.80–1.00) instead of 0.60, so the deceleration would be larger. The primary analysis is the conservative one.
- **PV source.** The git-archived Lafond et al. vintage (different source and dollar base) gives a historical $k$ of 0.083 (90%: 0.057–0.109), close to 0.089. It has only 4 current-window years, so no TAR.
- **Data verification.** Genome values match the 2022 git-archived OWID vintage in all 21 overlapping years. Transistors match in 21 of 23; the two differences (2002–2003) are a data revision in the source, not transcription errors. Supercomputer values were spot-checked against known TOP500 #1 systems. DRAM values could not be checked against an independent vintage. See `verification.txt`.

## How to read this

1. **These are mature frontier technologies.** The paper's hypothesis is about technology improving the *process* of discovery. The HTAB series measure products (chips, sequencers, panels), several of which are known to be approaching physical or economic limits (the end of Dennard scaling, DRAM cell scaling, the sequencing cost plateau). Deceleration here is expected under both the hypothesis and its negation.
2. **The current window is early.** Most current-window data end in 2021–2024. Any effect of AI-driven research, which the paper dates mainly to 2024–2026, is at most one or two data points in these series.
3. **AI itself is not in the HTAB.** Training compute, algorithmic efficiency and task horizons are the $A$ and $C$ components of FTAF, not historical baselines. Measuring their growth rate is a separate step.
4. **What the result does say.** The widespread impression that "everything is accelerating" is not supported for these five classic domains in 2016–2025. If recursive acceleration is real, it has to show up first somewhere else—in AI capability, in scientific cycle time, or in clinical translation—and later propagate to domains like these. That makes the controls and the $L$ component more important, not less.
5. **Controls also slowed.** Before 1986, US TFP grew 2.1% per year and world wheat yields 2.7% per year; after 1986, 1.3% and 1.2%. Agricultural TFP is the exception (0.4% → 1.6%). This matches the "ideas are getting harder to find" literature cited in the paper.

## Deviations from UNIVERSE.md

- Added the AR(1)-exact sensitivity interval and the robustness rule (see "Uncertainty").
- The universe itself was not changed: 5 fast and 3 control series, as frozen.

## Next steps

- Add the deferred series, especially the Eroom's-law control (drugs per R&D dollar) and battery cost.
- Extend the controls past 2019 so they have current-window data.
- Compute growth rates for the AI components ($A$, $C$) with the same code.
- Replace the interval method as described above before any preregistered test.
