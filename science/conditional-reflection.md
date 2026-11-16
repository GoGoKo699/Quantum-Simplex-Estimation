# Exact conditional states and reflections

This page supplies the two conditional operations used by the [simplex estimator](simplex-estimator.md), under the source interface in the [model](model.md). The operations use the source unitary and its inverse. They do not require an inverse of a postselected preparation circuit, knowledge of a conditional mass, or a supplied conditional-state oracle. The construction combines standard block encoding, oblivious amplitude amplification and randomized search with an explicit input-restoration argument; these ingredients are credited below.

## Interfaces and assumptions

Let $`U|0^n\rangle=|\psi\rangle`$ and let $`\Pi`$ be a known projector whose reflection can be computed reversibly. For one fixed invocation, define

```math
|v\rangle=\Pi|\psi\rangle,\qquad
s=\langle v|v\rangle>0,\qquad
|\phi\rangle=\frac{|v\rangle}{\sqrt{s}},\qquad
R_\phi=I-2|\phi\rangle\langle\phi|.
```

The two operations are:

| Operation | Exact output in the ideal model | Expected source calls |
| --- | --- | --- |
| `PrepareConditional` | One specimen in $`\lvert\phi\rangle`$ | $`C_{\mathrm{prep}}/\sqrt{s}`$ |
| `ReflectConditional` | $`R_\phi`$ on arbitrary data, or its controlled version | $`C_{\mathrm{ref}}/s`$ |

Both halt almost surely without knowing $`s`$. Source calls count applications of $`U`$ and $`U^\dagger`$ equally. The constants are universal and need not be optimized; the explicit reflection schedule below permits $`C_{\mathrm{ref}}=512`$ for the stated four-query block encoder. Known predicates, zero tests, ancillary registers and classical loops have additional costs stated below.

The reflection operation acts correctly when its data and control are entangled with an arbitrary untouched reference. Its measurements reveal no information about that input. The invocation fixes $`U`$ and $`\Pi`$, hence one mass $`s`$. A coherent control choosing different conditional nodes with different masses is outside this statement. In the estimator, the node and previously observed history are classical when a primitive is invoked.

There is no deterministic stopping deadline. At $`s=0`$ the conditional state is undefined and these routines are not zero tests. They must be called under the positive-mass promise, as supplied by the estimator's sampled-branch invariant. Exactness here refers to exact source queries and known-projector operations. Finite-precision implementation is treated separately in the resource account.

## 1. Exact projector encodings

For a projector $`Q`$, a single flag qubit gives the unitary

```math
E_Q=(H\otimes I)
\bigl(|0\rangle\langle0|\otimes I+
|1\rangle\langle1|\otimes(2Q-I)\bigr)
(H\otimes I),
\qquad
(\langle0|\otimes I)E_Q(|0\rangle\otimes I)=Q.
```

Thus $`E_Q`$ is an exact normalization-one block encoding of $`Q`$. The rank-one projector

```math
P_\psi=U|0^n\rangle\langle0^n|U^\dagger
```

has a reflection implemented by conjugating the known zero-state reflection with $`U`$ and $`U^\dagger`$. Multiplying three encodings with distinct flags produces a block encoding $`A_B`$ of

```math
B=\Pi P_\psi\Pi=|v\rangle\langle v|.
```

It uses one $`U`$ and one $`U^\dagger`$, two known $`\Pi`$ encodings and one known zero-state encoding. The three flags are projected onto zero only in the mathematical block; the circuit itself is unitary.

For the scalar mass, use a separate $`n`$-qubit program register. Prepare $`U|0^n\rangle`$ in it, apply $`E_\Pi`$ with another flag, and unprepare with $`U^\dagger`$. The joint zero-program, zero-flag block is

```math
\langle0^n|U^\dagger\Pi U|0^n\rangle=s.
```

Call this encoding $`A_s`$. On the arbitrary data register it encodes $`sI`$, with one $`U`$ and one $`U^\dagger`$ on the program register. This is an amplitude equal to $`s`$, rather than a claimed coherent estimate of $`s`$.

## 2. A flat four-way unitary block encoder

Prepare two selector qubits with Hadamards. Their four equally weighted branches apply encodings of

```math
sI,\qquad -B,\qquad -B,\qquad 0.
```

The zero branch flips an otherwise zero block flag. The minus signs are known selector phases. Unprepare the selector with Hadamards. With $`P`$ denoting the joint zero selector, program and block flags, the resulting unitary $`A`$ satisfies

```math
PAP\big|_{\mathrm{ran}P}
=\frac{sI-2B}{4}
=\frac{s}{4}R_\phi.
```

Here and below, the signal-zero subspace is identified with the data Hilbert space. No numerical value of $`s`$ is used. Flat selection avoids an exact arbitrary rotation for unequal LCU weights.

The two identical $`-B`$ branches share one implementation of $`A_B`$ selected by their known predicate. The source pairs in the scalar and rank-one encodings can run unconditionally, with only the known middle operations selected. An inactive scalar branch has $`U^\dagger I U=I`$; an inactive rank-one branch has $`U I U^\dagger=I`$. Therefore this SELECT construction needs no controlled-source oracle beyond $`U,U^\dagger`$ themselves.

| Item in one $`A`$ or $`A^\dagger`$ | Count |
| --- | --- |
| $`U`$ | $`2`$ |
| $`U^\dagger`$ | $`2`$ |
| Known $`\Pi`$ block encodings | $`3`$ |
| Known zero-state block encoding | $`1`$ |
| Selector qubits | $`2`$ |
| Projector block flags | $`4`$ |
| Program register | $`n`$ qubits |

The data register is additional to this ledger. The zero branch can use one of the four block flags. The signal contains $`n+6`$ qubits before predicate and zero-test workspace. All-zero signal reflections and measurements must include the program register as well as the small flags.

For a controlled reflection, replace the middle rank-one projector by

```math
|1\rangle\langle1|_c\otimes P_\psi,
```

leaving the scalar branch equal to $`sI`$ on both control values. The resulting block is

```math
\frac{s}{4}C_{R_\phi},\qquad
C_{R_\phi}=|0\rangle\langle0|_c\otimes I+
|1\rangle\langle1|_c\otimes R_\phi.
```

It has a common scalar amplitude on the whole control-plus-data space and the same source-call ledger. This direct construction matters: placing a control around an already measured RUS routine can distort control amplitudes when the two control branches have different success probabilities.

The sign convention in the estimator is $`S_\phi=2|\phi\rangle\langle\phi|-I=-R_\phi`$. As an uncontrolled channel these are identical. For controlled use the known correction is

```math
C_{S_\phi}=(Z_c\otimes I)C_{R_\phi}.
```

Thus a branch-dependent global sign is never silently discarded inside a controlled operation.

## 3. Oblivious amplification at any integer length

Put $`\alpha=s/4`$ and $`\theta=\arcsin\alpha`$. Let $`J=2P-I`$ and define

```math
G=-AJA^\dagger J,\qquad V_j=G^jA\quad(j\geq0).
```

The uniform-singular-value case of oblivious amplitude amplification gives

```math
PV_jP\big|_{\mathrm{ran}P}
=a_jR_\phi,\qquad
a_j=\sin((2j+1)\theta).
```

The same identity holds with the complete controlled target $`C_{R_\phi}`$. One $`V_j`$ uses exactly $`2j+1`$ applications of $`A,A^\dagger`$, hence $`4(2j+1)`$ source calls, and $`2j`$ signal reflections. An overall known sign from an equivalent circuit convention may be retained or corrected; it has no effect on the measured trial below. A negative $`a_j`$ is a scalar phase multiplying the entire target, including both branches of the directly encoded controlled unitary.

This is [BCCKS, Lemma 3.6](https://arxiv.org/pdf/1312.1414), rather than amplification about an unknown input specimen. Only the known signal projector is reflected.

## 4. An exact trial that either applies the target or restores the input

The following argument applies to any unitary $`V`$ with block $`PVP=aR`$, where $`R`$ is unitary and $`a`$ is a real scalar common to every input. Write $`p=a^2`$. The input is arbitrary and is not measured.

1. Apply $`V`$ and measure the binary predicate $`\{P,I-P\}`$. A zero-signal success returns the target output, tagged `DONE`.
2. On failure, apply $`V^\dagger`$ and measure the same binary predicate. A success restores the original input, tagged `RETRY`.
3. If this failed, apply $`V`$ and check again. A success returns the target, tagged `DONE`.
4. Alternate the inverse and forward steps until a success occurs.

Each check must be the **binary nondemolition measurement** of all-zero versus its complement. Measuring every signal qubit separately on a failure would refine the measurement, destroy the two-subspace argument and invalidate the restoration claim. Implement a binary check by computing the all-zero predicate into one flag, measuring only that flag, uncomputing the predicate and resetting the measured flag.

For the proof, let $`|i\rangle=|0\rangle|d\rangle`$ and $`|o\rangle=|0\rangle R|d\rangle`$. For $`0\lt p\lt 1`$, there are unit vectors $`|f\rangle,|g\rangle`$ in the nonzero-signal subspace such that

```math
V|i\rangle=a|o\rangle+\sqrt{1-p}|f\rangle,
\qquad
V|g\rangle=\sqrt{1-p}|o\rangle-a|f\rangle,
```

and consequently

```math
V^\dagger|f\rangle=\sqrt{1-p}|i\rangle-a|g\rangle.
```

To verify that $`|g\rangle`$ has no zero-signal component, define it from $`V^\dagger|o\rangle=a|i\rangle+\sqrt{1-p}|g\rangle`$. The identity $`PV^\dagger P=aR^\dagger`$ makes its projection onto $`P`$ vanish. Substitution gives the displayed equations. After the first failure, every further check therefore succeeds with probability $`1-p`$ and fails with probability $`p`$.

The expected number $`L`$ of $`V,V^\dagger`$ executions in one trial is

```math
\mathbb E L
=1+(1-p)\sum_{k\geq0}p^k=2,
```

whereas the probability that the trial finishes with the target is

```math
\Pr(\mathrm{DONE})
=p+(1-p)^2p\sum_{k\geq0}p^{2k}
=\frac{2p}{1+p}\geq p.
```

The `RETRY` probability is $`(1-p)/(1+p)`$. At $`p=0`$, the trial restores the input after two operations. At $`p=1`$, it returns the target after one. These endpoint cases require no limiting argument in the implementation.

More strongly, the Kraus operator of every finite `DONE` transcript is a scalar multiple of $`R`$; that of every finite `RETRY` transcript is a scalar multiple of $`I`$. Each transcript probability is independent of the input. Tensoring these identities with an arbitrary reference proves reference stability and absence of input-dependent history leakage. Unknown-state copies are never discarded in order to retry a reflection. A `RETRY` restores the original signal-zero input exactly, so the next randomized trial can use it.

## 5. Unknown mass: an integer randomized schedule

For a uniform random $`j\in\{0,\ldots,m-1\}`$, the first-check success probability has average

```math
\overline p_m
=\frac1m\sum_{j=0}^{m-1}\sin^2((2j+1)\theta)
=\frac12-\frac{\sin(4m\theta)}{4m\sin(2\theta)}.
```

In particular, $`\overline p_m\geq1/4`$ when $`m\geq1/\sin(2\theta)`$. The whole input-restoring trial succeeds at least this often. This is the trigonometric averaging step in [BBHT, Section 4, Lemma 2](https://arxiv.org/pdf/quant-ph/9605034).

A convenient implementation uses integer scales $`m_k=2^k`$. At each scale, run at most four independently randomized trials, stopping on `DONE`; after four `RETRY` outcomes double $`m`$. This is a BBHT scheduling variant with no real-valued scale computation. Let $`m_*`$ be the first such scale above $`1/\sin(2\theta)`$. Then

```math
m_*\lt \frac2{\sin(2\theta)},\qquad
\Pr(\hbox{four RETRYs at a scale }m\geq m_*)
\leq(3/4)^4=\frac{81}{256}.
```

One randomized trial costs at most $`8m`$ source calls in expectation: its expected number of $`V_j,V_j^\dagger`$ executions is at most two, and $`\mathbb E(2j+1)=m`$. Therefore a scale costs at most $`32m`$, even if all four trials are charged. The prethreshold scales and the tail give

```math
\begin{aligned}
\mathbb E Q_{\mathrm{ref}}
&\leq32(m_*-1)
+32m_*\sum_{\ell\geq0}
\left(2\frac{81}{256}\right)^\ell\\
&\lt 120m_*
\lt \frac{240}{\sin(2\theta)}
\leq\frac{1920}{\sqrt{15}\,s}
\lt \frac{512}{s}.
\end{aligned}
```

The penultimate inequality uses

```math
\sin(2\theta)
=\frac{s}{2}\sqrt{1-s^2/16}
\geq\frac{\sqrt{15}}8s.
```

The same stage tail proves almost-sure termination. The inner restoration loop also halts almost surely whenever entered: its continuing probability is a power of $`p\lt 1`$; when $`p=1`$ it is never entered.

The usual more finely rounded BBHT schedule also works: take $`m_k=\lceil(6/5)^k\rceil`$ and one randomized input-restoring trial per scale. Before the first scale exceeding $`b=1/\sin(2\theta)`$, the sum of scales is $`O(b)`$. Subsequently the reach probability is at most $`(3/4)^\ell`$, while $`m_{K+\ell}\leq(6/5)^{K+\ell}+1`$. The resulting cost series converges because $`(3/4)(6/5)=9/10\lt 1`$. This explicitly accounts for rounding instead of assuming an exact multiplicative ratio between consecutive integers. The powers-of-two, four-trial version above supplies the concrete constant used here.

## 6. Ordinary conditional-state preparation

Preparation is a separate, cheaper operation because a failed fresh preparation can be discarded. Write $`\sin^2\eta=s`$. Ordinary Grover amplification using reflections about $`|\psi\rangle`$ and $`\Pi`$ leaves the successful component proportional to $`|\phi\rangle`$, with coefficient $`\sin((2j+1)\eta)`$. Projecting onto $`\Pi`$ therefore returns exactly $`|\phi\rangle`$ on every successful attempt, up to an irrelevant global phase. The number of source calls for an attempt is $`2j+1`$.

Use the same integer-scale randomized schedule, with a fresh source state on each attempt. To cover masses close to one uniformly, precede each randomized attempt by one direct preparation and binary $`\Pi`$ check. If $`s\geq1/4`$, this direct check alone gives a constant success probability at every scale. If $`s\lt 1/4`$, the random-length success average is at least $`1/4`$ once

```math
m\geq\frac1{\sin(2\eta)}=O(s^{-1/2}),
\qquad
\sin(2\eta)=2\sqrt{s(1-s)}\geq\sqrt{3s}.
```

Four trials per doubling scale again make the expected tail summable. Thus $`\mathbb E Q_{\mathrm{prep}}\leq C_{\mathrm{prep}}/\sqrt{s}`$ for a universal constant. No value of $`s`$ is estimated and no inverse of this measured preparation routine is constructed. Reflection uses the preceding uniform block encoding instead.

## 7. Workspace, known gates and loop cost

Let $`g_\Pi`$ and $`w_\Pi`$ bound the known-gate and clean-workspace costs of a controlled projector reflection, including its inverse and the few additional known selector controls. The four-query encoder uses $`O(g_\Pi+n+1)`$ known gates. Source-internal workspace, if used by the implementation of $`U`$, is charged separately and returned as required by that interface.

A binary signal check or reflection uses an all-zero predicate on $`n+6`$ signal qubits. Computing that predicate reversibly into one measured flag, and uncomputing it, costs $`O(n+1)`$ known gates with $`O(n+1)`$ clean scratch. Therefore the total coherent width is $`O(n+w_\Pi)`$ in addition to source-internal workspace, plus the target/control registers already specified. A computational prefix projector has a reversible comparison circuit; it is not a table-loading oracle.

Each $`V_j`$ has $`2j+1`$ block-encoder calls, $`2j`$ known signal reflections and one binary check per execution of the restoration loop. Since the expected number of such executions is at most two, the same scheduling proof bounds **all** these operations, not only useful source calls. In particular,

```math
\mathbb E G_{\mathrm{known,ref}}
=O\!\left(\frac{g_\Pi+n+1}{s}\right),
\qquad
\mathbb E G_{\mathrm{known,prep}}
=O\!\left(\frac{g_\Pi+n+1}{\sqrt{s}}\right).
```

At scale $`m=2^k`$, the integer $`j`$ is sampled exactly with $`k`$ fair bits. Direction and success tags use constant classical state. Loop counters can be implemented with amortized $`O(j+k+1)`$ bit work per $`V_j`$ execution, and the outer scale is a binary shift. The stage analysis bounds this additional expected classical work by $`O(1/s)`$ for reflection and $`O(1/\sqrt{s})`$ for preparation. In particular there is no uncharged infinite zero-query computation between oracle calls. Stored classical integers and the stopping time have no deterministic maximum; this expected-work model does not imply a bounded-width classical controller or a fixed coherence deadline.

## Attribution and limits

- [Berry, Childs, Cleve, Kothari and Somma, *Exponential improvement in precision for simulating sparse Hamiltonians*, STOC 2014, arXiv:1312.1414v2](https://arxiv.org/abs/1312.1414): Lemma 3.6 and its two-subspace proof supply oblivious amplification on arbitrary input states.
- [Boyer, Brassard, Høyer and Tapp, *Tight bounds on quantum searching*, Fortschritte der Physik 46, 493–505 (1998)](https://arxiv.org/abs/quant-ph/9605034): Section 4, especially Lemma 2, supplies random-length amplification without a known success probability. The integer-stage modification and its bound are proved above.
- [Marriott and Watrous, *Quantum Arthur–Merlin Games*, Computational Complexity 14, 122–152 (2005)](https://arxiv.org/abs/cs/0506068), and [Watrous, *Zero-knowledge against quantum attacks*, SIAM Journal on Computing 39, 25–58 (2009)](https://arxiv.org/abs/quant-ph/0511020): antecedents for amplification and alternating projective quantum rewinding. The exact input-restoration calculation needed here is given explicitly above.
- [Guerreschi, *Repeat-until-success circuits with fixed-point oblivious amplitude amplification*, Physical Review A 99, 022306 (2019)](https://arxiv.org/abs/1808.02900): controlling a measured RUS operation can produce amplitude distortion. The common scalar in the directly controlled block encoding is the property that prevents it here.

The primitive is a reconstruction from this standard toolbox, not a separate novelty claim of the simplex result. Its resource bound is expected and may have long tails. It uses source-unitary access and its inverse, rather than copies alone. It does not establish $`O(1/\sqrt{s})`$ conditional-reflection cost, a deterministic query cap, coherence across nodes with different masses, or robustness to imperfect gates without a separate approximation argument.
