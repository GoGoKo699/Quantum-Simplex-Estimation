# Convex estimates and stochastic evolution

The [simplex estimator](simplex-estimator.md) produces a valid probability vector in every run and has the correct mean. These two properties let it represent a random convex combination or a random stochastic matrix without negative weights or a normalization step. This page gives their precise consequences. The propagation arguments below are elementary martingale consequences of the estimator, rather than separate claims of a new stochastic-process principle.

## 1. A finite known convex range

Let $`v_1,\ldots,v_d`$ be known vectors in a real finite-dimensional Hilbert space, let

```math
K=\mathrm{conv}\{v_1,\ldots,v_d\},\qquad
x=\sum_{j=1}^{d}p_jv_j,\qquad
D=\max_{i,j}\|v_i-v_j\|_2.
```

The supplied sampler returns label $`j`$ with probability $`p_j`$. Its construction, inverse and known label tests are charged as in the [model](model.md). If the vectors are given as a dense $`k\times d`$ classical table, forming the output uses $`O(kd)`$ arithmetic operations and reads that table. In addition to the estimator's own workspace, a streaming accumulation needs $`O(k)`$ working entries and access to the returned $`d`$ weights. Input storage, coefficient precision and output rounding are charged separately; no random access to an arbitrary table is free.

Apply the simplex estimator at scale $`T\ge1`$, write $`Z`$ for its output, and return

```math
\widehat x=\sum_{j=1}^{d}Z_jv_j.
```

**Proposition 1 (convex-range variance reduction).** The output satisfies

```math
\widehat x\in K\quad\text{almost surely},\qquad
\mathbb E\widehat x=x,
```

and, for a universal constant $`C`$,

```math
\mathbb E\|\widehat x-x\|_2^2
\le \frac{C D^2(d-1)}{T^2}.
```

The expected number of original sampler/inverse calls is $`O((d-1)T)`$. This is an ideal, expected-work statement with unbounded stopping tails; [finite precision and resource accounting](precision-and-resources.md) apply separately.

**Proof.** Nonnegative coefficients summing to one give membership in $`K`$. Taking expectations gives the exact mean. For the diameter bound, use the same split-revelation martingale as in the simplex proof. At a node whose random global mass is $`W`$, let $`r`$ be its true left conditional probability, and let $`x_L,x_R`$ be the true conditional means of the descendant vectors. Revealing the split estimate $`Y`$ changes the conditional expected final output by

```math
\Delta=W(Y-r)(x_L-x_R).
```

Both conditional means belong to $`K`$, so $`\|x_L-x_R\|_2\le D`$. The local estimate has $`\mathbb E[Y\mid\text{past}]=r`$ and the simplex construction establishes

```math
\mathbb E\!\left[W^2\mathrm{Var}(Y\mid\text{past})\right]
\le C_0/T^2
```

at each internal node. Orthogonal martingale increments add their squared Hilbert norms. There are $`d-1`$ internal nodes, proving the stated bound. Zero-mass nodes are skipped and have zero increment. $`\square`$

Every affine constraint satisfied by all the vectors is preserved exactly. For example, if $`Av_j=b`$ for every $`j`$, then $`A\widehat x=b`$ in every run. Any convex inequality defining a set that contains the vectors also remains satisfied. The result concerns a supplied finite convex representation; it does not supply vertices, membership oracles or a decomposition of an arbitrary unknown convex body.

For a differentiable function $`f`$ with $`L`$-Lipschitz gradient on $`K`$, the smoothness inequality and unbiasedness give

```math
\mathbb E f(\widehat x)-f(x)
\le \frac L2\mathbb E\|\widehat x-x\|_2^2.
```

If $`f`$ is also convex, this difference is nonnegative by Jensen's inequality. Thus smooth nonlinear losses have a controlled expected excess; their plug-in values are not generally unbiased.

## 2. A three-outcome forecast

Consider $`p=(1/2,1/3,1/6)`$ and split the first two labels from the third. Put $`s=5/6`$ and $`r=3/5`$. The algorithm first estimates $`s`$ by $`W\in[0,1]`$. If $`W>0`$, it obtains a conditionally unbiased estimate $`Y\in[0,1]`$ of $`r`$, using a budget determined by $`W`$. It returns

```math
Z=(WY,\,W(1-Y),\,1-W).
```

For instance, at scale $`T=7`$ the root clock has size seven, and the readout $`W=1/2`$ selects a child clock of size three. The further readout $`Y=1/2`$ gives the valid forecast $`(1/4,1/4,1/2)`$. Each realized forecast can differ from $`p`$; over fresh executions its mean equals $`p`$. No clipping or renormalization is applied. The adaptive budget changes the variance and cost, while the conditional identity $`\mathbb E[Y\mid W]=r`$ preserves the mean.

There is a direct prediction-quality interpretation. Draw an independent future outcome $`J\sim p`$, and write $`e_J`$ for its one-hot vector. The Brier loss is $`\|Z-e_J\|_2^2`$. Independence of $`J`$ from the estimation experiment gives the exact identity

```math
\mathbb E\|Z-e_J\|_2^2
=1-\|p\|_2^2+\mathbb E\|Z-p\|_2^2.
```

Here $`\|p\|_2^2=7/18`$, so the optimal forecast $`p`$ has expected loss $`11/18`$. The quantum estimate has expected excess $`O(T^{-2})`$ at fixed alphabet size and expected $`O(T)`$ source calls. An empirical frequency vector from $`N`$ ordinary categorical samples is also valid and unbiased, with exact excess $`(1-\|p\|_2^2)/N=11/(18N)`$. This compares these two implementations; it does not establish a new optimal dimension dependence or an unrestricted downstream-task lower bound.

The Brier identity itself does not require unbiasedness. Exact unbiasedness supplies the additional mean-preservation properties below. It should not be confused with conditional calibration of a forecast.

## 3. Fresh stochastic matrices preserve the mean evolution

Let $`P_t`$ be a deterministic $`r_{t-1}\times r_t`$ row-stochastic matrix. Estimate each row by a simplex block, and call the resulting random row-stochastic matrix $`Q_t`$. Fresh blocks can be independent within a matrix, although this is not necessary for the following statements. Use fresh randomness and source executions at successive times, so that, conditional on everything generated before time $`t`$,

```math
\mathbb E[Q_t\mid\mathcal F_{t-1}]=P_t.
```

This conditional-mean condition is the property needed in the proofs. Independent fresh matrices for fixed source circuits are a sufficient implementation. Shared hardware memory or adaptive reuse that violates it is outside the statement. Random query duration does not justify reusing a previous matrix; it is part of the charged cost of generating the fresh block.

For a fixed initial probability row vector $`\mu_0`$, define

```math
\mu_t=\mu_{t-1}Q_t,\qquad
\nu_t=\nu_{t-1}P_t,\qquad
\nu_0=\mu_0.
```

**Proposition 2 (validity and exact mean).** Every $`\mu_t`$ is a probability vector and

```math
\mathbb E\mu_t=\nu_t,
\qquad
\mathbb E[Q_1\cdots Q_h]=P_1\cdots P_h.
```

**Proof.** Products of row-stochastic matrices are row-stochastic. Conditional expectation gives

```math
\mathbb E[\mu_t\mid\mathcal F_{t-1}]
=\mu_{t-1}P_t.
```

Iterating this identity proves both claims. Entries are bounded, so all expectations exist without extra moment assumptions. $`\square`$

This is an unbiased estimator of the distribution vector or matrix product, with a valid probability object in each realization. If one additionally samples a trajectory from those matrices, its marginal law is correct under the same freshness condition. That does not imply a reduction of the variance of an arbitrary sampled trajectory payoff: the subsequent sampling can restore the original path fluctuations. Direct measurement of the supplied sampler already generates a categorical outcome in one call.

## 4. A variance bound for contractive mean dynamics

Assume now a fixed state count $`r`$. Suppose each mean matrix contracts zero-sum row vectors in Euclidean norm:

```math
\|aP_t\|_2\le\kappa_t\|a\|_2
\quad\text{whenever }a\mathbf1=0.
```

Also suppose the fresh matrix has a conditional row-error bound

```math
\mathbb E\!\left[
\|Q_t(i,\cdot)-P_t(i,\cdot)\|_2^2
\mid\mathcal F_{t-1}\right]\le v_t
\quad\text{for every }i.
```

The simplex blocks give $`v_t\le C(r-1)/T_t^2`$, uniformly over every row, at scale $`T_t`$.

**Proposition 3 (stable distribution-vector propagation).** With the preceding assumptions,

```math
\mathbb E\|\mu_h-\nu_h\|_2^2
\le \sum_{t=1}^{h}v_t
\prod_{u=t+1}^{h}\kappa_u^2.
```

In particular, if $`v_t\le v`$ and $`\kappa_t\le\kappa<1`$,

```math
\mathbb E\|\mu_h-\nu_h\|_2^2
\le v\frac{1-\kappa^{2h}}{1-\kappa^2}
\le \frac{v}{1-\kappa^2}.
```

The realized matrices $`Q_t`$ need not themselves contract Euclidean distances. The contraction hypothesis is on the deterministic mean matrices.

**Proof.** Put $`e_t=\mu_t-\nu_t`$ and $`\eta_t=\mu_{t-1}(Q_t-P_t)`$. Then

```math
e_t=e_{t-1}P_t+\eta_t,
\qquad
\mathbb E[\eta_t\mid\mathcal F_{t-1}]=0.
```

The cross term vanishes after conditional expectation. Since $`e_{t-1}\mathbf1=0`$,

```math
\mathbb E\|e_t\|_2^2
\le\kappa_t^2\mathbb E\|e_{t-1}\|_2^2
+\mathbb E\|\eta_t\|_2^2.
```

Conditional on the past, $`\mu_{t-1}`$ is a fixed probability vector. Convexity of the squared norm gives the pathwise inequality

```math
\left\|\sum_i\mu_{t-1}(i)
\bigl[Q_t(i,\cdot)-P_t(i,\cdot)\bigr]\right\|_2^2
\le\sum_i\mu_{t-1}(i)
\|Q_t(i,\cdot)-P_t(i,\cdot)\|_2^2.
```

Thus $`\mathbb E\|\eta_t\|_2^2\le v_t`$, without independence among rows. Iterate the scalar recurrence from $`e_0=0`$. $`\square`$

For doubly stochastic mean matrices, $`\kappa_t\le1`$ is always available, giving the simpler bound $`\sum_t v_t`$. One direct proof is Jensen's inequality for every output coordinate followed by the column-sum identity. A strict contraction requires a separate hypothesis; row stochasticity alone does not imply Euclidean contraction.

### An explicit contracting family

For $`0\le a<1`$, consider the binary mean kernel

```math
P_a=\frac12
\begin{pmatrix}
1+a&1-a\\
1-a&1+a
\end{pmatrix}.
```

Every zero-sum row vector is proportional to $`(1,-1)`$, and $`(1,-1)P_a=a(1,-1)`$. Thus $`\kappa=a`$. Estimate each binary row by the inherited bounded scalar block and its complement, using clock size $`M`$. If $`\kappa_M`$ denotes its scalar variance coefficient, the exact row trace-MSE is

```math
v=2\kappa_M\frac{1-a^2}{4}
=\frac{\kappa_M(1-a^2)}2.
```

Proposition 3 yields

```math
\mathbb E\|\mu_h-\nu_h\|_2^2
\le \frac{\kappa_M}{2}(1-a^{2h})
\le\frac{\kappa_M}{2}=O(M^{-2}).
```

The small row variance cancels the small contraction gap in this particular family. For empirical row estimates made from $`N`$ independent Bernoulli samples per row, the same calculation replaces $`\kappa_M`$ by $`1/N`$ and gives the bound $`(1-a^{2h})/(2N)`$. Quantum rows use $`O(M)`$ paid coherent source/inverse calls; empirical rows use $`N`$ ordinary source samples. This is a comparison of row-estimation blocks inside the same classical matrix propagation. It is not a lower bound for all classical ways of computing this binary family, and it supplies no advantage when the matrix entries are already given numerically.

For the general $`r`$-state algorithm at common scale $`T`$, generating every row at each of $`h`$ times costs expected $`O(hr(r-1)T)`$ original-source calls. The uniform-in-horizon error bound does not remove this linear horizon cost. Dense classical propagation additionally uses $`O(hr^2)`$ arithmetic operations and stores $`O(r^2)`$ entries if one full current matrix is materialized; rows may instead be processed sequentially with corresponding storage management.

## 5. Why one random table cannot be reused without analysis

Let $`P`$ have both binary rows $`(1/2,1/2)`$, and let

```math
Q=\begin{pmatrix}X&1-X\\Y&1-Y\end{pmatrix},
\qquad
\mathbb E X=\mathbb E Y=1/2,
\qquad
\mathrm{Var}(X)=\mathrm{Var}(Y)=v>0,
```

where $`X,Y`$ are independent. Then $`\mathbb E Q=P`$, but direct multiplication gives

```math
\mathbb E[Q^2]
=\begin{pmatrix}1/2+v&1/2-v\\1/2-v&1/2+v\end{pmatrix}
\ne P^2=P.
```

By contrast, independent fresh copies $`Q_1,Q_2`$ satisfy $`\mathbb E[Q_1Q_2]=P^2`$. Positivity and exact row means do not make nonlinear reuse unbiased. The same warning applies to powers, ratios, inverses, entropy and data-dependent rewards chosen from the estimated table.

## 6. What this capability adds

Prior quantum mean estimation already achieves a Heisenberg precision exponent, and prior exact debiasing already works for vector means. The [comparison](../references/related-work.md) explains the narrower addition here: exact unbiasedness and membership in the classical feasible convex range hold together, including on its boundary. The scalar construction is inherited; the conditional-reflection and random-mass budget argument make the finite-alphabet extension executable in the stated expected-work model. These properties support the stochastic operators above. They do not establish an end-to-end hardware advantage, optimal dependence on alphabet size, a new general mixing theorem or a faster trajectory sampler.
