# The Saka Law: Measuring Recursive Technological Acceleration and Its Implications for Biomedical Longevity

**Javier Carrasco ("Saka")**  
Version 0.3.1 — 26 September 2026  
Conceptual / forecasting paper — not peer reviewed

## Abstract

Technological forecasting often extrapolates individual trends—compute, biotechnology, energy, robotics or launch cost—without explicitly representing interactions between them. This paper proposes the **Saka Law of Recursive Technological Acceleration**, a falsifiable forecasting hypothesis: when a technology materially improves the process by which new technology is discovered, validated and deployed, the *growth rate* of technological progress can itself increase.

The idea is not new in economics: it is the feedback parameter of the Romer–Jones idea-production function, and it underlies both the "accelerating returns" literature and the recent literature on AI-driven explosive growth. Existing evidence also points the other way: research productivity has been falling across many fields for decades. The contribution of this paper is therefore not the idea itself but a **multi-domain operationalization and a preregistered calibration protocol** for testing it.

The paper introduces the **Future Technology Acceleration Framework (FTAF)**, a systems model combining artificial intelligence, compute, energy, robotics, biotechnology, measurement, space access, manufacturing and clinical translation. It further introduces a Historical Technology Acceleration Baseline (HTAB), a Technology Acceleration Ratio (TAR), an Evidence Maturity Score (EMS), a Longevity Translation Index (LTI), a Bottleneck & Risk Index (BPI), a Diffusion & Accessibility Index (DAI), and an operational healthy-longevity derivative termed the LEV proxy.

The framework explicitly rejects indefinite exponential extrapolation. It compares linear, exponential, power-law, logistic and change-point models, incorporates physical and translational bottlenecks, and proposes Monte Carlo forecasting with calibration against future observations. It ends with dated, quantitative predictions that can fail.

A motivating application is biomedical longevity. The key question is not whether ageing will be "solved" by a particular date, but whether scientific and medical progress can increasingly offset age-related functional decline and allow individuals to reach successive generations of therapies. This dynamic is formalized as a **Technology Survival Ladder**.

---

## 1. Introduction

Between the mid-1980s and the mid-2020s, computing, genomic measurement, communications, energy technologies, robotics and space launch systems changed by orders of magnitude. Forecasting the next decades by simply repeating historical averages, however, may be inadequate if the process that creates technology is itself becoming technologically amplified.

In 2026 several signals motivate examining this possibility. Frontier AI training compute continues to rise rapidly; algorithmic efficiency is improving; the stock of AI compute is expanding; autonomous task horizons are being measured over progressively longer tasks; self-driving laboratories are evolving from narrow automation toward systems that can propose, execute and interpret experiments; and AI systems are beginning to contribute to frontier mathematical research.

For example, on 8 September 2026 OpenAI published an AI-generated proof of finite-time blowup (singularity formation) for the three-dimensional Navier–Stokes equations, addressing the Millennium Prize Problem, together with a Lean formalization [1, 2]. At the time of writing, human experts still need to confirm that the formalized statement is equivalent to the problem as posed, and the result has not been accepted by the Clay Mathematics Institute. It is best treated as evidence of a new research-capability regime, not as proof that all scientific problems can now be rapidly solved.

The central thesis of this paper is therefore modest but consequential:

> **If technology improves the rate at which new technology is generated, then technological progress can enter a recursively accelerated regime, subject to physical, biological, economic and institutional bottlenecks.**

This statement is termed the **Saka Law** for shorthand. It is proposed as a hypothesis to be measured and potentially falsified, not as a universal law of nature. Section 4 restates it in a form that can be estimated.

---

## 2. Related work

**Endogenous and semi-endogenous growth.** Romer [3] made the production of ideas endogenous to the economy. Jones [4] wrote the idea-production function as

$$
\dot{A} = \delta\, R^{\lambda} A^{\phi},
$$

where $A$ is the stock of knowledge, $R$ research effort and $\phi$ the strength of the feedback from existing knowledge to the productivity of research. The Saka Law is, in this language, a claim about $\phi$ and about how technology now changes $R$ itself. Kremer [5] used a closely related model to explain the historically accelerating growth of world population and output.

**Ideas getting harder to find.** Bloom, Jones, Van Reenen and Webb [6] found that research productivity has fallen steadily across semiconductors, agriculture, medicine and firm-level data—roughly 5% per year in aggregate—so that sustaining constant growth has required ever more researchers. This is the main empirical counterweight to any acceleration hypothesis and is the baseline the framework must beat.

**Eroom's law.** In drug development, the number of new drugs approved per billion dollars of R&D spending halved roughly every nine years between 1950 and 2010 [7], despite large gains in underlying technologies such as sequencing and high-throughput screening. This is directly relevant to the clinical-translation component $L$ and to the longevity application.

**Accelerating returns and explosive growth.** Kurzweil's "Law of Accelerating Returns" [8] made an informal version of the recursive claim. Aghion, Jones and Jones [9] modelled AI as automation of tasks in both goods and idea production and showed that Baumol-type bottlenecks—tasks that remain essential but hard to automate—can prevent explosive growth even when most tasks are automated. Nordhaus [10] proposed empirical tests for an approaching "economic singularity" and found that most did not yet indicate one. Davidson [11] and Erdil and Besiroglu [12] reviewed the arguments for and against AI-driven explosive growth.

**Forecasting technological progress.** Nagy et al. [13] and Farmer and Lafond [14] compared Moore's-law-type and Wright's-law-type models on large sets of historical cost curves and showed how to produce calibrated forecast intervals from them. The HTAB and TAR constructs below follow this approach.

**Position of this paper.** The framework does not claim a new mechanism. Its contribution is to (i) track the feedback across several physical and institutional subsystems at once rather than in aggregate output alone, (ii) separate discovery from clinical translation explicitly, and (iii) commit to quantitative, dated predictions and a preregistered update procedure.

---

## 3. Why recursive acceleration is plausible in 2026 — and why it might not be

### 3.1 AI resources are growing rapidly

Epoch AI reports that frontier language-model training compute has grown at roughly 5× per year since 2020, while the total stock of AI compute has grown around 3.4× per year since 2022. The same source estimates pre-training compute efficiency improving by roughly 3× per year [15].

These variables should not be interpreted as equivalent to intelligence. They are inputs into an innovation process.

### 3.2 Autonomy is becoming measurable

METR's task-completion time-horizon methodology measures the duration of tasks, in human expert time, that frontier agents can complete at specified success probabilities. It provides a more behaviourally meaningful metric than raw parameter count and allows longitudinal tracking of agent autonomy [16].

### 3.3 Autonomous laboratories close part of the physical loop

Self-driving laboratories combine robotics, experimental platforms and AI. A 2026 *Nature Reviews Chemistry* review describes a transition from narrowly focused automation to multipurpose systems in which algorithms can propose, execute and interpret experiments with limited human intervention [17].

This matters because purely computational intelligence cannot fully accelerate experimental science if physical validation remains serial and human-limited.

### 3.4 Energy is a hard constraint

The International Energy Agency projects global data-centre electricity demand to roughly double from about 485 TWh in 2025 to about 950 TWh in 2030 in its 2026 update, with consumption from AI-focused data centres roughly tripling over the same period [18].

Thus, abundant compute cannot be modelled independently of energy infrastructure.

### 3.5 Biomedical translation is entering new regimes

In June 2026 the first participant was dosed in a Phase I trial of ER-100, an experimental partial epigenetic reprogramming therapy using controlled OCT4, SOX2 and KLF4 expression, in patients with glaucoma or non-arteritic anterior ischemic optic neuropathy (NAION) [19, 20]. The trial primarily evaluates safety and tolerability, so it must not be interpreted as evidence that systemic rejuvenation has been achieved.

Its importance to this framework is different: a class of interventions previously discussed mainly at preclinical level has crossed into human testing. This creates a measurable translation milestone.

### 3.6 Evidence against

A framework built only from supportive signals would be selected to confirm itself. The following observations point the other way and must be treated as part of the baseline:

- **Falling research productivity.** Across many domains, more research effort has been needed per unit of progress for decades [6].
- **Eroom's law.** Drug R&D output per dollar declined for sixty years despite large technological gains in the tools of discovery [7].
- **Low clinical success rates.** Only a minority of programmes entering Phase I reach approval—roughly one in seven across therapeutic areas, and far fewer in oncology [21]. Faster discovery that feeds the same attrition funnel does not by itself accelerate medicine.
- **Biological timescales.** Trials whose endpoints are morbidity or mortality in ageing populations take years by construction. Computation does not shorten the time it takes to observe that people live longer.
- **Slow longevity trend.** Record period life expectancy has risen by about 0.25 years per calendar year for more than 160 years [22]. Any claim of acceleration in healthy lifespan must show a departure from this remarkably stable line.
- **Automation bottlenecks.** In task-based models, the tasks that resist automation come to dominate cost and time, which can cap growth even when most tasks are automated [9].

---

## 4. The Saka Law, stated formally

Let $T(t)$ denote a broad technological-capability state, and let $g(t) = \dfrac{d \ln T}{dt}$ be its growth rate.

Conventional progress can be represented as

$$
\frac{dT}{dt} = f(T, R),
$$

where $R$ represents research resources. Recursive technological acceleration appears when part of $T$ increases the productivity of the process producing future $T$:

$$
\frac{dT}{dt} = f\big(T, R, A(T)\big),
$$

where $A(T)$ is technological augmentation of discovery itself.

A positive second derivative, $\ddot{T} > 0$, is **not** sufficient evidence: any ordinary exponential trend satisfies it. The signature of recursive acceleration is a rising growth rate—super-exponential growth:

$$
\frac{dg}{dt} = \frac{d^2 \ln T}{dt^2} > 0,
$$

sustained while technology is materially increasing the productivity of research, design, experimentation, verification, manufacturing or deployment.

In the idea-production form of Section 2, research productivity is $\dot{A}/R^{\lambda} = \delta A^{\phi}$. Historical estimates imply that this has been falling [6], i.e. that ideas have become harder to find. The Saka Law can therefore be stated as an estimable claim:

> **Recursive acceleration holds in a domain when research productivity per unit of human and capital input stops declining and begins to rise—equivalently, when the effective feedback parameter $\phi$, re-estimated on rolling windows, trends upward, after automation of research inputs is accounted for.**

This condition is not expected to hold indefinitely. Energy, fabrication capacity, experiment duration, regulation, biological timescales, capital and safety constraints can reduce or reverse acceleration.

Accordingly, the stronger form of the Saka Law is not "technology is exponential". It is:

> **The growth regime of technology depends partly on the growth rate of the systems that generate validated technological knowledge.**

---

## 5. Historical Technology Acceleration Baseline (HTAB)

A forecasting system should first ask whether the present regime is actually unusual relative to history.

For historical metric $i$ measured at times $t_1 < t_2$, define its average log-growth rate:

$$
k_i = \frac{\ln\left(V_{i,t_2} / V_{i,t_1}\right)}{t_2 - t_1}.
$$

For declining-cost technologies, the ratio is inverted. In practice $k_i$ should be estimated by regression on the full series rather than from two endpoints, with a standard error.

Potential HTAB series include:

- semiconductor density and compute;
- supercomputer performance;
- genomic sequencing cost;
- battery cost per kWh;
- photovoltaic module cost per watt;
- telecommunications bandwidth and cost;
- industrial robot density;
- launch cost and annual mass to orbit.

**Selection bias.** Every series above is one that is already known to have improved dramatically. A baseline built only from successes will overstate historical growth in some respects and hide stagnation in others. The HTAB should therefore also include domains that slowed or stalled, for example new drugs approved per unit of R&D spending [7], crop yields, transport speed, and construction productivity. The weights $w_i$ and the list of series must be fixed before current data are compared with them.

The historical baseline is a weighted log-growth average:

$$
k_{HTAB} = \sum_i w_i\, k_i,
$$

which is not a claim that the entire economy improves at one rate. Its purpose is to create a null model:

$$
H_0 : k_{current} = k_{historical},
$$

against which a modern acceleration regime can be tested.

---

## 6. Technology Acceleration Ratio (TAR)

Define

$$
TAR(t) = \frac{k_{current}(t)}{k_{HTAB}}.
$$

Interpretation:

- $TAR < 1$: technological growth slower than the historical baseline;
- $TAR \approx 1$: similar to the historical baseline;
- $TAR > 1$: accelerated relative to baseline.

Because $k_{current}$ is estimated on short windows, it is noisy. TAR must always be reported with an uncertainty interval, and a claim of acceleration requires the lower bound of that interval to exceed 1. A sustained $TAR > 1$ across independent domains would be much stronger evidence than a short-lived burst in a single field.

---

## 7. Future Technology Acceleration Framework (FTAF)

### 7.1 State vector

The proposed state vector is

$$
X_t = [A, C, E, R, B, D, S, M, L]
$$

with each component normalized to its 2026 value (2026 = 1):

| Symbol | Component | Candidate operational proxy |
|---|---|---|
| $A$ | AI and scientific-reasoning capability | Composite index of sub-measures (see below); METR 50%-success task horizon [16] is one component |
| $C$ | Compute availability | Installed AI compute stock, FLOP/s [15] |
| $E$ | Energy abundance and reliability | Electricity supplied to data centres and labs, TWh/yr, adjusted for unmet interconnection requests [18] |
| $R$ | Robotics / laboratory automation | Experiments per researcher per year in tracked self-driving-lab domains |
| $B$ | Biotechnology maturity | Inverse cost per genome and per edited cell line; number of modality classes in human trials |
| $D$ | Data and measurement capability | Size of openly accessible longitudinal multi-omic cohorts |
| $S$ | Space accessibility | Inverse launch cost per kg to LEO; orbital research payload mass per year |
| $M$ | Manufacturing capacity | Advanced-node wafer starts per year; cell- and gene-therapy manufacturing capacity |
| $L$ | Clinical translation efficiency | Inverse of median time from IND filing to approval |

The proxies are proposals. Each must be fixed, together with its data source, before the first forecast is scored.

**Why $A$ needs its own sub-index.** The METR time horizon is measured mostly on software and machine-learning tasks. An agent that can work autonomously on code for forty hours does not necessarily have equivalent capability in biological or chemical research. Using it alone would turn one domain-specific benchmark into a stand-in for "scientific intelligence" in general. $A$ is therefore defined as a weighted geometric mean of normalized sub-measures:

$$
A_t = \prod_k a_{k,t}^{\,v_k}, \qquad \sum_k v_k = 1,
$$

with candidate components: autonomous task horizon (METR); research-level mathematics benchmarks (e.g. FrontierMath); formal theorem proving (share of target statements with machine-checked proofs); scientific hypothesis generation, scored by later experimental confirmation; experimental planning in the wet-lab sciences; and coding. The sub-weights $v_k$ are fixed at preregistration, and results are reported both for the composite and for each component.

### 7.2 Aggregation

The initial gross score is a weighted geometric mean:

$$
FTAF_t = A_t^{0.25}\, C_t^{0.15}\, E_t^{0.10}\, R_t^{0.10}\, B_t^{0.15}\, D_t^{0.05}\, S_t^{0.05}\, M_t^{0.05}\, L_t^{0.10}
$$

The weights sum to one and are provisional. They reflect the relative importance judged by the author, not an estimate, and must be sensitivity-tested. Because the thesis of this paper is that clinical translation is the binding constraint in biomedicine, a biomedical variant of the index should test a larger weight on $L$.

A weighted geometric mean is a Cobb–Douglas aggregate with an elasticity of substitution of exactly 1. That means a proportional gain in one component fully offsets the same proportional loss in another, weighted by the exponents; the index only collapses when a component goes to zero. It therefore encodes only weak complementarity. To represent genuine bottlenecks, the framework uses the constant-elasticity-of-substitution (CES) generalization

$$
FTAF_t = \left( \sum_j w_j\, X_{j,t}^{\rho} \right)^{1/\rho}, \qquad \sigma = \frac{1}{1-\rho},
$$

where $\sigma < 1$ means the components are complements and the weakest subsystem increasingly limits the whole, as in Baumol-type models [9]. The geometric mean is the limit $\rho \to 0$ ($\sigma = 1$), and a strict weakest-link (Leontief) aggregate is the limit $\rho \to -\infty$. The value of $\sigma$ is a key uncertain parameter and must be varied in the sensitivity analysis.

### 7.3 Levels, growth rates and acceleration

$FTAF_t$ is a **level** index and equals 1 in 2026 by construction. Evidence for the Saka Law concerns its growth rate, $g_F(t) = d \ln FTAF_t / dt$, and whether that growth rate is rising, $dg_F/dt > 0$. Throughout the paper, "acceleration" refers to the second quantity.

---

## 8. Friction, evidence and accessibility

Three correction terms prevent the framework from confusing technical demonstrations with societal impact. They act at different levels and are therefore kept separate.

### 8.1 Bottleneck & Risk Index (BPI) — system level

$BPI_t \in [0,1]$ represents constraints that are **not already measured** by the nine components, such as:

- regulatory delays not captured in $L$;
- poor scientific reproducibility;
- safety limitations;
- capital constraints;
- geopolitical disruption;
- diminishing returns to scaling.

Energy, fabrication and translation limits are already represented by $E$, $M$ and $L$ and must not be counted again in BPI.

The system-level effective index is

$$
F^{sys}_t = FTAF_t \, (1 - BPI_t).
$$

### 8.2 Evidence Maturity Score (EMS) — intervention level

A preclinical result should not carry the same forecasting weight as a replicated human endpoint. EMS is a property of a specific intervention or claim, not of the technological system as a whole, so it is **not** multiplied into $F^{sys}_t$. It is used instead to weight evidence when updating the arrival hazards of Section 12.

A provisional ordinal scale is:

$$
\text{hypothesis} < \text{in vitro} < \text{animal} < \text{human observational} < \text{controlled trial} < \text{large RCT} < \text{independent replication} < \text{clinical benefit}
$$

### 8.3 Diffusion & Accessibility Index (DAI) — intervention level

A therapy that exists but is unaffordable or capacity-constrained has limited population impact. DAI is also intervention-specific and includes:

- price;
- annual treatment capacity;
- geographic diffusion;
- reimbursement / coverage;
- manufacturing scale;
- time to access.

DAI converts the arrival of a therapy into its population-level effect (Section 12); it does not enter the system index.

---

## 9. Scientific throughput rather than paper count

A core prediction of the Saka Law is that the scientific cycle itself should compress.

For a closed experimental loop

$$
\text{hypothesis} \rightarrow \text{experiment} \rightarrow \text{data} \rightarrow \text{analysis} \rightarrow \text{new hypothesis},
$$

define Scientific Cycle Time as the latency of one full loop:

$$
SCT = t_{\text{new hypothesis}} - t_{\text{previous hypothesis}},
$$

and the Scientific Acceleration Factor

$$
SAF_{science} = \frac{SCT_{baseline}}{SCT_t}.
$$

Latency alone can be misleading: a laboratory can shorten each loop while running fewer loops. The framework therefore also tracks throughput, $Q_t$ = validated and independently replicated discoveries per unit time in a fixed domain. The primary output is $Q_t$, not publication volume.

An AI system producing one million low-quality hypotheses is not scientific acceleration if experimental validation and replication remain unchanged.

**AI attribution scale.** To count "AI-originated" discoveries (prediction P6), each discovery is graded by the role of AI systems in its intellectual work:

| Level | Role of AI |
|---|---|
| $AI_0$ | Auxiliary tool (search, writing, routine code) |
| $AI_1$ | Data analysis or modelling on a human-designed study |
| $AI_2$ | Partial hypothesis generation or experimental design, with humans leading |
| $AI_3$ | Principal scientific contribution: AI proposed the hypothesis *and* designed the decisive experiment or proof; humans executed, checked or supervised |
| $AI_4$ | Essentially autonomous discovery: AI proposed, executed (in silico or through automated laboratories) and interpreted the work, with humans limited to approval and verification |

Levels are assigned from author-contribution statements (e.g. CRediT roles) and methods sections by two independent coders blind to the prediction, with inter-rater agreement (Cohen's $\kappa$) reported. Disagreements are resolved to the lower level. Only $AI_3$ and $AI_4$ discoveries count toward P6.

---

## 10. Longevity Translation Index (LTI)

Longevity forecasting is particularly vulnerable to overinterpreting animal or biomarker studies.

The LTI therefore tracks interventions through

$$
L_0 \rightarrow L_1 \rightarrow L_2 \rightarrow L_3 \rightarrow L_4 \rightarrow L_5 \rightarrow L_6 \rightarrow L_7 \rightarrow L_8
$$

where $L_0$ = hypothesis, $L_1$ = in vitro, $L_2$ = animal, $L_3$ = large animal, $L_4$ = Phase I, $L_5$ = Phase II, $L_6$ = Phase III, $L_7$ = approval, and $L_8$ = clinically meaningful or mortality benefit.

The model should estimate transition probabilities and transition times between levels, using historical baselines such as [21].

Two methodological requirements apply to these estimates and to predictions P7 and P8:

- **Composition bias.** A change in the mix of programmes can move averages without any change in the process: if many simple drugs and few oncology drugs enter development, median time to approval falls even if nothing improved. Comparisons are therefore made *within* strata of the same therapeutic area and the same modality (small molecule, biologic, cell therapy, gene therapy, etc.), between cohorts defined by the year of IND filing, and then combined with fixed stratum weights.
- **Censoring.** Many programmes in recent cohorts will still be unresolved when a window closes. Excluding them would bias recent times downward (only fast successes are observed). Times to approval are therefore estimated with survival analysis—Kaplan–Meier curves and Cox models with therapeutic area and modality as covariates—and phase progression with a multistate model ($L_4 \rightarrow L_5 \rightarrow L_6 \rightarrow L_7$, with failure as a competing absorbing state).

A major acceleration in ageing-biology papers with no reduction in $L_1 \rightarrow L_8$ translation time, and no improvement in transition probabilities, would argue against strong biomedical recursive acceleration.

---

## 11. Longevity Escape Velocity proxy

Longevity escape velocity (LEV) [23] can be represented in two related ways, which must not be mixed. They are not equivalent as observed quantities: one is a population measure, the other depends on an individual's own risk trajectory.

**Period definition (used by this framework).** Let $HALE_x(t)$ be the period healthy-life expectancy at a fixed age $x$ (for example 65) in calendar year $t$, computed from that year's age-specific health and mortality rates. Define

$$
LEV_x(t) = \frac{\partial\, HALE_x(t)}{\partial t}.
$$

Interpretation:

- $LEV_x < 0$: healthy-life expectancy at age $x$ is falling;
- $0 < LEV_x < 1$: medical progress offsets part of ageing; a person who ages one year gains less than one year of expected healthy life;
- $LEV_x \ge 1$: the healthy-life-expectancy frontier moves outward by at least one year per elapsed year—the operational definition of longevity escape velocity in this framework.

**Individual representation.** For a person aged $a(t)$, let $h(t)$ be their *remaining* expected healthy life. Ageing alone makes $h$ fall over time, so escape velocity corresponds to $dh/dt \ge 0$, not $\ge 1$. Using remaining life expectancy with a threshold of 1 would double-count the passage of time. Because $h_i(t)$ depends on the person's own health and risk, it cannot be read directly from period life tables; the two quantities agree only for an individual whose risk matches the population's at each age.

**Reference point, not an estimate.** Record period life expectancy *at birth* has risen by about 0.25 years per year for more than 160 years [22]. That is a reference for the frontier of total life expectancy; it is not an estimate of $LEV_{65}$, which is a different series (healthy rather than total life, at age 65 rather than at birth, and in a given population rather than the record-holding one). Healthy-life expectancy has generally grown more slowly than total life expectancy. The current empirical value of the proxy must be estimated from fixed-age HALE series, and establishing that baseline is one of the first data tasks of the framework.

This is an operational forecasting proxy rather than an accepted clinical metric. The framework does not claim that $LEV_x \ge 1$ has been achieved.

---

## 12. The Technology Survival Ladder

Long-range longevity forecasts should not require a single future "cure for ageing".

Instead, an individual may encounter sequential generations of treatment:

$$
\text{Therapy}_1 \rightarrow \Delta HLE_1 \rightarrow \text{Therapy}_2 \rightarrow \Delta HLE_2 \rightarrow \text{Therapy}_3
$$

If earlier interventions preserve enough function to reach later, more capable interventions, a ladder effect emerges.

For intervention class $j$, define the arrival hazard of clinical availability:

$$
\lambda_j(t) = \lambda_{0,j} \left[ F^{sys}_t \right]^{\alpha_j} G_j(t),
$$

where $\lambda_{0,j}$ is the baseline hazard in 2026, $\alpha_j$ the sensitivity of class $j$ to system-wide technological progress, and $G_j(t)$ a readiness factor determined by the class's current LTI level and the historical transition probabilities out of that level. Evidence about the class, weighted by EMS, updates $G_j$.

The cumulative arrival probability from 2026 ($t = 0$) to time $T$ is

$$
P_j(T) = 1 - \exp\left( - \int_0^T \lambda_j(t)\, dt \right).
$$

Population impact is then $P_j(T)$ multiplied by the class's projected $DAI_j$.

In version 0.2, $\lambda_{0,j}$, $\alpha_j$ and $G_j$ are not estimated. Doing so requires the LTI transition data described in Section 10. This should be interpreted as technology-arrival forecasting, not as a personalized survival probability.

---

## 13. Space as an experimental multiplier

Space is included with a relatively modest weight because biomedical progress does not require orbital laboratories. However, cheaper and more frequent launch could add experimental regimes difficult to reproduce on Earth:

- prolonged microgravity;
- altered fluid dynamics;
- radiation environments;
- protein crystallization;
- tissue and organoid growth;
- closed-loop autonomous biological experiments.

If reusable launch systems substantially reduce cost and increase cadence, the space term $S_t$ may undergo a measurable change point.

The value of space in the framework is therefore not speculative colonization; it is **expansion of experimental state space**. With a weight of 0.05, however, its effect on the index is small, and it could be moved to future work without changing the main results.

---

## 14. Energy as a cognitive-infrastructure constraint

AI systems transform electricity into computational work. Large-scale scientific agents, simulation and automated laboratories therefore depend on physical energy infrastructure.

The IEA's 2026 update emphasizes both rapidly improving energy efficiency per AI task and rapidly increasing aggregate demand from more intensive applications [18].

This creates a feedback structure:

$$
\text{Energy} \rightarrow \text{Compute} \rightarrow \text{AI} \rightarrow \text{Science} \rightarrow \text{better energy technology}
$$

Such a loop can accelerate, but transmission grids, generation capacity, transformers, storage and permitting can impose long delays.

---

## 15. Twenty-year scenario: 2026–2046

This section is explicitly speculative.

A naive continuation of recent AI growth rates would produce implausibly enormous multipliers. The Saka framework therefore assumes declining log-growth rates and explicit bottlenecks.

A reasonable scenario family for FTAF should include:

- **conservative:** rapid near-term growth followed by strong saturation;
- **central:** sustained AI/science acceleration with progressively declining growth rates;
- **aggressive:** major breakthroughs in AI, automation, energy or manufacturing that extend the high-growth regime.

Version 0.3.1 does not attach numbers to these scenarios. They will be quantified once the proxies of Section 7.1 have been populated.

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

## 16. 2046–2076 and the longevity question

Forecast uncertainty becomes extreme beyond 2046.

The relevant comparison is between the rate of ageing and the rate of medical progress, summarized by the proxy $LEV_x(t)$ of Section 11.

By 2076, a successful recursive-acceleration regime could plausibly produce periodic repair across multiple biological subsystems rather than a single rejuvenation treatment.

However, several problems may remain especially difficult:

- preserving brain information while rejuvenating neural tissue;
- preventing cancer under increased regenerative capacity;
- maintaining long-term genomic and epigenomic stability;
- controlling immune ageing without creating autoimmunity;
- proving that biomarker changes translate into morbidity and mortality reduction.

The framework therefore treats "systemic rejuvenation" and "longevity escape velocity" as high-uncertainty events rather than inevitable outcomes.

---

## 17. Predictions that make the framework falsifiable

The qualitative predictions of version 0.1 are replaced by dated, quantitative ones.

**This version is not the preregistration.** Version 0.3.1 fixes the *form* of each prediction and the rule for deriving its threshold, but not the thresholds themselves. The preregistration is made when that rule has been applied to historical data and the resulting numbers are frozen, with a timestamp, in a public file (planned: `forecasts/preregistration-2026.json`), before any data from the tested windows are examined.

**Windows.** Each window starts on the date the preregistration is frozen, not on 1 January 2026; data observed before that date are used only to estimate baselines. The window labels below (2026–2031, 2026–2036) are nominal and assume a freeze in late 2026.

**Status of the thresholds.** The numbers below (for example $TAR > 1.5$ or a 50% fall in SCT) are **placeholders chosen as plausible magnitudes, not derived values**. Before preregistration, each threshold must be derived from two inputs:

1. *Historical variability*: the distribution of the same statistic over past windows of the same length, so that a threshold is exceeded with at most 5% probability if the historical regime continues; and
2. *Minimum relevant effect*: the smallest change that would matter scientifically or clinically.

The preregistered threshold is the larger of the two. This turns the predictions from subjective cut-offs into statistical tests.

**Intervals.** All estimates are reported with 50%, 80%, 90% and 95% intervals. The **90% interval** is preregistered as the decision criterion: "lower bound above 1" or "interval excluding 0" below refers to it.

**Supporting predictions.** If recursive acceleration is real, then:

| # | Prediction | Window | Supports the hypothesis if… |
|---|---|---|---|
| P1 | Cross-domain acceleration | 2026–2031 | $TAR > 1.5$, with the lower bound of its 90% interval above 1, in at least 3 of the HTAB domains |
| P2 | Rising growth rate | 2026–2031 | Estimated $dg_F/dt > 0$ for FTAF, with its 90% interval excluding 0 |
| P3 | Research productivity reverses | 2026–2036 | Research productivity (in the sense of [6]) rises in at least 2 of the domains studied there |
| P4 | Autonomy keeps growing | 2026–2031 | The METR 50% time-horizon doubling time stays at or below 12 months, and the composite $A$ index keeps rising in its non-software components |
| P5 | Faster experimental loops | 2026–2031 | Median SCT falls by at least 50% in at least 2 tracked self-driving-lab domains, with no fall in $Q_t$ |
| P6 | Replicated AI discoveries | 2026–2031 | The annual number of independently replicated discoveries graded $AI_3$ or $AI_4$ (Section 9) at least doubles |
| P7 | Faster translation | 2026–2036 | Median IND-to-approval time, estimated by survival analysis within therapeutic area × modality strata (Section 10), falls by at least 20% relative to 2015–2025 IND cohorts in at least one therapeutic area |
| P8 | Better clinical success | 2026–2036 | Phase I-to-approval success probability, estimated with a multistate model within therapeutic area × modality strata (Section 10), improves by at least 30% relative to [21] in at least one therapeutic area |

**Refuting outcomes.** The hypothesis should be weakened or rejected as a useful forecasting framework if, by the end of the relevant window:

- $TAR$ is not distinguishable from 1 in a majority of HTAB domains (P1 fails);
- AI benchmark and autonomy metrics keep improving (P4 holds) while SCT, $Q_t$ and replication rates do not (P5 and P6 fail);
- clinical translation times and success probabilities are statistically unchanged (P7 and P8 fail);
- $LEV_{65}(t)$ for the largest high-income populations shows no increase over its own 2000–2025 trend through 2046;
- persistent energy, fabrication, regulatory or biological bottlenecks explain most of the shortfall.

Failure of P7, P8 and the LEV criterion while P1–P6 succeed would support recursive acceleration in computation and discovery but refute its extension to biomedicine—itself an informative result.

---

## 18. Forecasting protocol

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

Three technical cautions apply:

- A power law $y = a t^b$ depends on where $t = 0$ is placed; the origin must be fixed in advance and reported.
- Logistic curves fitted before the inflection point are poorly identified: the ceiling $L$ is essentially unconstrained. Logistic fits should report the profile likelihood of $L$ rather than a point estimate.
- AIC and BIC can only compare models fitted to the same response on the same scale with the same error structure; models fitted in levels and in logs must be compared by out-of-sample error instead.

### Monte Carlo

Simulate at least $10^5$ futures with distributions over:

- growth-rate decay;
- breakthrough probabilities;
- the elasticity of substitution $\sigma$ between subsystems;
- energy constraints;
- AI reliability;
- experimental throughput;
- regulatory timelines;
- clinical success probabilities.

Predictions should be scored retrospectively using Brier scores [24] where possible.

---

## 19. Discussion

The principal contribution of the Saka Law framework is not a claim that technology will grow exponentially forever, nor the idea that knowledge feeds back into its own production, which has a long history in growth economics [3–5, 9]. It is the proposal that **research productivity itself should be measured as an endogenous technological variable, across several physical and institutional subsystems, against a preregistered baseline**.

This changes long-range forecasting.

In a non-recursive model, the future is estimated mainly from the current stock of technology.

In a recursive model:

$$
\text{Future technology} = f\big(\text{current technology},\ \text{technology's ability to improve discovery}\big)
$$

If scientific cognition, experiment execution, measurement and manufacturing all become increasingly automated, technological progress may depart from historical baselines.

But a recursive process is not necessarily an explosive one. Real systems can settle into logistic, piecewise or bottleneck-limited regimes, and the evidence of falling research productivity [6, 7] means the burden of proof lies with the acceleration hypothesis.

The empirical task is therefore to measure the curvature of $\ln T$, not of $T$.

---

## 20. Conclusion

The Saka Law is proposed as a testable hypothesis of recursive technological acceleration:

> **When technology materially improves the processes that generate, validate and deploy new technology, the growth rate of technological progress can rise relative to its historical baseline, until constrained by physical, biological, economic or institutional bottlenecks.**

The Future Technology Acceleration Framework attempts to measure this effect across AI, compute, energy, robotics, biotechnology, measurement, space, manufacturing and clinical translation.

Its longevity application replaces deterministic predictions of "curing ageing" with a measurable sequence:

$$
\text{scientific acceleration} \rightarrow \text{biomedical translation} \rightarrow \text{functional repair} \rightarrow \text{healthy-life extension} \rightarrow \text{access to later therapies}
$$

The hypothesis will become scientifically useful only if its metrics are populated with reproducible data, its forecasts are preregistered, and its failures are recorded as rigorously as its successes.

---

## References

1. OpenAI. **On the Navier–Stokes Millennium Prize Problem.** 8 September 2026. https://openai.com/index/navier-stokes-solution/

2. Quanta Magazine. **AI Has Solved One of Math's \$1 Million Millennium Prize Problems.** 8 September 2026. https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/

3. Romer, P. M. **Endogenous technological change.** _Journal of Political Economy_ 98(5), S71–S102 (1990).

4. Jones, C. I. **R&D-based models of economic growth.** _Journal of Political Economy_ 103(4), 759–784 (1995).

5. Kremer, M. **Population growth and technological change: One million B.C. to 1990.** _Quarterly Journal of Economics_ 108(3), 681–716 (1993).

6. Bloom, N., Jones, C. I., Van Reenen, J. & Webb, M. **Are ideas getting harder to find?** _American Economic Review_ 110(4), 1104–1144 (2020).

7. Scannell, J. W., Blanckley, A., Boldon, H. & Warrington, B. **Diagnosing the decline in pharmaceutical R&D efficiency.** _Nature Reviews Drug Discovery_ 11, 191–200 (2012).

8. Kurzweil, R. **The Law of Accelerating Returns.** Essay, 2001.

9. Aghion, P., Jones, B. F. & Jones, C. I. **Artificial intelligence and economic growth.** In Agrawal, A., Gans, J. & Goldfarb, A. (eds.), _The Economics of Artificial Intelligence: An Agenda_, University of Chicago Press (2019).

10. Nordhaus, W. D. **Are we approaching an economic singularity? Information technology and the future of economic growth.** _American Economic Journal: Macroeconomics_ 13(1), 299–332 (2021).

11. Davidson, T. **Could advanced AI drive explosive economic growth?** Open Philanthropy report (2021).

12. Erdil, E. & Besiroglu, T. **Explosive growth from AI automation: A review of the arguments.** arXiv:2309.11690 (2023).

13. Nagy, B., Farmer, J. D., Bui, Q. M. & Trancik, J. E. **Statistical basis for predicting technological progress.** _PLoS ONE_ 8(2), e52669 (2013).

14. Farmer, J. D. & Lafond, F. **How predictable is technological progress?** _Research Policy_ 45(3), 647–665 (2016).

15. Epoch AI. **Trends in Artificial Intelligence.** Updated 2026. https://epoch.ai/trends

16. METR. **Task-Completion Time Horizons of Frontier AI Models.** Updated 8 May 2026. https://metr.org/time-horizons/

17. Canty, R. B. & Abolhasani, M. **The past, present and future of self-driving laboratories.** _Nature Reviews Chemistry_ 10, 523–537 (2026). https://doi.org/10.1038/s41570-026-00847-2

18. International Energy Agency. **Key Questions on Energy and AI.** 2026. https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary

19. Life Biosciences. **Life Biosciences Announces First Patient Dosed in Phase 1 Trial of ER-100 for Optic Neuropathies.** 9 June 2026. https://www.lifebiosciences.com/life-biosciences-announces-first-patient-dosed-in-phase-1-trial-of-er-100-for-optic-neuropathies/

20. ClinicalTrials.gov. **NCT07290244: Evaluating ER-100 for Safety in People With Glaucoma or Non-Arteritic Anterior Ischemic Optic Neuropathy.** https://clinicaltrials.gov/study/NCT07290244

21. Wong, C. H., Siah, K. W. & Lo, A. W. **Estimation of clinical trial success rates and related parameters.** _Biostatistics_ 20(2), 273–286 (2019).

22. Oeppen, J. & Vaupel, J. W. **Broken limits to life expectancy.** _Science_ 296(5570), 1029–1031 (2002).

23. de Grey, A. D. N. J. **Escape velocity: Why the prospect of extreme human life extension matters now.** _PLoS Biology_ 2(6), e187 (2004).

24. Brier, G. W. **Verification of forecasts expressed in terms of probability.** _Monthly Weather Review_ 78(1), 1–3 (1950).

25. International Energy Agency. **Energy and AI.** 2025. https://www.iea.org/reports/energy-and-ai

---

## Changes from version 0.3

- Intervals: 90% added to the reported set (50/80/90/95%), since it is the decision criterion.
- Stated explicitly that this version is not the preregistration; windows start when the thresholds are frozen, not on 1 January 2026.
- Added the $AI_0$–$AI_4$ attribution scale, with coding procedure; P6 counts only $AI_3$ and $AI_4$.
- P7 and P8: comparisons within therapeutic area × modality strata and IND-year cohorts to control composition bias; survival analysis (Kaplan–Meier, Cox) and multistate models to handle censored programmes.

## Changes from version 0.2

- LEV: the 0.25 years/year trend is now presented as a reference for record life expectancy at birth, not as an estimate of $LEV_{65}$; the fixed-age HALE baseline is to be estimated from data. The two LEV forms are described as related, not equivalent. The LEV refutation criterion is now relative to its own historical trend.
- Prediction thresholds are marked as placeholders, with a rule for deriving them from historical variability and minimum relevant effect.
- Intervals: 50/80/95% reported; the 90% interval is preregistered as the decision criterion (previously 80%).
- $A$ is now a composite index; the METR time horizon is one component rather than the whole proxy.

## Changes from version 0.1

- Restated the law as a claim about the **growth rate** of technology (super-exponential growth, rising research productivity) instead of $\ddot{T} > 0$, which any exponential satisfies.
- Added related work (idea-production function, falling research productivity, Eroom's law, AI and explosive growth) and a subsection of evidence against the hypothesis.
- Corrected the LEV proxy: it is now defined on period healthy-life expectancy at a fixed age with threshold 1, and the equivalent individual definition with threshold 0 is stated; added the historical reference of about 0.25 years per year.
- Clarified that a weighted geometric mean has unit elasticity of substitution and added a CES generalization with $\sigma$ as a sensitivity parameter.
- Separated system-level friction (BPI) from intervention-level evidence (EMS) and accessibility (DAI); removed double counting of energy, fabrication and translation in BPI.
- Defined $G_j(t)$ in the arrival hazard (previously $M_j$, which clashed with manufacturing).
- Added a table of candidate operational proxies for the nine components.
- Replaced qualitative predictions with dated, quantitative, preregistrable thresholds.
- Added selection-bias, uncertainty-interval and model-comparison cautions to HTAB, TAR and the fitting protocol.
- Made the Navier–Stokes and ER-100 descriptions precise.
- Fixed mathematical notation so equations render on GitHub.

---

## Disclosure

This document is a conceptual forecasting framework developed through human–AI collaboration. Named indices, weights, thresholds and long-range scenarios are proposals for testing, not established scientific standards. Biomedical sections are not medical advice and do not assert that ageing has been or will be cured.
