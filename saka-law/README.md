# The Saka Law

**A framework for measuring recursive technological acceleration and its implications for biomedical longevity**

Version 0.3 — 26 September 2026

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

## Suggested repository structure for future versions

```
saka-law/
├── README.md
├── paper.md
├── model-spec.md
├── data/
│   ├── historical_baseline.csv
│   ├── ai_metrics.csv
│   ├── biotech_translation.csv
│   └── energy_space_robotics.csv
├── notebooks/
│   ├── fit_growth_models.ipynb
│   └── monte_carlo_forecast.ipynb
└── figures/
```

## Citation

For now cite as:

**Carrasco, J. (Saka). (2026). _The Saka Law: Measuring Recursive Technological Acceleration and Its Implications for Biomedical Longevity_. Version 0.3.**

## Important note

This version contains no numerical forecasts. Its weights and prediction thresholds are **subjective proposals**, not estimates or clinical predictions. Future versions should populate the component proxies with reproducible datasets, fix the thresholds in a preregistration, and add out-of-sample validation.
