# Saka Forecasting Engine — Model Specification v0.3.1

## 1. State vector

At time $t$, define

$$
X_t = [A, C, E, R, B, D, S, M, L]
$$

where:

| Symbol | Component | Candidate operational proxy |
|---|---|---|
| $A$ | AI / scientific-intelligence capability | Composite index (Section 1.1); METR 50%-success task horizon is one component |
| $C$ | Compute availability | Installed AI compute stock, FLOP/s |
| $E$ | Energy abundance | Electricity supplied to data centres and labs, TWh/yr, adjusted for unmet interconnection requests |
| $R$ | Robotics and laboratory automation | Experiments per researcher per year in tracked self-driving-lab domains |
| $B$ | Biotechnology maturity | Inverse cost per genome and per edited cell line; modality classes in human trials |
| $D$ | Data and measurement capability | Size of openly accessible longitudinal multi-omic cohorts |
| $S$ | Space accessibility / orbital experimental capacity | Inverse launch cost per kg to LEO; orbital research payload mass per year |
| $M$ | Manufacturing capability | Advanced-node wafer starts per year; cell- and gene-therapy manufacturing capacity |
| $L$ | Clinical translation efficiency | Inverse of median time from IND filing to approval |

Each component is normalized to a baseline year, initially 2026 = 1. Proxies and data sources must be fixed before the first forecast is scored.

### 1.1 Composite scientific-capability index

METR time horizons are measured mostly on software/ML tasks and must not stand in for scientific capability in general. Define

$$
A_t = \prod_k a_{k,t}^{\,v_k}, \qquad \sum_k v_k = 1,
$$

over normalized sub-measures $a_k$: autonomous task horizon (METR); research-level mathematics (e.g. FrontierMath); formal theorem proving; scientific hypothesis generation scored by later experimental confirmation; wet-lab experimental planning; coding. Fix $v_k$ at preregistration; report the composite and each component.

## 2. Gross acceleration index

### 2.1 Default: weighted geometric mean

$$
FTAF_t = A_t^{0.25}\, C_t^{0.15}\, E_t^{0.10}\, R_t^{0.10}\, B_t^{0.15}\, D_t^{0.05}\, S_t^{0.05}\, M_t^{0.05}\, L_t^{0.10}
$$

Weights sum to 1, are provisional and must be sensitivity-tested (including a biomedical variant with a larger weight on $L$).

A weighted geometric mean is a Cobb–Douglas aggregate with elasticity of substitution $\sigma = 1$: a proportional gain in one component fully offsets a weighted proportional loss in another. It only collapses when a component reaches zero, so it encodes weak complementarity only.

### 2.2 Bottleneck-sensitive: CES

$$
FTAF_t = \left( \sum_j w_j\, X_{j,t}^{\rho} \right)^{1/\rho}, \qquad \sigma = \frac{1}{1-\rho}
$$

- $\rho \to 0$ ($\sigma = 1$): geometric mean (2.1).
- $\rho < 0$ ($\sigma < 1$): complements; the weakest subsystem increasingly limits the index.
- $\rho \to -\infty$: Leontief weakest-link, $FTAF_t = \min_j X_{j,t}$.

$\sigma$ is a key uncertain parameter and is sampled in the Monte Carlo (Section 11).

### 2.3 Level, growth rate, acceleration

$FTAF_t$ is a level and equals 1 in 2026 by construction. Define its growth rate

$$
g_F(t) = \frac{d \ln FTAF_t}{dt}.
$$

"Acceleration" in this framework means $dg_F/dt > 0$ (super-exponential growth), not $d^2 FTAF/dt^2 > 0$, which any exponential satisfies.

## 3. Friction, evidence and diffusion

The three correction terms act at different levels.

**System level.** $BPI_t \in [0,1]$ is the Bottleneck & Risk Index. It covers only constraints not already measured by $X_t$ (e.g. reproducibility, safety, capital, geopolitics, regulation beyond $L$). Energy, fabrication and translation limits are in $E$, $M$ and $L$ and must not be counted again.

$$
F^{sys}_t = FTAF_t \, (1 - BPI_t)
$$

**Intervention level.** For intervention or claim $j$:

- $EMS_j \in [0,1]$, the Evidence Maturity Score (Section 8), weights evidence when updating the readiness factor $G_j$ of the arrival hazard (Section 10).
- $DAI_j \in [0,1]$, the Diffusion & Accessibility Index, converts arrival probability into population impact.

EMS and DAI are not multiplied into $F^{sys}_t$.

## 4. Historical Technology Acceleration Baseline

For historical metric $i$, estimate a log-growth rate. The two-point form is

$$
k_i = \frac{\ln\left(V_{i,t_2} / V_{i,t_1}\right)}{t_2 - t_1},
$$

but $k_i$ should in practice be estimated by regression of $\ln V_i$ on $t$ over the full series, with a standard error. For decreasing-cost metrics, invert the ratio.

The historical baseline is

$$
k_{HTAB} = \sum_i w_i\, k_i,
$$

and the current Technology Acceleration Ratio is

$$
TAR_t = \frac{k_{current,t}}{k_{HTAB}}.
$$

Interpretation:

- $TAR < 1$: slower than historical baseline
- $TAR \approx 1$: similar to historical baseline
- $TAR > 1$: accelerated regime

Requirements:

- The series list must include domains that stagnated (e.g. drugs approved per R&D dollar, crop yields, transport speed, construction productivity), not only known success stories.
- Series and weights $w_i$ are fixed before current data are compared.
- $TAR$ is always reported with an uncertainty interval; acceleration requires its lower bound to exceed 1.

## 5. Growth-model comparison

For every major time series, fit at least:

1. Linear:
$$
y(t) = a + bt
$$

2. Exponential:
$$
y(t) = a e^{kt}
$$

3. Power law:
$$
y(t) = a t^{b}
$$

4. Logistic:
$$
y(t) = \frac{L}{1 + e^{-k(t - t_0)}}
$$

5. Piecewise / change-point models.

Model selection should use rolling out-of-sample error plus AIC/BIC and residual diagnostics. No permanent exponential assumption is allowed.

Cautions:

- The power law depends on the origin of $t$; fix it in advance and report it.
- Logistic fits before the inflection point leave the ceiling $L$ essentially unidentified; report its profile likelihood, not a point estimate.
- AIC/BIC are only comparable between models fitted to the same response, on the same scale, with the same error structure. Models fitted in levels and in logs are compared by out-of-sample error only.

## 6. Scientific translation

For a closed experimental loop, define Scientific Cycle Time (latency of one loop):

$$
SCT = t_{\text{new hypothesis}} - t_{\text{prior hypothesis}}
$$

and the Scientific Acceleration Factor

$$
SAF_{science} = \frac{SCT_{baseline}}{SCT_t}.
$$

Because latency can fall while the number of loops falls too, also track throughput:

$$
Q_t = \text{validated and independently replicated discoveries per unit time in a fixed domain.}
$$

Define the Translation Acceleration Factor

$$
TAF = \frac{T_{baseline,\ \text{discovery} \rightarrow \text{clinic}}}{T_{current,\ \text{discovery} \rightarrow \text{clinic}}}.
$$

These variables attempt to measure conversion of computational progress into physical and clinical progress.

### 6.1 AI attribution scale

Grade each discovery by the role of AI in its intellectual work:

- $AI_0$: auxiliary tool (search, writing, routine code);
- $AI_1$: data analysis or modelling on a human-designed study;
- $AI_2$: partial hypothesis generation or experimental design, humans leading;
- $AI_3$: principal contribution — AI proposed the hypothesis and designed the decisive experiment or proof;
- $AI_4$: essentially autonomous — AI proposed, executed (in silico or via automated labs) and interpreted; humans approve and verify.

Assigned from CRediT statements and methods sections by two independent coders blind to the prediction; report Cohen's $\kappa$; resolve disagreements to the lower level. Only $AI_3$ and $AI_4$ count toward P6.

## 7. Longevity Translation Index

Track progression of an intervention through

$$
L_0 \rightarrow L_1 \rightarrow L_2 \rightarrow L_3 \rightarrow L_4 \rightarrow L_5 \rightarrow L_6 \rightarrow L_7 \rightarrow L_8
$$

with $L_0$ = hypothesis, $L_1$ = in vitro, $L_2$ = animal, $L_3$ = large animal, $L_4$ = Phase I, $L_5$ = Phase II, $L_6$ = Phase III, $L_7$ = approval, $L_8$ = demonstrated clinical / mortality benefit.

The model should estimate transition hazards and transition times between levels, using historical baselines (e.g. Wong, Siah & Lo 2019), rather than treating a preclinical result as equivalent to a clinical outcome.

Requirements (also for P7, P8):

- **Composition bias:** compare within therapeutic area × modality strata and IND-filing-year cohorts; combine strata with fixed weights.
- **Censoring:** estimate time to approval with Kaplan–Meier and Cox models (covariates: area, modality); model phase progression $L_4 \rightarrow L_5 \rightarrow L_6 \rightarrow L_7$ as a multistate model with failure as a competing absorbing state.

## 8. Evidence Maturity Score

Suggested ordinal mapping:

- 0.05 — hypothesis / mechanistic speculation
- 0.15 — in vitro
- 0.25 — animal
- 0.40 — human observational
- 0.55 — small controlled human trial
- 0.70 — large randomized controlled trial
- 0.85 — independent replication
- 1.00 — demonstrated clinically meaningful endpoint / mortality benefit with replication

Values are provisional. EMS is intervention-level (see Section 3).

## 9. Longevity Escape Velocity proxy

**Period definition (framework default).** Let $HALE_x(t)$ be period healthy-life expectancy at fixed age $x$ (default $x = 65$) in calendar year $t$. Define

$$
LEV_x(t) = \frac{\partial\, HALE_x(t)}{\partial t}.
$$

Interpretation:

- $LEV_x < 0$: healthy-life expectancy at age $x$ is falling.
- $0 < LEV_x < 1$: medicine offsets part of chronological ageing.
- $LEV_x \geq 1$: operational definition of longevity escape velocity for this framework.

**Individual representation (related, not equivalent).** For individual $i$, let $h_i(t)$ be *remaining* expected healthy life. Ageing alone makes $h_i$ decrease, so escape velocity is $dh_i/dt \geq 0$. Do not combine remaining life expectancy with a threshold of 1. $h_i$ depends on individual risk and cannot be read from period tables; it matches the population measure only for someone whose risk equals the population's at each age.

**Reference, not an estimate.** Record period life expectancy at birth has risen by about 0.25 years per year since 1840 (Oeppen & Vaupel 2002). This is a different series from $HALE_{65}$ and does not estimate $LEV_{65}$; the proxy's current value must be estimated from fixed-age HALE series.

This is a forecasting construct, not an accepted clinical metric.

## 10. Technology Survival Ladder

For milestone therapy class $j$, define the time-dependent arrival hazard

$$
\lambda_j(t) = \lambda_{0,j} \left[ F^{sys}_t \right]^{\alpha_j} G_j(t)
$$

where:

- $\lambda_{0,j}$: baseline hazard in 2026;
- $\alpha_j$: sensitivity of class $j$ to system-wide progress;
- $G_j(t)$: readiness factor from the class's current LTI level and historical transition probabilities, updated with EMS-weighted evidence.

Cumulative arrival probability from 2026 ($t = 0$) to time $T$:

$$
P_j(T) = 1 - \exp\left( -\int_0^T \lambda_j(t)\, dt \right)
$$

Population impact is $P_j(T) \cdot DAI_j$.

A person's "technology survival ladder" is the sequence of future medical milestones that become reachable while the individual remains alive and sufficiently healthy to benefit.

It is not a personal mortality calculator.

## 11. Monte Carlo forecasting

Future versions should:

1. Specify distributions for annual growth and slowdown in each subsystem.
2. Sample the elasticity of substitution $\sigma$ (Section 2.2).
3. Sample bottlenecks and discontinuous breakthroughs.
4. Simulate at least $10^5$ trajectories.
5. Report medians and 10/50/90% intervals.
6. Score forecasts retrospectively using Brier scores and calibration plots.
7. Update priors at fixed intervals rather than after emotionally salient news.

## 12. Falsification criteria

v0.3.1 is **not** the preregistration: it fixes the form of each prediction and the threshold rule. The preregistration is the frozen, timestamped output of that rule (planned: `forecasts/preregistration-2026.json`), made before any data from the tested windows are examined. Each window starts on the freeze date; earlier data are used only for baselines. Window labels below are nominal, assuming a freeze in late 2026.

Thresholds below are **placeholders**. Before preregistration, each is replaced by the larger of (1) the value exceeded with at most 5% probability under the historical regime, from the statistic's variability over past windows of equal length, and (2) the minimum scientifically or clinically relevant effect.

Report 50/80/90/95% intervals; the **90% interval** is the preregistered decision criterion.

| # | Prediction | Window | Supports the hypothesis if… |
|---|---|---|---|
| P1 | Cross-domain acceleration | 2026–2031 | $TAR > 1.5$, lower 90% bound $> 1$, in at least 3 HTAB domains |
| P2 | Rising growth rate | 2026–2031 | $dg_F/dt > 0$, 90% interval excluding 0 |
| P3 | Research productivity reverses | 2026–2036 | Research productivity (Bloom et al. 2020 sense) rises in at least 2 of their domains |
| P4 | Autonomy keeps growing | 2026–2031 | METR 50% time-horizon doubling time $\leq$ 12 months, and non-software components of $A$ rising |
| P5 | Faster experimental loops | 2026–2031 | Median SCT falls $\geq$ 50% in at least 2 self-driving-lab domains, with no fall in $Q_t$ |
| P6 | Replicated AI discoveries | 2026–2031 | Annual independently replicated $AI_3$/$AI_4$ discoveries (Section 6.1) at least double |
| P7 | Faster translation | 2026–2036 | Median IND-to-approval time (survival analysis, within area × modality strata) falls $\geq$ 20% vs 2015–2025 IND cohorts in at least one therapeutic area |
| P8 | Better clinical success | 2026–2036 | Phase I-to-approval probability (multistate model, within strata) improves $\geq$ 30% vs Wong et al. 2019 in at least one area |

The Saka Law should be weakened or rejected as a useful forecasting hypothesis if, by the end of the relevant window:

- $TAR$ is not distinguishable from 1 in a majority of HTAB domains;
- AI capability and autonomy improve (P4) but SCT, $Q_t$ and replication do not (P5, P6 fail);
- biological translation times and success probabilities remain statistically unchanged (P7, P8 fail);
- $LEV_{65}(t)$ in the largest high-income populations shows no increase over its own 2000–2025 trend through 2046;
- persistent physical, economic or regulatory bottlenecks dominate the feedback loop.

Success of P1–P6 with failure of P7, P8 and the LEV criterion would support acceleration in computation and discovery but not its extension to biomedicine.

The model is therefore designed to permit a negative result.
