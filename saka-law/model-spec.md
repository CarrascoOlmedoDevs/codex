# Saka Forecasting Engine — Model Specification v0.1

## 1. State vector

At time (t), define

[
X_t = [A,C,E,R,B,D,S,M,L]
]

where:

- (A): AI/scientific-intelligence capability
- (C): compute availability
- (E): energy abundance
- (R): robotics and laboratory automation
- (B): biotechnology maturity
- (D): data and measurement capability
- (S): space accessibility / orbital experimental capacity
- (M): manufacturing capability
- (L): clinical translation efficiency

Each component should be normalized to a baseline year, initially 2026 = 1.

## 2. Gross acceleration factor

Use a weighted geometric mean:

[
FTAF_t =
A_t^{0.25}
C_t^{0.15}
E_t^{0.10}
R_t^{0.10}
B_t^{0.15}
D_t^{0.05}
S_t^{0.05}
M_t^{0.05}
L_t^{0.10}
]

Weights are provisional and must be sensitivity-tested.

A geometric rather than arithmetic aggregation is used because severe weakness in one necessary subsystem should not be fully compensated by extreme strength in another.

## 3. Friction and diffusion

Let:

- (BPI_t in [0,1]): Bottleneck & Risk Index
- (DAI_t in [0,1]): Diffusion & Accessibility Index
- (EMS_t in [0,1]): Evidence Maturity Score

Then:

[
F^{effective}_t = FTAF_t (1-BPI_t) DAI_t EMS_t
]

## 4. Historical Technology Acceleration Baseline

For historical metric (i), estimate a log-growth rate:

[
k_i = \frac{\ln(V_{i,t_2}/V_{i,t_1})}{t_2-t_1}
]

For decreasing-cost metrics, invert the ratio.

The historical baseline is:

[
k_{HTAB} = sum_i w_i k_i
]

and the current Technology Acceleration Ratio:

[
TAR_t = \frac{k_{current,t}}{k_{HTAB}}
]

Interpretation:

- (TAR < 1): slower than historical baseline
- (TAR \approx 1): similar to historical baseline
- (TAR > 1): accelerated regime

## 5. Growth-model comparison

For every major time series, fit at least:

1. Linear:
[
y(t)=a+bt
]

2. Exponential:
[
y(t)=ae^{kt}
]

3. Power law:
[
y(t)=at^b
]

4. Logistic:
[
y(t)=\frac{L}{1+e^{-k(t-t_0)}}
]

5. Piecewise / change-point models.

Model selection should use rolling out-of-sample error plus AIC/BIC and residual diagnostics. No permanent exponential assumption is allowed.

## 6. Scientific translation

Define Scientific Cycle Time:

[
SCT = t_{new\ hypothesis} - t_{prior\ hypothesis}
]

for a closed experimental loop.

Define Scientific Acceleration Factor:

[
SAF_{science} = \frac{SCT_{baseline}}{SCT_t}
]

Define Translation Acceleration Factor:

[
TAF = \frac{T_{baseline, discovery\rightarrow clinic}}{T_{current, discovery\rightarrow clinic}}
]

These variables attempt to measure conversion of computational progress into physical and clinical progress.

## 7. Longevity Translation Index

Track progression of an intervention through:

[
L_0=\text{hypothesis}
ightarrow
L_1=\text{in vitro}
ightarrow
L_2=\text{animal}
ightarrow
L_3=\text{large animal}
ightarrow
L_4=\text{Phase I}
ightarrow
L_5=\text{Phase II}
ightarrow
L_6=\text{Phase III}
ightarrow
L_7=\text{approval}
ightarrow
L_8=\text{demonstrated clinical / mortality benefit}
]

The model should estimate transition hazards between levels rather than treating a preclinical result as equivalent to a clinical outcome.

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

Values are provisional.

## 9. Longevity Escape Velocity proxy

Let (HLE(t)) be expected healthy-life expectancy at time (t).

Define:

[
LEV(t)=\frac{dHLE}{dt}
]

Interpretation:

- (LEV < 0): expected healthy years are being lost faster than medicine adds them.
- (0 < LEV < 1): medicine offsets part of chronological ageing.
- (LEV \geq 1): operational definition of longevity escape velocity for this framework.

This is a forecasting construct, not an accepted clinical metric.

## 10. Technology Survival Ladder

For milestone therapy (j), define time-dependent arrival hazard:

[
\lambda_j(t)=\lambda_{0,j}
[F^{effective}_t]^{\alpha_j}
M_j(t)
]

Then cumulative arrival probability by time (T):

[
P_j(T)=1-\exp\left(-\int_0^T \lambda_j(t)dt\right)
]

A person's "technology survival ladder" is the sequence of future medical milestones that become reachable while the individual remains alive and sufficiently healthy to benefit.

It is not a personal mortality calculator.

## 11. Monte Carlo forecasting

Future versions should:

1. Specify distributions for annual growth and slowdown in each subsystem.
2. Sample bottlenecks and discontinuous breakthroughs.
3. Simulate at least (10^5) trajectories.
4. Report medians and 10/50/90% intervals.
5. Score forecasts retrospectively using Brier scores and calibration plots.
6. Update priors at fixed intervals rather than after emotionally salient news.

## 12. Falsification criteria

The Saka Law should be weakened or rejected as a useful forecasting hypothesis if, over a sufficiently long measurement window:

- recursive AI capability improves but scientific cycle time does not fall;
- scientific output increases without an increase in independently replicated results;
- compute and algorithmic gains fail to translate into experimentally validated knowledge;
- biological translation times remain statistically unchanged;
- current acceleration metrics revert to the historical baseline;
- persistent physical, economic or regulatory bottlenecks dominate the feedback loop.

The model is therefore designed to permit a negative result.
