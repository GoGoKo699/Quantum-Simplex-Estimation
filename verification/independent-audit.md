# Independent algebra and boundary audit

This note records a separately tasked mathematical pass over the conditional-reflection and tree mechanisms. It is not independent external peer review, a hardware experiment, or an exhaustive proof certificate. The scientific pages contain the authoritative theorem statements.

## Projector and conditional-reflection encoding

For an exact projector $`Q`$, the signal-qubit unitary

```math
(H\otimes I)\operatorname{diag}(I,2Q-I)(H\otimes I)
```

has zero-signal block $`[I+(2Q-I)]/2=Q`$. Multiplying projector encodings with separate signal registers therefore yields top block $`\Pi_S|\psi\rangle\langle\psi|\Pi_S`$. The separate program-register construction yields the scalar block $`sI`$. These are different resources: a postselected specimen alone does not supply the conditional reflection.

The flat four-term linear combination can use branches with top blocks $`sI,-vv^\dagger,-vv^\dagger,0`$. The final zero block is implemented by a signal flip, not by a nonexistent zero unitary. Its selected unitary has top block $`(sI-2vv^\dagger)/4=(s/4)R_\phi`$. The controlled construction retains $`sI`$ in both control sectors and replaces $`vv^\dagger`$ by $`|1\rangle\langle1|\otimes vv^\dagger`$. A branch-dependent success amplitude would reveal the coherent control and would not justify the same argument.

## Repeat-until-success algebra

For a unitary with top block $`aV`$ and $`V`$ unitary, every halting path in the alternating forward/inverse flag-measurement protocol is a scalar multiple of $`V`$ or of the identity. Consequently, reference entanglement survives conditional on the complete classical transcript. With $`p=|a|^2`$, the mean execution count is $`2`$ for $`p<1`$ and $`1`$ at $`p=1`$; the desired-output probability is $`2p/(1+p)`$. At $`p=0`$ the trial resets after two executions and never declares the desired output. The enclosing unknown-amplitude search therefore needs the positive-mass promise for eventual termination.

## A uniform minimum-weight bound

For the dyadic sine-clock family, $`m\ge3`$ and $`\alpha=\pi/(m+1)\le\pi/4`$. The smallest positive readout is

```math
z_2=\frac{\cos\alpha-\cos2\alpha}{2\cos\alpha}
=\frac{\sin(3\alpha/2)\sin(\alpha/2)}{\cos\alpha}.
```

The elementary inequality $`\sin x\ge2x/\pi`$ for $`0\le x\le\pi/2`$ gives

```math
z_2\ge\frac{3\alpha^2}{\pi^2\cos\alpha}
\ge\frac3{(m+1)^2}\ge\frac1{m^2}.
```

The same bound applies to a positive value of $`1-Y`$ by the symmetry of the readout grid. If a node has global weight $`W\le1`$ and uses $`m\le TW`$, either positive child has weight at least

```math
Wz_2\ge\frac{W}{m^2}\ge\frac1{T^2W}\ge\frac1{T^2}.
```

A Bernoulli split retains $`W`$ on its unique positive child. Thus the minimum-positive-weight invariant survives arbitrary tree depth. It does not require a lower bound on the unknown true masses.

For completeness, convexity of $`\tan`$ on $`[0,\pi/4]`$ bounds $`\tan\alpha\le4\alpha/\pi`$, so the scalar variance factor obeys $`\kappa_m\le16/m^2`$. If the largest dyadic clock $`m=2^\ell-1\le t`$ is chosen for $`t\ge3`$, then $`m\ge t/3`$. These loose constants suffice for a uniform per-node martingale second-moment bound.

## Zero masses and the martingale

Exact nonnegativity and $`\mathbb EW=s`$ imply that a zero-mass node has $`W=0`$ almost surely. It is skipped. Arbitrary conventions for its undefined conditional distribution cannot affect the output. Likewise, a split with conditional probability zero or one is deterministic. Conditional descendant distributions on a zero-mass child can be assigned arbitrarily for a proof notation, because the corresponding random weight is identically zero.

In a preorder exposure of the splits, a node contributes the centered increment $`W(Y-r)(q_L-q_R)`$. The normalized descendant vectors have disjoint supports, so $`\|q_L-q_R\|_2^2\le2`$. Conditional centering makes distinct increments orthogonal in mean; summing their second moments is valid for any fixed finite binary tree.

## Numerical checks must preserve analytic endpoints

Floating-point evaluation of a sine transform at $`r=0`$ or $`r=1`$ can leave tiny spurious probability on mathematically impossible readouts. A finite-law checker should impose the proved deterministic endpoint laws explicitly. Otherwise it may spuriously enter a true zero-mass subset, on which the exact conditional routine is intentionally undefined. This is an endpoint identity, not license to drop low-probability outcomes for a generic interior parameter. Rare but positive masses must remain in the enumeration.

This distinction also matters in implementation: approximate physical gates can activate a nominally zero branch, so the ideal halting argument does not establish noisy or finite-precision halting. The separate truncation and error budget must cover that case.
