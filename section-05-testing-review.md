# Section 05 review: testing optimization models and decision-support systems

Review date: 2026-10-04.

Reviewed: [Section 05](book/05-testing/README.md), the repository writing specification, the shared cargo example,
the relevant glossary definitions, and the architecture in section 04. This report records findings and recommended
changes; it does not change the book.

## Overall assessment

The section has a strong foundation: testing promises, checking feasibility independently, comparing against
enumeration, and explaining why optimality properties can fail for heuristics. The greedy counterexample is
particularly useful.

The main weakness is that it treats hiding the algorithm as the central distinction between model testing and system
testing. Both can hide the algorithm. The actual distinction is the scope of the promises being checked.

The revision should first define the testing boundaries, repair the optimization result contract, and develop a
complete system example. The oracle and introductory chapters can then support that progression consistently.

## 1. First principles: what a test establishes

A test needs four things:

1. A subject: what component or system are we exercising?
2. A requirement: what must it do under these conditions?
3. An observation: what happened?
4. An oracle: how do we decide whether that observation meets the requirement?

An oracle need not supply one exact expected answer. It can check a condition, a relationship, or an allowed outcome.
That broader meaning is essential for optimization testing. The oracle literature includes specifications,
contracts, and metamorphic relationships among the sources of expected behavior.
[Barr et al., *The Oracle Problem in Software Testing*](https://discovery.ucl.ac.uk/id/eprint/1471263/)

A test may establish that a returned load respects capacity. It does not thereby establish that the load is optimal,
that the capacity belongs to the correct aircraft, or that the planner sees the correct load. Those are separate
requirements requiring separate evidence.

A stronger organizing principle for the section is:

> Decide what must be true, identify where that promise is made, and choose evidence capable of detecting its
> violation.

This principle applies throughout ordinary software and optimization software.

## 2. Define what “testing an optimization model” means

The phrase currently covers several different subjects:

| Subject | Question |
|---|---|
| Mathematical formulation | Do these variables, constraints, and objectives express the intended decision problem? |
| Formulation implementation | Does the program construct the intended mathematical problem from its inputs? |
| Optimization component | Does the component return an admissible result for the instance and guarantees it was given? |
| Decision-support system | Does the complete workflow produce and communicate the appropriate recommendation for the user's situation? |

These subjects overlap, but they are not interchangeable.

The current [model-testing chapter](book/05-testing/README.md#ch-model-testing) mostly tests an optimization component:
`Optimization.run(instance)`. That component includes formulation construction, solving, and translating the result
into a `Solution`.

This is a sensible boundary. State it directly:

> In this chapter, testing an optimization model means testing the software component that receives a mathematical
> instance and returns a solution or a stated outcome.

Then distinguish that activity from reviewing the formulation and validating the model's suitability.

Verification checks conformance to specified requirements; validation checks suitability for intended use. Both can
concern a component or an entire system. Validation is not confined to the business-to-mathematics translation.
[NASA, *Systems Engineering Handbook*](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf)

## 3. Model testing versus system testing

For an optimization component, suppose the input instance is $d$, its feasible set is $X(d)$, and its objective is
$f_d(x)$. An exact optimization contract might promise:

$$
x \in X(d), \qquad z=f_d(x), \qquad z=\max_{y\in X(d)} f_d(y)
$$

when a feasible solution exists, subject to the stated numerical conventions. These promises take the supplied
instance as their starting point.

A decision-support system has additional work:

$$
\text{source records}
\rightarrow \text{mathematical instance}
\rightarrow \text{optimization result}
\rightarrow \text{recommendation delivered to the user}
$$

Each arrow can introduce an error.

### A correct optimizer can produce a wrong recommendation

Consider cargo weights supplied in kilograms while the optimization component expects tonnes. The system passes
`2000` instead of `2`. The optimizer correctly solves the supplied instance and rejects a pallet that should fit.

Every optimization-component test can pass. The system is still wrong.

The reverse failure is equally possible: the optimizer returns the correct quantities, but the report associates
them with the wrong product identifiers. The mathematical result is correct while the delivered recommendation is
wrong.

| Concern | Optimization-component test | System test |
|---|---|---|
| Input meaning | Assumes a valid instance in agreed units | Checks selection, conversion, identifiers, and required data |
| Feasibility | Checks against the supplied instance | Checks the delivered recommendation against the relevant source records and rules |
| Objective | Checks reported value and promised quality | Checks that the value is communicated with the right units and meaning |
| Outcome | Distinguishes the outcomes in the component contract | Takes the appropriate user-visible action for each outcome |
| Identity | Preserves decision-variable identities | Preserves flight, booking, and product identities throughout the workflow |
| Timing | Meets any component timing promise | Produces a usable outcome within the workflow's deadline |
| Side effects | Usually returns a result | May write a plan, update state, or notify someone |

System testing includes model testing, but adds correctness of interpretation, composition, and delivery. It also
includes unit and integration tests of the surrounding components. Testing the system should not mean running every
check through its outermost interface.

This connects naturally to the architecture already developed in
[section 04](book/04-design/README.md#fig-cargo-architecture): readers, preprocessing, solution providers,
postprocessing, and writers.

## 4. Repair the optimization result contract

The [optimization contract](book/05-testing/README.md#model-contract) deliberately hides:

> “nothing about why the optimization module could fail to provide one”

That hides information a caller may need to behave correctly.

| Outcome | What the caller knows |
|---|---|
| Optimal solution | A feasible solution was found and optimality established under the declared tolerances |
| Feasible solution, optimality unproven | A usable candidate exists, but a better one may exist |
| Proven infeasible | No feasible solution exists for this instance |
| No solution found before stopping | Feasibility remains unresolved |
| Execution failure | The computation did not complete normally |

These outcomes can be expressed without exposing a solver brand or its internal status codes. A solver adapter
translates those codes into the application's vocabulary. Execution failures may instead use a defined error path;
the essential requirement is that their meaning remains distinguishable.

The draft says an exact solver stopped at its time limit loses its guarantee “without announcing it.” This is wrong
for solvers that report termination status. Gurobi, for example, distinguishes optimality, infeasibility, time limits,
and numerical termination.
[Gurobi status documentation](https://docs.gurobi.com/projects/optimizer/en/current/reference/numericcodes/statuscodes.html)

There is also an inconsistency within the section: the nightly planner relies on `result.status is infeasible`,
while the later optimization interface removes the distinction needed to produce that status reliably.

A richer result gives the system-testing chapter concrete behaviors to test: an unresolved run must not be reported
as proof of infeasibility, and a feasible incumbent must not be described as proven optimal.

## 5. Strengthen the time-limited contract

Under the [time-limited contract](book/05-testing/README.md#pseudo-time-limited-contract), an implementation that
returns `null` for every instance is correct. This follows from allowing `null` on feasible instances while only
checking returned solutions for validity.

The chapter should explicitly demonstrate this consequence:

> A correct implementation of a weak contract can still be useless.

Then introduce stronger promises where justified. Possibilities include:

- Return a supplied feasible starting solution if no improvement is found.
- Never return a solution worse than an accepted feasible baseline.
- Report termination and solution availability accurately.
- Meet a documented quality threshold for an agreed set of cases.
- Distinguish failure to find a solution from proof that none exists.

For this cargo model, with valid inputs, the committed load $x=l$ is feasible whenever its weight and volume fit.
The component can therefore construct a feasible fallback directly. Requiring that fallback is a design choice,
but the example provides a principled way to strengthen the contract.

Keep the greedy counterexample. Replace:

> “Behaviors 3 to 7 follow from optimality, so they no longer hold.”

with:

> These properties are no longer guaranteed by the weaker contract.

Some algorithms or explicit contracts may still guarantee particular relationships. The loss of optimality removes
the general inference, not every possible guarantee.

## 6. Quality can be tested as well as measured

The [quality discussion](book/05-testing/README.md#ch-mip-no-optimality) says that a deterioration gets investigated:

> “rather than failing a build”

That is a policy choice, not a fundamental distinction between testing and benchmarking.

A benchmark measures performance or quality. A test applies an acceptance rule. The same benchmark results can
support a report, an automated acceptance check, or both.

If the component promises never to worsen a supplied feasible baseline, that is an ordinary pass/fail assertion even
though optimality is unknown. For variable runtime or randomized behavior, acceptance may require repeated runs and
a carefully specified statistical rule. The section need not teach that entire subject, but should avoid teaching
that quality necessarily belongs outside automated acceptance.

### Problems in the benchmark example

- **Division by zero:** zero-revenue and empty instances are valid, so both denominators can be zero.
- **Changing populations:** average gaps can improve because the component stops returning solutions for difficult
  instances.
- **Missing validity checks:** an infeasible or misreported solution must not enter quality summaries.
- **Missing comparison conditions:** time budget, relevant settings, and execution environment affect interpretation.
- **Overstatement about large instances:** known optima can exist for large structured or previously certified cases.

Report availability and quality separately, retain results per instance, and define the zero-value convention
explicitly.

## 7. Interface testing does not prohibit formulation tests

The [model-testing chapter](book/05-testing/README.md#ch-model-testing) says:

> “Testing the formulation is possible, but I advise against it.”

The reasoning is too strong. A heuristic having no encoded mathematical formulation explains why formulation tests
cannot be shared with every implementation. It does not make them inappropriate for an implementation that does
construct one.

A model builder may itself have a meaningful contract: given these domain inputs, produce these variables,
coefficients, bounds, and constraints. Testing that boundary can be valuable when solve-based tests are expensive or
give poor failure localization.

For example, a missing constraint may not change the optimal solution on the selected cases. A focused construction
test may expose the omission immediately.

Recommended guidance:

- Use behavior tests to protect the optimization component's externally promised behavior.
- Add focused formulation-construction tests when they address a specific risk.
- Avoid assertions about incidental details such as constraint ordering or generated names unless those details are
  contractual.
- Keep real solve tests, because inspecting a formulation alone does not exercise solving and result extraction.

Exposing a vendor unnecessarily may be poor design, but exposing a valid bound or termination reason can be essential
to the application contract.

## 8. Strengthen the oracle chapter

### Include validity checks in the worked differential test

The differential-testing discussion correctly says that matching objective values establishes optimality only when
accompanied by solution-validity checks. However, the
[worked sweep](book/05-testing/README.md#pseudo-differential-sweep) omits those checks.

A broken implementation could return the expected objective alongside an impossible load and pass the example.

The worked test should check:

- Valid product identities and quantities.
- Feasibility against the instance.
- Independently recomputed revenue and totals.
- Agreement with the reference optimum where applicable.

Explain independence carefully. Reusing the production function that computes total weight can reproduce its defect
in the test. Recomputing weight from the declared rule provides different evidence.

### Explain what metamorphic tests cannot establish

Satisfying a relationship does not establish correctness. A function that always returns zero passes the sine
relationship. A component that always returns an empty load on uncommitted cargo instances satisfies several
objective relationships while failing to optimize.

The “reach of each oracle” discussion also overstates what size tells us. A metamorphic relationship may hold
mathematically at every size, but checking a relationship between optimal values still requires obtaining
sufficiently reliable optimal results. It does not remove the cost of those solves.

Replace the size-only comparison with a comparison of evidence:

| Evidence | What it can establish | Principal limitation |
|---|---|---|
| Independent feasibility and accounting checks | Candidate satisfies checked rules and reports values correctly | Does not establish optimality |
| Known optimum | Candidate reaches the reference value, with feasibility checked separately | Reference must be trustworthy and available |
| Independent enumeration | Agreement across many small cases | Computational cost and possible reference defects |
| Metamorphic relationship | Related executions respect a necessary relationship | Many incorrect implementations also satisfy it |
| Feasible solution plus valid matching upper bound | Optimality, within the stated numerical conventions | Bound validity must be established |

The final row explains why computing another complete solution is not always necessary. For maximization, a feasible
value $z$ and valid upper bound $U$ give $z\le z^*\le U$. If they coincide, they establish optimality.

## 9. Qualify the general testing lessons

These issues matter because the audience is learning the vocabulary for the first time. Line numbers below refer to
the reviewed version of `book/05-testing/README.md` and may move as it is edited.

| Passage | Problem | Recommended correction |
|---|---|---|
| Line 13: “everything that worked before still works” | Passing tests provide bounded evidence | Say the suite checks the behaviors and cases it covers |
| Line 123: signature, API, contract, abstraction treated as synonyms | A signature does not specify feasibility, optimality, or outcome semantics | Distinguish callable shape from behavioral promises |
| Line 240: failure has “one cause: `add`” | The test, expectation, or environment can be wrong | Isolation narrows diagnosis |
| Line 394: tests need no logic | Contradicts enumeration, generated cases, and independent constraint checks | Minimize unnecessary logic; keep necessary oracle logic simple and independently checked |
| Line 526: red then green establishes causality | Requires controlled conditions and failure for the intended reason | Present it as useful evidence under those conditions |
| Line 870: integration tests cover one happy path | Interface failures often involve adverse conditions | Choose cases by the interaction risks |
| Line 1293: a slow test becomes an integration test | Confuses execution cost with scope | Describe scope and resource requirements separately |
| Line 1736: “Nothing tests the test” | Reference implementations and test helpers can be tested; deliberate defects can assess detection | Say tests require scrutiny too |

The scope-versus-cost distinction is explicitly developed in *Software Engineering at Google*: a narrowly scoped
test can need substantial infrastructure, while a broad test can run cheaply in one process.
[Chapter 11](https://abseil.io/resources/swe-book/html/ch11.html)

The managed/unmanaged dependency rule should be presented as one useful approach. External adapters still need tests
against controlled implementations or sandbox services; checking that a notification method was called does not
establish that the real adapter communicates correctly.

## 10. Give numerical correctness a worked example

The [floating-point discussion](book/05-testing/README.md#difficulty-floating-point) says:

> “Equality can only mean equality within a tolerance.”

This is too broad. Product identifiers, integer counts after a defined conversion, and status values can require
exact equality. Approximate numerical comparisons need explicit rules.

Distinguish:

- Feasibility tolerance.
- Integrality tolerance.
- Objective comparison tolerance.
- Optimality gap.
- Operational acceptance of the delivered load.

Solver tolerances and units interact, so an arbitrary epsilon is not a complete policy.
[Gurobi, *Tolerances and User-Scaling*](https://docs.gurobi.com/projects/optimizer/en/current/concepts/numericguide/tolerances_scaling.html)

A useful cargo example is a nearly integral solver value converted into a whole pallet count. Test the conversion
and recompute feasibility after it; the published load must satisfy its own contract.

## 11. Develop the system chapter around one complete recommendation

Use the existing architecture and develop the chapter in this order:

1. **Open with a correct optimizer producing a wrong recommendation.** Use the kilograms-to-tonnes example to
   establish the problem.
2. **State the system contract.** Identify the flight, source records, required rules, allowed outcomes, and delivered
   artifact.
3. **Map tests to the architecture.** Reuse section 04's readers, preprocessing, provider, postprocessing, and writer.
4. **Test outcome handling.** Use a controllable stand-in provider to produce optimal, feasible, infeasible,
   unresolved, and failed outcomes. This exercises the surrounding policy without depending on solver timing.
5. **Test real connections.** Check data conversion, provider integration, and output serialization using their real
   implementations where needed.
6. **Work one small end-to-end case.** Start from representative source records, use the real optimization path, and
   inspect the delivered plan.
7. **State what this evidence cannot establish.** Correct implementation of declared rules does not prove that those
   rules capture the real operational need.

For the end-to-end example, check the recommendation against independently understood source records. If production
and test both use the same faulty input conversion, they can agree on the wrong instance.

Replace the current system-chapter claim that tests see “only what the interface returns.” Observable behavior
includes written records, notifications, state changes, and promised timing. The mocks chapter already teaches this
broader view.

## 12. Example and editorial consistency

- In the cargo model introduction, explicitly identify and link the sanctioned
  [unlimited-tender variant](book/appendix/cargo_model_example.md). The text currently links the base
  model while silently omitting its tender constraint.
- State valid-instance assumptions in the contract: positive weights and volumes, valid committed quantities, and a
  policy for product identities. “Instance is not null” is insufficient.
- When adding or removing products in set-inclusion arguments, explain the common coordinate interpretation, with
  absent products fixed to zero.
- Qualify “the rest of the load is unaffected” when an unusable product is added: the optimal value is unchanged,
  but a different tied optimum may be returned.
- Fix the sine example's mixture of degree-valued examples and the radian relationship $x+\pi$.
- Fix the enumeration count for cases with $l_i>m_i$; a negative factor cannot count candidates.
- Move “Ideas to develop” into the introduction and keep Conclusion as the final chapter, as the authoritative
  specification requires.
- Make the introduction open with the DSS-specific difficulty. At present that distinction arrives after the general
  motivation.
- Reconsider excluding all input validation and performance discussion while promising a complete system-testing
  treatment. Detailed performance engineering can remain elsewhere, but input contracts and deadline outcomes belong
  in the system argument.

## Recommended revision order

1. Define the testing boundaries and the scope of verification and validation.
2. Repair the optimization result contract and distinguish exact from best-effort guarantees.
3. Write the complete system example using the architecture from section 04.
4. Strengthen independent checking, oracle limitations, and quality acceptance.
5. Qualify the general testing claims and correct the numerical examples.
6. Complete the editorial and cross-reference consistency pass.

The resulting progression is from testing one promise, to testing a difficult mathematical promise, to testing the
complete process that turns that mathematical result into usable decision support.
