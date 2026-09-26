# The Saka Law

**A framework for measuring recursive technological acceleration and its implications for biomedical longevity**

Version 0.3.1 — 26 September 2026

This directory contains a conceptual forecasting paper developed around a proposed idea called the **Saka Law of Recursive Technological Acceleration**.

> **Status:** hypothesis / forecasting framework. It is not an established scientific law and it is not a claim that technological progress must remain exponential.

## Core idea

Technological progress can accelerate when technology begins to improve the process that produces new technology. In growth-economics terms, this is a claim about the feedback parameter of the idea-production function, set against evidence that research productivity has been falling for decades. The framework attempts to measure that feedback while explicitly accounting for bottlenecks, translation delays, evidence quality and accessibility.

The model combines:

- historical technology baselines;
- AI capability, compute and algorithmic efficiency;
- energy availability;
- robotics and autonomous laboratories;
- biotechnology maturity;
- measurement and biological data;
- manufacturing;
- space-enabled experimentation;
- clinical translation;
- bottlenecks, risks and diffusion.

The longevity component asks a narrower question: **can medical progress increase healthy-life expectancy fast enough to materially offset biological ageing?**

## Files

- [paper.md](./paper.md) — full conceptual paper.
- [model-spec.md](./model-spec.md) — equations, variables and proposed update procedure.

## Data and code (HTAB v0)

The first empirical baseline is in [data/htab/](./data/htab/):

- [UNIVERSE.md](./data/htab/UNIVERSE.md) — series, windows and estimation rules, frozen before the data were analysed.
- [RESULTS.md](./data/htab/RESULTS.md) — first HTAB and TAR results, uncertainty checks and how to read them.
- `raw.csv` — all series in long format with source, quality flag and methodology-break columns; `sources/` holds the retrieved snapshots.
- `results/` — per-domain and aggregate tables.

Code in [src/](./src/): `build_raw.py`, `build_htab.py`, `calculate_tar.py`, `coverage_check.py` (Python 3, numpy, scipy).

Planned additions: remaining HTAB series, AI-component growth rates, Monte Carlo forecasting, scoring, and the frozen preregistration in `forecasts/`.

## Citation

For now cite as:

**Carrasco, J. (Saka). (2026). _The Saka Law: Measuring Recursive Technological Acceleration and Its Implications for Biomedical Longevity_. Version 0.3.1.**

## Important note

This version contains no numerical forecasts. Its weights and prediction thresholds are **subjective proposals**, not estimates or clinical predictions. Future versions should populate the component proxies with reproducible datasets, fix the thresholds in a preregistration, and add out-of-sample validation.
