# Quantum Simplex Estimation

**Can quantum variance reduction return a genuine probability distribution in every run while remaining exactly unbiased?** This project gives a constructive answer for every finite output alphabet, including zero and arbitrarily rare probabilities.

Given a reversible source circuit and its inverse, the algorithm returns a classical random vector $`Z`$ satisfying, for $`d\ge2`$ outcomes and scale $`T\ge1`$,

```math
Z\in\Delta_d,\qquad
\mathbb EZ=p,\qquad
\mathbb E\|Z-p\|_2^2\le\frac{32(d-1)}{T^2},
\qquad
\mathbb EQ\le(C_{\rm prep}+C_{\rm ref})(d-1)T.
```

Here $`\Delta_d`$ is the set of nonnegative $`d`$-coordinate vectors summing to one, and $`Q`$ counts every source and inverse call, including failed attempts and rewinding. The constants are universal valid bounds for the stated conditional operations. The theorem has an **expected query bound with an unbounded stopping-time tail**. Exactness assumes ideal gates and exact mathematical readouts. [A separate capped implementation](science/precision-and-resources.md) preserves the simplex with controlled bias.

At a fixed alphabet size, root mean squared error $`\varepsilon`$ needs $`O_d(\varepsilon^{-1})`$ expected source calls; ordinary categorical sampling needs $`\Theta(\varepsilon^{-2})`$ samples for the same worst-case objective. Quantum multivariate precision and exact unbiased vector estimation are already established. The addition is keeping **positivity, normalization and exact unbiasedness together**. The displayed dependence on $`d`$ is not optimal distribution-estimation complexity.

## How the construction works

A binary tree splits the total probability mass into label masses. Each node receives a random estimated global weight $`W`$ and chooses its scalar clock in proportion to $`TW`$. A conditional reflection of true subset mass $`s`$ costs $`O(1/s)`$ expected source calls, but exact unbiasedness gives $`\mathbb EW=s`$. The random budget cancels that inverse-mass cost. A minimum positive sine-clock readout separately pays for preparing the conditional specimen. The [proof](science/simplex-estimator.md) includes both parts.

The scalar sine estimator is [inherited](science/scalar-clock.md). The conditional-reflection circuit is built explicitly from the original source using block encoding, oblivious amplification and input-restoring measured retries. A postselected state is never assumed to come with a free inverse.

## Read the science

Start with the [scientific route](science/README.md) or the [model and exact theorem](science/model.md).

| To inspect | Read |
| --- | --- |
| Algorithm, boundary cases, minimum weights and martingale proof | [Simplex estimator](science/simplex-estimator.md) |
| Exact conditional circuit, coherent controls and reference preservation | [Conditional reflection](science/conditional-reflection.md) |
| Finite execution cap, gate synthesis, rounding, gates and workspace | [Precision and resources](science/precision-and-resources.md) |
| Quantum and classical expected-work precision comparisons | [Lower bounds](science/lower-bounds.md) |
| Convex constraints, unbiased stochastic products and stable propagation | [Convex composition](science/convex-composition.md) |
| Closest prior results and imported ingredients | [Related work](references/related-work.md) and [bibliography](references/references.bib) |

The convex-range consequence preserves known affine constraints and positivity in each realization. Fresh unbiased random transition matrices preserve the mean evolution; for contracting mean dynamics their distribution-vector errors satisfy a stable variance bound. Reusing one random table under powers generally introduces bias. These results concern probability objects and their mean-square error, not a faster trajectory sampler or a demonstrated hardware advantage.

## Learn the construction

The [learning route](learning/README.md) starts from Andrew M. Childs's *Lecture Notes on Quantum Algorithms*, 17 April 2025. The [source-to-project bridge](learning/anchor-bridge.md) identifies the relevant foundations and supplies the missing links to this construction. The [30-milestone map](learning/milestones.md) follows the argument from reversible sources to the full estimator and its limits.

## Reproduce the finite checks

```bash
python3 verification/run_all.py
```

The [verification guide](verification/README.md) lists dependencies and the finite scope. It checks scalar moments with complex source garbage, complete finite tree laws, the actual controlled LCU and retry Kraus maps, and fresh-versus-reused stochastic tables. Floating-point checks support their tested cases; analytical proofs establish the uniform theorems.

## Scope

Source preparation, its matching inverse, known subset predicates, initialized program workspace, clock gates and returned output are charged. No QRAM or free data loading is assumed. The returned object is a classical probability vector; the construction does not supply a coherent normalized table oracle across different source instances. The classical comparison receives samples, while a classical algorithm exploiting a supplied circuit's code may have additional capabilities.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
