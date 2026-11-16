# Matched precision bounds and comparison models

The estimator's precision exponent is optimal for fixed output dimension in the declared expected-query model. The distinction from classical sampling is the available experiment: the quantum algorithm can run a source circuit and its inverse coherently, whereas the classical comparison receives independent categorical samples. The following bounds do not separate unrestricted classical and quantum algorithms for an explicitly supplied computational problem.

## Quantum lower bound with a uniform expected budget

Fix $`d\ge2`$. Let an algorithm return an arbitrary real vector $`\widehat p`$; the lower bound does not require positivity or unbiasedness. Suppose, uniformly over all allowed coherent source oracles,

```math
\mathbb E\|\widehat p-p\|_2^2\le\varepsilon^2,
\qquad
\mathbb E N\le Q.
```

Here $`N`$ counts every source, inverse-source and controlled-source call. Measurements, adaptive stopping, arbitrary known controls and extra workspace are permitted. For $`0<\varepsilon\le1/16`$,

```math
Q=\Omega(\varepsilon^{-1}).
```

**Proof.** It suffices to use two output labels, leaving the other probabilities zero. Supply the complete real rotation oracle

```math
U_\theta=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix},
\qquad
U_\theta|0\rangle
=\sqrt{1-a}\,|1\rangle+\sqrt a\,|2\rangle,
\qquad a=\sin^2\theta.
```

The displayed output labels are names for the two computational basis states. There is no unknown completion or garbage in this subfamily. Take

```math
a_\pm=\frac12\pm h,
\qquad h=4\varepsilon.
```

Thresholding the second returned coordinate at $`1/2`$ distinguishes these alternatives with error at most $`1/16`$ under each hypothesis: a wrong decision requires coordinate error at least $`h`$, and Markov's inequality applied to squared error gives $`\varepsilon^2/h^2=1/16`$.

Turn the expected-budget algorithm into a bounded-query discriminator by aborting after

```math
L=\lceil16Q\rceil
```

source calls and assigning any decision on an abort. The abort probability is at most $`1/16`$ under either hypothesis. Its error is therefore at most $`1/8`$, so the total-variation distance between its two decision distributions is at least $`3/4`$.

A usual query hybrid applies also to controlled calls, inverse calls and classically selected call types. Their operator-norm difference is bounded by

```math
\Delta=\|U_{\theta_+}-U_{\theta_-}\|
\le |\theta_+-\theta_-|
\le\frac{4h}{\sqrt3}
=\frac{16\varepsilon}{\sqrt3},
```

because $`a_\pm\in[1/4,3/4]`$ and $`d(\arcsin\sqrt a)/da=1/(2\sqrt{a(1-a)})\le2/\sqrt3`$ there. Defer the discriminator's measurements, pad halted branches with inactive controlled calls, and replace its at most $`L`$ calls one at a time. The final state distance, and hence any output total-variation distance, is at most $`L\Delta`$. Consequently

```math
L\Delta\ge\frac34.
```

For completeness, the uniform mean-square guarantee also implies $`Q\ge1/2`$ in the stated precision range. Apply it to the two point-mass sources, threshold the second coordinate at $`1/2`$, and note that the distributions before the first query are identical. The output total-variation distance cannot exceed the probability of making any query, which is at most $`Q`$, whereas the two threshold decisions have distance at least $`1-8\varepsilon^2>1/2`$. Thus $`L\le18Q`$. Combining the inequalities gives, for example,

```math
Q\ge\frac{\sqrt3}{384\,\varepsilon}.
```

Only the order is used. The expected-budget truncation is essential: a fixed-query polynomial or hybrid bound alone would not justify a claim about an unbounded stopping rule. $`\square`$

## Classical independent-sample lower bound

Suppose a classical algorithm receives only independent categorical samples from $`p`$, and returns a vector with the same uniform mean-square guarantee. It may randomize and choose its sample count adaptively. If its expected sample count is uniformly at most $`Q_{\mathrm{cl}}`$, then

```math
Q_{\mathrm{cl}}=\Omega(\varepsilon^{-2}).
```

**Proof.** Use the same Bernoulli pair $`a_\pm=1/2\pm h`$ and the same threshold test. Its decision distributions have total-variation distance at least $`7/8`$. For the stopped transcript, the relative-entropy chain rule gives

```math
D(\mathsf P_+\|\mathsf P_-)
=\mathbb E_+[N]\,
D\!\left(\mathrm{Ber}(a_+)\middle\|\mathrm{Ber}(a_-)\right).
```

The algorithm's own randomization and stopping decisions contribute no conditional divergence. The identity follows first for finite truncations and then for an integrable stopping time; the Bernoulli log-likelihood increments are bounded on the chosen interval. With natural logarithms,

```math
D\!\left(\mathrm{Ber}(a_+)\middle\|\mathrm{Ber}(a_-)\right)
=2h\log\frac{1+2h}{1-2h}
\le16h^2.
```

Pinsker's inequality and data processing therefore imply

```math
2\left(\frac78\right)^2
\le D(\mathsf P_+\|\mathsf P_-)
\le16h^2Q_{\mathrm{cl}},
\qquad
Q_{\mathrm{cl}}\ge\frac{49}{8192\,\varepsilon^2}.
```

Again the constant is inessential. $`\square`$

The empirical frequency vector achieves the classical order while remaining exactly unbiased and in the simplex:

```math
\widehat p_{\mathrm{emp}}=\frac1n\sum_{t=1}^n e_{J_t},
\qquad
\mathbb E\|\widehat p_{\mathrm{emp}}-p\|_2^2
=\frac{1-\|p\|_2^2}{n}\le\frac1n.
```

## What is matched

The [tree construction](simplex-estimator.md) has, for each fixed $`d`$, exactly unbiased simplex output, mean-square error $`O_d(T^{-2})`$ and expected source work $`O_d(T)`$. Taking $`T=\Theta_d(\varepsilon^{-1})`$ matches the quantum precision lower bound. The classical empirical vector and sample lower bound give $`\Theta(\varepsilon^{-2})`$ samples for the same mean-square objective.

These are precision statements at fixed dimension. The current upper bound's dependence on $`d`$ is not claimed optimal. Nor is the theorem a deterministic-depth statement: the conditional reflection and source preparation have unbounded stopping-time tails. The [precision and resource account](precision-and-resources.md) gives a separate capped implementation with explicit error.

For an explicitly compiled randomized sampler, its reversible source circuit may cost substantially more than one classical draw. All preparation, inverse, known-projector, workspace and control costs remain part of the comparison. If a classical algorithm can exploit the sampler's code or solve the underlying problem directly, the sample-only lower bound does not constrain that algorithm.
