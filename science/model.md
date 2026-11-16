# Model: a random probability vector that remains a probability vector

An empirical frequency vector has three useful properties at once: its entries are nonnegative, they sum to one in every realization, and their expectations equal the underlying probabilities. Ordinary quantum probability estimation can improve precision, but clipping or renormalizing its output generally changes the expectation. The problem here is to retain all three properties while reducing the mean squared error quadratically in the expected coherent source work.

The [construction and proof](simplex-estimator.md) establish this for every finite output alphabet. The accounting includes the conditional states and conditional reflections needed inside the construction. A postselected specimen is never treated as a supplied reversible conditional sampler.

## 1. Source and labels

Let $`U`$ be an available unitary on $`n`$ qubits, with access also to its exact inverse. The full source register includes all workspace and garbage used by its implementation. On its initialized input it prepares

```math
|\psi\rangle=U|0^n\rangle
=\sum_{i=1}^{d}|i\rangle|\gamma_i\rangle,
\qquad
p_i=\langle\gamma_i|\gamma_i\rangle,
\qquad
\sum_{i=1}^{d}p_i=1.
```

The vectors $`|\gamma_i\rangle`$ need not be normalized, known, mutually orthogonal, or equal. The label register makes the corresponding sectors orthogonal. Thus arbitrary source garbage is allowed, provided it remains part of the register on which $`U`$ and $`U^\dagger`$ act. The output distribution is

```math
p=(p_1,\ldots,p_d)\in\Delta_d,
\qquad
\Delta_d=\left\{x\in\mathbb R^d:x_i\ge0,\ \sum_i x_i=1\right\}.
```

Fix any known binary tree with these $`d`$ labels as leaves. Every internal node $`S`$ denotes the labels below it and has children $`L`$ and $`R`$. Its exact projector and true probability mass are

```math
\Pi_S=\sum_{i\in S}|i\rangle\langle i|\otimes I,
\qquad
s_S=\langle\psi|\Pi_S|\psi\rangle=\sum_{i\in S}p_i.
```

The reflections and measurements of these known label predicates are implemented and charged. For example, an ordered balanced tree uses known interval or prefix predicates on the label register. An arbitrary label-classification program must likewise be compiled and paid for. The formulation also permits known orthogonal projectors in place of the explicit label register when the required subset tests are implemented.

## 2. Allowed work and charged resources

The ideal algorithm may initialize clean workspace, perform known exact unitary gates and projective measurements, reset measured workspace, and use classical randomness and feedback. It uses $`U`$ and $`U^\dagger`$ on complete source-sized registers. One invocation of either counts as one original-source query. An independently supplied controlled-$`U`$ oracle is unnecessary: the required controlled conjugated projectors use unconditional $`U/U^\dagger`$ pairs around controlled known operations.

The principal theorem counts expected original-source queries. Every inverse, failed amplification attempt, rewind, and fresh conditional specimen is included. Native source gates, subset predicates, all-zero tests, LCU signals, sine-clock circuits, measurements, classical control, and returned output are additional implementation costs. No QRAM, amplitude lookup table, unknown conditional inverse, or data-loading oracle is supplied for free. A succinct reversible source circuit can be used directly; preparing that circuit's input and implementing it still belong in a complete application ledger.

The output is a **classical vector**, not a coherent preparation of its square roots. The subset at each invocation is a classical node already chosen by the algorithm. The construction does not promise to preserve a superposition over different sources or different subset masses.

## 3. Required output and error

For a precision parameter $`T\ge1`$, the algorithm returns $`\widehat p`$ satisfying

```math
\widehat p\in\Delta_d\quad\text{on every terminating history},
\qquad
\mathbb E_p\widehat p=p.
```

The error is the total Euclidean mean squared error, equivalently the trace of the covariance because the estimator is unbiased:

```math
\mathcal R_2(p)
=\mathbb E_p\|\widehat p-p\|_2^2
=\sum_{i=1}^{d}\operatorname{Var}_p(\widehat p_i).
```

Exact normalization refers to the complete returned vector, rather than separately normalized coordinates in expectation. In particular, if $`p_i=0`$, positivity and unbiasedness require $`\widehat p_i=0`$ almost surely. The construction respects these faces without knowing which probabilities vanish.

All exact statements use ideal gates and exact mathematical readouts, as in the inherited scalar sine estimator. A physical finite-precision implementation needs the separate [precision and resources account](precision-and-resources.md). In particular, a small implementation error must not be allowed to invoke an unbounded conditional routine on an exactly zero-mass subset.

## 4. Two paid conditional operations

For $`s_S>0`$, define the conditional pure state

```math
|\phi_S\rangle
=\frac{\Pi_S|\psi\rangle}{\sqrt{s_S}}.
```

The [conditional-reflection construction](conditional-reflection.md) supplies two operations from the original source and known subset predicate:

| Operation | Exact ideal guarantee | Expected original-source queries |
| --- | --- | --- |
| Prepare a conditional specimen | Return $`\lvert\phi_S\rangle`$ after verified success | At most $`C_{\rm prep}/\sqrt{s_S}`$ |
| Apply a conditional reflection | Apply $`V_S=I-2\lvert\phi_S\rangle\langle\phi_S\rvert`$, or its coherent controlled version, to arbitrary data and reference | At most $`C_{\rm ref}/s_S`$ |

Here $`C_{\rm prep}`$ and $`C_{\rm ref}`$ are universal valid constants for the specified amplification schedules and their constant-query block encodings. They do not depend on $`p`$, the data input, the reference, $`d`$, $`T`$, or $`s_S`$. Known-predicate and native gate costs remain charged separately.

These routines halt almost surely when $`s_S>0`$. Their runtimes have unbounded tails. The reflection routine is stronger than specimen preparation: conditional on every successful complete measured history, its data operation is a scalar multiple of the same target unitary, including on reference-entangled inputs. The measured history therefore does not reveal or disturb that data. This allows the reflection to be used inside a coherent amplitude-estimation block. Its controlled version has one common success amplitude across both control sectors.

There is no claim of termination for the conditional routines at $`s_S=0`$. The estimator's proof establishes that such a node is never entered with positive estimated weight in the ideal model.

## 5. The finite-alphabet result

**Theorem.** For $`d\ge2`$, the algorithm in [the construction](simplex-estimator.md) halts almost surely and, uniformly over the closed simplex, satisfies

```math
\widehat p\in\Delta_d,
\qquad
\mathbb E_p\widehat p=p,
\qquad
\mathbb E_p\|\widehat p-p\|_2^2
\le\frac{32(d-1)}{T^2},
```

and

```math
\mathbb E_p Q
\le (C_{\rm prep}+C_{\rm ref})(d-1)T.
```

For $`d=1`$, return $`(1)`$ without a source query. The displayed constants concern the stated allocation and the two paid primitive bounds; they are not optimized circuit constants. Simplex boundedness also gives the elementary error ceiling $`\mathcal R_2(p)\le2`$.

The construction also gives a certified finite-arithmetic clock-allocation rule with the same query bound and error constant64 in place of32. Its ideal quantum outputs remain exactly unbiased. This qualification avoids treating exact real-number floor comparisons as a free native operation; quantum gate synthesis and output rounding remain separate approximations.

At fixed $`d`$, the result is quadratic error reduction in expected source work while preserving exact probabilistic validity and unbiasedness. The stated dimension dependence is not optimal distribution-estimation complexity: achieving root mean squared Euclidean error $`\varepsilon`$ through this bound costs $`O(d^{3/2}/\varepsilon)`$ expected source queries. Ordinary multidimensional quantum estimation already gives stronger dimension-dependent precision bounds under its own guarantees. The addition studied here is the conjunction of the exact simplex constraint and exact unbiasedness.

There is no deterministic total-query or coherent-depth deadline in this theorem. Expected query complexity is also distinct from a complete physical-runtime advantage. The [lower-bound account](lower-bounds.md) states the matched classical and quantum precision comparisons under their actual resource models.

## 6. Why the random budget matters

Conditioning on a very rare subset is expensive. Giving every node the same large conditional amplitude-estimation clock would retain a cost proportional to $`1/s_S`$. Instead, the algorithm gives a node a clock proportional to its **random estimated global mass** $`W_S`$. Exact unbiasedness makes $`\mathbb E W_S=s_S`$, so the expected reflection cost contains

```math
\frac{\mathbb E(TW_S)}{s_S}=T.
```

That cancellation alone does not pay for entering the node. The discrete sine readout gives a smallest positive weight of order $`T^{-2}`$, which bounds how often a rare subset is entered and pays for its initial conditional specimen. Both facts are used in the full proof.
