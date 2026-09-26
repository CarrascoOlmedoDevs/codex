# HTAB universe v0 — frozen before analysis

Frozen: 26 September 2026, in the commit that adds this file, before any series except one (see "Disclosure") was downloaded or inspected. Any later change to this file must be made in a separate commit whose message explains the change, and results must then be reported both with the original and with the changed universe.

## Purpose

First empirical Historical Technology Acceleration Baseline (HTAB, paper §5) and first Technology Acceleration Ratio (TAR, paper §6). This is **v0**: a pilot with data that can be retrieved reproducibly today. It is not the preregistration of paper §17.

## Series

Roles: **fast** = domains chosen because they are known to have improved rapidly (the usual evidence for acceleration); **control** = domains expected to improve slowly, included to counter selection bias.

| id | Role | Domain | Metric | Entity | Direction | Source (retrieval) | Available years |
|---|---|---|---|---|---|---|---|
| genome | fast | Genomics | Cost of sequencing a full human genome (USD, nominal) | World | lower_is_better | NHGRI via Our World in Data grapher `cost-of-sequencing-a-full-human-genome` | 2001–2022 |
| transistors | fast | Semiconductors | Transistors per microprocessor | World | higher_is_better | Rupp & Horowitz via OWID grapher `transistors-per-microprocessor` | 1971–2021 |
| supercomputer | fast | Compute | Computational capacity of the fastest supercomputer (FLOP/s, TOP500 Rmax) | World | higher_is_better | TOP500 via OWID grapher `supercomputer-power-flops` | 1993–2025 |
| dram | fast | Memory | Price of memory (DRAM), USD per TB, nominal | World | lower_is_better | McCallum via OWID grapher `historical-cost-of-computer-memory-and-storage`, column `Memory` | 1956–2023 |
| pv | fast | Energy | Solar PV module cost (USD/W, constant USD) | World | lower_is_better | Nemet / IRENA via OWID grapher `solar-pv-prices` | 1975–2024 |
| ag_tfp | control | Agriculture | Agricultural total factor productivity index | World | higher_is_better | USDA ERS via `owid/owid-datasets` (git), column `tfp` | 1961–2019 |
| wheat | control | Agriculture | Wheat yield (t/ha) | World | higher_is_better | FAO via `owid/owid-datasets` (git) | 1961–2014 |
| us_tfp | control | Whole economy | Total factor productivity, United States | United States | higher_is_better | Bergeaud, Cette & Lecat (2016) via `owid/owid-datasets` (git) | 1800–2016 |

Year ranges come from file headers only; values were not inspected when choosing (except genome, see "Disclosure").

### Deferred (not in v0), with reason

| Planned series | Reason deferred |
|---|---|
| Battery cost per kWh | No machine-readable source reachable from this environment (OWID chart returned 403/404). |
| Launch cost per kg to LEO | Available source is per launch vehicle, not an annual series; needs its own estimation method. |
| Drugs approved per R&D dollar (Eroom's law control) | Requires combining FDA approvals with R&D spending; no reachable machine-readable source. |
| Construction productivity (control) | No reachable machine-readable source. |
| Telecommunications bandwidth / cost, industrial robot density | No reachable machine-readable source. |

Deferring the batteries and launch series removes two fast domains; deferring the drug and construction series removes two controls. The v0 universe therefore has 5 fast and 3 control series.

## Windows

- Analysis start: 1986, or the first year of the series if later (genome: 2001; supercomputer: 1993).
- **Historical window:** start → 2015.
- **Current window:** 2016 → last available year. TAR is computed only if the current window has at least 5 observations. Controls ending before 2021 (ag_tfp, wheat, us_tfp) therefore contribute to HTAB but not to TAR.
- Also reported: full-sample k (start → last year) and pre-1986 k where data exist, as context only.

## Transformation

Raw values are stored unchanged in `raw.csv`. The derived layer is

$$X_i(t) = V_i(t)/V_i(t_0)$$

(or $V_i(t_0)/V_i(t)$ for lower_is_better), and $y_i(t) = \ln X_i(t)$.

## Estimation

- $k_i$ = slope of OLS regression of $y_i(t)$ on year, in log units per year.
- Standard error: Newey–West HAC with lag $L = \lfloor 4 (n/100)^{2/9} \rfloor$, minimum 1.
- Intervals: 80%, 90%, 95%, from the t distribution with $n-2$ degrees of freedom (and $n-3$ with a break dummy).
- Doubling or halving time: $\ln 2 / |k_i|$.
- **Methodology breaks (primary analysis):** only breaks listed here are modelled, as a level-shift dummy. Listed: genome 2008 (switch from Sanger to next-generation sequencing in NHGRI cost accounting). Breaks found later in source notes are recorded in `raw.csv` but used only in sensitivity analyses.
- Series with missing years are used as they are; no interpolation.

## Aggregation

- Weights: equal within each group. Reported aggregates: $k_{HTAB}^{fast}$, $k_{HTAB}^{control}$, and $k_{HTAB}^{all}$ (equal weights over all 8 series).
- Uncertainty: moving-block bootstrap of residuals within each series (block length $L+1$), 10,000 replicates, seed 20260926, recomputing each $k_i$ and the aggregate.

## TAR and Δk

- $TAR_i = k_{i,current}/k_{i,historical}$.
- $\Delta k_i = k_{i,current} - k_{i,historical}$, always reported.
- $TAR_i$ is reported only if the 90% interval of $k_{i,historical}$ excludes 0; otherwise it is marked undefined, because a ratio to a near-zero rate is not interpretable.
- Aggregate TAR = $\bar{k}_{current}/\bar{k}_{historical}$ over series with a defined $TAR_i$, equal weights, with a bootstrap interval.
- Decision reading for v0: acceleration in a series is indicated when the 90% interval of $\Delta k_i$ lies above 0. This is descriptive for the pilot, not a test of the paper's predictions.

## Known limitations fixed in advance

- Nominal and constant-dollar series are mixed (genome, DRAM nominal; PV constant). With US inflation of roughly 2–3% per year, this biases nominal-cost $k$ downward by about 0.02–0.03 per year; a CPI-adjusted version is a sensitivity analysis for v1.
- OWID data are secondary compilations; values retrieved through a text-fetching tool are checked against the git-archived OWID vintage where one exists (genome, transistors, PV).
- The "fastest supercomputer" and "transistors per microprocessor" series are frontier maxima, not averages.

## Disclosure

While testing whether the OWID grapher CSV endpoint was reachable, the full genome sequencing-cost series was displayed before this file was written. Genome was already in the proposed universe (paper §5 and the plan of 26 September 2026) before that, so its inclusion was not influenced by the values. No other series values were seen.
