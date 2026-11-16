# Finite scientific checks

Run from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/run_all.py
```

The script writes [finite-report.json](finite-report.json), records its own SHA256 and the scientific files present at the run, and exits with an assertion failure if a checked statement fails. It uses NumPy only. The checked run used Python 3.12.14 and NumPy 2.3.5; exact runtime versions appear in the report. A different output path can be selected with `--output PATH`.

These are deterministic finite-dimensional floating-point calculations. They support the tested statements and detect several load-bearing implementation errors; they do not prove the general theorem, certify priority, establish finite gate synthesis, simulate hardware, or replace a scientific reading of the proofs.

## What is checked

| Check | Calculation | Failure it can detect |
|---|---|---|
| Scalar experiment with sampler junk | A six-dimensional complex target with three labels and two-dimensional junk; controlled Grover histories, the sine clock and final sine transform are evaluated directly | A wrong reflection sign, lost junk register, wrong clock phase or incorrect readout convention |
| Full probability trees | Every finite local clock law is summed recursively on balanced and comb trees with 3, 4, 5 and 8 leaves | Bias from adaptive allocation, incorrect branch normalization, missing ancestor covariance, zero-mass calls or loss of the positive-weight invariant |
| Actual controlled linear combination | Projector dilations and a separate scalar program build the flat four-term LCU on a 1152-dimensional Hilbert space | A claimed top block that is not the desired common scalar times the controlled reflection |
| Oblivious amplification and measured return | Amplified blocks at four trial lengths and ten subsequent forward/inverse flag checks are evaluated | Input-dependent or control-dependent success factors, incorrect inverse ordering, nonunitary return on a claimed halting branch |
| Stochastic composition | The finite estimator laws for all rows of a two-state transition table are enumerated | Confusing independent fresh tables with repeated use of the same random table |
| Contractive propagation | The first and second moments evolve through the exact $`\mathbb E[Q\otimes Q]`$ map for three binary contraction parameters and horizons zero through twelve | Incorrect horizon accumulation, contraction factor, or cancellation of the row variance and contraction gap |
| Brier excess risk | The estimate and a fresh outcome are summed independently | Confusing independent forecast risk with conditional calibration or a nonlinear unbiasedness claim |

The tree calculation integrates the two sibling kernels independently conditional on their common split. Its second-moment cross blocks use the resulting conditional means, rather than dropping cross-covariance or replacing the computed law by the claimed variance formula. This avoids explicitly expanding the Cartesian product of every leaf outcome while retaining the complete finite first and second moments.

## Boundaries and rare outcomes

The 184 tree cases include exact zeros, deterministic outcomes, interior probabilities, highly uneven masses down to $`10^{-12}`$, and two different tree shapes. Half test the allocation used in the ideal scientific proof:

```math
m(W)=0\quad(TW<3),\qquad
m(W)=2^{\lfloor\log_2(TW+1)\rfloor}-1\quad(TW\ge3).
```

Here $`m=0`$ means measuring one exact conditional specimen. The other half choose the conservative lower weight $`\overline W=\max\{0,W-1/(4T^2)\}`$. This is an admissible worst-error example for the certified finite-arithmetic allocation, rather than an implementation of interval cosine evaluation itself. The checks assert pathwise nonnegativity and normalization, the minimum positive global weight $`T^{-2}`$, vanishing calls to zero-mass subsets, exact-mean agreement within numerical tolerance, and the stated ideal bound

```math
T^2\,\mathbb E\|Z-p\|_2^2\le32(d-1).
```

For the conservative lower-weight policy, the asserted bound is $`64(d-1)`$ instead.

The scalar laws at conditional probabilities zero and one are set to their proved deterministic endpoint laws. A floating-point sine transform otherwise leaves tiny numerical leakage into impossible branches. No small-probability cutoff is used for an interior parameter, and rare positive masses are retained.

## Query accounting and stopping

The report evaluates two **accounting proxies**: $`s^{-1/2}`$ for an entered conditional specimen and $`m/s`$ for the conditional reflections at a node of original mass $`s`$. Their expectations are compared with $`T`$ per internal node. They are not measurements of the full algorithm's gate count or of a stopping-time distribution; BBHT/RUS constants and known gates are established separately in [conditional reflection](../science/conditional-reflection.md) and [resources](../science/precision-and-resources.md).

The LCU test uses actual projector unitary blocks, not a hypothetical unitary formed directly from the already-normalized target reflection. For each tested amplified block, the halting Kraus matrices are compared with a scalar identity or scalar controlled reflection on every input column. This also checks their action on a maximally entangled input/reference. Only ten follow-up paths are expanded numerically; the infinite stopping law and expected work follow from the written algebra, not from this finite expansion.

## Observed values and their meaning

The checked run gave maximum tree mean error below $`9\times10^{-16}`$. Maximum $`T^2`$ times trace MSE per internal node was below $`6.08`$ for the ideal allocator and $`9.12`$ for the conservative lower-weight allocator, within their proved constants $`32`$ and $`64`$. The controlled LCU top-block residual and tested halting Kraus residuals were below $`5\times10^{-16}`$. These are floating-point residuals, not certified exact error bars.

For the displayed two-state table, independent estimator tables reproduce the true squared transition matrix within numerical tolerance. Reusing the same table gives a maximum entry bias of about $`0.0270`$. The counterexample is retained because independent fresh records are a necessary premise of the composition claim.

The separate [algebra and boundary audit](independent-audit.md) reconstructs the minimum-weight, controlled-return and martingale steps. It records a distinct checking pass; it is not external expert review. Finite precision, truncation and physical noise remain governed by their explicit scientific statements.
