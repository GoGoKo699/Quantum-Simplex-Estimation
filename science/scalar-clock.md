# The inherited bounded scalar clock

The tree uses a scalar probability estimate whose output is always between zero and one and whose mean is exactly the probability. This page states the actual circuit and reconstructs its moment calculation so the finite-alphabet construction can be read without an external implementation assumption. The result is inherited from [Bounded Unbiased Amplitude Estimation, revision 940e1e99](https://github.com/GoGoKo699/Bounded-Unbiased-Amplitude-Estimation/tree/940e1e99b3d7b7b0be39eb6bcc1ea41fdf110101); the [related-work account](../references/related-work.md) separates it from the present contribution.

## Circuit and readout

Let $`|\phi\rangle`$ be an available initial specimen and let $`\Pi`$ be a known success projector. Put

```math
q=\langle\phi|\Pi|\phi\rangle,
\qquad G=(2|\phi\rangle\langle\phi|-I)(I-2\Pi).
```

The block requires controlled reflection about this specimen's state, not merely a means to prepare postselected copies. In this project [the conditional-reflection circuit](conditional-reflection.md) supplies that operation and its cost.

For $`m=2^\ell-1\ge3`$, set $`L=m+1`$, $`\alpha=\pi/L`$, and $`c=\cos\alpha`$. Clock labels run from one to $`m`$. Prepare the normalized sine clock and define the type-I discrete sine transform

```math
a_r=\sqrt{\frac2L}\sin(r\alpha),
\qquad D_{jr}=\sqrt{\frac2L}\sin(jr\alpha),
\qquad 1\le r,j\le m.
```

The real matrix $`D`$ is orthogonal and $`D|1\rangle=|a\rangle`$. Prepare $`|a\rangle|\phi\rangle`$, apply the controlled evolution

```math
\sum_{r=1}^m |r\rangle\langle r|\otimes G^r,
```

apply $`D`$ to the clock, measure its label $`j`$, and return

```math
Y=z_j=\frac{1-\cos(j\alpha)/c}{2}.
```

A binary power ladder expands the controlled evolution into exactly $`m`$ controlled Grover steps. The dyadic sine transforms have known ideal circuits with $`O(\log^2(m+1))`$ gates and $`O(\log(m+1))`$ workspace; the cited scalar source supplies their explicit construction. The native cost of each Grover step and the synthesis of the ideal clock rotations remain part of [the resource account](precision-and-resources.md).

## Why the measurement is bounded and unbiased

On the two-dimensional good/bad plane, $`G`$ has eigenvalues $`e^{\pm i\varphi}`$ with

```math
\cos\varphi=1-2q,
\qquad \sin^2\varphi=4q(1-q).
```

The initial state gives equal weights to the two eigenvectors. The reduced clock is the equal mixture of the phase vectors $`v(\varphi)_r=a_re^{ir\varphi}`$ and $`v(-\varphi)`$. Because $`D`$ is real, their clock measurement probabilities coincide. The endpoint cases $`q=0,1`$ follow directly from $`G|\phi\rangle=\pm|\phi\rangle`$.

Let $`H`$ be the path adjacency matrix, $`H_{r,s}=1`$ for $`|r-s|=1`$ and zero otherwise. With $`a_0=a_L=0`$,

```math
Ha=2ca,
\qquad DHD=\operatorname{diag}_{j=1}^m(2\cos(j\alpha)).
```

Thus the reported value is a projective measurement of

```math
B=\frac12\left(I-\frac{H}{2c}\right).
```

Its eigenvalues are exactly $`z_j\in[0,1]`$. The phased vector has

```math
\langle v(\varphi)|H|v(\varphi)\rangle=2c\cos\varphi,
\qquad \mathbb EY=\langle B\rangle=q.
```

At $`q=0`$ only $`j=1`$ occurs and $`Y=0`$; at $`q=1`$ only $`j=m`$ occurs and $`Y=1`$. These endpoint laws are exact, and are essential for never entering a zero-probability subset in the ideal tree.

## Exact variance

Since the mean is $`q`$, the variance on a phase vector is $`\|(B-qI)v(\varphi)\|^2`$. Direct substitution gives

```math
[(B-qI)v(\varphi)]_r
=\frac{i\sin\varphi}{4c}e^{ir\varphi}(a_{r-1}-a_{r+1}).
```

The sine addition formula yields

```math
\sum_{r=1}^{m}(a_{r-1}-a_{r+1})^2
=4\frac{m-1}{m+1}\sin^2\alpha.
```

Consequently both phase vectors, and their mixture with the same mean, have

```math
\operatorname{Var}(Y)
=\kappa_m q(1-q),
\qquad
\kappa_m=\frac{m-1}{m+1}\tan^2\!\left(\frac\pi{m+1}\right).
```

In particular $`\kappa_m=O(m^{-2})`$. The tree needs one further discrete property: the smallest positive readout, including for the complementary value $`1-Y`$, is

```math
z_2=\frac{\sin(3\alpha/2)\sin(\alpha/2)}{\cos\alpha}
\ge\frac3{(m+1)^2}.
```

This minimum output weight pays for the frequency of expensive conditional-state preparations. Scalar variance reduction alone does not supply that global tree accounting.
