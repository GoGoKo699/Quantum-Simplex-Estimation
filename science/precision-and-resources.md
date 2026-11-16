# Precision, stopping time and native resources

Exact unbiasedness belongs to the ideal estimator. A finite execution cap, gate approximation or output rounding changes that statement. This page bounds those changes while keeping every returned vector in the simplex.

## Ideal resource contract

Let $`U|0\rangle=\sum_j\sqrt{p_j}|j\rangle|\mathrm{junk}_j\rangle`$ on $`n`$ source qubits, with the full circuit's workspace included. Inverse calls are available and charged. For each node's known subset $`S`$, let $`\Pi_S`$ test membership of the output label. Its predicate, reflection and workspace are known circuit resources.

The [tree estimator](simplex-estimator.md) uses a scale $`T\ge1`$ and has

```math
\mathbb E\|Z-p\|_2^2\le V_d(T)
:=\frac{32(d-1)}{T^2},
\qquad
\mathbb EZ=p,
\qquad Z\in\Delta_d.
```

Let the exact conditional-source preparation and exact conditional reflection satisfy the uniform bounds

```math
\mathbb E N_{\mathrm{prep}}(s)
\le\frac{C_{\mathrm{prep}}}{\sqrt s},
\qquad
\mathbb E N_{\mathrm{ref}}(s)
\le\frac{C_{\mathrm{ref}}}{s},
\qquad s>0.
```

Both $`N`$ variables count original $`U/U^\dagger`$ calls, including those inside amplification and rewinding. The tree's mass-weighted budgets give

```math
\mathbb E N_U
\le (C_{\mathrm{prep}}+C_{\mathrm{ref}})(d-1)T
```

after increasing the constants to include initial preparations and the one-specimen branches. This is an expected bound, with no positive lower promise on nonzero probabilities. See [conditional reflection](conditional-reflection.md) for the exact primitive and its scalar success amplitude.

### Binary flag checks are necessary

The rewinding test is the two-outcome measurement $`\{P,I-P\}`$, where $`P`$ projects all block-encoding signal registers to zero. Implement it by computing the all-zero predicate into one flag, measuring that flag, and uncomputing the predicate. Measuring each signal qubit separately on a failure refines the measurement, can reveal data information and does not implement the proved rewinding instrument.

### Known gates and workspace

An explicit flat four-branch block encoding selects $`sI,-vv^\dagger,-vv^\dagger,0`$ with Hadamard-prepared selector bits. Its zero block is $`(s/4)R_\phi`$. One encoding uses a constant number of original source calls; a paired implementation uses two $`U`$ and two $`U^\dagger`$ calls, three known subset-projector encodings and one known all-zero-projector encoding. Its signal and program registers use $`n+6`$ qubits, in addition to the data, predicate workspace and any explicitly compiled reflection workspace. Ordinary controlled conjugated projectors can surround a controlled known reflection with unconditional $`U/U^\dagger`$; inactive branches cancel. A controlled conditional reflection instead needs the common scalar block for the whole controlled unitary, as explained in the primitive proof.

Write $`g_U`$ for a source circuit's gate count, $`g_S`$ for the relevant known predicate/reflection cost, and $`g_0(n)`$ for its all-zero logic. Each block step and binary flag check has known gate cost $`O(g_U+g_S+g_0(n))`$, with every oracle call counted. If $`U`$ is supplied as an abstract oracle, $`g_U`$ is an external implementation cost, not zero. If the sampler uses a classical dataset, building its reversible access circuit is also charged; this result assumes no free QRAM or data loading.

The local scalar clocks have size at most $`T`$. Their quantum clock registers use $`O(\log(T+2))`$ qubits. Denote their total known preparation, readout and arithmetic cost by $`g_{\mathrm{clock}}(T)`$ per node. The inherited dyadic sine-transform circuit provides $`g_{\mathrm{clock}}(T)=O(\log^2(T+2))`$ ideal gates, with its required ideal rotation angles; finite synthesis is accounted for below, rather than assumed exact in a fault-tolerant gate set.

The unknown-angle search can use power-of-two stages and four randomized trials per stage. This avoids rejection sampling when selecting trial lengths. Binary loop counters have amortized cost linear in the number of controlled block steps plus their initialization. At stage $`k`$ the $`O(k)`$ random bits and counter initialization are bounded by $`O(2^k)`$; the same geometric-tail estimate that bounds source calls also bounds their expected total. The rewinding loop only alternates a direction bit and performs binary checks. Thus expected known control, measurement and classical-bit work can be charged alongside the expected source work. The tree's recorded split weights and its budget arithmetic are additional classical resources.

For fixed compiled primitives, one can therefore choose a finite, uniform upper bound $`B_d(T)`$ on **all** ideal elementary work events, including source calls, known unitary steps, measurements, coin bits and classical control. A representative resource expression is

```math
B_d(T)
=O\!\left((d-1)T\,[g_U+g_S+g_0(n)+1]
+(d-1)g_{\mathrm{clock}}(T)
+g_{\mathrm{arith}}(d,T)\right).
```

Here $`g_{\mathrm{arith}}`$ is the explicitly chosen split-weight and budget implementation; it is not an oracle. A source-query bound alone is insufficient to certify a wall-clock or total-gate cap. The cap theorem below uses an actual bound on the work being capped.

The ideal stopping rule has no deterministic classical counter-size bound. Quantum source/program workspace remains finite for each primitive invocation; trial lengths are classical controls. A finite execution cap bounds the counters and all working storage as well. No claim of an optimal space bound is made.

## A finite-arithmetic budget allocator

The exact-budget policy in the tree proof uses real-valued comparisons. The following variant avoids treating exact algebraic floors as a free classical operation. For this variant take an integer $`T\ge1`$ (rounding a requested scale up costs only a constant factor). Keep each ideal output weight $`W`$ defined by the recorded scalar clock outcomes, but compute a certified rational lower approximation

```math
\frac{3W}{4}\le\underline W\le W
```

when $`W>0`$. Zero weights are recognized from the clock's exact endpoint label or a zero Bernoulli child; no numerical zero test is needed. If $`T\underline W<3`$, use the one-specimen conditional draw. Otherwise choose the largest dyadic clock $`m=2^\ell-1\le T\underline W`$. This choice depends only on earlier classical outcomes and so preserves exact conditional unbiasedness in the ideal quantum model.

The cost argument is unchanged because $`m\le TW`$. The smallest-positive-weight invariant also remains valid: in a clock branch $`m+1\le TW+1\le4TW/3`$, so its smallest positive child is at least $`27/(16T^2W)\ge T^{-2}`$; in a Bernoulli branch a positive child retains $`W`$. The root has weight one.

The variance constant increases. In a one-specimen branch, $`TW<4`$ and

```math
W^2\mathrm{Var}(Y\mid W)\le W^2/4<4/T^2.
```

In a clock branch, $`L=m+1>(T\underline W+1)/2\ge3TW/8`$. Using the scalar bound $`\kappa_m\le16/L^2`$ and $`r(1-r)\le1/4`$ gives

```math
W^2\mathrm{Var}(Y\mid W)
\le\frac{256}{9T^2}.
```

The same martingale calculation as in the tree proof therefore yields

```math
\mathbb EZ=p,
\qquad Z\in\Delta_d,
\qquad
\mathbb E\|Z-p\|_2^2
\le V_d^{\mathrm{finite\ allocator}}(T)
:=\frac{64(d-1)}{T^2}.
```

Every positive $`W`$ is at least $`T^{-2}`$. Compute a dyadic $`\widehat W`$ with $`|\widehat W-W|\le1/(8T^2)`$ and set $`\underline W=\max\{0,\widehat W-1/(8T^2)\}`$; the offset is a known rational and can be represented exactly. Then $`W-1/(4T^2)\le\underline W\le W`$, hence $`\underline W\ge3W/4`$. Certified interval evaluation of the at most $`d-1`$ algebraic split factors supplies such an approximation. Per-factor absolute precision of order $`1/(dT^2)`$ suffices because products of factors in $`[0,1]`$ have additive error bounded by the sum of factor errors. This uses $`O(\log(d+1)+\log(T+2))`$ fractional bits and explicitly charged arithmetic. Known cosine values can be enclosed with certified increasing precision; their ideal representation need not be compared exactly with a dyadic budget threshold. Retain exact ideal split values in the mathematical estimator, then use the separate final-output rounding step below when an ordinary finite-bit vector is required.

## A capped, perturbed implementation theorem

Consider either exact ideal allocator above, with expected elementary work at most $`B=B_d(T)`$. Write $`V(T)`$ for its proved mean-square bound: $`32(d-1)/T^2`$ for the original exact-budget policy, or $`64(d-1)/T^2`$ for the certified finite-arithmetic allocator. Count the events to be capped so that every unitary application, binary measurement and classical control action is included. Let $`0<\delta<1`$, and set

```math
K=\left\lceil\frac B\delta\right\rceil.
```

Abort before exceeding $`K`$ events, discard the private computation registers, and return a fixed fallback $`z_0\in\Delta_d`$. An abort may occur during a conditional primitive; the theorem concerns the overall classical estimator, not an exact truncated reflection exported for arbitrary external data.

Suppose each implemented unitary event differs from its ideal unitary by operator norm at most $`\eta`$. Equivalently one may assume half-diamond error at most $`\eta`$ for each elementary quantum channel. The compiled and ideal capped programs use the same classical decoding and fallback rules. Invalid clock labels or malformed histories must decode to a specified value in $`[0,1]`$ or to the fallback, so a perturbation cannot create an undefined output.

Finally, round the recorded local binary split values within $`[0,1]`$ and form the leaf probabilities by exact rational multiplication and complementation. Assume the resulting vector differs from the unrounded vector by at most $`\rho`$ in Euclidean norm, on every history. Call this final output $`\widetilde Z`$. Then

```math
\widetilde Z\in\Delta_d,
\qquad
\|\mathbb E\widetilde Z-p\|_2
\le\sqrt2\,(\delta+K\eta)+\rho,
```

and

```math
\sqrt{\mathbb E\|\widetilde Z-p\|_2^2}
\le
\sqrt{V(T)+2(\delta+K\eta)}+\rho.
```

The perturbed, capped program's expected event count is at most

```math
B+K^2\eta,
```

and its deterministic event count is at most $`K`$.

**Proof.** Markov's inequality bounds the ideal abort probability by $`B/K\le\delta`$. Couple the complete and capped ideal runs identically until an abort. Their output distributions have total-variation distance at most $`\delta`$. A telescoping hybrid over the at most $`K`$ elementary channels adds at most $`K\eta`$ total variation, even with adaptive measurements and stopping: include the classical history in the channel's output. Thus the implemented unrounded distribution is within $`\tau=\delta+K\eta`$ of the complete ideal output law.

The simplex has Euclidean diameter $`\sqrt2`$, so a maximal coupling bounds the difference of the output means by $`\sqrt2\tau`$. Squared loss to any fixed $`p\in\Delta_d`$ lies in $`[0,2]`$, giving unrounded mean-square error at most $`V(T)+2\tau`$. The deterministic rounding error gives the displayed bias and root-mean-square bounds by the triangle inequality and Minkowski's inequality.

For the work bound, compare the two capped **transcript** laws, whose distance is at most $`K\eta`$; their realized event counts lie in $`[0,K]`$. Their expected counts differ by at most $`K^2\eta`$. The ideal capped count has expectation at most $`B`$. $`\square`$

### Precision choice retaining the expected exponent

For fixed $`d`$ and $`T\ge2`$, one possible choice is

```math
\delta=T^{-2},
\qquad
K=\lceil B_d(T)T^2\rceil,
\qquad
\eta\le\frac{\delta}{K},
\qquad
\rho\le T^{-1}.
```

Then $`K\eta\le\delta`$, the mean-square error remains $`O_d(T^{-2})`$, and expected capped work is at most $`B_d(T)+K\delta\le2B_d(T)+\delta`$. The deterministic cap is of order $`B_d(T)T^2`$, which is $`O_d(T^3)`$ in a unit-cost primitive model, not $`O_d(T)`$. The approximation changes exact unbiasedness; this example only bounds its bias. A smaller bias or a different failure allocation can be obtained by decreasing the displayed tolerances and charging the resulting cap and synthesis work.

For a gate-synthesis scheme with cost logarithmic in inverse error, the requested per-event tolerance contributes $`O(\log T+\log B_d(T))`$ synthesis precision. This observation is conditional on an actual implementation of the source and known rotations with that cost; it is not a hardware crossover claim. When compiling changes the number of elementary gates, use the pre-synthesis event count for the hybrid and multiply by the actual synthesis cost, or recompute a bound for the events actually capped. Do not identify an abstract-unitary cap with an elementary-gate cap.

## Rounding while preserving the simplex

At each internal node round its split $`y_v`$ down to a $`b`$-bit binary value $`\bar y_v\in[0,1]`$, with $`|\bar y_v-y_v|<2^{-b}`$. Form child weights as $`W\bar y_v`$ and $`W(1-\bar y_v)`$ using exact rational arithmetic. Every leaf weight is nonnegative and the sum remains exactly one. Successive replacement of the node splits gives

```math
\|\bar Z-Z\|_2
\le\|\bar Z-Z\|_1
\le2\sum_{v\ \mathrm{internal}}|\bar y_v-y_v|
<2(d-1)2^{-b}.
```

Thus $`b\ge\lceil\log_2(2(d-1)/\rho)\rceil`$ suffices. Store the split values or their exact dyadic products; independently rounding the final leaf coordinates need not preserve normalization. The rounding described here is deterministic and generally biased.

The certified budget allocator above changes the work allocation and its universal variance constant, while retaining the exact ideal weights. Approximate weights used as the returned vector instead require the final-output error account. Budget approximation and output rounding are different operations.

## Why the cap is needed at zero mass

In the exact proof, $`W>0`$ implies that the corresponding true subset mass $`s`$ is positive, almost surely. This follows from positivity and $`\mathbb EW=s`$. The conditional search/reflection therefore terminates on every reached positive-weight branch. At $`s=0`$ the primitive has no termination promise and is never invoked by the ideal estimator.

A gate error can make a zero-weight branch appear with positive probability. An untruncated conditional search on such a branch can run forever, however small that probability is. The finite cap prevents this failure and the transcript hybrid bounds its statistical effect. It is incorrect to infer a noisy finite expected runtime merely from the ideal zero-mass guard. Likewise, a small probability of nontermination cannot be discarded in an expected-work claim.

The guaranteed exact object is the ideal positive, normalized and unbiased record. The capped finite-precision object always remains a valid probability vector, with the bias, accuracy and work bounds stated above.
