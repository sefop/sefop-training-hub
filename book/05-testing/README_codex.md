# Section 05: Testing decision-support software

## Introduction

Decision-support software must recommend an action even when the best action is expensive to
determine. A test may be able to check that a load fits without knowing whether it earns the most
revenue. Even a correctly optimized load can become a wrong recommendation if the software uses the
wrong aircraft capacity or attaches quantities to the wrong products. Testing therefore needs
evidence about both the mathematical result and its meaning to users.

The organizing principle of this section is simple: decide what must be true, identify where that
promise is made, and choose evidence capable of detecting its violation. Small experiments make
software changes easier to assess. Their value depends on what they observe and check, not merely on
how many of them pass.

### Out of scope

- **Detailed performance engineering:** solver tuning, capacity planning, and statistical runtime
  comparisons need a separate treatment; deadline responses and comparable quality measurements
  belong here.
- **Reviewing the mathematical formulation:** the cargo rules are taken as specified; reviewing
  whether those rules represent the intended decision is a separate activity.
- **Operational validation methods:** user studies and field evaluation are outside this section;
  the distinction between satisfying a specification and meeting an operational need remains
  essential.
- **Multiple objectives:** the appendix defines a second-objective evolution, but this section tests
  one objective.
- **Language and test-tool setup:** runnable examples and setup instructions belong in the practice
  repositories.

Read the chapters in order. The calculator establishes how to test a promise, the linear expression
shows how tests can guide development, and the nightly planner introduces dependencies and real
connections. The cargo chapters then distinguish solution validity, optimality evidence, and
best-effort guarantees before testing a complete recommendation. Test-driven development is a
development workflow; the remaining chapters also apply to tests written after implementation.

## Chapters

| #   | Chapter                                                                       | After it you can…                                                |
| --- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| 1   | [What a test establishes](#ch-interface)                                      | State the promise, observation, and limits of a test.            |
| 2   | [Unit testing](#ch-unit-testing)                                              | Turn one component's promises into repeatable experiments.       |
| 3   | [Writing trustworthy tests](#ch-clear-tests)                                  | Make expectations understandable and failures informative.       |
| 4   | [Test-driven development](#ch-tdd)                                            | Develop one behavior through a failing test and a small change.  |
| 5   | [Controlling dependencies with test doubles](#ch-mocks)                       | Supply difficult outcomes and observe outgoing actions.          |
| 6   | [Integration testing](#ch-integration)                                        | Check real connections where components can disagree.            |
| 7   | [Defining the optimization component contract](#ch-model-testing)             | Specify valid inputs, outcome meanings, and solution guarantees. |
| 8   | [Checking solution validity and numerical correctness](#ch-solution-validity) | Independently check a candidate and its numerical conversion.    |
| 9   | [Testing optimality when the answer is hard to know](#ch-oracles)             | Combine known answers, enumeration, relationships, and bounds.   |
| 10  | [Testing without an optimality guarantee](#ch-mip-no-optimality)              | Specify and assess useful best-effort behavior.                  |
| 11  | [Testing the complete decision-support workflow](#ch-dss-testing)             | Check a recommendation from source records through delivery.     |
| 12  | [Conclusion](#ch-conclusion)                                                  | Assemble complementary evidence around the promises that matter. |

## How to read the pseudocode

Pseudocode is structured English rather than a particular programming language. `public` marks an
operation callers may use; `private` marks state or an operation kept inside a component. These are
the [public and private](../appendix/glossary.md#public-and-private) access markers. A constructor
creates an object, and a named argument such as `scalar=3` identifies the meaning of its input. A
record groups named values.

`expect condition, "message"` checks an assertion: if the condition is false, the test fails and
reports the message. The message is optional. `expect calling operation raises error` checks the
specified error outcome. Test support operations described in prose stand for small helpers whose
implementation belongs in the practice repositories.

## Practice and editorial notes

This is an alternate draft. Its numbered headings follow the requested review format; its topic
anchors preserve existing chapter links wherever the subject survives. The published section and its
navigation remain separate.

Exercises live in [the Python repository](https://github.com/sefop/training-testing-python) and
[the Java repository](https://github.com/sefop/sefop-training-java). The **Exercise maintenance
notes** under each relevant chapter describe follow-up work, not changes already made to those
repositories. Keep both languages aligned on scenarios, expected behavior, and deliberate defects;
keep package names based on topics rather than numbers.

Before promoting this draft, align the shared glossary definitions of automated test, benchmark,
unit test, end-to-end test, validation, implementation detail, and managed/unmanaged dependency with
the qualified definitions used here. In particular, quality measurements can support acceptance
checks, test scope does not determine speed, and timing can be contractual. Existing glossary
entries are linked for navigation; this draft states the intended meaning locally. The glossary's
test-double entry already defines stubs. Update the three book navigation locations if promotion
changes the published section's scope, and reconcile the richer outcome vocabulary with section 04.

Figure placeholders include an intended asset name and a drawing brief. They are not links to
missing files. Use the section's `assets/` folder, a light background, and the book's established
colors when producing them.

---

<a id="ch-interface"></a>

## 1. What a test establishes

An experiment is useful only when we know which claim it challenges. A program producing a number
tells us little until we state what that number should mean. A test makes the claim and the
observation explicit, then applies a rule for deciding whether they agree.

### The promise and its interface

An [interface](../appendix/glossary.md#interface) is the set of operations a component offers its
callers. The signature of an operation describes its callable shape: its name, inputs, and return
type. The [contract](../appendix/glossary.md#contract) states the behavioral promise: which inputs
are acceptable, what the operation guarantees, and which errors it reports. A signature alone does
not supply that promise.

For a calculator, `add(a, b) returns number` is a signature. Its contract might require finite
numeric inputs, promise their sum, and specify errors for invalid inputs or an unrepresentable
result. The algorithm used to add them is an
[implementation detail](../appendix/glossary.md#implementation-detail) unless callers explicitly
depend on it. Tests of the sum should survive a change in that algorithm.

### The test as an experiment

For the claim that adding two numbers returns their sum, the experiment can be stated without
reading the implementation:

| Part                  | Calculator example                     |
| --------------------- | -------------------------------------- |
| Subject               | The calculator's `add` operation       |
| Requirement           | Return the sum of two accepted numbers |
| Controlled conditions | A fresh calculator with inputs 2 and 3 |
| Observation           | The returned value                     |
| Judging rule          | The value must equal 5                 |

A failure calls for investigation: the implementation, the expectation, the setup, or the
environment may be wrong. Controlling conditions narrows the possible explanations. A pass supplies
evidence for the checked claim on these conditions; it does not establish every behavior on every
input.

### An expected answer is not always a value

A [test oracle](../appendix/glossary.md#test-oracle) is the means of judging an observation. Knowing
that 2 plus 3 equals 5 supplies one. Checking that swapping the operands leaves the result unchanged
supplies another, weaker kind of evidence. A function returning zero for every input would pass the
swapping check.

An [automated test](../appendix/glossary.md#automated-test) performs the experiment and applies its
oracle without a person inspecting every result. Its expectation may describe a value, a condition,
a relationship, or an allowed error. Several different checks may be needed to challenge the same
implementation effectively.

### Verification and validation

[Verification](../appendix/glossary.md#verification) checks conformance to specified requirements.
[Validation](../appendix/glossary.md#validation) checks suitability for intended use. Both questions
can apply to a component or a complete system. A correctly calculated tax may satisfy a stated
formula while being unsuitable because the formula applies to a different jurisdiction.

The distinction matters when interpreting a passing test: checking a requirement does not establish
that the requirement is the right one. This section develops verification through automated
experiments. NASA's
[_Systems Engineering Handbook_](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf),
sections 5.3 and 5.4, develops the broader distinction.

### Choosing the test boundary

The boundary identifies how much of the software the experiment exercises:

| Scope                                                        | Meaning                                    | Example                                         |
| ------------------------------------------------------------ | ------------------------------------------ | ----------------------------------------------- |
| [Unit test](../appendix/glossary.md#unit-test)               | One selected component or unit of behavior | A calculator operation                          |
| [Integration test](../appendix/glossary.md#integration-test) | Real components working together           | A writer and reader agreeing on a record format |
| [End-to-end test](../appendix/glossary.md#end-to-end-test)   | The complete selected user workflow        | Source records becoming a delivered report      |

State that boundary explicitly when labels could be ambiguous. Separately record execution cost and
requirements, such as access to a file system or service. A narrow test can be expensive, and a
broad workflow can run cheaply in one process. _Software Engineering at Google_,
[chapter 11](https://abseil.io/resources/swe-book/html/ch11.html), distinguishes test scope from
resource constraints.

---

<a id="ch-unit-testing"></a>

## 2. Unit testing

A promise usually contains more than one way to be wrong. Addition can return the wrong sum,
mishandle zero, or accept an input that should be rejected. A
[unit test](../appendix/glossary.md#unit-test) concentrates on one such behavior within a selected
component, so its setup and observations remain easy to understand.

### From promises to cases

Start with the [contract](../appendix/glossary.md#contract). For the calculator, ordinary addition
is the [happy path](../appendix/glossary.md#happy-path): accepted inputs and a successful result.
Include specified errors and [boundary values](../appendix/glossary.md#boundary-value-analysis),
where the behavior changes.

| Promise             | Selected case                                        | Expected observation |
| ------------------- | ---------------------------------------------------- | -------------------- |
| Sum                 | Add 2 and 3                                          | 5                    |
| Zero identity       | Add -3 and 0                                         | -3                   |
| Commutativity       | Swap 2 and 3                                         | The same result      |
| Invalid-input error | Add text `"3"` and 4                                 | Reject the input     |
| Overflow error      | Add two values whose sum exceeds the supported range | Report overflow      |

The cases are examples, not an exhaustive proof. Negative values, representable extremes, and
specified numerical rounding rules may justify additional cases. Choose them because they challenge
a promise, not to reach a target number of tests.

### Arrange, act, assert

[Arrange, act, assert](../appendix/glossary.md#arrange-act-assert) gives the experiment three
visible parts: establish the conditions, exercise the behavior, and check the observation.
[Pseudocode: calculator sum](#pseudo-calculator-sum) keeps all three together.

<a id="pseudo-calculator-sum"></a>

**Pseudocode: calculator sum**

```
// pseudocode: calculator-sum
public test_add_two_numbers_returns_their_sum()
    calculator = Calculator()
    result = calculator.add(2, 3)
    expect result == 5, "add(2, 3) returned {result}; expected 5"
```

The operation under examination is called once. That is a useful default for a simple value test; a
relationship test intentionally needs related calls, and a state-changing behavior may need a
sequence.

### A calculator example

The sum test gives a concrete expected value.
[Pseudocode: calculator behaviors](#pseudo-calculator-behaviors) adds a relationship and an error,
each in a separate experiment.

<a id="pseudo-calculator-behaviors"></a>

**Pseudocode: calculator behaviors**

```
// pseudocode: calculator-behaviors
public test_add_swapped_operands_returns_the_same_value()
    calculator = Calculator()
    first = calculator.add(2, 3)
    second = calculator.add(3, 2)
    expect first == second

public test_add_text_reports_invalid_input()
    calculator = Calculator()
    expect calling calculator.add("3", 4) raises InvalidInput
```

Each test has an independently understandable purpose. An implementation that always returns 5
passes the first sum case and the swapping case, but should fail tests for other sums and invalid
inputs. This is why complementary cases matter even for a small operation.

### Organizing tests

Keep tests outside production source files, with names that make the corresponding component easy to
find. Give each test its own mutable objects and temporary records. A test must not need another
test to run first. Together, these experiments form a
[test suite](../appendix/glossary.md#test-suite), a collection that can be run again whenever the
implementation changes.

**Exercise maintenance notes:** Retain the calculator exercise. Include ordinary values, identity,
commutativity, invalid input, and the language's declared overflow policy. Add a constant-return
defect to demonstrate that passing a relationship test is insufficient. Do not require identical
numeric ranges across Python and Java.

---

<a id="ch-clear-tests"></a>

## 3. Writing trustworthy tests

A failed experiment is useful when another person can see what it measured and why its expectation
is justified. Test code needs that same scrutiny. A complicated expectation can conceal a mistake as
effectively as complicated production code.

### Complete and concise

Keep the inputs that explain the result visible in the test. For the calculator, `add(2, 3)` and the
expected 5 belong together. Hiding them behind `first_operand()` and `expected_result()` makes
readers search for the claim. Unrelated configuration, such as a log-file name, adds detail without
strengthening the experiment.

Shared setup is useful when it removes incidental work. Let it create an empty temporary directory
or construct routine objects; keep the values that determine the expected behavior local. A little
repetition is worthwhile when each test becomes understandable on its own.

### One behavior per test

A behavior can have several observable parts. Reporting an invalid input may require an error
category and an identifier for the offending field. Checking both can belong to one test. In
contrast, addition, division, and file writing should not share a test merely because the same
object offers them.

Use the test's purpose to decide the grouping. When a failure occurs, the reader should know which
promise is under investigation without first untangling several unrelated scenarios.

### Simple, independent expectations

Prefer an obvious expected value when one is available. Necessary checking logic can still contain
arithmetic, conditions, or loops. The concern is whether the reader can trust the
[oracle](../appendix/glossary.md#test-oracle), not whether the test contains a particular
programming construct.

Do not obtain the expected sum by calling the same production operation a second time. More
generally, a checking helper should derive its result from the requirement rather than reuse the
implementation under examination. Give nontrivial helpers their own small, independently checkable
examples. Separate implementation reduces shared defects; it cannot eliminate a shared
misunderstanding of the requirement.

### Names and failure messages

A name should identify the behavior and the case, such as
`test_add_zero_preserves_a_negative_operand`. A failure message should report relevant inputs and
the expected and observed results. For repeated generated cases, include the actual failing input
rather than only its position in a sequence.

Avoid messages such as "wrong result" when the values are available. An informative failure is part
of the test's usefulness: someone may investigate it long after its author has forgotten the
example.

### Checking the tests themselves

[Code coverage](../appendix/glossary.md#code-coverage) records which production statements or
branches execute during the suite. It can expose an error path that no test reaches. It does not
show whether the observations are checked well: removing an assertion may leave execution coverage
unchanged.

[Mutation testing](../appendix/glossary.md#mutation-testing) introduces deliberate defects and
checks whether tests notice them. Start simply: replace addition by a constant or disable input
rejection. An undetected defect invites investigation into missing cases or weak assertions. Some
automated mutations preserve behavior, so a surviving mutation is a question to examine rather than
automatic proof of a deficient suite.

**Exercise maintenance notes:** Replace "no logic in tests" with "simple, independently justified
expectations." Include one case where several assertions check one behavior, and one deliberate
defect that leaves execution coverage unchanged while exposing a missing assertion. Keep the
expected defect and detecting test explicit.

---

<a id="ch-tdd"></a>

## 4. Test-driven development

A requirement is easier to discuss when it has a concrete example. Writing that example as a failing
test before implementing the behavior makes the expectation visible while the design is still taking
shape. [Test-driven development](../appendix/glossary.md#test-driven-development) organizes this
work into short cycles.

### Red, green, refactor

1. **Red:** write a test for the next behavior and confirm that it fails for the intended reason.
2. **Green:** make a small implementation change that satisfies the expectation and preserves
   existing tests.
3. **Refactor:** improve the structure while preserving the checked behavior.

[Refactoring](../appendix/glossary.md#refactoring) means changing internal structure without
changing behavior. A cycle does not require a structural change when nothing would be improved. Run
the existing [test suite](../appendix/glossary.md#test-suite) as well as the new test to detect lost
behavior.

<a id="fig-tdd-cycle"></a>

**Figure: test-driven development cycle**

> **Figure placeholder:** `assets/tdd-cycle-revised.svg`. Draw the three-step loop: intended
> failure, smallest useful implementation change, structural improvement. Put "next requirement" on
> the returning arrow. No claims of proof or guaranteed correctness; the figure teaches the
> sequence.

### Failing for the intended reason

A failed test is useful evidence only if it reached the expected point. A missing operation can be
the intended initial failure when defining an interface. Once that operation exists, a test meant to
challenge its calculation should fail on the calculation, not because a data file is absent.

Keep the conditions controlled between runs and inspect the failure. Red followed by green then
supports the explanation that the implementation change satisfied this expectation. Unrelated edits,
nondeterministic behavior, or a test that did not execute weaken that inference.

### A linear expression example

Consider the scalar part of a linear expression, $a_0 + \sum_i a_i x_i$. Begin with three
requirements: its default scalar is zero, a supplied scalar is retained, and adding a scalar
increases the stored value. Coefficients are not needed to teach these three changes.

[Pseudocode: expression behavior tests](#pseudo-expression-behavior-tests) presents the tests in
their development order. Introduce and run one at a time; implement its behavior before introducing
the next.

<a id="pseudo-expression-behavior-tests"></a>

**Pseudocode: expression behavior tests**

```
// pseudocode: expression-behavior-tests
public test_empty_expression_has_zero_scalar()
    expression = LinearExpression()
    expect expression.scalar() == 0

public test_expression_keeps_supplied_scalar()
    expression = LinearExpression(scalar=3)
    expect expression.scalar() == 3

public test_add_scalar_increases_existing_scalar()
    expression = LinearExpression(scalar=1)
    expression.add_scalar(3)
    expect expression.scalar() == 4
```

For the first test, create the class and return zero. Before the second test, accepting a scalar
while ignoring it would still satisfy the first; the second challenges that behavior. Store the
supplied scalar, defaulting to zero. The third introduces the addition operation. The resulting
implementation is [Pseudocode: expression scalar](#pseudo-expression-scalar).

<a id="pseudo-expression-scalar"></a>

**Pseudocode: expression scalar**

```
// pseudocode: expression-scalar
class LinearExpression
    private stored_scalar

    public constructor(scalar=0)
        stored_scalar = scalar

    public scalar() returns number
        return stored_scalar

    public add_scalar(value)
        stored_scalar = stored_scalar + value
```

The three tests now pass. Negative additions and repeated additions supply useful additional cases.
Each new test should express a required behavior rather than merely describe the current
representation of `stored_scalar`.

### What the cycle establishes

The cycle makes requirements concrete and provides feedback on small changes. It does not show that
all relevant requirements have been discovered or that the checking logic is correct. Passing tests
support the behaviors and cases they exercise. Review the requirements and the tests as well as the
implementation.

### Further reading

- Kent Beck, _Test-Driven Development: By Example_, Addison-Wesley, 2002: worked examples of
  developing behavior through small red, green, refactor cycles.

**Exercise maintenance notes:** Retain the linear-expression exercise and its topic-based package
name. Ask learners to record the intended failure before each implementation change. Develop
coefficients, repeated variables, and expression addition afterward. Remove claims that the cycle
proves causality or guarantees complete coverage.

---

<a id="ch-mocks"></a>

## 5. Controlling dependencies with test doubles

Some behavior is visible only through another component. A nightly planner asks a notifier to send a
message; checking the planner's return value alone cannot establish that it requested the right
notification. We need a way to observe that request without sending a real message on every test
run.

### Why replace a dependency

A [dependency](../appendix/glossary.md#dependency) is another component the subject calls. A
[test double](../appendix/glossary.md#test-double) stands in for it during the experiment. Replacing
a dependency can make an otherwise awkward situation repeatable: a service is unavailable, an
unusual outcome must occur, or an outgoing action would affect someone outside the test.

Pass the collaborator into the subject rather than constructing it inside the behavior being
checked. This is [dependency injection](../appendix/glossary.md#dependency-injection): supplying a
dependency from outside. The same calling [interface](../appendix/glossary.md#interface) accepts the
real collaborator or its controlled replacement.

### Supplying outcomes with a stub

A stub is a test double that supplies selected answers. In this example, a result reader normally
obtains a nightly planning result. A stub reader can return `infeasible`, meaning the planning
calculation established that no plan satisfies the stated constraints. That lets a test exercise the
planner's response without arranging an actual planning calculation.

The result here is a small record with `instance_id` and `status`. For this example, the planner
sends the specified alert only when the status is `infeasible`; any other status does not produce
that particular alert. That is the behavior under examination, not a complete policy for every
operational outcome.

### Recording actions with a mock

A [mock](../appendix/glossary.md#mock) records calls so the test can inspect them. A recording
notifier needs only a list of messages and the operation the planner calls. In
[Pseudocode: controlled planner collaborators](#pseudo-controlled-planner-collaborators),
`messages()` exposes that list to the test; `notify` sends nothing externally.

<a id="pseudo-controlled-planner-collaborators"></a>

**Pseudocode: controlled planner collaborators**

```
// pseudocode: controlled-planner-collaborators
class FixedResultReader
    private result

    public constructor(result)
        keep result

    public read(instance_id) returns Result
        expect instance_id == result.instance_id
        return result

class RecordingNotifier
    private recorded_messages = empty list

    public notify(message)
        append message to recorded_messages

    public messages() returns list
        return a copy of recorded_messages
```

The assertion in the stub catches a request for an unexpected instance. It checks the test's setup
assumption; it does not demonstrate that a real reader selects records correctly.

### The nightly planner example

[Pseudocode: nightly planner policy](#pseudo-nightly-planner-policy) supplies the production
behavior and its test. List equality checks the complete sequence, so a duplicate notification fails
as well as a missing one.

<a id="pseudo-nightly-planner-policy"></a>

**Pseudocode: nightly planner policy**

```
// pseudocode: nightly-planner-policy
class NightlyPlanner
    private reader, notifier

    public constructor(reader, notifier)
        keep reader and notifier

    public review_tonight(instance_id)
        result = reader.read(instance_id)
        if result.status == infeasible:
            notifier.notify("Instance " + instance_id + ": no feasible plan exists.")

public test_infeasible_night_requests_one_alert()
    result = Result(instance_id="night-A", status=infeasible)
    reader = FixedResultReader(result)
    notifier = RecordingNotifier()
    planner = NightlyPlanner(reader, notifier)

    planner.review_tonight("night-A")

    expect notifier.messages() == ["Instance night-A: no feasible plan exists."]
```

A companion case supplies a successful result and expects an empty message list. Together they
challenge whether the policy sends this alert under the right condition. They do not depend on
whether a real planning algorithm can produce either result during the test.

### What a replacement cannot establish

A mock demonstrates which request the caller made. It does not demonstrate successful delivery by
the actual notification service. A stub demonstrates how the caller responds to a supplied result,
not whether the real reader can obtain that result. Treat these as explicit limits of the
experiment.

Use replacements where they help control or observe a relevant boundary. Replacing every internal
collaborator can make tests depend on an incidental sequence of calls and conceal disagreements
between real components.

**Exercise maintenance notes:** Expand the mocks exercise to include a result-reader stub and a
recording notifier. Test an infeasible outcome, a successful outcome, the instance identifier, and
duplicate alerts. State explicitly that these tests do not verify message delivery. Keep the
hand-written double visible before introducing tooling.

---

<a id="ch-integration"></a>

## 6. Integration testing

Two components may each behave correctly against their own expectations and still disagree when
connected. A writer may produce `infeasible` while a reader expects a different spelling. An
[integration test](../appendix/glossary.md#integration-test) exercises the real connection so that
this disagreement becomes observable.

### Choosing connections by risk

Choose a boundary where misunderstanding is plausible: record fields, numerical units, identifiers,
error meanings, or communication protocols. The purpose is to check agreement across that boundary.
It is not necessary to include every component simply because it is available.

For a nightly planner, connecting the real result writer, reader, and policy checks whether a stored
outcome causes the intended response. A [mock](../appendix/glossary.md#mock) can still record the
outgoing notification, because this experiment concerns the path to that request.

### The nightly planner with real files

`ResultsWriter` stores a result in a folder and `ResultsReader` reads the requested instance from
it. [Pseudocode: stored nightly result](#pseudo-stored-nightly-result) gives them the same temporary
folder, which starts empty and is removed after the test even if the assertion fails.

<a id="pseudo-stored-nightly-result"></a>

**Pseudocode: stored nightly result**

```
// pseudocode: stored-nightly-result
public test_stored_infeasible_result_requests_one_alert()
    folder = a fresh temporary folder with automatic cleanup
    ResultsWriter(folder).write(Result(instance_id="night-A", status=infeasible))
    notifier = RecordingNotifier()
    planner = NightlyPlanner(ResultsReader(folder), notifier)

    planner.review_tonight("night-A")

    expect notifier.messages() == ["Instance night-A: no feasible plan exists."]
```

Changing only the writer's representation without updating the reader should break their agreement
here. A writer and reader can also share the same mistaken interpretation. Add a separately
specified record example when compatibility with a documented external format matters; a successful
round trip alone cannot establish it.

### Testing adverse conditions

A successful connection is only one case. Suppose the agreed
[contract](../appendix/glossary.md#contract) says that a missing result raises `ResultMissing` and
an unknown stored status raises `InvalidResult`. Use an empty folder for the first and an
independently written malformed record for the second. Neither should cause the specific "no
feasible plan exists" notification.

Select adverse cases from actual promises. Tests should not silently decide an application's
recovery policy. If the requirements do not distinguish missing data from an infeasible plan,
clarify that distinction before encoding an expectation.

### Testing external adapters

An [adapter](../appendix/glossary.md#adapter-pattern) translates between the application's
operations and an external format or service. Test the actual notification adapter against a
controlled service or test account, checking the destination, payload, and response handling. A
local recording notifier does not exercise that translation.

Distinguishing privately used storage from externally visible actions can help decide which
dependencies to keep real. It is a design aid, not a universal rule that some adapters never need
real-connection tests.

### Keeping integration tests repeatable

Use isolated records, explicit configuration, and cleanup that runs on failure. Avoid another test's
database rows or yesterday's files. When an external test service is required, identify that
requirement so failures can be diagnosed and the suite can be scheduled sensibly.

Execution time is a separate property from integration scope. Record expensive or restricted
resources explicitly; do not relabel a test just because its input grew larger.

**Exercise maintenance notes:** Retain the real writer/reader example; add missing-record and
invalid-status cases. Include an independently specified stored record so matching writer and reader
defects cannot be the only evidence. Document the exact incompatible format change used in the
exercise and which assertions detect it.

---

<a id="ch-model-testing"></a>

## 7. Defining the optimization component contract

For a calculator, the expected result is cheap to establish independently. For an optimization
problem, finding the best objective value may require substantial computation. Before deciding how
to test the answer, we must say which computation is responsible for which promise.

### Which subject are we testing

"Testing the model" can refer to several different subjects:

| Subject                  | Question                                                                               |
| ------------------------ | -------------------------------------------------------------------------------------- |
| Mathematical formulation | Do the variables, constraints, and objective express the intended decision?            |
| Formulation construction | Does the program construct the specified mathematical problem from the supplied data?  |
| Optimization component   | Does an instance produce an outcome and candidate satisfying the component's promises? |
| Decision-support system  | Do source records become an appropriate, correctly communicated recommendation?        |

Here the optimization component receives a mathematical instance, constructs and solves its
formulation when needed, and translates the result into application vocabulary. Its
[contract](../appendix/glossary.md#contract) concerns that whole boundary. Reviewing the mathematics
and validating operational suitability are separate activities.

### The cargo instance

We use the [unlimited-tender evolution](../appendix/running-example.md#ev-unlimited-tender) of the
shared cargo example throughout this section, including the complete workflow. Supply imposes no
upper bound on a product's quantity; capacities still do. This is an explicit variant, not an
accidental omission of the base model's tender constraint. Each pallet has strictly positive weight
and volume.

| Symbol       | Meaning                                        | Unit                    |
| ------------ | ---------------------------------------------- | ----------------------- |
| $I$          | Finite set of products with unique identifiers | None                    |
| $w_i$, $v_i$ | Positive weight and volume per pallet          | Tonnes, cubic meters    |
| $r_i$        | Nonnegative revenue per pallet                 | Thousands of US dollars |
| $l_i$        | Nonnegative integer quantity committed to fly  | Pallets                 |
| $W$, $V$     | Nonnegative aircraft capacities                | Tonnes, cubic meters    |
| $x_i$        | Integer quantity selected for loading          | Pallets                 |

All numerical inputs must be finite. Product identifiers must be nonempty and unique; missing or
duplicate identifiers are rejected. The instance and its required fields must be present. The
component reports `InvalidInput` when these assumptions fail. A valid instance whose commitments
exceed capacity is infeasible, not malformed.

The optimization problem is the following
[mixed-integer program](../appendix/glossary.md#mixed-integer-program), abbreviated MIP, with
integer variables throughout:

$$
\max_x \sum_{i\in I} r_i x_i
\quad\text{subject to}\quad
\sum_{i\in I} w_i x_i\le W,\quad
\sum_{i\in I} v_i x_i\le V,\quad
x_i\ge l_i,\quad x_i\in\mathbb Z\quad(i\in I).
$$

`Instance.products` is a collection of records containing `id`, `weight`, `volume`, `revenue`, and
`committed_quantity`. `weight_capacity` and `volume_capacity` belong to the instance. The names in
the pseudocode refer to the quantities in this table.

### Results with distinct meanings

A caller needs to know what the computation established. The absence of a candidate alone cannot say
why none is available. Use application-level outcomes rather than exposing a particular solver's
status codes.

| Status       | Candidate | Meaning                                                                            |
| ------------ | --------- | ---------------------------------------------------------------------------------- |
| `optimal`    | Required  | Feasible candidate with optimality established under the declared numerical policy |
| `feasible`   | Required  | Feasible candidate; optimality is not established                                  |
| `infeasible` | Absent    | Infeasibility was established for this instance                                    |
| `unresolved` | Absent    | Computation stopped without a candidate or a proof of infeasibility                |
| `failed`     | Absent    | Computation did not complete normally; an execution failure is reported            |

Invalid input is a separate error before optimization. This draft uses a returned `failed` status
for execution failure; a defined error path is another possible interface choice. The important
requirement is to preserve the distinctions the caller needs.

[Pseudocode: optimization result contract](#pseudo-optimization-result-contract) gives the result
its shape. A `Solution.picked` map has exactly one entry per input product identifier, including
zero quantities. Optional values are written as `absent`, which means the value is unavailable
rather than zero.

<a id="pseudo-optimization-result-contract"></a>

**Pseudocode: optimization result contract**

```
// pseudocode: optimization-result-contract
record Solution
    picked                              // product identifier -> integer pallet count
    objective_value                     // thousands of US dollars
    total_weight                        // tonnes
    total_volume                        // cubic meters

record SolveResult
    status                              // optimal, feasible, infeasible, unresolved, failed
    solution                            // present only for optimal or feasible
    upper_bound                         // optional valid bound on maximum revenue
    termination_reason                  // application-level explanation

class Optimization
    public run(instance, policy) returns SolveResult
        // requires: a valid instance and supported policy
        // raises InvalidInput for malformed input
        // returns a result consistent with its status and declared guarantees
```

The policy states the permitted stopping conditions and numerical conventions. Requesting an exact
solve does not turn an interrupted computation into a proven optimum. A time limit with a valid
candidate yields `feasible` unless optimality was established; without a candidate or infeasibility
proof, it yields `unresolved`. Execution failures must not be translated into `infeasible`.

### Solution guarantees

For any returned solution, let $x$ denote the picked quantities and $z$ the reported revenue. The
component promises $x\in X(d)$ and $z=f_d(x)$ for the supplied instance $d$, using the declared
acceptance policy. Reported weight and volume must also agree with the load. An `optimal` status
adds the promise that its quality satisfies the declared optimality criterion.

For the small integer-valued teaching cases, exact optima and totals can be checked directly. For
general numerical inputs, record the comparison and gap conventions explicitly. Several loads may
share the best revenue. Unless the contract specifies a tie-breaking rule, tests compare validity
and value rather than requiring one selected load. Reordering the input may change which tied load
returns without changing the optimal value.

For this particular model, the committed vector $x=l$ is feasible if its weight and volume fit. If
either sum exceeds capacity, every admissible vector also exceeds that capacity. This gives a simple
independent feasibility decision for valid instances of this variant; it is not a general shortcut
for arbitrary optimization models.

### Choosing internal test boundaries

Behavior tests exercise `run` with the real optimization path. A stand-in returning a prepared
answer cannot establish that the component constructs, solves, and extracts the right problem.

Focused formulation-construction tests are also useful when construction has a meaningful contract.
For example, check that the weight row uses weights and the volume row uses volumes. A missing
constraint might leave the optimum unchanged on a selected example, while inspecting the constructed
row exposes it immediately.

Avoid asserting incidental constraint order or generated names unless clients rely on them. Such
tests belong to the implementation that constructs a formulation; a heuristic need not share them.
Keep real solve tests as well, because correctly constructed rows alone do not check solving or
result extraction.

**Exercise maintenance notes:** Replace `Solution or null` with the result vocabulary above in both
languages. Add malformed-input cases and result-shape checks. Preserve the unlimited-tender
assumption explicitly. Include an optional construction exercise that swaps weight and volume
coefficients, alongside real solve tests that detect the same defect through behavior. Update the
nightly planner's result types consistently.

---

<a id="ch-solution-validity"></a>

## 8. Checking solution validity and numerical correctness

A claimed revenue is useful only when it belongs to an admissible load. An impossible load can
advertise the right optimal value by accident. Begin with the candidate itself: check its quantities
against the instance, then recompute what those quantities mean.

### Checking the returned load

The [contract](../appendix/glossary.md#contract) defines the candidate's shape and rules. Check
product identifiers before using them to look up weights or revenues. An unknown identifier, a
missing quantity, a nonfinite number, or a noninteger pallet count is a defect in the returned
solution.

Then check commitments and capacities. These checks establish admissibility for the supplied
instance, not that the supplied instance describes the right aircraft or booking list. Their subject
is the optimization component's result.

### Recomputing reported values

Compute weight, volume, and revenue from the instance and selected quantities, without using the
production functions that produced the reported totals.
[Pseudocode: independent cargo checker](#pseudo-independent-cargo-checker) shows the calculation for
small teaching instances with exact integer-valued coefficients and capacities.

<a id="pseudo-independent-cargo-checker"></a>

**Pseudocode: independent cargo checker**

```
// pseudocode: independent-cargo-checker
public check_solution(instance, solution)
    expect solution is present
    expect solution.picked.keys == the set of instance product identifiers
    weight = 0
    volume = 0
    revenue = 0

    for each product in instance.products:
        quantity = solution.picked[product.id]
        expect quantity is a finite integer, "invalid quantity for {product.id}"
        expect quantity >= product.committed_quantity
        weight = weight + product.weight * quantity
        volume = volume + product.volume * quantity
        revenue = revenue + product.revenue * quantity

    expect weight <= instance.weight_capacity
    expect volume <= instance.volume_capacity
    expect solution.total_weight == weight
    expect solution.total_volume == volume
    expect solution.objective_value == revenue
```

The helper is itself testable. Give it an independently worked valid load, then alter one quantity,
identifier, or reported total at a time and check that it rejects the defect. Keep the arithmetic
simple enough to audit against the stated model. Sharing input record types is harmless; sharing the
production total calculator would undermine the independence of this check.

### Defining numerical comparisons

Not every field needs approximate equality. Identifiers, statuses, and published whole-pallet counts
have exact meanings. For approximate numerical values, specify the policy and units for each kind of
check:

| Check                          | Meaning                                                                            |
| ------------------------------ | ---------------------------------------------------------------------------------- |
| Feasibility tolerance          | Permitted residual in a numerical constraint, expressed in that constraint's units |
| Integrality tolerance          | How close a raw solver value must be to an integer before conversion is allowed    |
| Objective comparison tolerance | Permitted discrepancy when comparing reported and independently computed values    |
| Optimality gap                 | Permitted separation between a feasible objective and a valid bound                |
| Operational acceptance         | Rules the delivered pallet quantities must actually satisfy                        |

For approximate objective comparisons, one possible explicit rule is
$|a-b|\le\epsilon_{\mathrm{abs}}+\epsilon_{\mathrm{rel}}\max(|a|,|b|)$, with nonnegative tolerances
chosen for the objective's units and scale. This is a comparison convention, not permission to
exceed aircraft capacity. Reject nonfinite values before applying it. Conversion from kilograms to
tonnes must also convert any weight tolerance.

For this teaching workflow, source weights are whole kilograms, volumes are whole liters, and
revenues are whole dollars. Independent acceptance calculations use those integer units, so a
published load must fit exactly and reported totals must reconcile after unit conversion. Solver
arithmetic may be approximate; operational acceptance does not inherit its tolerance automatically.
Real measurement uncertainty requires an explicit business policy.

### From solver values to whole pallets

Suppose a product weighs 2,000 kilograms per pallet and the aircraft can carry 4,000 kilograms. A
raw solver value of `1.9999998` is within an illustrative integrality tolerance of $10^{-6}$ of 2.
Convert it to 2 only under the declared rule, then recompute its delivered weight as 4,000
kilograms. Merely truncating it to 1 loses a pallet.

Now change capacity to 3,999 kilograms and supply the same raw value directly to the conversion
test. The converted load weighs too much and must be rejected. The test does not need to persuade a
real solver to return that value; it exercises the conversion boundary with controlled input.

<a id="pseudo-pallet-conversion"></a>

**Pseudocode: checked pallet conversion**

```
// pseudocode: pallet-conversion
public convert_quantity(raw_quantity, integrality_tolerance) returns integer
    if raw_quantity is not finite:
        raise InvalidCandidate
    quantity = nearest integer to raw_quantity
    if absolute(raw_quantity - quantity) > integrality_tolerance:
        raise InvalidCandidate
    return quantity

public test_converted_load_is_checked_against_capacity()
    quantity = convert_quantity(1.9999998, integrality_tolerance=0.000001)
    expect quantity == 2
    expect quantity * 2000 <= 4000
    expect quantity * 2000 > 3999
```

[Pseudocode: checked pallet conversion](#pseudo-pallet-conversion) exposes the arithmetic. The
actual result translation must enforce the rejection as well: test that a converted candidate
exceeding 3,999 kilograms produces `InvalidCandidate`, rather than a publishable solution. Also test
quantities just inside and outside the conversion tolerance. Arbitrary rounding can violate
constraints and must not be presented as an automatic repair.

`CandidateTranslator` is the production component at that boundary. Its `translate` operation
accepts an instance and raw quantities, converts eligible values, recomputes totals, and rejects any
resulting load that violates the instance's operational rules. It uses its own implementation of
those rules; the test does not supply the independent checker as production validation.
[Pseudocode: reject rounded overload](#pseudo-reject-rounded-overload) tests the rejection directly.
The enclosing optimization component maps an invalid solver candidate to `failed` with an
explanation, never to `infeasible`.

<a id="pseudo-reject-rounded-overload"></a>

**Pseudocode: reject rounded overload**

```
// pseudocode: reject-rounded-overload
public test_candidate_translation_rejects_rounded_overload()
    product = Product(id="A", weight=2, volume=1, revenue=10, committed_quantity=0)
    instance = Instance(products=[product], weight_capacity=3.999, volume_capacity=10)
    translator = CandidateTranslator(integrality_tolerance=0.000001)

    expect calling translator.translate(instance, raw_quantities={A: 1.9999998}) raises InvalidCandidate
```

The translator evaluates acceptance in the exact source units: 3.999 tonnes means 3,999 kilograms
here.

### What validity does not establish

With no committed cargo, the empty load is feasible and reports zero revenue truthfully. If a
profitable pallet fits, that load is still suboptimal. Independent validity checks are necessary
evidence for every returned candidate; they provide no general assurance that the search found a
good one.

**Exercise maintenance notes:** Extract the validity checker as shared test support and test it with
deliberately corrupted candidates. Require all differential and quality exercises to invoke it. Add
conversion cases for nearly integral values, materially fractional values, nonfinite values, and a
rounded load that exceeds capacity. State the exact integer-unit acceptance policy separately from
the solver's numeric settings.

---

<a id="ch-oracles"></a>

## 9. Testing optimality when the answer is hard to know

Checking a load's constraints is cheaper than finding the best load. Once a candidate passes those
checks, what evidence can establish that its value is optimal? The
[oracle problem](../appendix/glossary.md#oracle-problem) is the difficulty of judging an answer when
an independent expected answer is costly to obtain. Several complementary methods make this
difficulty manageable on selected cases.

### Known answers and boundary cases

A [known oracle](../appendix/glossary.md#known-oracle) uses an answer established independently
before the test. For the [cargo example](../appendix/running-example.md#ex-two-pallet), A weighs 2
tonnes, occupies 1 cubic meter, and earns 10 thousand dollars; B weighs 1 tonne, occupies 2 cubic
meters, and earns 6. Capacities are 2 tonnes and 2 cubic meters, with no commitments. These
capacities limit each product to one pallet even under unlimited tender.

The possible integer pairs within the individual limits are $(0,0)$, $(1,0)$, $(0,1)$, and $(1,1)$.
The last violates both capacities. The remaining revenues are 0, 10, and 6, so one A is the unique
optimum. A test checks validity, truthful totals, the `optimal` outcome, and revenue 10. Here
checking the selected load is justified by uniqueness; it would not be justified for a tied optimum
without a tie-breaking promise.

Choose additional cases where behavior changes:

| Case                                               | Independently established expectation                         |
| -------------------------------------------------- | ------------------------------------------------------------- |
| Empty product set                                  | Empty optimal load, revenue zero                              |
| Every uncommitted pallet exceeds a capacity        | Empty optimal load, revenue zero                              |
| Commitments exceed one capacity                    | Proven infeasible                                             |
| One positive-revenue product fitting $m\ge2$ times | Load $m$ pallets; catches accidental binary-variable modeling |
| Two mutually exclusive loads tie                   | Either valid load with the common optimum value               |
| Weight binds but volume does not, then the reverse | Correct value in each case; challenges swapped coefficients   |

Known answers need not be confined to tiny instances. A large structured case or a previously
certified optimum can also supply one. What matters is the trustworthiness and applicability of the
reference.

### Independent enumeration

For small instances, a second implementation can enumerate every candidate. This is a
[pseudo-oracle](../appendix/glossary.md#pseudo-oracle): an independently implemented reference that
may itself have defects. [Differential testing](../appendix/glossary.md#differential-testing)
compares its results with the component's results on the same inputs.

For each product, define $m_i=\lfloor\min(W/w_i,V/v_i)\rfloor$. Enumerate integer quantities from
$l_i$ to $m_i$, discard combinations exceeding either capacity, and keep a greatest-revenue feasible
load. If any $l_i>m_i$, there are no candidates. The number of combinations before joint capacity
checks is $\prod_i\max(0,m_i-l_i+1)$; for no products, the single candidate is the empty load.

The reference uses the declared rules directly and does not call the production formulation builder
or total calculator. Check it against the hand-worked cases before using it as evidence. Independent
implementations can still share a mistaken requirement, so agreement is evidence rather than an
infallible verdict.

[Pseudocode: checked differential sweep](#pseudo-checked-differential-sweep) combines comparison
with independent validity checks. The generated cases use integer coefficients, so the checker from
[Checking solution validity and numerical correctness](#ch-solution-validity) applies exactly.

<a id="pseudo-checked-differential-sweep"></a>

**Pseudocode: checked differential sweep**

```
// pseudocode: checked-differential-sweep
public test_generated_small_instances_agree_with_enumeration()
    generator = random generator with seed 42

    repeat 200 times:
        instance = use generator to create a valid instance with 0 to 4 uniquely identified products
                   weights and volumes from 1 to 5
                   revenues from 0 to 20 and commitments from 0 to 2
                   capacities from 0 to 8
        record the instance and generator seed in the failure context
        reference = EnumerationSolver().run(instance)
        candidate = Optimization().run(instance, small_exact_policy)

        if reference.status == infeasible:
            expect candidate.status == infeasible
            expect candidate.solution is absent
        else:
            expect reference.status == optimal
            check_solution(instance, reference.solution)
            expect candidate.status == optimal
            check_solution(instance, candidate.solution)
            expect candidate.solution.objective_value == reference.solution.objective_value
```

`small_exact_policy` requires these bounded teaching cases to finish with a proof; an unresolved or
failed run is not a passing comparison. At most $9^4=6561$ candidate combinations are examined per
instance. A [random seed](../appendix/glossary.md#random-seed) fixes the generated sequence for a
given generator implementation. Saving the actual failing instance is stronger than retaining the
seed alone, particularly across versions or languages. Solver settings and execution conditions may
need recording separately.

### Relationships between runs

A [metamorphic relation](../appendix/glossary.md#metamorphic-relation) connects the outputs of
related executions. For exact maximization, write $z^*(d)$ for the optimal objective of instance
$d$. The following relations assume feasible instances and established optimal values; approximate
results require a numerical comparison justified by their stated guarantees.

| Transformation                                               | Required relation between optimal values |
| ------------------------------------------------------------ | ---------------------------------------- |
| Reorder the product records                                  | Value unchanged                          |
| Multiply every revenue by a positive factor $k$              | Value multiplied by $k$                  |
| Increase revenues without changing feasibility               | Value does not decrease                  |
| Increase capacity or release commitments                     | Value does not decrease                  |
| Decrease capacity or add commitments, preserving feasibility | Value does not increase                  |

For adding or removing products, compare both feasible sets in the union of their coordinates,
fixing absent products to zero. Adding an uncommitted product expands that set. Removing an
uncommitted product restricts it. Adding a product that cannot fit leaves the optimal value
unchanged, but may change which tied solution returns.

Each run still needs independent validity and outcome checks. Reversing product order does not
justify demanding the same load. Increasing capacity does not justify a monotonicity assertion about
arbitrary feasible candidates.

Relationships provide necessary conditions, not complete correctness. On uncommitted instances,
always returning the empty load can satisfy all the value relationships above while failing to
optimize. Nor do relations remove the cost of obtaining the optimal values they compare: a large
instance can remain expensive to test this way.

### Bounds as evidence

For maximization, a feasible candidate with value $z$ and a valid upper bound $U$ satisfy $z\le
z^*\le U$. If $z=U$, optimality follows without producing a second optimal solution. With a declared
absolute gap tolerance $\delta$, $U-z\le\delta$ establishes that the candidate is within that
objective distance of optimal.

The [linear relaxation](../appendix/glossary.md#linear-relaxation) drops the whole-pallet
requirement while keeping the other constraints. Its exact optimum is an upper bound for this
maximization problem because every integer load remains feasible in the relaxation. For numerical
computation, obtain a trustworthy upper bound, for example from a valid dual solution; an arbitrary
feasible solution of the relaxation is not necessarily an upper bound.

On the two-product example, the relaxed optimum is $32/3$, achieved at $x_A=x_B=2/3$. It exceeds the
integer optimum 10, so that relaxation bound alone does not certify the integer load as optimal.
This is a limitation of the evidence, not a defect in the valid load.

<a id="fig-oracles-bounds"></a>

**Figure: candidate, optimum, and bound**

> **Figure placeholder:** `assets/oracles-candidate-optimum-bound.svg`. Draw a number line with a
> feasible value $z$, an unknown optimum $z^*$, and a valid upper bound $U$ in that order.
> Distinguish the true shortfall from the bound-based gap. Include a second line where $z=U$
> certifies optimality. Do not imply every bound is tight.

### Choosing complementary evidence

Choose evidence by what it establishes, then consider its computational cost:

| Evidence                                | What it checks or establishes                  | Principal limitation                              |
| --------------------------------------- | ---------------------------------------------- | ------------------------------------------------- |
| Independent candidate checks            | Feasibility and truthful accounting            | No assurance of optimality                        |
| Known optimum plus validity             | Reference optimal value attained               | Requires a trustworthy applicable reference       |
| Enumeration plus validity               | Agreement over many small cases                | Combinatorial cost and possible reference defects |
| Metamorphic relation                    | Necessary relationship between executions      | Incorrect implementations may satisfy it          |
| Feasible value and matching valid bound | Optimality under the declared numerical policy | Requires a valid, sufficiently tight bound        |

Use selected known cases to make expectations auditable, generated comparisons to explore
unanticipated small cases, and relationships or bounds where their prerequisites hold. No single
technique substitutes for the others.

### Further reading

- Barr et al.,
  [_The Oracle Problem in Software Testing: A Survey_](https://discovery.ucl.ac.uk/id/eprint/1471263/),
  IEEE Transactions on Software Engineering, 2015: a survey of ways to judge software behavior when
  expected results are difficult to obtain.
- William M. McKeeman, _Differential Testing for Software_, Digital Technical Journal, 1998:
  comparing independent implementations to expose disagreement.
- Laurence A. Wolsey, _Integer Programming_, second edition, Wiley, 2020: relaxations, bounds, and
  integer optimality.

**Exercise maintenance notes:** Update the oracles exercise to use explicit statuses and run the
independent checker on both candidates and reference solutions. Save generated failing instances.
Add the multiple-pallet case, tied optima, empty products, and overcommitted cases. Replace the sine
detour with cargo transformations, require their preconditions, and show an always-empty
implementation passing relationships but failing a known-answer test. Include one matching-bound
case and one loose-bound case. Fix enumeration counts when a lower bound exceeds an upper bound; do
not silently skip unresolved runs.

---

<a id="ch-mip-no-optimality"></a>

## 10. Testing without an optimality guarantee

A planner may need an answer before the search can prove it is best. The best feasible solution
found so far, the [incumbent](../appendix/glossary.md#incumbent), can still be useful. Its tests
must reflect what the component actually promises about that answer and about stopping without one.

### What the weaker contract still promises

The [contract](../appendix/glossary.md#contract) still requires valid candidates, truthful totals,
and accurate outcome reporting. It must not describe an unproven candidate as optimal or an
unresolved search as proof of infeasibility. Controlled tests of result translation can exercise
these distinctions without relying on a solver to reach a particular time limit during a test.

Optimal-value relationships are no longer guaranteed by this weaker contract. A particular algorithm
may retain some relationships, or a stronger contract may require them. The loss of optimality
removes the general inference; it does not prove every such relationship false.

### A greedy counterexample

Consider a [heuristic](../appendix/glossary.md#heuristic) that sorts products by revenue per tonne
and loads each while it fits. With weight capacity 3 and volume capacity 10, product A has weight 3,
volume 1, and revenue 10. Initially A is the only product and none is committed, so the method loads
one A and earns 10.

Add an uncommitted product D with weight 2, volume 1, and revenue 7. Its revenue per tonne is 3.5,
greater than A's $10/3$. The heuristic loads one D, leaving only one tonne. No additional pallet
fits, so it earns 7. Both returned loads are valid under unlimited tender. The optimum remains 10,
because A is still available.

An assertion that the returned revenue must not decrease would fail on a permitted heuristic
behavior. The expanded feasible set guarantees a relationship between optima, not between these two
search results.

### A contract that permits useless behavior

Suppose the only promises are that returned candidates are feasible and that `unresolved` is
permitted on every feasible instance. A component that always returns `unresolved` on feasible cases
can satisfy those promises without ever helping the planner. Correctness under a weak contract is
not the same as usefulness.

For this cargo variant, feasibility is directly decidable from the committed load. We can strengthen
the application contract by requiring a feasible result whenever those commitments fit and normal
execution completes. This is a deliberate guarantee of the wrapper around the search, not something
a generic time-limited solver provides.

### Fallbacks and baseline guarantees

Construct $x=l$ as a fallback after checking the valid instance and its commitments. Start the
search with that candidate or retain it outside the search. If no better candidate is available when
the search stops normally, return the fallback as `feasible`. When the commitments do not fit,
return `infeasible` with the established reason. Execution failure remains a distinct outcome under
this draft's policy.

A supplied feasible baseline can strengthen quality further: the result must have revenue at least
that baseline's revenue. Validate the baseline independently before accepting it, and associate it
with the current instance. [Pseudocode: baseline guarantee](#pseudo-baseline-guarantee) checks this
promise on a small instance whose available baseline earns 10; the best-effort result need not be
labeled optimal.

<a id="pseudo-baseline-guarantee"></a>

**Pseudocode: baseline guarantee**

```
// pseudocode: baseline-guarantee
public test_best_effort_preserves_a_valid_baseline()
    instance = the two-product cargo instance
    baseline = Solution(picked={A: 1, B: 0}, objective_value=10, total_weight=2, total_volume=1)
    check_solution(instance, baseline)

    result = Optimization().run(instance, best_effort_policy(baseline=baseline))

    expect result.status is optimal or feasible
    check_solution(instance, result.solution)
    expect result.solution.objective_value >= baseline.objective_value
```

Test the fallback path deterministically by replacing only the internal search collaborator with a
[test double](../appendix/glossary.md#test-double) that reports no improvement or no candidate
before stopping. Keep real-search tests to check integration with the actual optimizer. A supplied
outcome tests the wrapper's policy, not the search algorithm's quality.

### Measuring quality fairly

A [benchmark](../appendix/glossary.md#benchmark) runs a fixed collection of instances under recorded
conditions to measure quality or performance. Retain a row for every instance and run, including
unsuccessful outcomes. Otherwise, an average can improve merely because the difficult cases stopped
returning candidates.

Check candidate validity before computing quality. For a known optimum $z^_$, the absolute shortfall
is $z^_-z$; when $z^_>0$, its relative form is $(z^_-z)/z^*$. For a valid upper bound $U$, use $U-z$
and, when $U>0$, $(U-z)/U$. The latter is a bound-based measure, not an observed exact relative
shortfall.

Revenues are nonnegative in this model. If the applicable reference is zero and the candidate is
valid, its revenue must also be zero; define the relative gap as zero. A candidate exceeding a
purported optimum or upper bound beyond the numerical policy is an inconsistency to investigate, not
a negative gap to average. If there is no candidate or no applicable reference, record the gap as
unavailable.

| Record for each run                                        | Why it matters                                                      |
| ---------------------------------------------------------- | ------------------------------------------------------------------- |
| Instance identity and retained input                       | Keeps comparisons on the same problem                               |
| Outcome and independent validity result                    | Separates unavailable and invalid results from quality measurements |
| Recomputed revenue, reference value, and reference kind    | Distinguishes exact shortfall from a bound-based measure            |
| Absolute and relative gap, or reason unavailable           | Handles zero references and missing evidence explicitly             |
| Time budget, elapsed time, settings, seed, and environment | Makes performance comparisons interpretable                         |

Report candidate availability over the fixed set of known-feasible cases, status counts over the
whole set, and invalid-result counts separately. Summarize gaps only over explicitly identified
valid comparable runs, retaining the per-instance values. Do not silently discard failures when
comparing versions. A seed helps reproduce generated inputs or randomized choices; it does not
guarantee identical wall-clock-limited search trajectories.

### Turning measurements into acceptance

A measurement and an acceptance rule answer different questions. The benchmark records what
happened. A test applies a stated requirement, such as returning a valid candidate on every agreed
feasible case or never worsening an accepted baseline. The same results can support both a report
and an automated pass/fail decision.

Choose thresholds from the application's needs and describe the conditions under which they apply. A
strict quality threshold on a fixed deterministic case can be an ordinary assertion. Noisy runtime
or randomized quality criteria may need repeated runs and a specified statistical rule; one
favorable average does not establish reliability. Detailed statistical benchmark design is outside
this section.

**Exercise maintenance notes:** Replace the old `null`-based time-limit exercise with status
translation, fallback, and baseline tests. Keep the greedy counterexample. Require benchmarks to
validate candidates, preserve every case, distinguish exact and bound-based gaps, and handle zero
references. Include a deliberately misleading average caused by missing difficult cases, plus one
explicit quality acceptance rule. Keep wall-clock experiments separate from deterministic policy
tests.

---

<a id="ch-dss-testing"></a>

## 11. Testing the complete decision-support workflow

A mathematical solution is useful only if it answers the user's actual question. A valid, optimal
load for the wrong data can still produce a wrong recommendation. The system therefore owes its
users more than the optimization component owes its caller: it must preserve meaning from the source
records to the delivered plan.

### A correct optimizer, a wrong recommendation

Suppose a product catalogue gives a pallet's weight as 2,000 kilograms while the optimization
component expects tonnes. Preprocessing passes `2000` instead of `2` and correctly passes aircraft
capacity as 2 tonnes. The optimizer rejects the pallet because it cannot fit in the supplied
instance. It has obeyed its [contract](../appendix/glossary.md#contract), but the recommendation is
wrong.

A second failure can occur after optimization: quantities are associated with the wrong product
identifiers when the report is sorted. Every optimization-component test can pass while the
delivered load list is wrong. System testing must include these translations, not simply rerun
mathematical assertions through a different interface.

### The system's promise

For this worked example, retain the
[unlimited-tender variant](../appendix/running-example.md#ev-unlimited-tender). The source booking
records identify participating products and committed quantities; they impose no tender upper bound.
A different tender policy would be a different model contract.

Define the following application policy for the example. A request identifies one flight and one
fixed snapshot of bookings, product records, and aircraft capacity. The reader selects that flight,
rejects missing or ambiguous records, and preserves product identifiers. Preprocessing converts the
units declared in those records. The optimizer returns the outcome vocabulary from
[Defining the optimization component contract](#ch-model-testing). Postprocessing accepts only a
valid whole-pallet load, and the writer produces a flight-specific load list with quantities,
totals, units, and outcome wording.

Use this explicit response policy:

| Outcome       | User-visible response                                                          |
| ------------- | ------------------------------------------------------------------------------ |
| `optimal`     | Publish the checked load labeled optimal under the declared numerical policy   |
| `feasible`    | Publish the checked load labeled feasible, optimality unproven                 |
| `infeasible`  | Publish a no-plan outcome explaining that the stated constraints cannot be met |
| `unresolved`  | Publish a no-plan outcome saying no solution was found before stopping         |
| `failed`      | Publish a computation-failed outcome without claiming infeasibility            |
| Invalid input | Identify the rejected source data and publish no recommendation                |

An outcome record is not a loadable plan. Neither an old plan nor a partial output file may appear
as the new recommendation. Each delivered artifact carries the requested flight and source-snapshot
identifiers so its origin can be checked.

The example also specifies a delivery deadline. If a complete accepted plan cannot be delivered
before it, report that no plan was delivered by the deadline and do not release a later candidate
automatically. The search budget must leave time for checking and writing. This is a chosen workflow
requirement, not a theorem about optimization.

### Mapping checks to the architecture

Reuse the boundaries in section 04's
[cargo architecture](../04-design/README.md#ch-cargo-architecture). An
[adapter](../appendix/glossary.md#adapter-pattern) handles an external representation;
`PlanFlightLoad` coordinates preprocessing, optimization, and postprocessing, and a solution
provider performs the optimization.

| Part                  | Focused evidence                                                                                |
| --------------------- | ----------------------------------------------------------------------------------------------- |
| Reader                | Selects the requested flight and snapshot; rejects missing and duplicate required records       |
| Preprocessing         | Converts units, preserves commitments, and retains identifier associations                      |
| Solution provider     | Satisfies its mathematical and outcome contract on the supplied instance                        |
| Postprocessing        | Converts quantities safely, preserves identities, recomputes totals, and selects honest wording |
| Writer                | Delivers the specified fields and units without exposing partial or stale plans                 |
| Workflow coordination | Applies outcome and deadline policy across these parts                                          |

Use [unit tests](../appendix/glossary.md#unit-test) for focused transformations and
[integration tests](../appendix/glossary.md#integration-test) for real connections. A small number
of [end-to-end tests](../appendix/glossary.md#end-to-end-test) then exercise the complete selected
workflow. Testing a system is the combined activity; it does not require every rule to be checked
through the outermost entry point.

<a id="fig-dss-testing-evidence-map"></a>

**Figure: evidence across the cargo workflow**

> **Figure placeholder:** `assets/dss-testing-evidence-map.svg`. Draw source records, reader,
> preprocessing, optimization provider, postprocessing, writer, and delivered plan. Under the flow,
> show overlapping brackets for a unit-conversion test, a real provider integration test, and one
> end-to-end test. Mark the kilograms-to-tonnes boundary and the product-identity boundary. Use the
> architecture's existing vocabulary and colors.

### Handling every optimization outcome

A [test double](../appendix/glossary.md#test-double) supplying selected provider results makes
response-policy cases deterministic. Supply each status in the response table and inspect the
delivered artifact and any specified notifications. For candidate-bearing statuses, give the
stand-in a valid load consistent with its totals.

Check both what appears and what must not appear. An unresolved outcome must not produce the phrase
"no feasible load exists." A feasible candidate must not be labeled optimal. A failed run must not
leave a previous flight's plan presented as the current result. Feed an invalid candidate directly
to postprocessing and check rejection, because accepting a provider result is itself a boundary
worth testing.

For deadline policy, supply a controllable clock and a provider whose completion time the test
selects. A clock is just a collaborator returning the current time. Test a completed delivery before
the deadline and a provider that finishes after it; do not depend on deliberate pauses or a solver
happening to run slowly. Separately exercise the real timeout and cancellation connection under
controlled conditions. A simulated clock tests the policy, not actual runtime capacity.

### Checking real connections

Connect the actual reader to preprocessing using representative source records. An observation at
the provider boundary can check that 2,000 kilograms became 2 tonnes and stayed associated with
product A. A separate integration test connects the real provider so the mathematical computation is
exercised as well.

Connect postprocessing to the real writer and inspect the written representation. Test a sort order
in which rows change position, since identifiers must travel with quantities rather than be
reconstructed from row positions. Include a controlled write failure to verify that no partial file
becomes a delivered recommendation.

These tests localize failures: a conversion defect can be diagnosed without waiting for a full
solve, while a real provider test checks that a compatible instance and result actually cross that
boundary.

### One complete cargo recommendation

Choose a small known instance so that the entire delivered answer is independently checkable. These
are the source records for flight `F-101`, snapshot `S-1`; all source values use the exact
integer-unit policy already defined.

| Record                           | Source fields                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------ |
| Aircraft for `F-101`             | Weight capacity 2,000 kilograms; volume capacity 2,000 liters                  |
| Product `A`                      | Weight 2,000 kilograms; volume 1,000 liters; revenue 10,000 dollars per pallet |
| Product `B`                      | Weight 1,000 kilograms; volume 2,000 liters; revenue 6,000 dollars per pallet  |
| Booking for `F-101`, product `A` | Committed quantity 0; unlimited tender                                         |
| Booking for `F-101`, product `B` | Committed quantity 0; unlimited tender                                         |
| Aircraft for `F-202`             | Weight capacity 6,000 kilograms; volume capacity 6,000 liters                  |
| Booking for `F-202`, product `A` | Committed quantity 0; unlimited tender                                         |
| Booking for `F-202`, product `B` | Committed quantity 0; unlimited tender                                         |

All records belong to snapshot `S-1`; both flights use the same product catalogue. The unrelated
flight has larger capacities, making an incorrect flight selection observable. Retain the requested
snapshot identifier in the expected artifact.

The output format for this example is a comma-separated values file with one row per participating
product, including zero quantities, and a separate summary record. The summary gives the flight,
snapshot, outcome, and totals in kilograms, liters, and dollars. Define this format in the
exercise's input/output examples, independently of the production writer.

[Pseudocode: delivered cargo recommendation](#pseudo-delivered-cargo-recommendation) runs the real
path. `read_artifact_independently` is a test helper that reads the documented output format without
using the production postprocessor or its conversion helpers. Check that helper against a
hand-written artifact before using it here.

<a id="pseudo-delivered-cargo-recommendation"></a>

**Pseudocode: delivered cargo recommendation**

```
// pseudocode: delivered-cargo-recommendation
public test_flight_request_delivers_the_expected_load()
    folder = a fresh temporary folder with automatic cleanup
    write the literal F-101 and F-202 source records from the example into folder
    application = assemble the real reader, preprocessing, optimizer, postprocessing, and writer

    application.plan_flight("F-101", snapshot="S-1", sources=folder, policy=small_exact_policy)

    artifact = read_artifact_independently(folder, flight="F-101", snapshot="S-1")
    expect artifact.flight_id == "F-101"
    expect artifact.snapshot_id == "S-1"
    expect artifact.status == optimal
    expect artifact.product_rows == {A: 1, B: 0}
    expect artifact.total_weight_kg == 2000
    expect artifact.total_volume_liters == 1000
    expect artifact.total_revenue_dollars == 10000
    expect artifact.labels specify kilograms, liters, and dollars
    expect there is exactly one completed artifact for this request
```

The expected result follows from the source records: two A pallets exceed weight capacity, two B
pallets exceed volume capacity, and one of each exceeds both. One A earns more than one B. This is
the known two-product case expressed in the user's units, with the real translations included.

The test does not compute its expectation by invoking the production kilograms-to-tonnes conversion.
That would risk agreeing with the same defect. It checks the delivered identifiers and units as well
as the objective, because a mathematically correct quantity vector is insufficient evidence about
the artifact the planner receives.

### Where this evidence stops

> [!WARNING] Passing these tests establishes evidence about the declared rules and workflow, not
> that those rules fully capture the operational decision.

[Validation](../appendix/glossary.md#validation) asks whether this system is suitable for its
intended use. A planner may need loading balance, compatibility rules, or information not included
in this teaching model. Users and domain experts must assess that suitability. A complete end-to-end
experiment remains bounded by the requirements and cases it checks.

**Exercise maintenance notes:** Add a system-testing exercise in both languages using the
unlimited-tender model. Provide literal input records, the documented output format, and the
independent expected artifact above. Include another flight, each provider outcome, an invalid
source record, an invalid candidate, a write failure, and controlled deadline cases. Add deliberate
kilograms-to-tonnes and product-row association defects. Require learners to identify which focused
test diagnoses each defect and which end-to-end assertion detects its delivered effect. Keep the
real-solver example separate from tests using a stand-in provider.

---

<a id="ch-conclusion"></a>

## 12. Conclusion

Confidence in a recommendation rests on complementary evidence about the promises that connect its
inputs to its delivered meaning.

- [What a test establishes](#ch-interface): state the claim, observation, and limits of the
  evidence.
- [Unit testing](#ch-unit-testing): turn each selected behavior into a repeatable experiment.
- [Writing trustworthy tests](#ch-clear-tests): keep expectations auditable and investigate the
  tests themselves.
- [Test-driven development](#ch-tdd): use intended failures to guide small implementation changes.
- [Controlling dependencies with test doubles](#ch-mocks): supply difficult conditions and observe
  outgoing actions.
- [Integration testing](#ch-integration): exercise real connections where components can disagree.
- [Defining the optimization component contract](#ch-model-testing): distinguish assumptions,
  outcomes, and guarantees.
- [Checking solution validity and numerical correctness](#ch-solution-validity): check admissibility
  and accounting.
- [Testing optimality when the answer is hard to know](#ch-oracles): combine evidence with explicit
  limits.
- [Testing without an optimality guarantee](#ch-mip-no-optimality): require fallbacks and assess
  quality promises.
- [Testing the complete decision-support workflow](#ch-dss-testing): check meaning through delivery.

With these checks in place, the next section considers how to put the system in front of its users.

---

[← Book contents](../../README.md) ·
[Next section: Deploying decision-support software →](../06-deployment/README.md)
