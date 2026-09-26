# The Saka Law: Measuring Recursive Technological Acceleration and Its Implications for Biomedical Longevity

**Javier Carrasco ("Saka")**  
Version 0.1 — 26 September 2026  
Conceptual / forecasting paper — not peer reviewed

## Abstract

Technological forecasting often extrapolates individual trends—compute, biotechnology, energy, robotics or launch cost—without explicitly representing interactions between them. This paper proposes the **Saka Law of Recursive Technological Acceleration**, a falsifiable forecasting hypothesis: when a technology materially improves the process by which new technology is discovered, validated and deployed, the rate of technological progress can itself accelerate.

The paper introduces the **Future Technology Acceleration Framework (FTAF)**, a systems model combining artificial intelligence, compute, energy, robotics, biotechnology, measurement, space access, manufacturing and clinical translation. It further introduces a Historical Technology Acceleration Baseline (HTAB), Technology Acceleration Ratio (TAR), Evidence Maturity Score (EMS), Longevity Translation Index (LTI), Bottleneck & Risk Index (BPI), Diffusion & Accessibility Index (DAI), and a proposed healthy-longevity derivative termed the LEV proxy.

The framework explicitly rejects indefinite exponential extrapolation. It instead compares linear, exponential, power-law, logistic and change-point models, incorporates physical and translational bottlenecks, and proposes Monte Carlo forecasting with calibration against future observations.

A motivating application is biomedical longevity. The key question is not whether ageing will be "solved" by a particular date, but whether scientific and medical progress can increasingly offset age-related functional decline and allow individuals to reach successive generations of therapies. This dynamic is formalized as a **Technology Survival Ladder**.

---

## 1. Introduction

Between the mid-1980s and the mid-2020s, computing, genomic measurement, communications, energy technologies, robotics and space launch systems changed by orders of magnitude. Forecasting the next decades by simply repeating historical averages, however, may be inadequate if the process that creates technology is itself becoming technologically amplified.

In 2026 several signals motivate examining this possibility. Frontier AI training compute continues to rise rapidly; algorithmic efficiency is improving; the stock of AI compute is expanding; autonomous task horizons are being measured over progressively longer tasks; self-driving laboratories are evolving from narrow automation toward systems that can propose, execute and interpret experiments; and AI systems are beginning to contribute to frontier mathematical research.

OpenAI, for example, published an AI-generated proposed solution to the Navier–Stokes Millennium Prize Problem on 8 September 2026 together with a Lean formalization. This is best treated as evidence of a new research capability regime, not as proof that all scientific problems can now be rapidly solved [1].

The central thesis of this paper is therefore modest but consequential:

> **If technology improves the rate at which new technology is generated, then technological progress can enter a recursively accelerated regime, subject to physical, biological, economic and institutional bottlenecks.**

This statement is termed the **Saka Law** for shorthand. It is proposed as a hypothesis to be measured and potentially falsified, not as a universal law of nature.

---

## 2. The Saka Law

Let (T(t)) denote a broad technological-capability state. Conventional progress can be represented as:

[
\frac{dT}{dt}=f(T, R)
]

where (R) represents research resources.

Recursive technological acceleration appears when part of (T) increases the productivity of the process producing future (T):

[
\frac{dT}{dt}=f(T,R,A(T))
]

where (A(T)) is technological augmentation of discovery itself.

A simplified condition for recursive acceleration is:

[
\frac{d^2T}{dt^2}>0
]

while the technology is materially increasing the productivity of research, design, experimentation, verification, manufacturing or deployment.

This condition is not expected to hold indefinitely. Energy, fabrication capacity, experiment duration, regulation, biological timescales, capital and safety constraints can reduce or reverse acceleration.

Accordingly, the stronger form of the Saka Law is not "technology is exponential". It is:

> **The growth regime of technology depends partly on the growth rate of the systems that generate validated technological knowledge.**

---

## 3. Why recursive acceleration is plausible in 2026

### 3.1 AI resources are growing rapidly

Epoch AI reports that frontier language-model training compute has grown at roughly 5× per year since 2020, while the total stock of AI compute has grown around 3.4× per year. The same source estimates pre-training compute efficiency improving by roughly 3× per year [2].

These variables should not be interpreted as equivalent to intelligence. They are inputs into an innovation process.

### 3.2 Autonomy is becoming measurable

METR's task-completion time-horizon methodology measures the duration of tasks, in human expert time, that frontier agents can complete at specified success probabilities. It provides a more behaviorally meaningful metric than raw parameter count and allows longitudinal tracking of agent autonomy [3].

### 3.3 Autonomous laboratories close part of the physical loop

Self-driving laboratories combine robotics, experimental platforms and AI. A 2026 Nature Reviews Chemistry review describes a transition from narrowly focused automation to multipurpose systems in which algorithms can propose, execute and interpret experiments with limited human intervention [4].

This matters because purely computational intelligence cannot fully accelerate experimental science if physical validation remains serial and human-limited.

### 3.4 Energy is a hard constraint

The International Energy Agency projects global data-centre electricity demand to roughly double from about 485 TWh in 2025 to about 950 TWh in 2030 in its 2026 update. Electricity consumption from AI-focused data centres is projected to grow faster still [5].

Thus, abundant compute cannot be modelled independently of energy infrastructure.

### 3.5 Biomedical translation is entering new regimes

In June 2026 the first participant was dosed in a Phase I trial of ER-100, an experimental therapy using controlled OCT4, SOX2 and KLF4 expression for optic neuropathies. The trial primarily evaluates safety and tolerability, so it must not be interpreted as evidence that systemic rejuvenation has been achieved [6].

Its importance to this framework is different: a class of interventions previously discussed mainly at preclinical level has crossed into human testing. This creates a measurable translation milestone.

---

## 4. Historical Technology Acceleration Baseline (HTAB)

A forecasting system should first ask whether the present regime is actually unusual relative to history.

For historical metric (i), define:

[
k_i=
\frac{\ln(V_{i,t_2}/V_{i,t_1})}{t_2-t_1}
]

For declining-cost technologies, the ratio is inverted.

Potential HTAB series include:

- semiconductor density and compute;
- supercomputer performance;
- genomic sequencing cost;
- battery cost per kWh;
- photovoltaic module cost per watt;
- telecommunications bandwidth and cost;
- industrial robot density;
- launch cost and annual mass to orbit.

The historical baseline is a weighted log-growth average rather than a claim that the entire economy improves at one rate.

The purpose of HTAB is to create a null model:

[
H_0: k_{current}=k_{historical}
]

against which a modern acceleration regime can be tested.

---

## 5. Technology Acceleration Ratio (TAR)

Define:

[
TAR(t)=\frac{k_{current}(t)}{k_{HTAB}}
]

Interpretation:

- (TAR<1): technological growth slower than historical baseline;
- (TAR\approx1): similar to historical baseline;
- (TAR>1): accelerated relative to baseline.

A sustained (TAR>1) across independent domains would be stronger evidence than a short-lived burst in a single field.

---

## 6. Future Technology Acceleration Framework (FTAF)

The proposed state vector is:

[
X_t=[A,C,E,R,B,D,S,M,L]
]

with:

- (A): AI and scientific reasoning capability;
- (C): compute availability;
- (E): energy abundance and reliability;
- (R): robotics / laboratory automation;
- (B): biotechnology maturity;
- (D): data and measurement capability;
- (S): space accessibility and orbital experimental capacity;
- (M): manufacturing capacity;
- (L): clinical translation efficiency.

The initial gross score is a weighted geometric mean:

[
FTAF_t=
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

The weights are provisional.

The geometric mean encodes complementarity. Unlimited AI with no energy, no experimental throughput or no manufacturing should not imply unlimited real-world technological progress.

---

## 7. Friction, evidence and accessibility

Three correction terms prevent the framework from confusing technical demonstrations with societal impact.

### 7.1 Bottleneck & Risk Index (BPI)

(BPI \in [0,1]) represents constraints such as:

- energy and grid limitations;
- chip fabrication and supply chains;
- scarce materials;
- regulatory delays;
- poor scientific reproducibility;
- safety limitations;
- capital constraints;
- geopolitical disruption;
- biological complexity;
- diminishing returns to scaling.

### 7.2 Evidence Maturity Score (EMS)

A preclinical result should not carry the same forecasting weight as a replicated human endpoint.

A provisional scale is:

[
\text{hypothesis}
<
\text{in vitro}
<
\text{animal}
<
\text{human observational}
<
\text{controlled trial}
<
\text{large RCT}
<
\text{independent replication}
<
\text{clinical benefit}
]

### 7.3 Diffusion & Accessibility Index (DAI)

A therapy that exists but is unaffordable or capacity-constrained has limited population impact.

DAI therefore includes:

- price;
- annual treatment capacity;
- geographic diffusion;
- reimbursement / coverage;
- manufacturing scale;
- time to access.

The effective acceleration factor is then:

[
F^{effective}_t=
FTAF_t(1-BPI_t)EMS_tDAI_t
]

---

## 8. Scientific throughput rather than paper count

A core prediction of the Saka Law is that the scientific cycle itself should compress.

Define Scientific Cycle Time:

[
SCT=
t_{new\ hypothesis}-t_{previous\ hypothesis}
]

for a closed loop:

[
hypothesis
ightarrow
experiment
ightarrow
data
ightarrow
analysis
ightarrow
new\ hypothesis
]

and:

[
SAF_{science}=\frac{SCT_{baseline}}{SCT_t}
]

The primary output should be **validated and replicated discoveries per unit time**, not publication volume.

An AI system producing one million low-quality hypotheses is not scientific acceleration if experimental validation and replication remain unchanged.

---

## 9. Longevity Translation Index (LTI)

Longevity forecasting is particularly vulnerable to overinterpreting animal or biomarker studies.

The LTI therefore tracks interventions through:

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
L_8=\text{clinically meaningful / mortality benefit}
]

The model should estimate transition probabilities and transition times.

A major acceleration in ageing biology papers with no reduction in (L_1\rightarrow L_8) translation time would argue against strong biomedical recursive acceleration.

---

## 10. Longevity Escape Velocity proxy

Let (HLE(t)) represent expected remaining healthy-life expectancy.

Define:

[
LEV(t)=\frac{dHLE}{dt}
]

This is an operational forecasting proxy rather than an accepted clinical metric.

Interpretation:

- (LEV<0): loss of expected healthy years dominates;
- (0<LEV<1): medical progress offsets part of ageing;
- (LEV\ge1): healthy-life expectancy frontier moves outward by at least one year per elapsed year.

The framework does not claim that (LEV\ge1) has been achieved.

---

## 11. The Technology Survival Ladder

Long-range longevity forecasts should not require a single future "cure for ageing".

Instead, an individual may encounter sequential generations of treatment:

[
Therapy_1
ightarrow
\Delta HLE_1
ightarrow
Therapy_2
ightarrow
\Delta HLE_2
ightarrow
Therapy_3
]

If earlier interventions preserve enough function to reach later, more capable interventions, a ladder effect emerges.

For intervention class (j), define:

[
\lambda_j(t)=
\lambda_{0,j}
[F^{effective}_t]^{\alpha_j}
M_j(t)
]

and cumulative arrival probability:

[
P_j(T)=1-
\exp\left(
-\int_0^T\lambda_j(t)dt
\right)
]

This should be interpreted as technology-arrival forecasting, not as a personalized survival probability.

---

## 12. Space as an experimental multiplier

Space is included with a relatively modest weight because biomedical progress does not require orbital laboratories. However, cheaper and more frequent launch could add experimental regimes difficult to reproduce on Earth:

- prolonged microgravity;
- altered fluid dynamics;
- radiation environments;
- protein crystallization;
- tissue and organoid growth;
- closed-loop autonomous biological experiments.

If reusable launch systems substantially reduce cost and increase cadence, the space term (S_t) may undergo a measurable change point.

The value of space in the framework is therefore not speculative colonization; it is **expansion of experimental state space**.

---

## 13. Energy as a cognitive-infrastructure constraint

AI systems transform electricity into computational work. Large-scale scientific agents, simulation and automated laboratories therefore depend on physical energy infrastructure.

The IEA's 2026 update emphasizes both rapidly improving energy efficiency per AI task and rapidly increasing aggregate demand from more intensive applications [5].

This creates a feedback structure:

[
Energy
ightarrow
Compute
ightarrow
AI
ightarrow
Science
ightarrow
better\ energy\ technology
]

Such a loop can accelerate, but transmission grids, generation capacity, transformers, storage and permitting can impose long delays.

---

## 14. Twenty-year scenario: 2026–2046

This section is explicitly speculative.

A naive continuation of recent AI growth rates would produce implausibly enormous multipliers. The Saka framework therefore assumes declining log-growth rates and explicit bottlenecks.

A reasonable scenario family for FTAF should include:

- **conservative:** rapid near-term growth followed by strong saturation;
- **central:** sustained AI/science acceleration with progressively declining growth rates;
- **aggressive:** major breakthroughs in AI, automation, energy or manufacturing that extend the high-growth regime.

The central qualitative expectation for 2046 is not "immortality". It is increased probability of:

- highly longitudinal personalized medicine;
- earlier multi-modal cancer detection;
- broader use of in-vivo gene editing;
- organoids as therapeutic decision tools in selected cancers;
- clinically useful regeneration of multiple tissues;
- substantially increased organ replacement options;
- autonomous laboratories as standard research infrastructure;
- at least some human interventions that restore age-related function in specific tissues.

The most important uncertainty is whether these capabilities compress **clinical translation time**, not merely discovery time.

---

## 15. 2046–2076 and the longevity question

Forecast uncertainty becomes extreme beyond 2046.

The relevant variable is the relative rate of:

[
V_{ageing}
quad vs. quad
V_{medical\ progress}
]

By 2076, a successful recursive-acceleration regime could plausibly produce periodic repair across multiple biological subsystems rather than a single rejuvenation treatment.

However, several problems may remain especially difficult:

- preserving brain information while rejuvenating neural tissue;
- preventing cancer under increased regenerative capacity;
- maintaining long-term genomic and epigenomic stability;
- controlling immune ageing without creating autoimmunity;
- proving that biomarker changes translate into morbidity and mortality reduction.

The framework therefore treats "systemic rejuvenation" and "longevity escape velocity" as high-uncertainty events rather than inevitable outcomes.

---

## 16. Predictions that make the framework falsifiable

The Saka hypothesis predicts that if recursive acceleration is real, at least some of the following should be observable over the next decade:

1. AI capability continues improving while cost per fixed capability falls.
2. Scientific-agent task horizons increase.
3. Median scientific cycle time decreases in automated domains.
4. The number of independently replicated AI-originated discoveries rises.
5. Discovery-to-human translation times begin to fall in at least selected biomedical domains.
6. Laboratory automation increases experiments per scientist per unit time.
7. Energy and compute infrastructure expand sufficiently to prevent persistent binding constraints.
8. The gap between preclinical and clinical success rates improves rather than merely producing more preclinical candidates.

Evidence against the hypothesis would include:

- rapid AI benchmark progress with stagnant experimental throughput;
- no improvement in replication rates;
- unchanged or worsening clinical translation times;
- persistent energy/fabrication constraints that neutralize compute growth;
- saturation of AI autonomy;
- rising scientific output without rising validated discovery.

---

## 17. Forecasting protocol

Future versions should use a preregistered update process.

### Quarterly

Update:

- AI capability and autonomy;
- compute stock and price-performance;
- energy availability and data-centre constraints;
- laboratory automation;
- major clinical translation milestones.

### Annually

Fit:

- linear;
- exponential;
- power-law;
- logistic;
- piecewise/change-point models.

Evaluate using:

- rolling out-of-sample error;
- AIC/BIC;
- residual diagnostics;
- calibration.

### Monte Carlo

Simulate at least (10^5) futures with distributions over:

- growth-rate decay;
- breakthrough probabilities;
- energy constraints;
- AI reliability;
- experimental throughput;
- regulatory timelines;
- clinical success probabilities.

Predictions should be scored retrospectively using Brier scores where possible.

---

## 18. Discussion

The principal contribution of the Saka Law framework is not a claim that technology will grow exponentially forever. It is the proposal that **research productivity itself should be treated as an endogenous technological variable**.

This changes long-range forecasting.

In a non-recursive model, the future is estimated mainly from the current stock of technology.

In a recursive model:

[
Future\ technology
=
f(
current\ technology,
technology's\ ability\ to\ improve\ discovery
)
]

If scientific cognition, experiment execution, measurement and manufacturing all become increasingly automated, technological progress may depart from historical baselines.

But a recursive process is not necessarily an explosive one. Real systems can settle into logistic, piecewise or bottleneck-limited regimes.

The empirical task is therefore to measure the curvature.

---

## 19. Conclusion

The Saka Law is proposed as a testable hypothesis of recursive technological acceleration:

> **When technology materially improves the processes that generate, validate and deploy new technology, the rate of technological progress can accelerate relative to its historical baseline, until constrained by physical, biological, economic or institutional bottlenecks.**

The Future Technology Acceleration Framework attempts to measure this effect across AI, compute, energy, robotics, biotechnology, measurement, space, manufacturing and clinical translation.

Its longevity application replaces deterministic predictions of "curing ageing" with a measurable sequence:

[
scientific\ acceleration
ightarrow
biomedical\ translation
ightarrow
functional\ repair
ightarrow
healthy-life\ extension
ightarrow
access\ to\ later\ therapies
]

The hypothesis will become scientifically useful only if its metrics are populated with reproducible data, its forecasts are preregistered, and its failures are recorded as rigorously as its successes.

---

## References

1. OpenAI. **On the Navier–Stokes Millennium Prize Problem.** 8 September 2026. https://openai.com/index/navier-stokes-solution/

2. Epoch AI. **Trends in Artificial Intelligence.** Updated 2026. https://epoch.ai/trends

3. METR. **Task-Completion Time Horizons of Frontier AI Models.** Updated 8 May 2026. https://metr.org/time-horizons/

4. Canty, R. B. & Abolhasani, M. **The past, present and future of self-driving laboratories.** _Nature Reviews Chemistry_ 10, 523–537 (2026). https://doi.org/10.1038/s41570-026-00847-2

5. International Energy Agency. **Key Questions on Energy and AI.** 2026. https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary

6. Life Biosciences. **Life Biosciences Announces First Patient Dosed in Phase 1 Trial of ER-100 for Optic Neuropathies.** 9 June 2026. https://www.lifebiosciences.com/life-biosciences-announces-first-patient-dosed-in-phase-1-trial-of-er-100-for-optic-neuropathies/

7. International Energy Agency. **Energy and AI.** 2025. https://www.iea.org/reports/energy-and-ai

---

## Disclosure

This document is a conceptual forecasting framework developed through human–AI collaboration. Named indices, weights and long-range scenarios are proposals for testing, not established scientific standards. Biomedical sections are not medical advice and do not assert that ageing has been or will be cured.
