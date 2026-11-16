# Related work and the contribution retained here

The problem is to output a classical random probability vector whose coordinates are nonnegative, sum to one in every realization, and have exactly the desired means. At fixed alphabet size, its mean-square error decreases quadratically with the expected number of coherent source calls. Each qualification matters: multivariate estimation, the Heisenberg precision exponent and exact quantum debiasing are already established.

## 1. Multidimensional probability estimation

[Joran van Apeldoorn (TQC 2021)](https://doi.org/10.4230/LIPIcs.TQC.2021.9) gives multidimensional amplitude estimation from a probability-source unitary and its inverse. Theorem 5 and the subsequent reductions establish approximate distribution estimation with near-optimal query bounds for several norms. Section 2.2.3, Lemma 8 explicitly turns coordinate estimates into a probability vector by clipping, thresholding and redistributing mass. Its guarantee is approximation with high probability; the redistribution does not promise exact coordinate means. Thus simplex-valued quantum estimation itself is prior work.

[Cornelissen, Hamoudi and Jerbi (STOC 2022)](https://doi.org/10.1145/3519935.3520045) develop near-optimal multivariate mean estimation in Euclidean norm, including the transition between low- and high-dimensional regimes. [Tang (2025, v3)](https://arxiv.org/abs/2504.06940v3) improves logarithmic overheads using generalized Grover operators; Theorems I.2–I.3 and IV.9 give high-probability error guarantees, and Algorithms 5 and 7 use coordinatewise median readout. These results address accuracy and resources, with no joint exact-unbiasedness and convex-range guarantee used here. The present estimator does not improve their optimal dependence on dimension.

## 2. Exact unbiased vector estimates already exist

[Sidford and Zhang (NeurIPS 2023)](https://papers.neurips.cc/paper_files/paper/2023/hash/6ed9931d6e1fb6a85efa1b2c014a47e1-Abstract-Conference.html), Section 2, Theorem 4, gives an exactly unbiased estimate of a vector mean with mean-square error at most $`\sigma^2`$ in expected $`\widetilde O(L\sqrt d/\sigma)`$ source queries, where the input trace variance is at most $`L^2`$. Their Algorithm 1 removes bias through a geometric random level and signed telescoping correction

```math
\widehat\mu=\widetilde\mu_0+
2^J(\widetilde\mu_J-\widetilde\mu_{J-1}).
```

This is exactly unbiased, but need not remain in the convex range even when its constituent estimates do. It supplies an essential baseline: neither vector unbiasedness nor expected-work Heisenberg scaling is a new claim here.

[Luo, Liu, Allcock, Zhang and Lui (2026)](https://arxiv.org/abs/2607.25492) extend this approach to heavy-tailed multivariate means. The displayed Algorithm 2 in [v1](https://arxiv.org/abs/2607.25492v1) again uses signed geometric-level extrapolation; Theorem 3.7 controls the error moment and expected queries. Their [QTML 2026 extended abstract](https://indico.nithecs.ac.za/event/12/contributions/506/) formulates exact mean and moment requirements and identifies generalized multilevel Monte Carlo as the debiasing mechanism. Those stated guarantees do not assert simplex containment. This comparison concerns that explicit construction and those guarantees, not an exhaustive classification of all possible estimators in the work.

The distinction can be expressed as follows.

| Earlier capability | Requirement additionally met here |
|---|---|
| Accurate probability vector after nonlinear repair | Exact mean for every coordinate, without repair |
| Exactly unbiased vector with signed extrapolation | Nonnegative, normalized output in every realization |
| Exactly unbiased bounded scalar probability | A jointly valid finite-alphabet vector from the original paid source |

## 3. The bounded scalar estimator is an inherited foundation

The sine-clock/discrete-sine-transform construction in [Lin, *Bounded Unbiased Amplitude Estimation*, revision 940e1e99](https://github.com/GoGoKo699/Bounded-Unbiased-Amplitude-Estimation/tree/940e1e99b3d7b7b0be39eb6bcc1ea41fdf110101) supplies

```math
0\le Z_M\le1,\qquad
\mathbb E Z_M=p,\qquad
\operatorname{Var}(Z_M)=\kappa_Mp(1-p),\qquad
\kappa_M=\frac{M-1}{M+1}\tan^2\frac{\pi}{M+1}.
```

Its endpoint determinism, minimum positive readout and efficient dyadic clocks are also inherited. The present work uses those facts rather than reclassifying them as a new scalar result. Earlier work such as [Cornelissen and Hamoudi (SODA 2023)](https://doi.org/10.1137/1.9781611977554.ch46) already develops nearly unbiased mean estimation, state restoration and applications to products of normalizer ratios; these are further antecedents for composition-aware estimation.

The new constructive issue is normalization inside a split. Postselecting a source on a subset prepares a conditional specimen, but does not give a coherent inverse or a reflection about that normalized state. The [conditional-reflection construction](../science/conditional-reflection.md) implements the required controlled reflection from the original source and known subset tests in expected inverse-mass work. The [simplex algorithm](../science/simplex-estimator.md) chooses each local budget from the random mass assigned to its node. Exact conditional means preserve unbiasedness, and the random-mass weighting controls the inverse-mass expected cost even near the boundary. Independent coordinate estimation followed by renormalization does not supply this argument.

## 4. Standard primitives underlying the reflection

The common-singular-value block encoding uses standard projector encodings and linear combination of unitaries. Oblivious amplification follows [Berry, Childs, Cleve, Kothari and Somma (2014), Lemma 3.6](https://arxiv.org/abs/1312.1414v2). The randomized unknown-angle amplification schedule follows [Boyer, Brassard, Høyer and Tapp (1998), Section 4](https://arxiv.org/abs/quant-ph/9605034). Alternating forward/inverse projective restoration is related to the state-preserving amplification and rewinding framework of [Marriott and Watrous (2005)](https://doi.org/10.1007/s00037-005-0194-x); the specific two-dimensional calculation is given in full in this repository.

[Guerreschi (2019)](https://doi.org/10.1103/PhysRevA.99.022306) explains the amplitude distortion caused by naively controlling a repeat-until-success circuit. Here the complete controlled reflection has one common scalar success amplitude on both control branches before amplification. The construction does not control an already measured routine whose two branches succeed at different rates. These primitives and warnings are credited ingredients, not separate discoveries attributed to this project.

## 5. Operational scope

The resulting capability is quantum variance reduction within a known finite classical convex range. Its [convex and stochastic-operator consequences](../science/convex-composition.md) preserve positivity, normalization and applicable linear constraints in every run while retaining the exact mean. Fresh stochastic matrices compose with the correct mean product; under an explicit contraction assumption on their mean matrices, their distribution-vector error obeys a stable variance recurrence.

These propagation identities are elementary consequences of conditional expectation and the simplex theorem. They do not assert a new mixing principle or an unrestricted trajectory-sampling speedup. Sampling a label directly from the supplied source already takes one source execution. Reusing the same random table in nonlinear powers can introduce bias. The algorithm has unbounded stopping tails, and finite precision or noise requires a separate approximation budget. The [lower-bound discussion](../science/lower-bounds.md) keeps the fixed-dimension precision conclusion separate from the unresolved optimal joint dependence on dimension.

Bibliographic data are collected in [references.bib](references.bib).
