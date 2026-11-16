# Thirty milestones: from one source to a valid random probability vector

This is the common understanding map for Quantum Simplex Estimation. Its single educational anchor is Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, **17 April 2025**, available from the [author's course page](https://www.cs.umd.edu/~amchilds/qa/). The source pointers below identify exact sections in that version. The anchor supplies quantum-circuit, amplification, phase-estimation and block-encoding foundations; the statistical argument, inherited sine measurement and present conditional tree are supplied by this repository and its credited research sources.

The map has **12 background/preliminaries milestones, M01–M12, and 18 narrative/innovation milestones, M13–M30**. The first phase joins a labelled quantum experiment, a valid probability estimate and the operations that can be paid for. The second builds the conditional reflection and random-mass tree, proves their global statistical and resource guarantees, then explains composition and implementation limits. This allocation follows the two ingredients that must meet: a quantum operation must remain coherent inside a split, and its random classical output must remain a valid probability vector outside it.

Each milestone has a conceptual target and earlier dependencies. The map covers the connected scientific account without assigning every technical detail or implying that all of it appears in the anchor. Begin with the [source-to-project bridge](anchor-bridge.md) for notation and a complete small example. The [scientific reading route](../science/README.md) provides direct access to the authoritative proofs.

## Phase I: background and preliminaries

### M01 — A labelled experiment and its hidden workspace

**Phase:** background/preliminaries.

- **Central question:** What distribution is produced when a coherent source has both an output label and unobserved garbage?
- **Understanding target:** Explain why the squared norm of each labelled component is its outcome probability, and why garbage may be arbitrary while the complete source register must remain available to its inverse.
- **Dependencies and story role:** No earlier milestone. This identifies the experiment whose probabilities the project estimates.
- **Conceptual connection:** Measurement probabilities connect quantum amplitudes to an ordinary categorical distribution without assuming clean label amplitudes.
- **Source pointers:** Childs §§1.1–1.2; [model §1](../science/model.md#1-source-and-labels).

### M02 — Three properties of an empirical probability vector

**Phase:** background/preliminaries.

- **Central question:** Why are positivity, normalization and the correct expectation separate requirements?
- **Understanding target:** Distinguish a valid probability vector in each run from a vector whose coordinates merely have the right means. Interpret mean squared Euclidean error as total coordinate variance for an unbiased estimator.
- **Dependencies and story role:** M01. This turns the source experiment into a precise statistical output problem.
- **Conceptual connection:** The simplex is both a feasible set for every realization and the domain of the unknown target. Averaging and nonlinear repair have different effects on the mean.
- **Source pointers:** Childs §1.1 for outcome probabilities; the statistical definitions are in [model §3](../science/model.md#3-required-output-and-error) and [the classical empirical vector](../science/lower-bounds.md#classical-independent-sample-lower-bound).

### M03 — A coherent query and its inverse

**Phase:** background/preliminaries.

- **Central question:** Which access distinguishes the quantum experiment from receiving independent classical samples?
- **Understanding target:** Identify the actual source unitary, inverse and known controls. Explain why a reversible circuit can be run coherently, whereas a measured output specimen alone is not an inverse oracle.
- **Dependencies and story role:** M01–M02. This fixes the resource model before an apparent precision gain is interpreted.
- **Conceptual connection:** Reversible computation and query accounting connect a source program to the operations an amplitude-estimation circuit can execute.
- **Source pointers:** Childs §§1.4, 1.6 and 21.1–21.2; [model §2](../science/model.md#2-allowed-work-and-charged-resources).

### M04 — A subset test is a binary projective measurement

**Phase:** background/preliminaries.

- **Central question:** How can a label subset be tested while preserving coherence inside its two outcome sectors?
- **Understanding target:** Describe the projector for a known subset, its reflection, and the good/bad decomposition. Distinguish the two-outcome test of an all-zero flag from measuring every signal register separately on failure.
- **Dependencies and story role:** M01 and M03. This supplies the measurement interface used by both conditioning and rewinding.
- **Conceptual connection:** A classical label predicate becomes a coherent reflection; the precise measurement instrument determines what information a failure record reveals.
- **Source pointers:** Childs §§1.1–1.2 and 19.3; [projector encodings](../science/conditional-reflection.md#1-exact-projector-encodings) and [binary flag checks](../science/precision-and-resources.md#binary-flag-checks-are-necessary).

### M05 — Two reflections produce a probability-dependent rotation

**Phase:** background/preliminaries.

- **Central question:** Why does a success probability appear as an angle in Grover dynamics?
- **Understanding target:** Relate the normalized good/bad plane, the reflection about the prepared state, and the success reflection. Track the sign convention that makes the cosine of the Grover eigenphase equal to one minus twice the probability.
- **Dependencies and story role:** M03–M04. This provides the local quantum mechanism behind probability estimation.
- **Conceptual connection:** Geometry of two reflections turns a measurement probability into coherent phase information.
- **Source pointers:** Childs §§19.1–19.3; [scalar circuit](../science/scalar-clock.md#circuit-and-readout) and [its good/bad reduction](../science/scalar-clock.md#why-the-measurement-is-bounded-and-unbiased).

### M06 — Amplification without knowing the success mass

**Phase:** background/preliminaries.

- **Central question:** How can a conditional specimen be obtained when its probability is unknown?
- **Understanding target:** Explain why randomly selected amplification lengths and verified success avoid a supplied probability estimate. Separate almost-sure termination and finite expected work from a deterministic deadline.
- **Dependencies and story role:** M04–M05. This introduces the stopping-time resource that later conditioning must pay for.
- **Conceptual connection:** Coherent amplification changes the cost of obtaining a successful specimen; its success test does not create a reversible conditional source.
- **Source pointers:** Childs §19.3 for amplification; the unknown-mass schedule and its exact successful state are derived in [conditional preparation](../science/conditional-reflection.md#6-ordinary-conditional-state-preparation).

### M07 — A phase clock becomes a classical readout

**Phase:** background/preliminaries.

- **Central question:** What do controlled powers and a Fourier-type readout extract from an eigenphase?
- **Understanding target:** Follow a clock register through controlled evolution and basis change. Distinguish an estimate's numerical output, its expectation and its probability law.
- **Dependencies and story role:** M03 and M05. This prepares the reader for the particular sine clock rather than assuming that all phase readouts share its moments.
- **Conceptual connection:** Phase estimation supplies the architecture; choosing a clock state and readout observable determines the estimator's statistical properties.
- **Source pointers:** Childs §§4.1–4.3 and 19.3; [scalar clock circuit and readout](../science/scalar-clock.md#circuit-and-readout).

### M08 — A bounded observable gives a bounded unbiased scalar

**Phase:** background/preliminaries.

- **Central question:** Why does the inherited sine measurement always report a number between zero and one with exactly the right mean?
- **Understanding target:** Connect the sine state, path-adjacency eigenvectors and the measured clock observable. Explain how its spectrum gives boundedness and its phased expectation gives unbiasedness.
- **Dependencies and story role:** M02, M05 and M07. This establishes the scalar ingredient that the present work inherits.
- **Conceptual connection:** An observable's spectrum controls individual realizations, while its expectation controls the estimator's mean; these are different parts of the same measurement construction.
- **Source pointers:** Childs §4.3 for the clock foundation; the specific sine observable and proof are in [the inherited scalar account](../science/scalar-clock.md#why-the-measurement-is-bounded-and-unbiased), with attribution in [related work §3](../references/related-work.md#3-the-bounded-scalar-estimator-is-an-inherited-foundation).

### M09 — Scalar variance and exact endpoint behavior

**Phase:** background/preliminaries.

- **Central question:** Which properties of the scalar law matter beyond its precision exponent?
- **Understanding target:** Interpret the variance coefficient proportional to the probability times its complement, deterministic outputs at zero and one, and the smallest positive discrete readout. Recognize that all three will enter the tree proof.
- **Dependencies and story role:** M08. This identifies the specific inherited facts needed for rare branches and simplex faces.
- **Conceptual connection:** A local measurement's support is a computational resource: its minimum positive value will control the frequency of expensive conditional work.
- **Source pointers:** Childs §19.3 for counting background; [scalar variance and discrete support](../science/scalar-clock.md#exact-variance) and [the scalar facts used by the tree](../science/simplex-estimator.md#1-inherited-scalar-sine-estimator).

### M10 — Small operator blocks inside larger unitaries

**Phase:** background/preliminaries.

- **Central question:** How can a contraction such as a projector or weighted operator be represented by a unitary circuit?
- **Understanding target:** Identify a block encoding's signal-zero subspace, normalization and data register. Explain how products and linear combinations produce the desired zero block, and why oblivious amplification needs a scalar times a unitary on all data inputs.
- **Dependencies and story role:** M03–M05. This supplies the algebraic toolbox for constructing a conditional reflection from the original source.
- **Conceptual connection:** A probabilistic block can implement an operation on unknown data only when its success structure preserves that data coherently.
- **Source pointers:** Childs §§28.3 and 29.1; [projector products](../science/conditional-reflection.md#1-exact-projector-encodings), [flat LCU](../science/conditional-reflection.md#2-a-flat-four-way-unitary-block-encoder) and [oblivious amplification](../science/conditional-reflection.md#3-oblivious-amplification-at-any-integer-length).

### M11 — Conditional means connect adaptive local experiments

**Phase:** background/preliminaries.

- **Central question:** What statistical identity remains useful when a later experiment's budget depends on an earlier result?
- **Understanding target:** Explain conditional unbiasedness given the completed record, the tower rule for expectations, and why zero-mean martingale increments have no cross terms in total mean squared error.
- **Dependencies and story role:** M02 and M09. This supplies the local-to-global probability language needed for the adaptive tree.
- **Conceptual connection:** A random budget can change work and variance while preserving the mean, provided the local estimator is unbiased at every selected budget.
- **Source pointers:** Childs §21.1 for the algorithmic setting; the required probability argument is supplied in [split means](../science/simplex-estimator.md#3-what-every-split-preserves) and [the vector martingale](../science/simplex-estimator.md#5-uniform-mean-squared-error).

### M12 — The complete background contract

**Phase:** background/preliminaries.

- **Central question:** What must be available, paid for and returned before a scalar quantum estimate can become a valid multinomial estimate?
- **Understanding target:** Assemble the source/inverse, known subset predicates, initial conditional specimens, controlled reflections, scalar readout and conditional-mean rules into one operational problem. State why scalar precision alone does not settle it.
- **Dependencies and story role:** M01–M11. This integrates the background phase and fixes the question answered by the construction.
- **Conceptual connection:** Quantum access and classical output geometry impose simultaneous requirements; neither one may be removed from the resource comparison.
- **Source pointers:** Childs §§1.4, 19.3, 21.1–21.2, 28.3 and 29.1; [model §§2–5](../science/model.md#2-allowed-work-and-charged-resources) and [the retained contribution](../references/related-work.md#5-operational-scope).

## Phase II: narrative and innovation

### M13 — The missing inverse inside a conditional split

**Phase:** narrative/innovation.

- **Central question:** Why does preparing a postselected conditional specimen fail to provide everything needed by its sine estimator?
- **Understanding target:** Distinguish a successful state specimen from an exact coherent reflection about that normalized state. Identify the unknown subset mass in the desired normalized projector and the operations that the original source actually supplies.
- **Dependencies and story role:** M06, M08, M10 and M12. This isolates the load-bearing implementation gap before the tree is assembled.
- **Conceptual connection:** A conditional state's normalization is harmless when merely measuring one specimen but becomes an operator-construction problem when the state must define a coherent reflection.
- **Source pointers:** Childs §§19.3 and 29.1; [paid conditional interfaces](../science/model.md#4-two-paid-conditional-operations) and [the conditional-reflection setup](../science/conditional-reflection.md#interfaces-and-assumptions).

### M14 — A common-amplitude controlled reflection block

**Phase:** narrative/innovation.

- **Central question:** How can the unnormalized source data encode the normalized conditional reflection?
- **Understanding target:** Reconstruct the scalar-mass block and projected rank-one block, then combine them into the subset mass times the desired reflection. Explain why the controlled construction must have the same scalar amplitude on both control sectors.
- **Dependencies and story role:** M10 and M13. This provides the concrete operator to which amplification and rewinding can be applied.
- **Conceptual connection:** The unknown normalization moves into a common success amplitude; it is not estimated or supplied as a free parameter.
- **Source pointers:** Childs §§28.3 and 29.1; [the flat four-way block encoding](../science/conditional-reflection.md#2-a-flat-four-way-unitary-block-encoder).

### M15 — A failure that restores unknown data

**Phase:** narrative/innovation.

- **Central question:** How can a measured attempt be repeated without discarding or disturbing unknown input data?
- **Understanding target:** Follow the alternating forward/inverse binary checks. Explain why each terminating history applies either the target unitary or the identity up to one scalar, including when the data is entangled with a reference.
- **Dependencies and story role:** M04, M10 and M14. This resolves the coherence requirement inside the conditional scalar clock.
- **Conceptual connection:** Equal singular values turn the signal measurements into input-independent records, so classical retries can coexist with an exact coherent data operation.
- **Source pointers:** Childs §28.3 for oblivious amplification; [the exact restoring trial](../science/conditional-reflection.md#4-an-exact-trial-that-either-applies-the-target-or-restores-the-input) supplies the project-specific calculation.

### M16 — Two different prices for conditioning

**Phase:** narrative/innovation.

- **Central question:** What is the expected cost of obtaining a specimen, and of applying a reflection, on a rare subset?
- **Understanding target:** Derive the distinct inverse-square-root-mass and inverse-mass bounds from the verified-success and input-restoring schedules. Explain their almost-sure termination and unbounded tails without assuming the mass is known.
- **Dependencies and story role:** M06 and M14–M15. This completes the paid conditional toolkit before its cost is cancelled globally.
- **Conceptual connection:** State acquisition and coherent operation on arbitrary data are different tasks and need separate resource ledgers.
- **Source pointers:** Childs §§19.3 and 28.3; [unknown-mass reflection schedule](../science/conditional-reflection.md#5-unknown-mass-an-integer-randomized-schedule), [specimen preparation](../science/conditional-reflection.md#6-ordinary-conditional-state-preparation) and [native work](../science/conditional-reflection.md#7-workspace-known-gates-and-loop-cost).

### M17 — A three-label split that conserves mass

**Phase:** narrative/innovation.

- **Central question:** How can two binary estimates form one jointly valid three-outcome estimate?
- **Understanding target:** Explain the output consisting of a first mass times a conditional split, its complementary child, and the remaining root mass. Track positivity and exact normalization on an individual run.
- **Dependencies and story role:** M02, M08 and M16. This turns the paid ingredients into a complete small example of the proposed output object.
- **Conceptual connection:** Complementary child weights are formed together, so their joint normalization does not require repairing independently estimated coordinates.
- **Source pointers:** Childs §19.3 for the binary quantum building block; [three-label example](../science/simplex-estimator.md#7-three-labels-as-a-worked-example) and [forecast example](../science/convex-composition.md#2-a-three-outcome-forecast).

### M18 — Unbiasedness survives a random local budget

**Phase:** narrative/innovation.

- **Central question:** Why does selecting a child clock from the first random weight preserve the correct leaf means?
- **Understanding target:** Use the conditional mean at every allowed clock and the tower rule to obtain the mean of each product weight. Explain why zero true mass gives zero estimated mass almost surely and prevents an undefined conditional call.
- **Dependencies and story role:** M11 and M17. This proves the statistical correctness of adaptive splitting before discussing its precision.
- **Conceptual connection:** Exact positivity makes the expectation-zero statement operational: it becomes an exact guard against entering a zero-probability subset.
- **Source pointers:** Childs §§1.1 and 19.3 for source/estimation foundations; [preserved split means and zero-mass induction](../science/simplex-estimator.md#3-what-every-split-preserves).

### M19 — Spend coherent work in proportion to estimated mass

**Phase:** narrative/innovation.

- **Central question:** Why does a node with a small received weight use an ordinary sample while a larger one receives a sine clock?
- **Understanding target:** Explain the threshold at received weight times scale equal to three, the largest allowed dyadic clock, and why the local weighted variance remains uniformly bounded by a constant times inverse scale squared.
- **Dependencies and story role:** M09, M16 and M18. This introduces the allocation that changes the complete expected-cost comparison.
- **Conceptual connection:** A small mass can tolerate a noisy local split because its contribution to the final vector is multiplied by that mass.
- **Source pointers:** Childs §§4.3 and 19.3; [the allocation algorithm](../science/simplex-estimator.md#2-the-algorithm) and [its local variance bound](../science/simplex-estimator.md#5-uniform-mean-squared-error).

### M20 — A discrete minimum pays for rare entries

**Phase:** narrative/innovation.

- **Central question:** How can the tree pay for initially preparing a rare conditional specimen?
- **Understanding target:** Follow the invariant that every positive global weight is at least inverse scale squared. Combine it with the exact mean weight to bound the probability that a node is entered, and explain why the invariant does not deteriorate with depth.
- **Dependencies and story role:** M09 and M18–M19. This supplies the resource argument that a variance bound or reflection-cost cancellation alone would miss.
- **Conceptual connection:** Discrete output support links a statistical realization to the expected frequency of an expensive quantum operation.
- **Source pointers:** Childs §19.3 for conditional preparation background; [minimum positive weights](../science/simplex-estimator.md#4-a-minimum-positive-global-weight) and [specimen cost](../science/simplex-estimator.md#6-expected-original-source-queries).

### M21 — The local errors form one vector martingale

**Phase:** narrative/innovation.

- **Central question:** Why do the split errors add in mean square rather than accumulating as an uncontrolled product error?
- **Understanding target:** Describe the frontier's true conditional leaf distributions, the zero-mean increment revealed by one split, and the disjoint child supports. Use their bounded norm and orthogonal martingale increments to obtain the finite-alphabet trace-MSE bound.
- **Dependencies and story role:** M11 and M18–M20. This integrates the local statistical mechanism into the full error theorem.
- **Conceptual connection:** The tree's exact mass conservation and conditional unbiasedness produce a martingale whose endpoint is the returned vector.
- **Source pointers:** Childs §21.1 for the algorithmic setting; the martingale argument and constant32 are supplied in [uniform mean squared error](../science/simplex-estimator.md#5-uniform-mean-squared-error).

### M22 — Cancellation of the inverse-mass reflection cost

**Phase:** narrative/innovation.

- **Central question:** Why does an arbitrarily small subset probability not destroy the uniform expected query bound?
- **Understanding target:** Separate the initial specimen charge from the repeated reflection charge. For the latter, combine the clock bound by scale times random weight with the weight's exact mean; include every inverse, failed trial and rewind.
- **Dependencies and story role:** M16, M18–M20. This integrates the implementation and probability accounting into the global work bound.
- **Conceptual connection:** The same conditional unbiasedness that preserves the final means cancels the inverse true mass in expected coherent work.
- **Source pointers:** Childs §§21.1–21.2 and 28.3; [expected source-query proof](../science/simplex-estimator.md#6-expected-original-source-queries) and [conditional native ledger](../science/conditional-reflection.md#7-workspace-known-gates-and-loop-cost).

### M23 — The complete finite-alphabet theorem

**Phase:** narrative/innovation.

- **Central question:** Which guarantees have now been established together, and with which dependence on alphabet size?
- **Understanding target:** State exact simplex membership, exact coordinate means, the mean squared error bound proportional to the number of internal nodes over scale squared, and expected work proportional to internal nodes times scale. Distinguish fixed-dimension precision optimality from an unproved dimension-optimal law.
- **Dependencies and story role:** M17–M22. This is the first synthesis of the complete ideal contribution.
- **Conceptual connection:** A local measurement, a paid conditional operation and a global probability argument jointly produce a valid classical probability object at the quantum precision rate.
- **Source pointers:** Childs §§19.3 and 21.1–21.2 for precision/query foundations; [model theorem](../science/model.md#5-the-finite-alphabet-result), [full tree proof](../science/simplex-estimator.md) and [what is matched](../science/lower-bounds.md#what-is-matched).

### M24 — Convex constraints remain true in each realization

**Phase:** narrative/innovation.

- **Central question:** What changes when the probability weights multiply known vectors rather than one-hot label vectors?
- **Understanding target:** Explain why the resulting estimate stays in the supplied finite convex hull, preserves its affine constraints, and has the correct mean. Relate the variance to the hull's diameter and distinguish smooth-loss control from unbiased nonlinear plug-in values.
- **Dependencies and story role:** M02, M21 and M23. This identifies a consequence of the joint output constraint beyond coordinate accuracy.
- **Conceptual connection:** The simplex theorem transfers through a known affine map while retaining both feasibility and the expectation.
- **Source pointers:** Childs §1.4 for implementing the supplied computation; the geometric consequence and paid table/output costs are in [finite convex ranges](../science/convex-composition.md#1-a-finite-known-convex-range).

### M25 — Fresh stochastic matrices preserve mean evolution

**Phase:** narrative/innovation.

- **Central question:** When does a product of random valid transition matrices have the desired mean product?
- **Understanding target:** Identify the conditional-mean requirement on each fresh matrix and show how it preserves probability vectors and their mean evolution. Explain the explicit failure when one unbiased random matrix is reused in its own square.
- **Dependencies and story role:** M11, M23–M24. This turns a one-run feasible estimate into a composition rule with an essential freshness condition.
- **Conceptual connection:** Entrywise unbiasedness becomes compositional only when the next random operator has the correct mean conditional on the past.
- **Source pointers:** Childs §18.2 for Markov-chain context; [fresh matrix products](../science/convex-composition.md#3-fresh-stochastic-matrices-preserve-the-mean-evolution) and [the reuse counterexample](../science/convex-composition.md#5-why-one-random-table-cannot-be-reused-without-analysis) supply the project statements.

### M26 — Stable error under a contractive mean kernel

**Phase:** narrative/innovation.

- **Central question:** Which contraction property prevents fresh row-estimation error from growing indefinitely?
- **Understanding target:** Derive the error recurrence with a zero-mean innovation and identify the contraction assumption on deterministic mean matrices. Explain the binary contracting example, the remaining linear horizon cost, and why row stochasticity alone does not imply Euclidean contraction.
- **Dependencies and story role:** M11, M21 and M25. This supplies a concrete useful regime for repeated valid stochastic operators.
- **Conceptual connection:** Martingale noise cancellation combines with deterministic contraction; the random realized matrices need not themselves contract.
- **Source pointers:** Childs §18.2 for transition-operator background; [contractive variance propagation](../science/convex-composition.md#4-a-variance-bound-for-contractive-mean-dynamics) and [the explicit binary family](../science/convex-composition.md#an-explicit-contracting-family).

### M27 — Precision lower bounds with the same budget convention

**Phase:** narrative/innovation.

- **Central question:** What does the precision comparison establish when algorithms may stop adaptively?
- **Understanding target:** Explain the two nearby Bernoulli-source alternatives, expected-budget truncation in the quantum hybrid, and the stopped-transcript divergence in the classical sample bound. State exactly which precision orders are matched at fixed dimension.
- **Dependencies and story role:** M03, M06, M22–M23. This places the achieved precision rate against an appropriate baseline without substituting a fixed-query proof for an expected-query claim.
- **Conceptual connection:** A resource definition must travel through a lower-bound argument just as carefully as through an algorithm.
- **Source pointers:** Childs §§21.1–21.2 for query models and lower-bound context; [the quantum expected-budget proof](../science/lower-bounds.md#quantum-lower-bound-with-a-uniform-expected-budget), [the classical sample proof](../science/lower-bounds.md#classical-independent-sample-lower-bound) and [comparison scope](../science/lower-bounds.md#what-is-matched).

### M28 — Finite budget arithmetic and finite output are different

**Phase:** narrative/innovation.

- **Central question:** Which classical approximations can change work allocation while preserving the ideal estimator's exact mean?
- **Understanding target:** Explain certified lower approximations of a positive weight, endpoint-based zero recognition, and the relaxed error constant of the finite allocator. Distinguish that policy from rounding returned split values, which preserves the simplex but generally introduces bias.
- **Dependencies and story role:** M19–M23. This makes the mathematical budget rule executable without treating exact real comparisons as free.
- **Conceptual connection:** An approximate past-record-dependent choice of an otherwise unbiased experiment differs from approximation of the experiment's returned value.
- **Source pointers:** Childs §§1.4–1.5 and 3.4 for effective computation and synthesis context; [the certified allocator](../science/simplex-estimator.md#9-a-certified-finite-arithmetic-clock-choice) and [simplex-preserving output rounding](../science/precision-and-resources.md#rounding-while-preserving-the-simplex).

### M29 — A finite cap protects the zero-mass boundary

**Phase:** narrative/innovation.

- **Central question:** Why does a tiny gate error require more than the ideal almost-sure termination argument?
- **Understanding target:** Explain how an error could activate a zero-mass branch, why all work events must be included in a cap, and how abort probability, channel perturbation and rounding affect bias and mean squared error. Distinguish expected work from the larger worst-case execution cap.
- **Dependencies and story role:** M04, M18, M22 and M28. This completes the implementation qualification that accompanies the exact ideal result.
- **Conceptual connection:** Exact boundary support protects the ideal stopping rule; a perturbed implementation instead needs an explicit total-work and statistical-error budget.
- **Source pointers:** Childs §§2.1, 3.4 and 1.7 for error accumulation, synthesis and fault-tolerance background; [capped implementation theorem](../science/precision-and-resources.md#a-capped-perturbed-implementation-theorem), [retaining the expected precision exponent](../science/precision-and-resources.md#precision-choice-retaining-the-expected-exponent) and [zero-mass qualification](../science/precision-and-resources.md#why-the-cap-is-needed-at-zero-mass).

### M30 — The contribution, its uses and its boundaries

**Phase:** narrative/innovation.

- **Central question:** What can now be produced, after the inherited tools and all material qualifications are stated?
- **Understanding target:** Give one connected account from the original paid source to an unbiased feasible probability vector, its expected-work precision law, and its convex/stochastic uses. Credit existing scalar, multivariate and debiasing results, and retain the limits on dimension, stopping tails, finite precision, coherent multirow use and unrestricted classical advantage.
- **Dependencies and story role:** M12 and M23–M29. This integrates both phases into the complete scientific account rather than adding another extension.
- **Conceptual connection:** The surviving addition is the simultaneous per-realization convex constraint and exact ideal mean, supported by an executable conditional construction and global cost proof.
- **Source pointers:** Childs §§19.3, 21.1–21.2, 28.3 and 29.1 for the assembled toolbox; [model theorem](../science/model.md#5-the-finite-alphabet-result), [operational contribution and attribution](../references/related-work.md#5-operational-scope), [convex/stochastic scope](../science/convex-composition.md#6-what-this-capability-adds) and [precision account](../science/precision-and-resources.md).
