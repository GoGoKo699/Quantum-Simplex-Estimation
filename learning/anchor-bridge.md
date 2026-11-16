# From quantum algorithms to a valid random probability vector

A source can produce three labels, but its probabilities are unknown. Measuring it repeatedly gives a frequency vector: every entry is nonnegative, the entries sum to one, and their means are correct. The aim here is to keep those properties while reducing the mean-square error quadratically with expected coherent source work. A small coordinate error alone does not ensure this: clipping or renormalizing estimates can change their means.

The single anchor is **Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, 17 April 2025**. Use the [official notes page](https://www.cs.umd.edu/~amchilds/qa/) and its [dated document](https://www.cs.umd.edu/~amchilds/qa/qa.pdf). Page references below are the printed page numbers. The [milestones](milestones.md) organize this project's story; the notes are selective support, not a book-length prerequisite.

## 1. Selective readings

| Anchor section | Printed page | Connection here |
|---|---:|---|
| §§1.1–1.2, quantum data and circuits; §1.4, reversible computation | 1–2 | The complete source, its garbage, and its inverse |
| §4.3, phase estimation | 19 | Coherent powers write phase information into a clock |
| §19.3, amplitude amplification and quantum counting | 88 | Two reflections amplify or measure an event |
| §§21.1–21.3, query complexity, quantum queries, and polynomials | 97–98 | Why an access model and its charged calls matter |
| §28.3, linear combinations of unitaries | 140 | The conditional unitary's scaled success block and oblivious amplification |
| §29.1, block encoding | 143 | A matrix represented by a unitary's flagged block |
| §2.1, subadditivity of errors | 7 | Accumulated approximation in a finite implementation |

A first reading can use §§1.1–1.4, 4.3 and 19.3, then follow the example below. Return to §§28.3 and 29.1 for the conditional circuit. The query sections supply background; the project's expected-work lower bound uses its separately stated source model, not an automatic transfer of a Boolean-oracle theorem.

### Notation dictionary

| Object in the notes | Object in this project | Distinction to retain |
|---|---|---|
| The unitary whose eigenphase is estimated | The Grover product $G$ | The original source is $U$; the clock uses a derived unitary |
| Eigenphase in $e^{i\varphi}$ | Grover phases $\pm\varphi$, with $\cos\varphi=1-2q$ | A phase is not itself the event probability |
| Success probability in amplification | Conditional split probability $q=s_L/s_S$ | The original subset mass is the different quantity $s_S$ |
| Flagged block of a unitary | $(s_S/4)V_S$ | Its success amplitude is $s_S/4$, not $\sqrt{s_S}$ |
| One query in a chosen oracle model | One call to $U$ or $U^\dagger$ | Native gates and known tests also cost work |

Here $V_S=I-2|\phi_S\rangle\langle\phi_S|$ and $|\phi_S\rangle=\Pi_S U|0\rangle/\sqrt{s_S}$. The scalar clock uses the opposite state-reflection sign, $-V_S$; a controlled call includes the corresponding known minus phase. The [scalar page](../science/scalar-clock.md) fixes that convention.

## 2. The missing steps supplied by this project

The notes introduce the algorithmic language. The research account supplies the following specific connections.

1. **A bounded exactly unbiased scalar readout.** The inherited sine-clock estimator returns $Y\in[0,1]$, has mean $q$, and has variance $\kappa_m q(1-q)$. Its exact law and attribution are in [the scalar account](../science/scalar-clock.md). A generic accurate phase readout does not automatically have those moments.
2. **Conditioning without a free conditional inverse.** Filtering a source prepares one conditional specimen. It does not supply the reflection needed by amplitude estimation. The [conditional-reflection proof](../science/conditional-reflection.md) builds the controlled reflection from the original source and known subset tests. Its common success amplitude and input-restoring retries preserve arbitrary data and references.
3. **A budget coupled to a random mass.** A node receives an estimated global mass $W$. It gets a coherent clock only when $TW\ge3$, with clock length at most $TW$. Exact $\mathbb EW=s_S$ pays for the reflection's expected inverse-mass cost. A separate minimum positive weight pays for entering the node.
4. **A full vector proof.** Local mass conservation gives the simplex constraint; conditional expectation gives exact means; martingale increments give the total variance. See [the tree proof](../science/simplex-estimator.md), including zero-mass branches.

These are different arguments. A correct conditional mean does not alone bound work, and a finite expected work bound does not impose a deterministic stopping deadline.

## 3. A complete three-outcome example

Let the source probabilities be

$$
p=(1/2,1/3,1/6).
$$

The algorithm does not receive these numbers. They specify the example whose output law we can calculate. Split labels $\{1,2\}$ from label $3$, so the true root split probability is $s=5/6$. Inside the first group the probability of label $1$ is $r=(1/2)/(5/6)=3/5$.

Use scale $T=3$. The root's sine clock has length $m=3$, whose three possible readouts are $0,1/2,1$. For an event probability $q$, its law is

$$
\Pr(Y=0)=(1-q)^2,\qquad
\Pr(Y=1/2)=2q(1-q),\qquad
\Pr(Y=1)=q^2.
$$

This follows from the three-point support, exact mean $q$, and variance $q(1-q)/2$. At this smallest clock its law coincides with the average of two Bernoulli samples; this example illustrates assembly and accounting, not an asymptotic advantage from that one clock.

Call the root readout $W$. Its probabilities are $1/36$, $5/18$, and $25/36$ respectively. The next action depends on that readout:

- If $W=0$, skip the first group and return $(0,0,1)$.
- If $W=1/2$, then $TW=3/2<3$. Prepare one conditional specimen and measure its label, using a Bernoulli readout $Y$ of mean $r=3/5$.
- If $W=1$, then $TW=3$. Prepare the conditional specimen and use a length-three sine clock for $r$.

In either nonzero branch return

$$
Z=(WY,\,W(1-Y),\,1-W).
$$

The complete ideal output law is therefore:

| Returned vector $Z$ | Probability |
|---|---:|
| $(0,0,1)$ | $1/36$ |
| $(1/2,0,1/2)$ | $1/6$ |
| $(0,1/2,1/2)$ | $1/9$ |
| $(0,1,0)$ | $1/9$ |
| $(1/2,1/2,0)$ | $1/3$ |
| $(1,0,0)$ | $1/4$ |

All six vectors are valid probability vectors. The table probabilities sum to one. Multiplying the first coordinates by their probabilities gives

$$
\mathbb EZ_1=\frac12\frac16+\frac12\frac13+\frac14=\frac12.
$$

The same calculation gives $\mathbb EZ_2=1/3$ and $\mathbb EZ_3=1/6$. Thus the **whole output vector** is exactly unbiased, even though individual runs can be far from $p$. Its exact squared-norm moment is $\mathbb E\|Z\|_2^2=25/36$. Since $\|p\|_2^2=7/18$, its trace mean-square error is $11/36$.

### What was measured and what was paid

At the root, a clock measurement produces $W$. At the child, either one label measurement or another clock measurement produces $Y$. The source's garbage stays inside the full source register used by its inverse and reflection; its particular state does not alter this probability calculation.

Both conditional operations are charged. The root has true mass one. The child has true mass $5/6$, is entered with probability $35/36$, and uses three controlled conditional reflections only in the $W=1$ branch, of probability $25/36$. The primitive bounds therefore give

$$
\mathbb EQ\le
C_{\rm prep}\left(1+\frac{35}{36}\sqrt{\frac65}\right)
+C_{\rm ref}\left(3+\frac{25}{36}\frac{3}{5/6}\right)
\le6(C_{\rm prep}+C_{\rm ref}).
$$

Here $Q$ counts original source and inverse calls; the universal constants are the explicitly implemented primitive bounds in [the model](../science/model.md). Known predicate logic, clock gates, measurements and classical arithmetic remain additional costs. This is an expectation, because the exact conditional routines can retry for arbitrarily long.

For larger $T$, the same construction selects longer clocks only for sufficiently large received weights. Its proof gives total vector error at most $32(d-1)/T^2$ and expected source work at most $(C_{\rm prep}+C_{\rm ref})(d-1)T$. The boundary case is essential: a true zero-mass subset receives positive estimated mass with probability zero, so no undefined conditional operation is entered.

## 4. From the example to the complete result

The example has two splits. A $d$-label tree has $d-1$. To follow the global proof, keep two different masses visible: the true subset mass $s_S$ determines the cost of a conditional operation, while the random received mass $W_S$ determines its clock. Conditional unbiasedness links them through $\mathbb EW_S=s_S$.

The minimum positive weight is a second link. Every visited node has $W_S\ge T^{-2}$. Hence a rare node cannot be visited too frequently. That pays for the conditional specimen; the separate bound on $\mathbb E(TW_S)/s_S$ pays for its controlled reflections. The [martingale proof](../science/simplex-estimator.md) then adds bounded split variances without assuming independent final coordinates.

The [convex-composition page](../science/convex-composition.md) translates the returned weights into known finite convex combinations and fresh stochastic transition tables. It also gives an explicit counterexample to reusing one table under powers. The [precision page](../science/precision-and-resources.md) explains why a finite execution cap and finite gate synthesis preserve a controlled approximation rather than the full exact ideal claim. These boundaries belong to the theorem's meaning, not to optional implementation details.

Use the [milestones](milestones.md) for the full local-to-global route, or the [science index](../science/README.md) for direct access to the canonical statements and proofs. Research citations in [related work](../references/related-work.md) establish attribution; they are not additional educational anchors.
