# Strategy for making optimization patterns useful in SEFOP

## Purpose and instructions for the LLM

Use this brief to revise the optimization-patterns material into practical software design
guidance for operations research scientists and their managers. Read `.claude/CLAUDE.md` first
and follow its audience, reasoning, terminology, pseudocode, figure, and writing conventions.

The main target is Chapter 8, "Optimization patterns", in `book/04-design/README.md`, anchored
at `ch-optimization-patterns`. It is not Chapter 8 of the testing section, which is "Testing an
optimization model". Read both sections before deciding how to integrate the changes.

Implement the strategy with judgment. The proposed responsibilities below are design guidance,
not a mandatory class hierarchy. Preserve useful existing material and avoid unrelated rewrites.

## Diagnosis

The current chapter proposes four recurring arrangements: single, sequential, iterated, and selected
solve. It explains their structures and, especially, which result statuses they can justify.
Those are useful contributions, but they leave a practical question unanswered: how should a
reader divide responsibilities when building one of these arrangements?

The opening currently says, "As with design patterns, the gain is a vocabulary." Vocabulary is
useful, but the chapter should also help readers make design decisions. The audience already
recognizes sequential models, decomposition loops, and algorithm selection. SEFOP can explain
which software boundaries these arrangements need and why those boundaries make change cheaper.

The material already has connections to the book:

- The contracts chapter defines `Instance`, `Solution`, `Result`, and `SolutionProvider`.
- The Strategy material implements selection between interchangeable providers.
- Chapter 9, "A clean architecture for the cargo loading system", chooses a selected solve and
  explains why its formulation stays with its solver beside the use cases.
- The testing section applies the shared optimization contract and its result statuses.

Strengthen those connections through practical consequences rather than adding more navigation.

The current section has ten chapters, ending with "10. Conclusion". There is no separate
formulation-placement chapter. Keep the current term "sequential solve", its figure anchor
`fig-sequential-solve`, and its asset name. Do not restore removed material as part of this task.

## Central teaching claim

An optimization arrangement determines who owns coordination, which records cross module
boundaries, and which guarantees the whole can make.

Keep the existing idea that a complete arrangement can present one provider boundary to its
caller. Explain how the internal responsibilities support that boundary. Intermediate stages
and evaluators may need their own contracts and records: do not force every internal operation
to use the final problem's `Instance` and `Result` unchanged.

Resolve this explicitly with the current statement that every provider takes the same `Instance`
and returns the same `Result`. Interchangeable providers for one problem share one contract;
providers solving different subproblems need contracts for those subproblems. Nesting works only
when an inner arrangement's complete output satisfies the contract expected at that boundary.
Describe any translation required rather than claiming arbitrary arrangements plug together.

Present the four patterns as a small catalogue of useful arrangements, not an exhaustive or
mutually exclusive classification. They can be combined. The names are proposed vocabulary;
do not claim they are established terminology or that comparable terminology does not exist
without evidence.

## Reframe the opening around a design problem

Begin with a principle readers already accept, identify the difficulty specific to optimization
software, and then introduce the arrangements as a response. A possible direction is:

> An optimization step may start as one model and grow into several models, a heuristic, or a
> loop with a simulation. When their coordination and their algorithms live together, changing
> one changes the others. How should the software divide those responsibilities?

Adapt this wording to the surrounding chapter. The lead should establish the problem before
naming the solution. Explain that the aim is to contain foreseeable changes, using the design
principles already introduced in the section.

## Add design guidance to each arrangement

Retain the problem, structure, and consequences where they help. Add concrete responsibility and
boundary decisions, together with the reason for each decision. Avoid mechanically repeating
the same subsection template if the material reads better in prose.

### Single solve

- Keep solver objects and algorithm-specific state inside the provider.
- Return ordinary records that express the promised decision and status.
- Split internal modules when they have different reasons to change, rather than creating a
  module for every variable or constraint automatically.
- Explain when one cohesive provider is sufficient. More boundaries have a cost.

Connect this guidance to information hiding and the earlier discussion of when splitting stops
helping. Leave the cargo provider's architectural placement to Chapter 9's existing discussion.

### Sequential solve

- Give each stage a contract appropriate to the decision it actually solves.
- Define the intermediate record explicitly, including what the next stage may assume.
- Have a coordinator construct the next stage's input and handle an incomplete or failed stage.
- Keep solver-specific variables and model objects out of the intermediate record unless a
  deliberate, explained design requires that dependency.
- Distinguish a one-way sequence from a design that retries earlier decisions after later failure.

Explain how these choices contain changes to a stage while acknowledging real coupling through
the intermediate record. Preserve the warning that optimal stages do not generally prove a
globally optimal decision. A failure under a fixed earlier choice does not by itself establish
infeasibility of the original problem.

Do not treat a sequence of preprocess, solve, and postprocess as a sequential solve: the pattern
coordinates different optimization decisions. Explain the distinction briefly if the example
would otherwise invite confusion.

### Iterated solve

- Let a coordinator own iteration state, the best accepted solution, and termination.
- Give the evaluator an explicit contract and an evaluation record describing acceptance and
  feedback. Define their meanings before using them.
- Separate algorithm-specific interpretation of feedback from the coordination of rounds.
- Keep mutable search state local to one invocation, or make any deliberate reuse explicit.
- Define what happens at a limit, when no candidate is accepted, and when a later round fails.
- Evaluate the retained answer against the original problem's objective and feasibility rules.

Clarify whether the provider returns a partial candidate or a complete solution. The evaluator
may complete a candidate, as in the existing decomposition example, so its output may need the
complete answer and its objective value as well as acceptance and feedback. An acceptance flag
alone is insufficient if the coordinator has no complete answer to retain.

Distinguish an unsuccessful search outcome from a raised operational error. Preserve the existing
rule that a solver crash or license error is raised rather than converted to `not_found` or
`infeasible`. Retaining an earlier candidate after a later search finds nothing is different
from silently returning that candidate after a crash. Any recovery policy needs an explicit
contract; adding one is not required here.

Explain who owns the overall stopping budget and how it relates to each provider's limit. A
round limit bounds the number of calls; it does not alone bound elapsed time. Keep this practical
and avoid introducing a deadline-management framework.

Explain how these boundaries let the evaluator, provider, and stopping policy change for different
reasons. Do not prescribe a separate class for each responsibility unless the example needs it.
Preserve the distinction between an accepted candidate and a proof about the original instance.
Termination without further feedback does not automatically prove optimality.

### Selected solve

- Keep selection policy separate from algorithm implementations, even if it is a private method
  in the same coordinator.
- Pass providers in from outside, using the dependency-injection approach already introduced.
- Require interchangeable providers to honor the same public contract.
- Distinguish selecting one provider from fallback or retry after a provider returns or fails.
- Explain that thresholds depend on measured behavior and that guarantees come from the result.

Reuse the earlier Strategy explanation instead of teaching it again. Selected solve should be a
short application of that material, with only the additional optimization-specific decisions.

## Develop one worked design example

Prefer an iterated solve because selected solve already has concrete pseudocode in the Strategy
chapter. Use one existing example if it can support clear contracts without a long explanation
of a new optimization problem. Do not force all four arrangements into the cargo example.

The section introduction currently says every chapter designs the cargo system and that the
formulation stays fixed, although Chapter 8 already uses other domains. If a worked example uses
another domain, adjust that setup narrowly to describe cargo as the running example with explicit
exceptions. Do not invent a cargo simulation requirement merely to preserve that sentence.

Show enough to make the design reviewable:

1. The original decision and what counts as an accepted complete answer.
2. The coordinator, provider, evaluator, and records they exchange.
3. A small amount of structured-English pseudocode showing ownership and flow.
4. How the coordinator retains an accepted answer and derives the final status honestly.
5. Concrete change requests that demonstrate the value and limits of the boundaries.

For example, replacing a simulation should primarily change the evaluator, changing a round
limit should change coordination policy, and changing a formulation should primarily change
the provider. State the assumptions that make these claims true. A change to the shared feedback
record can require changes on both sides; do not promise that every change stays in one module.

Keep the example small. Do not build a universal framework for arbitrary pipelines, portfolios,
or decomposition algorithms. Use the repository's figure conventions if a class diagram helps
explain the boundaries; keep flow diagrams only where they teach a different idea.

## Integrate the design and testing sections

Keep design explanations in Section 04 and introduce testing techniques in Section 05, where
the reader has learned them. Do not insert mock-based testing lessons into the design chapter.

In the testing section, distinguish two public behaviors:

- The complete arrangement returns a result satisfying the optimization contract. These checks
  need real optimization behavior and suitable oracles.
- A coordinator handles outcomes from its dependencies according to its own contract. Controlled
  dependencies can make those outcomes deliberate and reproducible.

Useful coordinator scenarios for an iterated solve include preserving the best accepted answer
after a later round finds no candidate, stopping at the configured limit, returning `not_found`
when no candidate was accepted, propagating operational errors according to the contract, and
avoiding an unsupported `optimal` or `infeasible` status.

These tests check a coordinator's public behavior. They should not assert private call sequences
unless the sequence itself is a necessary part of the public promise. Controlled dependencies
do not establish that the real formulation or algorithm produces correct decisions.

Use the existing Mocks and Integration testing material as prerequisites. Inspect the scope of
"11. Testing a decision-support system" before choosing where to develop the connection. Keep
any remaining stub honest about what is still planned.

Treat this testing expansion as a follow-up unless a small change is necessary to keep existing
claims consistent. The primary deliverable is a useful design chapter. Do not complete the
decision-support-system testing stub merely because this brief identifies future examples.

## Connect the chapter to the rest of the design argument

Make each boundary decision an application of concepts already taught:

| Earlier concept | Application in optimization arrangements |
| --- | --- |
| Information hiding | Solver objects and algorithm state stay behind provider boundaries. |
| Cohesion | Coordination rules belong together; formulation logic belongs with its own responsibility. |
| Coupling | Intermediate and feedback records make dependencies explicit and limited. |
| Single responsibility | Selection, iteration, evaluation, and solving can change for different reasons. |
| Contracts | Each boundary states what inputs mean and what outcomes establish. |
| Dependency injection | Coordinators receive the providers or evaluators they use. |
| Strategy | Selected solve applies the existing interchangeable-provider design. |

Keep architecture placement and internal coordination as distinct design decisions. Strengthen
the cargo architecture's explanation of why selected solve addresses its stated change request.
Do not expand it into demonstrations of arrangements the cargo problem does not need.

The cargo chapter already records its solver dependency as a deliberate exception with a cost.
Preserve that reasoning. This task does not require a new modelling-layer comparison or a change
to the chosen ring. Update the section's reading-order description and conclusion so Chapter 8
promises responsibility and boundary guidance as well as names and result guarantees.

Revise "Check yourself" to include a design decision and a change request, not only identifying
an arrangement and its status. A reader should explain where a change belongs and when it must
cross a shared record boundary.

## Scope and safeguards

- Prioritize Chapter 8 of Section 04; change adjacent chapters only where integration requires it.
- Retain useful result-status reasoning, but make it one consequence of the design.
- Deepen sequential and iterated solve; shorten repetition of Strategy.
- Avoid adding algorithm surveys or formulation theory that do not explain software boundaries.
- Define new software terms and update the glossary when necessary.
- Preserve established chapter anchors. Update navigation and indexes when their claims change.
- Add practice links only when the corresponding exercises actually exist.
- Cite published sources for external claims. Verify new technical or historical claims rather
  than inventing authority for the proposed catalogue.
- Follow the repository's 100-column prose wrapping and language-agnostic pseudocode conventions.

## Acceptance criteria and verification

The revised material should let a reader answer these questions:

1. Which arrangement fits the stated problem, and what does choosing it cost?
2. Which module owns coordination, state, and termination?
3. What records cross boundaries, and what do their contracts promise?
4. What can change independently, and what changes necessarily cross boundaries?
5. What does the final status establish about the original decision?
6. Which public boundaries allow coordination to be checked separately from optimization
   correctness?

Before expanding scope, complete the smallest coherent revision: the Chapter 8 opening, practical
guidance for the four arrangements, one worked example, design-oriented self-check questions,
and the affected introduction and conclusion wording. Glossary and figure changes should support
that revision. Treat substantial new testing prose as a separate follow-up.

Check that the worked example actually demonstrates its claimed boundaries and guarantees.
Review the section introductions, conclusions, glossary, chapter tables, and root index for
consistency where affected. After editing any link or anchor, run
`python .claude/tools/check_links.py` from the repository root.

This repository has no build or test suite. Verification consists of reviewing the prose,
pseudocode, figures, contracts, and links. Report the changed files, the main teaching improvement,
the checks performed, and any substantive unresolved issue.
