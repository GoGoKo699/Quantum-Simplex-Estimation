# Learning route

The scientific question is how to estimate several outcome probabilities with quantum precision while returning a valid probability vector in every run. The construction joins a scalar sine-clock estimator, paid reflections about conditional states, and a probability tree whose random node weights determine its work.

The single educational anchor is **Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, 17 April 2025**, available from the [official notes page](https://www.cs.umd.edu/~amchilds/qa/). The [anchor bridge](anchor-bridge.md) gives selective section readings, a notation dictionary, the steps supplied by this project, and a complete three-outcome example. The notes provide foundations rather than the simplex theorem.

The [30-milestone map](milestones.md) has twelve background milestones and eighteen narrative milestones. The first phase connects source circuits, reflections, phase information and charged queries. The second builds the conditional operation and random-mass tree into the theorem, then connects it to convex constraints, stochastic evolution and implementation limits. These are common understanding targets for the project; they do not record an individual reader's assessment or progress.

| Starting point | Route |
|---|---|
| A concrete first encounter | [Worked example](anchor-bridge.md#3-a-complete-three-outcome-example) |
| The prerequisite-to-result connection | [Selective readings and notation](anchor-bridge.md#1-selective-readings) |
| The complete understanding map | [Milestones M01–M30](milestones.md) |
| The formal theorem and assumptions | [Scientific model](../science/model.md) |
| The proofs without the learning route | [Science index](../science/README.md) |
| What the finite checks establish | [Verification guide](../verification/README.md) |

Every route preserves the same qualifications: fixed-alphabet Heisenberg scaling concerns expected source/inverse work with unbounded stopping tails; exactness uses ideal operations; finite caps and synthesis introduce a separately controlled approximation. Positivity and normalization do not make nonlinear reuse of an estimate unbiased.
