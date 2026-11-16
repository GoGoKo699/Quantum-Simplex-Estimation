# A probability tree with unbiased random budgets

The construction splits a probability mass repeatedly until only the requested labels remain. Each split preserves the mass it receives. A large received mass earns a coherent sine-clock estimate of the next conditional probability; a small received mass uses one ordinary conditional sample. The mass itself controls the clock length, which is what pays for rare conditioning.

The [model](model.md) defines the source, the closed-simplex guarantee, and the charged resources. The exact paid reflection used below is established in [conditional reflection](conditional-reflection.md). No reversible conditional sampler is assumed.

## 1. Inherited scalar sine estimator

We use the ideal scalar result from [Bounded Unbiased Amplitude Estimation](https://github.com/GoGoKo699/Bounded-Unbiased-Amplitude-Estimation/tree/940e1e99b3d7b7b0be39eb6bcc1ea41fdf110101), specifically its [model](https://github.com/GoGoKo699/Bounded-Unbiased-Amplitude-Estimation/blob/940e1e99b3d7b7b0be39eb6bcc1ea41fdf110101/science/model-and-estimator.md) and [variance proof](https://github.com/GoGoKo699/Bounded-Unbiased-Amplitude-Estimation/blob/940e1e99b3d7b7b0be39eb6bcc1ea41fdf110101/science/variance-proof.md). This scalar theorem is an inherited ingredient, not a new precision law here. The [local scalar-clock account](scalar-clock.md) gives its circuit and reconstructs the moment proof.

Let $`|\phi\rangle`$ be an initial state, let $`\Pi`$ be its success projector, and put $`q=\langle\phi|\Pi|\phi\rangle`$. For $`m=2^\ell-1\ge3`$, set

```math
L=m+1,\qquad \alpha=\frac\pi L,
\qquad
z_j=\frac{1-\cos(j\alpha)/\cos\alpha}{2},
\quad 1\le j\le m.
```

A sine-clock block with $`m`$ controlled Grover steps returns $`Y\in\{z_1,\ldots,z_m\}`$ such that

```math
0\le Y\le1,
\qquad
\mathbb E Y=q,
\qquad
\operatorname{Var}(Y)=\kappa_m q(1-q),
\qquad
\kappa_m=\frac{m-1}{m+1}\tan^2\!\left(\frac\pi{m+1}\right).
```

It needs one initial specimen and the coherent controlled reflection about that state. In the present application these are supplied by the paid conditional operations on the original source.

**Reflection sign.** The scalar convention is

```math
G=(2|\phi\rangle\langle\phi|-I)(I-2\Pi).
```

Our conditional primitive returns $`V=I-2|\phi\rangle\langle\phi|`$. Thus the first scalar reflection is $`-V`$. In a controlled Grover call, include the known minus phase on its active control branch. Omitting it would change the clock's probability interpretation.

Two scalar facts will be used with explicit constants. Since $`\alpha\le\pi/4`$, convexity of the tangent function gives $`\tan\alpha\le4\alpha/\pi`$, and hence

```math
\kappa_m\le\frac{16}{L^2}.
\tag{1}
```

Also $`z_1=0`$, $`z_m=1`$, the readouts increase with $`j`$, and they are symmetric under $`z\mapsto1-z`$. The smallest positive readout, and the smallest positive complementary readout, is

```math
z_2
=\frac{\sin(3\alpha/2)\sin(\alpha/2)}{\cos\alpha}
\ge\frac{3}{L^2}.
\tag{2}
```

For the inequality, both sine arguments lie in $`[0,\pi/2]`$, where $`\sin u\ge2u/\pi`$, and $`\cos\alpha\le1`$.

## 2. The algorithm

Choose any fixed binary tree with $`d`$ label leaves and a precision parameter $`T\ge1`$. Process its $`d-1`$ internal nodes in any deterministic order in which each parent precedes its children. The root has estimated global mass $`W_{\rm root}=1`$.

At an internal node $`S`$ with children $`L,R`$, do the following.

1. If $`W_S=0`$, assign zero weight to both children and skip all conditional-source work.
2. Otherwise prepare a fresh exact specimen $`|\phi_S\rangle=\Pi_S|\psi\rangle/\sqrt{s_S}`$ using the paid conditional-preparation routine.
3. Put $`x=TW_S`$. If $`x<3`$, measure whether the specimen lies in $`L`$. Use the resulting $`Y_S\in\{0,1\}`$.
4. If $`x\ge3`$, choose

```math
m_S=2^{\lfloor\log_2(x+1)\rfloor}-1,
\qquad L_S=m_S+1.
\tag{3}
```

   Run the scalar sine estimator with this clock, initial specimen $`|\phi_S\rangle`$, success projector $`\Pi_L`$, and the paid controlled conditional reflection. Its result is $`Y_S\in[0,1]`$.
5. Set

```math
W_L=W_SY_S,
\qquad
W_R=W_S(1-Y_S).
\tag{4}
```

At the end return the leaf weights $`\widehat p_i=W_{\{i\}}`$. A conditional specimen is consumed by its one split; the algorithm does not assume that a previously measured or disturbed specimen can be reused as a fresh source.

The choice in (3) is the largest available dyadic sine clock not exceeding $`x`$. At the fence $`x=3`$ it chooses $`m_S=3`$. For every large-clock branch,

```math
3\le m_S\le x,
\qquad
\frac{x+1}{2}<L_S\le x+1\le\frac43 x.
\tag{5}
```

The exact allocation rule is stated in the ideal arithmetic model. Section9 supplies a certified finite-arithmetic allocation with the same query bound and error constant64 in place of32. Its arithmetic costs are charged; exact comparison with an unknown probability is never assumed.

## 3. What every split preserves

Every local output lies in $`[0,1]`$, so (4) preserves nonnegativity and conserves exactly the mass entering the node. Starting with root mass one therefore proves

```math
\widehat p_i\ge0,
\qquad
\sum_i\widehat p_i=1
```

on every terminating history.

For a positive true node mass define the conditional split probability

```math
q_S=\frac{s_L}{s_S}.
```

Let $`\mathcal F`$ contain all completed earlier split records and all earlier classical decisions. If $`W_S>0`$, the fresh local block satisfies

```math
\mathbb E[Y_S\mid\mathcal F]=q_S.
\tag{6}
```

For the ordinary-sample branch this is its measurement probability. For the sine branch it is the scalar unbiasedness theorem at the clock selected from $`\mathcal F`$. The exact conditional reflection remains a unitary channel on its data, including arbitrary clock entanglement, despite its measured retry history. Its successful histories do not introduce a data-dependent conditioning error.

Induction over the tree now proves

```math
\mathbb E W_S=s_S
\tag{7}
```

for every node. It holds at the root. If it holds at a node of positive true mass, (6) gives $`\mathbb E W_L=q_S\mathbb E W_S=s_L`$, and likewise for $`R`$. If $`s_S=0`$, nonnegativity and (7) imply $`W_S=0`$ almost surely, so the algorithm skips that node. This establishes the induction without invoking a conditional routine at zero mass. At the leaves, (7) is exactly $`\mathbb E\widehat p=p`$.

This also proves almost-sure termination by induction: the tree contains finitely many internal nodes, and each conditional operation that is actually invoked has positive mass and halts almost surely.

## 4. A minimum positive global weight

The discrete readout prevents a rare node from being entered too often. More precisely, every node obeys the pathwise invariant

```math
W_S=0\quad\text{or}\quad W_S\ge\frac1{T^2}.
\tag{8}
```

The root satisfies it because $`T\ge1`$. A direct Bernoulli split gives each positive child the parent's weight. In a large-clock split, either child, when positive, has weight at least $`W_Sz_2`$. Equations (2) and (5) give

```math
W_Sz_2
\ge\frac{3W_S}{L_S^2}
\ge\frac{27}{16T^2W_S}
\ge\frac1{T^2},
\tag{9}
```

because $`0<W_S\le1`$. This proves (8) at every depth; the lower bound does not deteriorate down the tree.

Combining (7) and (8) yields the entry-probability bound

```math
\Pr(W_S>0)\le\min\{1,T^2s_S\}.
\tag{10}
```

This is a probability statement derived from the ideal output law, not an assumption that the algorithm knows $`s_S`$.

## 5. Uniform mean squared error

At either type of split,

```math
W_S^2\operatorname{Var}(Y_S\mid\mathcal F)
\le\frac{16}{T^2}.
\tag{11}
```

For $`TW_S<3`$, the left side is $`W_S^2q_S(1-q_S)\le9/(4T^2)`$. For $`TW_S\ge3`$, (1) and (5), together with $`q_S(1-q_S)\le1/4`$, give

```math
W_S^2\kappa_{m_S}q_S(1-q_S)
\le\frac{4W_S^2}{L_S^2}
\le\frac{16W_S^2}{(TW_S+1)^2}
\le\frac{16}{T^2}.
```

To sum these local errors, for every positive true node mass let $`r_S`$ be the true conditional distribution of its descendant leaves, embedded in $`\mathbb R^d`$. At a zero-mass node assign any fixed normalized vector supported on its leaves; its random weight is zero almost surely, so that arbitrary assignment has no effect.

At an intermediate frontier of the processed tree, define

```math
Z_k=\sum_{S\text{ in frontier}}W_Sr_S.
```

Initially $`Z_0=p`$. At the end $`Z_{d-1}=\widehat p`$. Splitting a positive-mass node changes this vector by

```math
\delta_S
=W_S(Y_S-q_S)(r_L-r_R).
\tag{12}
```

The identity uses $`r_S=q_Sr_L+(1-q_S)r_R`$. A skipped node has zero increment. By (6), each increment has conditional mean zero. Thus $`(Z_k)`$ is a finite vector martingale.

The child distributions have disjoint supports and each has Euclidean norm at most one. Consequently

```math
\|r_L-r_R\|_2^2
=\|r_L\|_2^2+\|r_R\|_2^2
\le2.
```

Martingale increments at different steps are orthogonal in mean: conditioning the later increment on the earlier record makes its inner product with any earlier increment vanish. Equations (11) and (12) therefore give

```math
\begin{aligned}
\mathbb E\|\widehat p-p\|_2^2
&=\sum_{S\text{ internal}}\mathbb E\|\delta_S\|_2^2\\
&\le2\sum_{S\text{ internal}}
\mathbb E\!\left[W_S^2\operatorname{Var}(Y_S\mid\mathcal F)\right]\\
&\le\frac{32(d-1)}{T^2}.
\end{aligned}
\tag{13}
```

This is a finite-alphabet uniform bound, including every face of the simplex. It is not a dimension-optimal multivariate estimation law.

## 6. Expected original-source queries

Fix an internal node of positive true mass $`s=s_S`$. Its initial conditional specimen costs at most $`C_{\rm prep}/\sqrt{s}`$ expected source queries when the node is entered. By (10), its unconditional contribution is at most

```math
\frac{C_{\rm prep}}{\sqrt{s}}\Pr(W_S>0)
\le C_{\rm prep}\frac{\min\{1,T^2s\}}{\sqrt{s}}
\le C_{\rm prep}T.
\tag{14}
```

The last inequality follows by separating $`s\le T^{-2}`$ and $`s\ge T^{-2}`$. This is the step that pays for entering rare subsets.

A large-clock block makes exactly $`m_S`$ controlled Grover calls, each requiring one paid controlled conditional reflection and known subset logic. Set $`m_S=0`$ for the direct-sample or skipped branches. Since $`m_S\le TW_S`$, the expected source-query contribution of these reflections is

```math
\mathbb E\!\left[\frac{C_{\rm ref}m_S}{s}\right]
\le C_{\rm ref}T\frac{\mathbb EW_S}{s}
=C_{\rm ref}T.
\tag{15}
```

The reflection primitive's expected bound holds on arbitrary data and reference conditional on the current history. It therefore applies to every call inside the coherent clock block. Linearity of expectation adds those costs; no independence of successive runtimes is assumed. Its measured histories implement the intended controlled unitary exactly, so the random runtimes do not alter the scalar law used in (6).

Zero-mass nodes are skipped almost surely and contribute nothing. Summing (14) and (15) over the $`d-1`$ internal nodes proves

```math
\mathbb E Q
\le(C_{\rm prep}+C_{\rm ref})(d-1)T.
\tag{16}
```

All inverses and failed conditional attempts are included through the primitive bounds. At the root one may use the original source and its direct reflection; using the general bound only loosens the constant.

The local clocks obey $`m_S\le T`$. Their known sine preparation/readout work is therefore at most $`O((d-1)\log^2(T+1))`$ ideal clock gates, in addition to the source and known-predicate work of the conditional routines. Classical random schedules and retry counters are finite on each terminating history but have no fixed maximum size. A source-query bound alone is not a deadline for every kind of computation; [precision and resources](precision-and-resources.md) gives the implementation scope.

## 7. Three labels as a worked example

Take the tree whose root divides $`\{1,2\}`$ from $`\{3\}`$. Its first result is $`Z`$, an estimate of $`s=p_1+p_2`$. The singleton right child already has weight $`1-Z`$. If $`Z>0`$, the second split estimates $`r=p_1/s`$ with a clock selected from $`TZ`$, giving $`Y`$. The returned vector is

```math
\widehat p=(ZY,\ Z(1-Y),\ 1-Z).
```

For example, when $`p=(0.2,0.3,0.5)`$, the conditional mean of $`Y`$ is $`0.4`$ at every selected clock, and the mean of $`Z`$ is $`0.5`$. Thus the first two coordinates have means $`0.2`$ and $`0.3`$ even though the second clock depends on the random first result. Their sum equals $`Z`$ in every realization, so no normalization repair is needed.

If instead $`p_1+p_2=0`$, the first output is exactly $`Z=0`$ and the undefined conditional source is never called. If $`p_1=0<p_2`$, the conditional second output is exactly $`Y=0`$. These endpoint properties are part of the proof, rather than exceptions removed by a positive-probability promise.

## 8. Scope of the result

The scalar sine law, standard amplification, block encoding, and rewinding are inherited ingredients. The contribution here is the complete conditional construction and random mass allocation that retain exact unbiasedness and a valid probability vector at every realization while obtaining the uniform expected-work bound.

The proof does not supply a deterministic query cap, an exact finite-gate noisy-device guarantee, a clean coherent multirow probability oracle, an optimal dependence on $`d`$, or unbiasedness of arbitrary nonlinear functions of one returned vector. Those distinctions matter when the estimator is used in [positive compositions](convex-composition.md) or compared with earlier [multivariate estimation](../references/related-work.md).

## 9. A certified finite-arithmetic clock choice

The exact scalar outputs are specified by the measured integer labels and their known dyadic clock sizes. A weight is a product of such known factors. Its being exactly zero can be tracked by a Boolean flag: only the known endpoint readouts or a zero Bernoulli branch create a zero factor. The algorithm therefore need not decide whether a numerically tiny approximation is zero.

For an exactly positive weight, compute a rational approximation $`\widetilde W`$ with a certified error

```math
|\widetilde W-W|\le\frac1{8T^2},
\qquad
\overline W=\max\left\{0,\widetilde W-\frac1{8T^2}\right\}.
```

The invariant (8) implies

```math
\frac34 W\le\overline W\le W.
\tag{17}
```

Use $`T\overline W`$ in place of $`TW`$ in the threshold and clock rule (3), while retaining the exact mathematical factors $`Y`$ in the returned weights. This is a past-record-dependent integer clock choice, so the conditional mean (6) and exact unbiasedness are unchanged. Since the resulting $`m\le T\overline W\le TW`$, the minimum-positive-weight argument and both source-query bounds are unchanged as well.

On a direct-sample branch, $`T\overline W<3`$ implies $`TW<4`$, giving $`W^2\operatorname{Var}(Y)\le4/T^2`$. On a sine branch, the proof of (11) instead gives

```math
W^2\operatorname{Var}(Y\mid\mathcal F)
\le\frac{16W^2}{T^2\overline W^2}
\le\frac{256}{9T^2}.
```

Consequently this allocation satisfies the convenient uniform bound

```math
\mathbb E\|\widehat p-p\|_2^2
\le\frac{64(d-1)}{T^2},
\qquad
\mathbb E Q
\le(C_{\rm prep}+C_{\rm ref})(d-1)T.
\tag{18}
```

For rational or integer supplied $`T`$, deciding the next clock from rational $`\overline W`$ uses ordinary finite arithmetic. At most $`d-1`$ known readout factors occur along a path. Evaluating each factor and the product with certified errors of order $`1/(dT^2)`$ suffices, using $`O(\log(d+1)+\log(T+1))`$ fractional bits plus ordinary precision overhead. This describes an effective allocation route, not free arithmetic or a new optimal gate-complexity theorem. The [resource account](precision-and-resources.md) distinguishes this classical allocation approximation from synthesizing the quantum gates or rounding the returned vector: those other approximations can change the estimator law and need their own error budget.
