# Section 05 — Testing decision-support software

## Introduction

Testing matters in the [software development lifecycle](../appendix/glossary.md#software-development-lifecycle)
because it serves both abilities a team needs: [learning quickly](../03-software-development-lifecycle/README.md#ch-learning)
and [adapting quickly](../03-software-development-lifecycle/README.md#ch-adapting). For learning, a test is how the
scientific method reaches code: it writes a hypothesis about what the code must do in a form anyone can check, and
running it is the experiment that confirms or refutes it. For adapting, testing is one of two pillars. Design is the
other: it keeps each change small and confined to one part, as [the design section](../04-design/README.md) shows. An
[automated test suite](../appendix/glossary.md#test-suite) then shows, on every change, that everything that worked
before still works. With both pillars in place, a team can change working code as often as the business asks.
Decision-support software adds one difficulty ordinary software rarely poses: the correct answer of its optimization
model is hard to know in advance.

### Verification vs validation

A model reaches its users through two translations: a business problem becomes a mathematical model, and the
mathematical model becomes code. [Validation](../appendix/glossary.md#validation) checks the first translation and asks
*are we building the right model?*, a business question. [Verification](../appendix/glossary.md#verification) checks the
second and asks *are we building the model right?*, a software question: does the code do what the mathematical model
says? [Figure: verification and validation](#fig-verification-validation) places each question on its translation.

<a id="fig-verification-validation"></a>

**Figure: verification and validation**

<p align="center">
  <img src="assets/intro-verification-validation.svg" width="760"
       alt="A chain of three boxes joined by arrows labeled translation: a business problem, a decision to support; a
mathematical model, max c transpose x subject to A x at most b; and code, model.py or Model.java. A muted brace under
the first translation reads validation, are we building the right model, a business question. An emphasized brace
under the second translation reads verification, are we building the model right, a software question, this
section">
</p>

This section deals only with verification.

### Types of tests

Tests fall into two families, told apart by the question each one answers.

| Type | The question it answers | Examples |
|---|---|---|
| [Functional](../appendix/glossary.md#functional-test) | Does the program provide its services correctly? | A sum is right; bad input is rejected |
| [Non-functional](../appendix/glossary.md#non-functional-test) | How well does the program provide them? | Security, speed, usability, availability, scalability |

This section is about functional tests.

### Hierarchy of functional tests

Functional tests come in three levels, told apart by how much of the program each one runs. A
[unit test](../appendix/glossary.md#unit-test) checks one small piece of code in isolation. An
[integration test](../appendix/glossary.md#integration-test) combines several units and checks that they work
together. An [end-to-end test](../appendix/glossary.md#end-to-end-test) runs the whole application in a real-world
scenario, the way its users would.

<a id="fig-test-pyramid"></a>

**Figure: test pyramid**

<p align="center">
  <img src="assets/unit-test-pyramid.svg" width="640"
       alt="A pyramid of three levels of functional tests: unit tests at the wide base, integration tests in the middle,
            end-to-end tests at the narrow top. Cost per test rises toward the top, speed rises toward the base, and the
            base holds the most tests">
</p>

Take a small program that reads a user's records, computes their income and tax, and reports the result.
[Figure: test levels](#fig-test-levels) draws it once per level and colors what a single test of that level runs.

<a id="fig-test-levels"></a>

**Figure: test levels**

<p align="center">
  <img src="assets/unit-test-levels.svg" width="780"
       alt="The same example program drawn three times, as six functions in three modules with data flowing downward:
read_user and read_db in reading data, calculate_income and calculate_tax in business logic, create_report and
display_report in processing results. Unit tests: each function is highlighted on its own. Integration tests: two groups
are highlighted, reading data, and business logic together with processing results. End-to-end tests: the whole program
is highlighted as one">
</p>

As [Figure: test pyramid](#fig-test-pyramid) shows, each step up runs more of the program, so each test costs more to
write and runs slower. A healthy suite holds many unit tests, fewer integration tests and a handful of end-to-end
tests.

### Out of scope

- **Performance and scale.** No chapter tests how fast a solver is or how large an instance it handles.
- **Input validation.** Items are never checked for nonsense values such as a negative weight: every infeasible
  instance in this section comes from the capacities, never from a malformed item.
- **Pareto fronts.** Models with several objectives appear only in their lexicographic form.
- **Validation.** Whether a model captures the right decision is a business question, not covered in this book.
- **Reviewing a formulation.** Checking the mathematics of a model on paper is not covered: the tests here check the
  output of solving it.

[Interface vs implementation](#ch-interface) separates what a unit promises from how it keeps the promise, and every
later chapter tests the promise. [Unit testing](#ch-unit-testing), [Writing good tests](#ch-clear-tests) and
[Test-driven development](#ch-tdd) test one unit on its own. [Mocks](#ch-mocks) and
[Integration testing](#ch-integration) take a test beyond the unit, to the systems it calls and the files it reads.
[Testing an optimization model](#ch-model-testing) then meets the difficulty specific to decision-support software and
sets up the pipeline and contract that the next four chapters test: a single objective, then two, first with optimality
guaranteed ([single](#ch-mip-optimal), [multi](#ch-multi-optimal)) and then without ([single](#ch-mip-no-optimality),
[multi](#ch-multi-no-optimality)). [Testing a decision-support system](#ch-dss-testing) applies them to the whole system
behind its interface. Read them in order: each chapter uses only what the chapters before it defined.

<a id="ch-interface"></a>

## Interface vs implementation

Every unit of code has two parts. Its [interface](../appendix/glossary.md#interface) says what the unit does: its
name, the inputs it accepts, and the outputs and errors it returns. Programmers also call it the signature, the
application programming interface (API), the [contract](../appendix/glossary.md#contract), or the
[abstraction](../appendix/glossary.md#abstraction). Its implementation is how the unit does it, and everything in it
is an [implementation detail](../appendix/glossary.md#implementation-detail). Any code that calls the unit is one of
its *clients*. Implementation details include any [private](../appendix/glossary.md#public-and-private) method the
unit calls, such as `is_finite` in the figure: no client can call it, so it can change freely.
[Figure: interface and implementation](#fig-interface-implementation) marks the parts on the calculator's `add`.

<a id="fig-interface-implementation"></a>

**Figure: interface and implementation**

<p align="center">
  <img src="assets/interface-implementation.svg" width="780"
       alt="The pseudocode of add and its private helper is_finite, in one color with comments in green, and three
braces on the right. The first brace, in blue, marks the interface: the line public add(a, b) returns number and the
comments stating its promises (the sum, commutativity, identity, an invalid-input error, an overflow error), labeled
what the unit does, also called signature, API, contract or abstraction, its comments are part of it, visible to every client.
The second brace, in orange, marks the implementation: the input checks that call is_finite, the sum, the overflow check
and the return, labeled how the unit does it, hidden from clients, one of many possible behind the interface. The third
brace, in orange, marks the private method is_finite(x), labeled also an implementation detail, clients cannot call it">
</p>

Two design practices follow from the split. The interface states what the unit does and never how, and the comments
that state its promises belong to it as much as its first line does. The implementation stays hidden from the
clients, so it can change, or give way to a different implementation, without any client noticing.

A wall socket shows the same split. [Figure: socket](#fig-socket) draws it: the socket is the interface, a fixed shape
that delivers a fixed voltage. Behind the wall, the power may come from a gas plant, a wind farm or solar panels; that
is the implementation, and the utility can change it at any time. The lamp, the laptop and the phone are the clients,
and they rely on the socket alone. Telling the interface from the implementation is foundational knowledge, in
[design](../04-design/README.md) as much as in [testing](#ch-unit-testing).

<a id="fig-socket"></a>

**Figure: socket**

<p align="center">
  <img src="assets/interface-socket.svg" width="780"
       alt="The electricity service in three zones. Left, in orange, the implementation hidden behind the wall: a gas
plant, a wind farm and solar panels wired to one line. Middle, in blue, the interface: a socket on the wall. Right, in
green, the clients: a lamp, a laptop and a phone plugged into the socket">
</p>

<a id="ch-unit-testing"></a>

## Unit testing

A unit test sits at the base of the pyramid: it checks one unit of code, such as a function, on its own, and runs in
milliseconds.

### What to test

An interface has one or more *behaviors*, and each one is something to test. The interface in
[Figure: interface and implementation](#fig-interface-implementation) promises five:

1. **The base case**, also called the [happy path](../appendix/glossary.md#happy-path): `add(3, 4) = 7`.
2. **Commutativity**: `add(3, 4) = add(4, 3)`.
3. **Identity**: `add(3, 0) = 3`.
4. **Invalid input**: `add("3", 4)` fails with an invalid-input error.
5. **Overflow**: adding the largest representable number to itself fails with an overflow error.

A behavior may need more than one case: identity holds for 3, and also for a negative number and a very large one.

### How to write a unit test

A unit test's name says what it checks, in three parts: the unit, the behavior and case, and the expected result.
`test__add__given_two_numbers__returns_their_sum` tests `add`, given two ordinary numbers, and expects their sum. When
it fails, its name alone reports which behavior broke.

The body follows the [arrange, act, assert (AAA)](../appendix/glossary.md#arrange-act-assert) pattern: *arrange* the
objects and inputs the test needs, *act* by calling the unit once, and *assert* that the result meets the expectation.
In the pseudocode, `expect` makes the assertion: the test fails if its condition is false.

<a id="pseudo-add-test"></a>

**Pseudocode: add test**

```
// pseudocode: add-test
public test__add__given_two_numbers__returns_their_sum()
    // Arrange
    calculator = Calculator()

    // Act
    result = calculator.add(1, 2)

    // Assert
    expect result == 3
```

### A scientific experiment

A unit test is a scientific experiment in miniature, and it holds every part an experiment in a laboratory holds.
The table finds each part in [Pseudocode: add test](#pseudo-add-test).

| Part of the experiment | In Pseudocode: add test |
|---|---|
| Hypothesis | The name: `add`, given two numbers, returns their sum |
| Controlled conditions | *Arrange*: a new `Calculator` and the fixed inputs 1 and 2 |
| Intervention | *Act*: one call, `calculator.add(1, 2)` |
| Observation | `result`, the value the call returns |
| Prediction checked against the observation | *Assert*: `expect result == 3` |
| Conclusion | The test passes, and the evidence supports the hypothesis; or it fails, and refutes it |

The parts carry the principles of [the scientific method](../03-software-development-lifecycle/README.md#ch-learning)
with them. The hypothesis is testable, because the assertion states it as an objective, measurable condition. The
conditions are controlled, because the test runs one unit on its own, with inputs it fixes itself, so a failure has
one cause: `add`. And the experiment is reproducible: anyone can run it again, on any machine, and get the same result.

### Where to place the test

Test code lives apart from production code, in a folder tree that mirrors it, so each module's tests sit at the same
place in the tests tree as the module does in the source tree.

<a id="pseudo-test-layout"></a>

**Pseudocode: test layout**

```
// pseudocode: test-layout
project/
    src/
        calculator
    tests/
        test_calculator_add
        test_calculator_divide
```

### Code coverage

How do you know you tested every behavior? The starting point is
[code coverage](../appendix/glossary.md#code-coverage): a tool records which lines of the production code the tests
run, and reports the rest. [Pseudocode: add coverage](#pseudo-add-coverage) marks each line of `add` for a suite
that holds only the happy-path test.

<a id="pseudo-add-coverage"></a>

**Pseudocode: add coverage**

```
// pseudocode: add-coverage
public add(a, b) returns number
    if not is_finite(a)                     // ✓ run
        fail with invalid-input error       // ✗ not run
    if not is_finite(b)                     // ✓ run
        fail with invalid-input error       // ✗ not run
    result = a + b                          // ✓ run
    if result is too large to represent     // ✓ run
        fail with overflow error            // ✗ not run
    return result                           // ✓ run
```

> [!NOTE]
> The pseudocode is illustrative: a coverage tool reports the same pattern for `add` written in a real language, over
> more lines.

The three lines that never run belong to the invalid-input and overflow behaviors. Add a test for each, and every line
runs: coverage reaches 100%. Now delete the commutativity test. Coverage stays at 100%, because the happy-path test
already runs every line the commutativity test runs. Coverage points at lines no test runs; it cannot point at a
behavior no test checks. Use it to find what is missing, and use the list of behaviors to decide when you are done.

### Exercise: a calculator

The exercise lives in the practice repositories: test the calculator's `divide` the way this part tested `add`.

> **Practice it**
>
> - Python: [Unit testing exercise](https://github.com/sefop/training-testing-python/tree/main/src/unit_tests_and_coverage)
> - Java: [Unit testing exercise](https://github.com/sefop/sefop-training-java/tree/main/src/main/java/unit_tests_and_coverage)

<a id="ch-clear-tests"></a>

## Writing good tests

[Unit testing](#ch-unit-testing) gave a test its structure and its name; the practices below tell a good test from a
bad one.

### Complete and concise

A test is *complete* when its body holds everything a reader needs to understand its result, and *concise* when it
holds nothing else. [Pseudocode: cluttered test](#pseudo-cluttered-test) fails both ways: the constructor arguments
play no part in addition, and the numbers that decide the result hide inside helper functions.

<a id="pseudo-cluttered-test"></a>

**Pseudocode: cluttered test**

```
// pseudocode: cluttered-test
public test__add__given_two_numbers__returns_their_sum()
    calculator = Calculator(precision=10, rounding="half-even", log_file="calc.log")
    result = calculator.add(first_operand(), second_operand())
    expect result == 5
```

[Pseudocode: concise test](#pseudo-concise-test) keeps the numbers that matter in view and drops the rest.

<a id="pseudo-concise-test"></a>

**Pseudocode: concise test**

```
// pseudocode: concise-test
public test__add__given_two_numbers__returns_their_sum()
    calculator = Calculator()
    result = calculator.add(2, 3)
    expect result == 5
```

### One behavior per test

[Pseudocode: method test](#pseudo-method-test) checks three behaviors of `add` at once. When it fails, its name cannot
say which behavior broke, and the first failing `expect` stops the test, so the ones after it go unchecked.

<a id="pseudo-method-test"></a>

**Pseudocode: method test**

```
// pseudocode: method-test
public test__add__works()
    calculator = Calculator()
    expect calculator.add(3, 4) == 7
    expect calculator.add(3, 4) == calculator.add(4, 3)
    expect calculator.add(3, 0) == 3
```

[Pseudocode: behavior tests](#pseudo-behavior-tests) splits it into one test per behavior, each named for the
behavior it checks. A name that needs the word "and" describes two behaviors, and belongs to two tests.

<a id="pseudo-behavior-tests"></a>

**Pseudocode: behavior tests**

```
// pseudocode: behavior-tests
public test__add__given_two_numbers__returns_their_sum()
    calculator = Calculator()
    result = calculator.add(3, 4)
    expect result == 7

public test__add__given_swapped_operands__returns_the_same_sum()
    calculator = Calculator()
    expect calculator.add(3, 4) == calculator.add(4, 3)

public test__add__given_zero__returns_the_other_number()
    calculator = Calculator()
    result = calculator.add(3, 0)
    expect result == 3
```

### No logic in tests

Production code must handle any input, so it needs logic: loops, conditions, arithmetic. A test handles a few chosen
inputs, so it needs none, and each piece of logic it carries is a computation its reader must run in their head.
[Pseudocode: logic test](#pseudo-logic-test) loops over six pairs of numbers and computes each expected value with
`a + b`, the very operation `add` performs. The test repeats the implementation instead of checking it.

<a id="pseudo-logic-test"></a>

**Pseudocode: logic test**

```
// pseudocode: logic-test
public test__add__given_two_numbers__returns_their_sum()
    calculator = Calculator()
    for each a in [1, 2, 3]
        for each b in [4, 5]
            expect calculator.add(a, b) == a + b
```

[Pseudocode: concise test](#pseudo-concise-test) is straight-line code with a literal expected value: a reader checks
that 2 plus 3 is 5 at a glance.

### Clear failure messages

When a test fails, its failure message is often the first thing a reader sees, and sometimes the only one. A good
message states the inputs, the expected value and the actual value. So far, `expect` has taken a condition; it also
takes a message after a comma, which the test reports when the condition is false.
[Pseudocode: vague failure](#pseudo-vague-failure) reduces the comparison to true or false before asserting it, so
its failure reads only "expected true, got false".

<a id="pseudo-vague-failure"></a>

**Pseudocode: vague failure**

```
// pseudocode: vague-failure
public test__add__given_two_numbers__returns_their_sum()
    calculator = Calculator()
    result = calculator.add(2, 3)
    expect (result == 5) is true
```

[Pseudocode: clear failure](#pseudo-clear-failure) fails with "add(2, 3) returned 6, expected 5", which points at the
broken behavior before anyone opens the test.

<a id="pseudo-clear-failure"></a>

**Pseudocode: clear failure**

```
// pseudocode: clear-failure
public test__add__given_two_numbers__returns_their_sum()
    calculator = Calculator()
    result = calculator.add(2, 3)
    expect result == 5, "add(2, 3) returned {result}, expected 5"
```

### Descriptive and meaningful

Production code follows [don't repeat yourself (DRY)](../appendix/glossary.md#dont-repeat-yourself): each piece of
knowledge lives in one place, so a change is one edit. Test code follows
[descriptive and meaningful phrases (DAMP)](../appendix/glossary.md#descriptive-and-meaningful-phrases) instead: a
little repetition is welcome when it lets each test be read on its own.
[Pseudocode: too-DRY tests](#pseudo-too-dry-tests) shares its calculator and its numbers across the file, so to check
either test, a reader must first scroll up to learn what `a` and `b` are.

<a id="pseudo-too-dry-tests"></a>

**Pseudocode: too-DRY tests**

```
// pseudocode: too-dry-tests
calculator = Calculator()
a = 3
b = 4

public test__add__given_two_numbers__returns_their_sum()
    expect calculator.add(a, b) == 7

public test__add__given_swapped_operands__returns_the_same_sum()
    expect calculator.add(a, b) == calculator.add(b, a)
```

[Pseudocode: behavior tests](#pseudo-behavior-tests) repeats `calculator = Calculator()` and its numbers in every
test, and each test reads on its own.

### Further reading

- Titus Winters, Tom Manshreck and Hyrum Wright, *Software Engineering at Google*, O'Reilly, 2020, chapter 12, "Unit
  Testing": the source of these five practices, each shown on tests from a code base of Google's size.
- Vladimir Khorikov, *Unit Testing: Principles, Practices and Patterns*, Manning, 2020, chapter 3, "The anatomy of a
  unit test": the same ground from another angle, on one behavior per test, no branching in tests, and setup shared
  between tests.

<a id="ch-tdd"></a>

## Test-driven development

[Test-driven development (TDD)](../appendix/glossary.md#test-driven-development) writes each test before the code it
checks. In the terms of the scientific experiment in [Unit testing](#ch-unit-testing), it states the hypothesis
before it builds the experiment: the test says what the code must do while that code does not exist yet.

### The cycle: red, green, refactor

TDD advances in short cycles of three steps, named after the colors a test tool shows:

1. **Red.** Write one test for the next requirement, run it, and watch it fail.
2. **Green.** Write the minimum code that makes it pass.
3. **Refactor.** Improve the code while every test keeps passing. Changing code without changing what it does is
   called [refactoring](../appendix/glossary.md#refactoring).

Then the next requirement starts the next cycle. [Figure: TDD cycle](#fig-tdd-cycle) draws the loop.

<a id="fig-tdd-cycle"></a>

**Figure: TDD cycle**

<p align="center">
  <img src="assets/tdd-cycle.svg" width="520"
       alt="A loop of three steps. Red: write a failing test. Green: make it pass with the minimum code. Refactor:
improve the code, tests still pass. An arrow labeled next requirement leads from refactor back to red">
</p>

### Why each step matters

**Red shows that the test can fail.** A test that has never failed has never been shown to test anything: it may
check the wrong value, or not run at all. Watching it fail first is the evidence that it can tell working code from
missing code.

**Red, then green, shows causality.** The test failed, one change was made, and now the test passes: that change is
why it passes. This is the causality principle of
[the scientific method](../03-software-development-lifecycle/README.md#ch-learning) applied to code: change one thing
at a time, so the result shows what caused it. A test written after the code passes on its first run, and cannot tell
whether the code made it pass or whether it would have passed anyway.

**Green with the minimum code keeps every line accountable.** Each line of production code exists because a test
demanded it, so no line goes untested and no behavior is built that nobody asked for.

**Refactor is safe because the tests check the interface.** The tests pin down what the code does, never how, as
[Interface vs implementation](#ch-interface) set out. The code can change shape underneath them, and a test that
turns red means a promise broke, not that the code merely moved.

### A linear expression example

A linear expression has the form $a_0 + a_1 x_1 + \dots + a_n x_n$: a scalar $a_0$, and a coefficient $a_i$ for each
variable $x_i$. The class `LinearExpression` represents one. The scalar and the coefficients are floating-point
numbers, and each variable is identified by its name, a string. For example:

| Expression | Scalar | Coefficients |
|---|---|---|
| $0$ | 0.0 | none |
| $1 + 2x$ | 1.0 | `"x"`: 2.0 |
| $-1 - x + 2y$ | -1.0 | `"x"`: -1.0, `"y"`: 2.0 |

This example builds the scalar part test-first, in three cycles, with these requirements:

- An expression built with no arguments has scalar 0.0.
- An expression built with a scalar has that scalar.
- Adding a value to the scalar increases the scalar by that value.

**Cycle 1.** [Pseudocode: empty expression test](#pseudo-empty-expression-test) states the first requirement. It is
red: `LinearExpression` does not exist yet.

<a id="pseudo-empty-expression-test"></a>

**Pseudocode: empty expression test**

```
// pseudocode: empty-expression-test
public test__linear_expression__given_no_arguments__has_scalar_zero()
    expression = LinearExpression()
    expect expression.scalar() == 0.0
```

The minimum code that turns it green returns a constant, as
[Pseudocode: constant scalar](#pseudo-constant-scalar) shows. It looks like cheating, and on purpose: one test
demands no more than this, and the next test will force the real code.

<a id="pseudo-constant-scalar"></a>

**Pseudocode: constant scalar**

```
// pseudocode: constant-scalar
class LinearExpression
    public scalar() returns number
        return 0.0
```

**Cycle 2.** [Pseudocode: scalar-only test](#pseudo-scalar-only-test) states the second requirement. It is red: the
constant 0.0 is not 3.0.

<a id="pseudo-scalar-only-test"></a>

**Pseudocode: scalar-only test**

```
// pseudocode: scalar-only-test
public test__linear_expression__given_a_scalar__has_that_scalar()
    expression = LinearExpression(scalar = 3.0)
    expect expression.scalar() == 3.0
```

To pass both tests, the expression must keep the scalar it receives, with 0.0 when it receives none.
[Pseudocode: stored scalar](#pseudo-stored-scalar) does that, and the constant is gone. The refactor step finds
nothing to improve yet, and a cycle may end that way.

<a id="pseudo-stored-scalar"></a>

**Pseudocode: stored scalar**

```
// pseudocode: stored-scalar
class LinearExpression
    private stored_scalar

    public constructor(scalar = 0.0)
        stored_scalar = scalar

    public scalar() returns number
        return stored_scalar
```

**Cycle 3.** [Pseudocode: add scalar test](#pseudo-add-scalar-test) states the third requirement. It is red:
`add_scalar` does not exist yet.

<a id="pseudo-add-scalar-test"></a>

**Pseudocode: add scalar test**

```
// pseudocode: add-scalar-test
public test__add_scalar__given_a_value__increases_the_scalar_by_it()
    expression = LinearExpression(scalar = 1.0)
    expression.add_scalar(3.0)
    expect expression.scalar() == 4.0
```

[Pseudocode: add scalar](#pseudo-add-scalar) adds the method, and all three tests pass.

<a id="pseudo-add-scalar"></a>

**Pseudocode: add scalar**

```
// pseudocode: add-scalar
class LinearExpression
    private stored_scalar

    public constructor(scalar = 0.0)
        stored_scalar = scalar

    public scalar() returns number
        return stored_scalar

    public add_scalar(value)
        stored_scalar = stored_scalar + value
```

The scalar part is done. The variables are the exercise: building an expression with a term, adding a term to a
variable that is already present, merging two expressions, and reading back the variables and their coefficients,
one cycle at a time.

### Further reading

- Kent Beck, *Test-Driven Development: By Example*, Addison-Wesley, 2002: the book that named the cycle, worked
  through at the same small step size as this chapter.

> **Practice it**
>
> - Python: [Test-driven development exercise](https://github.com/sefop/training-testing-python/tree/main/src/test_driven_development)
> - Java: [Test-driven development exercise](https://github.com/sefop/sefop-training-java/tree/main/src/main/java/test_driven_development)

<a id="ch-mocks"></a>

## Mocks

A unit test checks the behaviors a unit promises through its [interface](../appendix/glossary.md#interface). A unit
rarely works alone: it calls another unit, its [dependency](../appendix/glossary.md#dependency), to do part of its
work. A behavior may be visible in a returned value or error, in an outgoing call, or in both: `add` returns a sum,
while a nightly planning job asks a notifier to wake someone up. The earlier tests checked the first kind. The second
raises a problem: a unit test must not make an external call for real.

### Why the real dependency stays out of the test

A test runs many times a day, on developers' laptops and on shared servers. When a dependency's calls reach a person
or an external system, every run would wake a real person or write to a real system. That system may also be slow,
or out of reach from the machine that runs the test. And whatever record it keeps lives outside the program, where
the test has no dependable way to read it.

### What a mock is

A [mock](../appendix/glossary.md#mock) is a stand-in that the test puts in place of the dependency. It accepts the
same calls as the real one, does nothing else, and records every call it receives, with its arguments. The unit
receives it the way it would receive the real dependency, from outside, through
[dependency injection](../appendix/glossary.md#dependency-injection). After acting, the test asserts on the record.

[Figure: real notifier and mock](#fig-mocks-real-vs-mock) sets the two side by side. They share the same
[interface](#ch-interface); only what sits behind it differs.

<a id="fig-mocks-real-vs-mock"></a>

**Figure: real notifier and mock**

<p align="center">
  <img src="assets/mocks-real-vs-mock.svg" width="700"
       alt="Two notifiers side by side with the same interface on top, notify(message), joined by an equals sign. Left,
the real notifier: behind the interface, in orange, its implementation connects to the SMS service and sends the text,
and an arrow leaves the object to a phone, labeled a real person is woken up. Right, the mock notifier: behind the same
interface, in green, only a record of the calls it received, notify with the message Instance 2026-09-26: no feasible
plan exists, labeled sends nothing. Caption: same interface, the unit that calls notify cannot tell them apart">
</p>

Nothing more is needed to build one. [Pseudocode: recording notifier](#pseudo-recording-notifier) is a complete mock
of a notifier: it keeps the messages it is asked to send, and sends none.

<a id="pseudo-recording-notifier"></a>

**Pseudocode: recording notifier**

```
// pseudocode: recording-notifier
class RecordingNotifier implements Notifier
    private messages = empty list

    public notify(message)
        append message to messages
```

Test tools build such an object for any interface, so tests rarely write one by hand. The pseudocode writes
`notifier = mock(Notifier)` to create one, and reads its record with two assertions:

- `expect notifier.notify called once with "<message>"` holds when exactly one call was made, with that argument.
- `expect notifier.notify never called` holds when no call was made.

### A worked example

Every night, a planning job solves tomorrow's plan. When the model reports that no feasible plan exists, someone must
act before morning, so the job notifies the planner on call. [Pseudocode: nightly planner](#pseudo-nightly-planner)
receives the result of the solve and the notifier; it never calls the solver itself.

<a id="pseudo-nightly-planner"></a>

**Pseudocode: nightly planner**

```
// pseudocode: nightly-planner
interface Notifier
    public notify(message)

class NightlyPlanner
    private notifier

    public constructor(notifier)
        keep notifier

    public review(result)
        if result.status is infeasible
            notifier.notify("Instance " + result.instance_id + ": no feasible plan exists.")
```

The notification is the behavior, so the test checks the notification.
[Pseudocode: infeasible notifies test](#pseudo-infeasible-notifies-test) hands `NightlyPlanner` a mock and an infeasible
result, then asserts on the one call the mock recorded.

<a id="pseudo-infeasible-notifies-test"></a>

**Pseudocode: infeasible notifies test**

```
// pseudocode: infeasible-notifies-test
public test__review__given_an_infeasible_plan__notifies_once_with_the_instance()
    // arrange
    notifier = mock(Notifier)
    planner = NightlyPlanner(notifier)
    result = SolveResult(instance_id = "2026-09-26", status = infeasible)

    // act
    planner.review(result)

    // assert
    expect notifier.notify called once with "Instance 2026-09-26: no feasible plan exists."
```

A feasible night must stay quiet. [Pseudocode: feasible silent test](#pseudo-feasible-silent-test) asserts that no
notification was sent, which only a record of calls can show.

<a id="pseudo-feasible-silent-test"></a>

**Pseudocode: feasible silent test**

```
// pseudocode: feasible-silent-test
public test__review__given_a_feasible_plan__sends_no_notification()
    // arrange
    notifier = mock(Notifier)
    planner = NightlyPlanner(notifier)
    result = SolveResult(instance_id = "2026-09-26", status = feasible)

    // act
    planner.review(result)

    // assert
    expect notifier.notify never called
```

### What to mock

Mock the dependencies whose calls reach people or external systems. Those calls are behaviors a client relies on,
so checking them checks the [interface](#ch-interface). Keep the unit's own internal parts real. A test that mocks
them checks how the unit does its work, and breaks the day that work is reorganized, even though no promise changed.

### Further reading

- Vladimir Khorikov, *Unit Testing: Principles, Practices and Patterns*, Manning, 2020, chapters 5, "Mocks and test
  fragility", and 9, "Mocking best practices": when a mock protects a test and when it makes the test brittle.
- Titus Winters, Tom Manshreck and Hyrum Wright, *Software Engineering at Google*, O'Reilly, 2020, chapter 13, "Test
  Doubles": the other kinds of stand-ins, such as stubs and fakes, and when to prefer the real dependency.

> **Practice it**
>
> - Python: [Mocks exercise](https://github.com/sefop/training-testing-python/tree/main/src/mocks)
> - Java: [Mocks exercise](https://github.com/sefop/sefop-training-java/tree/main/src/main/java/mocks)

<a id="ch-integration"></a>

## Integration testing

The [integration test](../appendix/glossary.md#integration-test) is the middle level of
[Figure: test pyramid](#fig-test-pyramid). A program's units do not only call each other: they also meet real things
outside the program, such as files, databases and other systems, and many bugs live in that meeting. A file written
in one format and read in another, a folder that is not where the code expects it: a unit test with a
[mock](../appendix/glossary.md#mock) cannot see such bugs, because the mock stands exactly where the bug is. An
integration test runs the units together with those real dependencies.

### Which dependencies stay real

Not every dependency should be real in an integration test. The rule depends on who else can see it.

- A [managed dependency](../appendix/glossary.md#managed-dependency) is used only by your program, such as its own
  files or its own database. It stays real: how the program uses it is an implementation detail, and only the real
  one shows whether that detail works.
- An [unmanaged dependency](../appendix/glossary.md#unmanaged-dependency) is observed by other people or systems,
  such as the notifier. It stays a mock, as in [Mocks](#ch-mocks): a test must not wake a real person, and the call
  itself is the behavior to check.

[Figure: real and mocked dependencies](#fig-integration-dependencies) applies the rule to the nightly planner.

<a id="fig-integration-dependencies"></a>

**Figure: real and mocked dependencies**

<p align="center">
  <img src="assets/integration-dependencies.svg" width="720"
       alt="NightlyPlanner in the middle of an integration test. On the left, in green, the results file: a managed
dependency, only this program uses it, so the test keeps it real. On the right, in purple, the notifier: an unmanaged
dependency, people observe it, so the test replaces it with a mock">
</p>

### What an integration test covers

An integration test is slower and costlier than a unit test, so it covers one happy path per scenario, through every
real dependency. The edge cases stay in unit tests, with one exception: an edge case that only the real dependency
can produce, such as tonight's file being missing, belongs in an integration test.

### A worked example

The nightly planner no longer receives the result of the solve as an argument. The solve job saves each night's
result to a file with a `ResultsWriter`, and the planner reads it back with its own `ResultsReader`. They are two
units, owned by two teams, and they share no code: each one encodes its own idea of the file's format.
[Pseudocode: nightly planner with reader](#pseudo-nightly-planner-with-reader) shows the planner.

<a id="pseudo-nightly-planner-with-reader"></a>

**Pseudocode: nightly planner with reader**

```
// pseudocode: nightly-planner-with-reader
class NightlyPlanner
    private reader
    private notifier

    public constructor(reader, notifier)
        keep reader and notifier

    public review_tonight(instance_id)
        result = reader.read(instance_id)
        if result.status is infeasible
            notifier.notify("Instance " + instance_id + ": no feasible plan exists.")
```

[Pseudocode: infeasible night integration test](#pseudo-infeasible-night-integration-test) writes a real file with
the real writer, runs the planner with the real reader, and keeps only the notifier a mock.

<a id="pseudo-infeasible-night-integration-test"></a>

**Pseudocode: infeasible night integration test**

```
// pseudocode: infeasible-night-integration-test
public test__review_tonight__given_an_infeasible_result_on_disk__notifies_once()
    // Arrange
    folder = a new, empty temporary folder
    ResultsWriter(folder).write(SolveResult(instance_id = "2026-09-26", status = infeasible))
    notifier = mock(Notifier)
    planner = NightlyPlanner(ResultsReader(folder), notifier)

    // Act
    planner.review_tonight("2026-09-26")

    // Assert
    expect notifier.notify called once with "Instance 2026-09-26: no feasible plan exists."
```

Suppose the solve job's team changes how it writes the status, `Infeasible` instead of `infeasible`, and updates its
own tests to match. The writer's tests pass, and so do the reader's, each against its own idea of the format. Only
this test, which joins the two, fails.

### Further reading

- Vladimir Khorikov, *Unit Testing: Principles, Practices and Patterns*, Manning, 2020, chapters 8, "Why integration
  testing?", and 10, "Testing the database": the rule for managed and unmanaged dependencies, and how many
  integration tests to write.
- Titus Winters, Tom Manshreck and Hyrum Wright, *Software Engineering at Google*, O'Reilly, 2020, chapter 14,
  "Larger Testing": tests beyond the unit, and the gaps in unit tests they close.

> **Practice it**
>
> - Python: [Integration testing exercise](https://github.com/sefop/training-testing-python/tree/main/src/integration_testing)
> - Java: [Integration testing exercise](https://github.com/sefop/sefop-training-java/tree/main/src/main/java/integration_testing)

---

<a id="ch-model-testing"></a>

## Testing an optimization model

Every test so far compared an output with an expected value that someone could work out before running the code:
`add(2, 3)` is 5, and a notification carries a known message. An optimization model breaks that assumption, because its
expected output is the very thing it exists to compute.

Before jumping into the details, lets clarify some things first. Testing an optimization model can mean two different things:
1. Given some instance data, test the formulation is coded correctly.
2. Given some instance data, test the output of the solved model is correct.

What should we do? the difference is subtle, but very important. Both are plausible, indeed. Let's go back to the first
principles to answer the question.

Testing the formulation is possible, but I advise against it. This idea has 2 flaws. The first flaw is that it
assumes there is a formulation coded in the first place, which might not necessarily be true in some situations. For
example, if you are solving a problem with a heuristic or metaheuristic, then there is no formulation coded. The
second flaw is that it does not test the public behavior of interest (the optimization model output). The
formulation is indeed, an implementation detail. Thus, we should only test the output of the solved model. That is
the correct public behavior that (should) be offered by this abstraction. If the abstraction is promising that a
particular solver is being used (Gurobi, XPress, Cplex, etc.), that is a design problem (known as a leaky abstraction).

<a id="model-difficulties"></a>

### Why an optimization model is harder to test

Six properties of an optimization model make its output harder to test than the output of the calculator.

<a id="difficulty-oracle"></a>

**The oracle problem.** Whatever decides whether an output is correct is called a
[test oracle](../appendix/glossary.md#test-oracle). For the calculator, the oracle is arithmetic you already know: 2
plus 3 is 5, worked out without reading a line of `add`. For an optimization model, writing `expect result.objective_value == ???`
needs the optimal value, and for an instance large enough, computing it independently means solving
the problem the model exists to solve. The difficulty has a name in the software testing literature: the
[oracle problem](../appendix/glossary.md#oracle-problem). [Figure: the oracle problem](#fig-oracle-problem) sets the two
situations side by side.

<a id="fig-oracle-problem"></a>

**Figure: the oracle problem**

<p align="center">
  <img src="assets/model-testing-oracle-problem.svg" width="760"
       alt="Two tests side by side. Left, an ordinary test: the inputs 2 and 3 go into add, which returns 5, and the
expected value 5 comes from arithmetic done in your head, so the two can be compared. Right, a test of an optimization
model on a large instance: the instance goes into the model and its solver, which returns an objective value, but the
expected value is a question mark, because the only way to compute it is to solve the same problem again">
</p>

<a id="difficulty-uniqueness"></a>

**The answer may not be unique.** A model instance can have a single optimal solution, or several that tie at the same
objective value. Which one comes back depends on the solver, its settings, even the order of the input. A test cannot know
in advance which of the optimal solutions it will receive, nor whether there is more than one.

<a id="difficulty-infeasible"></a>

**An empty feasible region is an answer.** Constraints can contradict each other: one demands $x \ge 2$ while another
allows at most $x \le 1$. Then no solution exists, and "infeasible" is the correct output, not a failure. A correct
model must say so rather than return a solution, and a test must treat that statement as an answer to check, like any
other.

<a id="difficulty-floating-point"></a>

**Numbers are floating point.** A computer stores most decimal numbers approximately: 0.1 + 0.2 is not exactly 0.3. A
solver computes with that finite precision, and it accepts a constraint as satisfied when it is violated by less than a
small tolerance. Two correct answers can therefore differ in their last digits, an objective value can come back as
25.999999998 instead of 26, and a constraint $x \le 10$ can be met at 10.000000001. Equality can only mean equality
within a tolerance.

<a id="difficulty-optimality"></a>

**Optimality may not be guaranteed.** A [heuristic](../appendix/glossary.md#heuristic) gives up the guarantee of
optimality on purpose, in exchange for speed on large instances. An exact solver stopped by a time limit does the same
without announcing it: it returns the best solution found so far, which need not be the best one. For such solvers, "the
optimal value" is not something the output promises, and two runs may even return different solutions.

<a id="difficulty-algorithm"></a>

**The algorithm may change.** An optimization model can be solved with many algorithms, such as a commercial-solver,
a heuristic, a metaheuristic, dynamic programming, etc. Thus, the tests should not use leaked information from the
algorithm to assert correctness.

<a id="model-cargo"></a>

### A cargo model example

For the next parts of the section we are going to use this example. The full definition of the cargo loading system is
written here [the appendix](../appendix/running-example.md#an-optimization-model-for-this-problem): for one cargo
flight, the question is what cargo to load to maximize revenue and respect operational constraints. The model is
is a [mixed-integer program](../appendix/glossary.md#mixed-integer-program) (MIP).

The symbols are defined in the following table:

| Symbol | Meaning                                                      | Unit |
|:---:|--------------------------------------------------------------|---|
| $r_i$ | revenue of one pallet of product $i$, non-negative           | thousands of USD |
| $w_i$ | weight of one pallet, positive                               | tonnes |
| $v_i$ | volume of one pallet, positive                               | m³ |
| $l_i$ | pallets of product $i$ that must fly, a non-negative integer | pallets |
| $W$, $V$ | max weight and hold capacity, non-negative                   | tonnes, m³ |
| $x_i$ | pallets of product $i$ to load                               | pallets |

The optimization model is:

$$
\begin{aligned}
\max_{x} \quad & \sum_{i \in I} r_i x_i & \text{maximize revenue} \\
\text{s.t.} \quad &
\sum_{i \in I} w_i x_i \le W & \text{weight capacity} \\ &
\sum_{i \in I} v_i x_i \le V & \text{hold capacity} \\ &
x_i \ge l_i \quad \forall i \in I & \text{committed freight} \\ &
x_i \in \mathbb{Z} \quad \forall i \in I & \text{whole pallets}
\end{aligned}
$$

<a id="model-what-to-test"></a>

### What to test

[Interface vs implementation](#ch-interface) set the rule every chapter since has followed: a test checks what code
promises, not how it keeps the promise. A model, however, is not one unit of code. Between an instance and a decision,
five modules work in sequence:

1. **Receive the instance**, already checked for nonsense values.
2. **Build the model**: its variables, objective and constraints.
3. **Solve it** with an algorithm.
4. **Assemble the solution**: read the solver's values back into pallets per product and totals.
5. **Return the result.**

None of them on its own shows that the load is right. A model built correctly and solved correctly still yields the
wrong load if the assembly reads the values in the wrong order. The tests therefore run the five modules together, as
[integration tests](../appendix/glossary.md#integration-test): they hand the pipeline an instance and check what comes
back, as [Figure: the pipeline under test](#fig-model-pipeline) shows.

<a id="fig-model-pipeline"></a>

**Figure: the pipeline under test**

<p align="center">
  <img src="assets/model-testing-pipeline.svg" width="760"
       alt="Five orange boxes in a row inside a dashed boundary labeled integration test: receive the instance, build
the model, solve, assemble the solution, return the result. An instance enters the boundary on the left and a result
leaves it on the right, both through a blue edge labeled contract. The test hands in the instance and reads only the
result">
</p>

The solver stays real in these tests. It is a library inside the program, not a
[managed dependency](../appendix/glossary.md#managed-dependency) such as the program's own files, but it stays real for
the reason [What an integration test covers](#what-an-integration-test-covers) gives for edge cases: the optimum, an
infeasible instance and a tie are behaviors that only the real solver produces.

**The contract comes first.** A promise must be written down before it can be tested. A
[contract](../appendix/glossary.md#contract) is the promise a piece of code makes to its callers: what it needs as input
and what it guarantees as output, and nothing about how. Everything else, the algorithm, its running time, its internal
data structures, is an [implementation detail](../appendix/glossary.md#implementation-detail). For the cargo model,
`solve` returns a `result` with five fields:

- `status`: `OPTIMAL` when a load was found and proven the best, or `INFEASIBLE` when no load is feasible. The contract
  names the second because [an empty feasible region is an answer](#difficulty-infeasible).
- `picked`: the pallets loaded of each product, from product name to a whole number, 0 for a product left behind.
- `objective_value`: the revenue of the load.
- `total_weight` and `total_volume`: the weight and the volume of the load.

Two clauses complete it:

1. When `status` is `INFEASIBLE`, the other fields carry no meaning.
2. When several loads tie for the best revenue, any one of them may be returned.

**Why the contract, and not the algorithm.** [The algorithm may change](#difficulty-algorithm), and a test that checks
how the answer was computed turns red at a legitimate change even though nothing a user cares about got worse. A
[regression](../appendix/glossary.md#regression), a behavior that used to work and no longer does, never happened, yet
the test reports one. Take two pipelines around the same model: `enumeration_solver()` tries every load, and
`mip_solver()` calls a MIP solver. [Pseudocode: algorithm-coupled test](#pseudo-algorithm-coupled-test) is coupled to
the first:

<a id="pseudo-algorithm-coupled-test"></a>

**Pseudocode: algorithm-coupled test**

```
// pseudocode: algorithm-coupled-test
a = item(name="A", weight=2, volume=1, revenue=10)
b = item(name="B", weight=1, volume=2, revenue=6)

solver = enumeration_solver()
result = solver.solve([a, b], weight_capacity=2, volume_capacity=2)

expect solver.loads_checked == 4             // how the answer was found
expect result.objective_value == 10
```

Replace `enumeration_solver()` with `mip_solver()` and this test breaks: a MIP solver never enumerates loads, so there
is no count to check. The optimum is still 10, yet the test fails. [Pseudocode: contract test](#pseudo-contract-test)
reads only what the contract promises:

<a id="pseudo-contract-test"></a>

**Pseudocode: contract test**

```
// pseudocode: contract-test
for solver in [enumeration_solver(), mip_solver()]:
    result = solver.solve([a, b], weight_capacity=2, volume_capacity=2)

    expect result.status == OPTIMAL
    expect result.objective_value == 10
```

Running it against two very different algorithms is itself the evidence that it tests the contract: if it depended on
either one's internals, one of the two would fail.

You already make this separation in optimization. The formulation says *what* the optimal solution is; branch-and-bound,
cutting planes or enumeration say *how* to find it. That is why you can change solvers without rewriting the model, and
why a contract test runs unchanged against every solver that keeps the promise.

---

<a id="ch-mip-optimal"></a>

## Testing a single-objective mixed-integer program with optimality guaranteed

The contract of [What to test](#model-what-to-test) promises the best load there is, whenever the status is `OPTIMAL`. A
promise can only be tested through what it implies about an output, and each implication needs a
[test oracle](../appendix/glossary.md#test-oracle) to check it. Which oracle a test can use depends on what it knows
before it runs: the answer itself, a second way to compute the answer, or nothing about the answer at all.

<a id="mip-conditions"></a>

### What the contract implies

The promise of a mixed-integer program (MIP) solved to optimality implies the conditions below, sorted by what the test
knows:

| Oracle | What the test knows | Conditions it checks |
|---|---|---|
| [Known oracle](../appendix/glossary.md#known-oracle) | The expected answer, worked out before the run | The status and the objective value of an instance small enough to solve by hand. The status of an instance of any size, from its committed pallets alone. |
| [Pseudo-oracle](../appendix/glossary.md#pseudo-oracle) | A second, independent way to compute the answer | The status and the objective value agree with those of enumeration. |
| [Unknown oracle](../appendix/glossary.md#unknown-oracle) | Nothing about the answer | `picked` respects both capacities and the committed pallets. The objective value and the totals match `picked`. [Metamorphic relations](../appendix/glossary.md#metamorphic-relation) between runs hold. |

The status of a large instance is known in advance only because of this model: every pallet weighs something and takes
room, so the committed pallets alone are the lightest and smallest load allowed, and the instance is infeasible exactly
when they exceed a capacity. For a MIP in general, deciding feasibility can be as hard as solving it.

The literature on the [oracle problem](../appendix/glossary.md#oracle-problem) sorts oracles by mechanism rather than by
what a test knows, so its terms do not map one to one onto these three: a known oracle is its
[specified oracle](../appendix/glossary.md#specified-oracle), and it counts both pseudo-oracles and metamorphic
relations as [derived oracles](../appendix/glossary.md#derived-oracle). It also names an
[implicit oracle](../appendix/glossary.md#implicit-oracle), a failure wrong in any program: a crash, and a hang once the
test sets a time limit that turns it into a failure.

[Figure: the reach of each oracle](#fig-oracle-classes) shows why a suite needs all three.

<a id="fig-oracle-classes"></a>

**Figure: the reach of each oracle**

<p align="center">
  <img src="assets/mip-optimal-oracle-classes.svg" width="760"
       alt="A horizontal axis of instance size, from tiny to large, with three bands. Hand-calculated optimal values,
the known oracle, reach only tiny instances. Enumeration, the pseudo-oracle, reaches small ones. Output relations, the
unknown oracle, reach every size, but check only conditions a correct output must meet">
</p>

> [!NOTE]
> The unknown oracle reaches any size because it never establishes optimality: a load that meets every condition can
> still leave revenue behind.

<a id="mip-known-oracle"></a>

### Known oracle

The simplest oracle is a person. In the example instance of [A cargo model example](#model-cargo), chocolate fits at
most once by weight and water at most once by volume, so each $x_i \in \{0, 1\}$ and there are $2 \times 2 = 4$
candidate loads, few enough to list:

| $x_A$ | $x_B$ | Weight (≤ 2) | Volume (≤ 2) | Revenue | Feasible? |
|:---:|:---:|:---:|:---:|:---:|---|
| 0 | 0 | 0 | 0 | 0 | yes |
| 1 | 0 | 2 | 1 | 10 | yes |
| 0 | 1 | 1 | 2 | 6 | yes |
| 1 | 1 | 3 | 3 | 16 | no, both capacities exceeded |

The best feasible load is $x_A = 1$, $x_B = 0$, worth a revenue of 10. Nobody needed a solver to produce that answer, so
it can serve as the expected value of a test:

<a id="pseudo-two-pallet-test"></a>

**Pseudocode: two-pallet test**

```
// pseudocode: two-pallet-test
a = item(name="A", weight=2, volume=1, revenue=10)
b = item(name="B", weight=1, volume=2, revenue=6)

result = solve([a, b], weight_capacity=2, volume_capacity=2)

expect result.status == OPTIMAL
expect result.objective_value == 10
```

The price of a human oracle grows fast. The capacities allow at most $m_i = \lfloor \min(W / w_i, V / v_i) \rfloor$
pallets of product $i$, so the candidate loads number $\prod_{i \in I} (m_i - l_i + 1)$: 4 for this instance, but
$4^{30} \approx 1.2 \times 10^{18}$ for 30 products that each fit up to 3 times. A person can only be the oracle at
teaching scale.

The harder question is *which* instances to write. Small instances picked at random tend to cover whatever comes to mind
first, which is usually the ordinary case. Bugs, however, cluster at the edges: an empty catalogue, a capacity of
exactly zero, two products that tie. Two standard techniques find the edges:

- **[Equivalence partitioning](../appendix/glossary.md#equivalence-partitioning)** splits the input space into classes
  expected to behave the same way, then tests one instance per class.
- **[Boundary value analysis](../appendix/glossary.md#boundary-value-analysis)** adds instances exactly on the border
  between two classes, where behavior changes character.

If you have done sensitivity analysis, you have seen this structure. As you vary a right-hand side, the optimal basis
stays the same over a range, then changes at a breakpoint. The ranges are equivalence classes; the breakpoints are
boundary values. You would never probe sensitivity only in the middle of each range, and the same holds for tests.
Applied to the cargo model, the two techniques produce the situations below, from the simplest to the most involved:

| # | Situation | Expected behavior |
|:---:|---|---|
| 1 | No products at all | Nothing to load: `OPTIMAL`, an empty load worth zero. |
| 2 | Committed cargo exceeds the payload | The committed pallets alone weigh more than the aircraft may carry: `INFEASIBLE`. |
| 3 | Committed cargo exceeds the hold | The mirror of situation 2, for volume. |
| 4 | Committed cargo fits exactly | The boundary between 2–3 and the rest: the committed load is the only feasible one. |
| 5 | Nothing fits on its own | Every product exceeds a capacity on its own; the empty load is still feasible, worth zero. |
| 6 | Unique optimum | One product dominates the other; the basic case. |
| 7 | Only the payload capacity binds | The optimum exhausts the payload and leaves volume unused. |
| 8 | Only the hold capacity binds | The mirror of situation 7. |
| 9 | Both capacities bind at once | The optimum exhausts both capacities. |
| 10 | Several optimal loads | Two interchangeable products tie; only the revenue is asserted, never which product was picked. |
| 11 | Several pallets of one product | The optimum loads a product more than once: quantities are integers, not 0/1 choices. |
| 12 | One product too heavy to load | A product that exceeds the payload on its own is left behind without disturbing the rest of the load. |

Read situations 2 and 3 against 4 and 5. All four leave the aircraft carrying the committed load and nothing more, and
only two of them are infeasible. That distinction is exactly what a boundary is for.
[Pseudocode: committed mail test](#pseudo-committed-mail-test) writes situation 2: two pallets of mail are committed,
one tonne each, and the aircraft may carry one tonne.

<a id="pseudo-committed-mail-test"></a>

**Pseudocode: committed mail test**

```
// pseudocode: committed-mail-test
m = item(name="M", weight=1, volume=1, revenue=4, min_quantity=2)

result = solve([m], weight_capacity=1, volume_capacity=5)

expect result.status == INFEASIBLE
```

The expected status was derived without a solver: the mail weighs 2 tonnes, and the aircraft may carry 1. The test does
not assert the load or the revenue, because the contract says those fields carry no meaning when the instance is
infeasible. The same sum gives the expected status of an instance of any size, so for this model the known oracle of the
status scales, while the known oracle of the optimal value stops at teaching scale.

<a id="mip-pseudo-oracle"></a>

### Pseudo-oracle

A [pseudo-oracle](../appendix/glossary.md#pseudo-oracle) is a second, independent implementation of the same contract.
[Differential testing](../appendix/glossary.md#differential-testing) runs both on the same inputs and compares their
outputs. For small instances, enumeration makes a good pseudo-oracle: it is slow, but correct by inspection. A MIP
solver such as Gurobi is very unlikely to compute a wrong optimum for the model it was given; the realistic risk is that
the code builds a different model from the one on paper, and a disagreement with enumeration points at that.

This is the disciplined version of a sanity check most modelers already run by hand, comparing a new model with brute
force on a toy case. Three details turn that habit into a reliable test:

1. **Generate many instances instead of picking a few.** Hundreds of small random instances explore corners that nobody
   would think to write by hand, including infeasible ones whenever the generator commits more cargo than the aircraft
   can carry.
2. **Fix the [random seed](../appendix/glossary.md#random-seed).** The same inputs must always produce the same outputs,
   as in a controlled experiment. A failure that vanishes on the retry cannot be investigated, so the test must also
   report the instance that failed.
3. **Compare only what the contract promises.** The status and the objective value, never `picked`: when several loads
   tie, the contract allows the two implementations to return different ones.

<a id="pseudo-differential-sweep"></a>

**Pseudocode: differential sweep**

```
// pseudocode: differential-sweep
rng = random_generator(seed=20260908)

repeat 200 times:
    items = a list of rng.integer(1, 4) items, each with
                weight  = rng.integer(1, 5),  volume       = rng.integer(1, 5),
                revenue = rng.integer(0, 20), min_quantity = rng.integer(0, 2)
    weight_capacity = rng.integer(0, 8)
    volume_capacity = rng.integer(0, 8)

    reference = enumeration_solver().solve(items, weight_capacity, volume_capacity)
    candidate = mip_solver().solve(items, weight_capacity, volume_capacity)

    expect candidate.status == reference.status
    if reference.status == OPTIMAL:
        expect candidate.objective_value == reference.objective_value
```

Weights and volumes start at 1, so no product fits more than 8 times, and enumeration checks at most $9^4 = 6561$ loads.
The reference stays cheap.

What does this catch that the known oracle does not? Suppose the code mistakenly uses each product's volume in the
weight constraint. Some of the twelve situations catch that mistake and some do not, because they were chosen to cover
the contract, not this particular error. A sweep over 200 generated instances is far more likely to hit one that exposes
it. Neither guarantees detection; the difference is how reliably each one finds a mistake nobody anticipated.

- **The reference must stay tractable.** Differential testing against enumeration lives in the same small-instance
  regime as the known oracle. It broadens coverage within that regime; it does not reach the large instances.
- **The two implementations must be independent.** If both share the same misunderstanding, say both treat every product
  as a 0/1 choice, they agree with each other and are both wrong.

<a id="mip-unknown-oracle"></a>

### Unknown oracle

The known oracle and the pseudo-oracle both stop at small instances, and the instances that matter in practice, a real
booking list on a real aircraft, are far beyond them. For such an instance a test knows nothing about the answer. It
still knows what every correct answer must satisfy.

**Checking is cheaper than solving.** Proving a load optimal is expensive; checking that it is feasible and reported
correctly takes one pass over the products. [Pseudocode: load checks](#pseudo-load-checks) applies after every solve
that returns `OPTIMAL`, whatever the instance.

<a id="pseudo-load-checks"></a>

**Pseudocode: load checks**

```
// pseudocode: load-checks
private expect_valid_load(items, weight_capacity, volume_capacity, result)
    for each item in items:
        expect result.picked[item.name] is a whole number, "pallet split"
        expect result.picked[item.name] >= item.min_quantity, "committed pallets left behind"
    expect result.total_weight == sum of item.weight × result.picked[item.name], "weight misreported"
    expect result.total_volume == sum of item.volume × result.picked[item.name], "volume misreported"
    expect result.objective_value == sum of item.revenue × result.picked[item.name], "revenue misreported"
    expect result.total_weight <= weight_capacity, "payload exceeded"
    expect result.total_volume <= volume_capacity, "hold exceeded"
```

The helper holds logic, which [No logic in tests](#no-logic-in-tests) warns against. The warning is about a test that
repeats the implementation; these sums do not: the pipeline searches for a load, and the helper only adds one up. On its
own, it does not certify optimality: a feasible load can leave revenue behind.

**Metamorphic relations.** A [metamorphic relation](../appendix/glossary.md#metamorphic-relation) is a relation that
must hold between the outputs of two related runs, even when neither output is known. The recipe has three steps:

1. Take an instance, any instance.
2. Transform it in a way whose effect on the optimum you can prove.
3. Solve both versions and check that the relation holds.

You already prove relations like these as theorems. Relaxing a constraint cannot make the optimal value worse, the same
reasoning that makes an LP relaxation a valid bound. A metamorphic relation turns such a theorem into a test, as
[Figure: a metamorphic relation](#fig-metamorphic-relation) shows. For the cargo model, four hold on every feasible
instance:

<a id="fig-metamorphic-relation"></a>

**Figure: a metamorphic relation**

<p align="center">
  <img src="assets/mip-optimal-metamorphic-relation.svg" width="720"
       alt="An instance and a transformed copy with a larger payload capacity. Both go through the pipeline, and both
optimal revenues are unknown, shown as question marks. A green check between them tests only that the second is at least
the first">
</p>

| Transformation | Relation on the optimal revenue | Why it holds |
|---|---|---|
| Add a product that need not fly | Never decreases | Every previous load is still available, with the new product at zero. |
| Raise the payload or the hold capacity | Never decreases | Relaxing a constraint only enlarges the feasible region. |
| Commit more pallets of a product | Never increases | Tightening a constraint only shrinks the feasible region. |
| Multiply every revenue by $k > 0$ | Scales by exactly $k$ | The feasible region is unchanged; only the objective is rescaled. |

None of the four compares `picked`. A transformation can turn a near-tie into an exact tie, and the contract never
promised which load wins among equals. [Pseudocode: capacity relation test](#pseudo-capacity-relation-test) writes the
second relation:

<a id="pseudo-capacity-relation-test"></a>

**Pseudocode: capacity relation test**

```
// pseudocode: capacity-relation-test
a = item(name="A", weight=2, volume=1, revenue=10)
b = item(name="B", weight=1, volume=2, revenue=6)
c = item(name="C", weight=3, volume=1, revenue=14)

before = solve([a, b, c], weight_capacity=5, volume_capacity=4)
after  = solve([a, b, c], weight_capacity=8, volume_capacity=4)

expect after.objective_value >= before.objective_value
```

The optimum of the first instance happens to be 26 (two pallets of A and one of B), but the test never needs to know
that. The same lines work unchanged on a booking list of four thousand products, which is what makes the unknown oracle
the part of the suite that scales.

### Check yourself

1. Two loads tie at 5 revenue. Pipeline A returns one of them and pipeline B the other. Which contract test should fail?
2. An instance has 4,000 products, and its committed pallets weigh 1 tonne more than the aircraft may carry. What status
   must the result carry, and did you need a solver to know?
3. A broken pipeline always returns `OPTIMAL` with an empty load worth 0. Which of the four relations does it violate?
4. Why is the random seed of the differential sweep fixed rather than drawn fresh on every run?

<details>
<summary>Answers</summary>

1. None. Clause 2 of the contract allows any optimal load, so a contract test asserts only the revenue.
2. `INFEASIBLE`, known from one sum over the committed pallets, with no solver. That shortcut belongs to this model.
3. None of them: 0 ≥ 0, 0 ≤ 0 and 0 = k × 0. The load checks catch it when pallets are committed, and otherwise only the
   known oracle and the pseudo-oracle do.
4. So that a failure reproduces on the next run and can be investigated.

</details>

### Further reading

- Barr et al., ["The Oracle Problem in Software Testing: A Survey"](https://ieeexplore.ieee.org/document/6963470), IEEE
  Transactions on Software Engineering, 2015: the survey that names the oracle problem and sorts oracles by mechanism.
- Maurício Aniche, *Effective Software Testing: A developer's guide*, Manning, 2022: equivalence partitioning and
  boundary analysis in depth, under the name specification-based testing.
- T. Y. Chen et al., "Metamorphic Testing: A Review of Challenges and Opportunities," *ACM Computing Surveys*, 2018: a
  broad review of the technique and where it has been applied.
- William M. McKeeman, "Differential Testing for Software," *Digital Technical Journal*, 1998: the paper that named the
  technique.

> **Practice it**
>
> - Python: Single-objective MIP with optimality exercise (coming soon)
> - Java: Single-objective MIP with optimality exercise (coming soon)

---

<a id="ch-multi-optimal"></a>

## Testing a multi-objective mixed-integer program with optimality guaranteed

The contract of [What to test](#model-what-to-test) lets the pipeline return any of several loads that tie for the best
revenue. For a test that is a convenience. For the airline it is a gap: two loads can carry the same revenue and differ
in everything else, and the pipeline picks one for reasons nobody chose. Which one should the user receive?

The airline's answer is the lightest, because weight burns fuel. That is the
[second objective](../appendix/running-example.md#ev-second-objective): among the loads with the best revenue, minimize
the total weight. Optimizing objectives in a fixed order like this is
[lexicographic optimization](../appendix/glossary.md#lexicographic-optimization).

### The contract

The `result` keeps its five fields. What they promise changes:

- `OPTIMAL` now means that both levels were proven: no load earns more revenue, and no load with that revenue weighs
  less.
- `total_weight` is the second objective: the minimum weight among the loads with the best revenue.
- Clause 2 narrows: any one of several loads may be returned only when they tie on both revenue and weight.

The oracles of [Testing a single-objective mixed-integer program with optimality guaranteed](#ch-mip-optimal) apply to
the revenue unchanged, because the first level is that model. What follows is what each one adds for the weight.

### What each oracle adds

**Known oracle.** A tie now has one right answer, so a test can assert which load comes back.
[Pseudocode: lightest tie test](#pseudo-lightest-tie-test) offers two ways to earn 6: one pallet of A, weighing 3
tonnes, or two pallets of B, weighing 2.

<a id="pseudo-lightest-tie-test"></a>

**Pseudocode: lightest tie test**

```
// pseudocode: lightest-tie-test
a = item(name="A", weight=3, volume=1, revenue=6)
b = item(name="B", weight=1, volume=2, revenue=3)

result = solve([a, b], weight_capacity=3, volume_capacity=4)

expect result.status == OPTIMAL
expect result.objective_value == 6
expect result.total_weight == 2
expect result.picked["B"] == 2
```

Three pallets of B would earn 9 but need 6 m³, and A with a pallet of B would weigh 4 tonnes, so 6 is the best revenue.
Under the single-objective contract, `picked` could not be asserted; here the second objective decides it.

**Pseudo-oracle.** Enumeration compares loads by revenue first and weight second, and the differential sweep adds one
comparison: `candidate.total_weight == reference.total_weight` whenever the status is `OPTIMAL`.

**Unknown oracle.** The load checks apply unchanged. The relations of the single-objective chapter still hold for the
revenue, but not all of them say anything about the weight: adding a product can raise the revenue and, with it, the
weight. Three relations do:

| Relation | Why it holds |
|---|---|
| The revenue equals the one of the single-objective pipeline on the same instance | The first level is the single-objective model. |
| The weight never exceeds that of the single-objective pipeline's load | That load has the best revenue, and the second level picks the lightest among such loads. |
| Multiplying every revenue by $k > 0$ scales the revenue by $k$ and leaves the weight unchanged | The scaling keeps every tie, so the same loads have the best revenue. |

[Pseudocode: lexicographic relation test](#pseudo-lexicographic-relation-test) checks the first two, where
`single_objective_solver()` is the pipeline of the single-objective chapter.

<a id="pseudo-lexicographic-relation-test"></a>

**Pseudocode: lexicographic relation test**

```
// pseudocode: lexicographic-relation-test
single = single_objective_solver().solve(items, weight_capacity, volume_capacity)
both   = solve(items, weight_capacity, volume_capacity)

expect both.objective_value == single.objective_value
expect both.total_weight <= single.total_weight
```

Like every unknown oracle, it runs on any `items`, whatever their size.

### Check yourself

1. In the lightest tie test, why may the test assert `picked["B"] == 2` when the single-objective tests never assert
   `picked`?
2. Adding a product that need not fly never lowers the revenue. Does it ever lower the weight?
3. A pipeline returns the single-objective load unchanged, ignoring the second objective. Which relation of the table
   catches it?

<details>
<summary>Answers</summary>

1. The contract now decides between tied loads: only one load has the best revenue and the lowest weight.
2. It can. If the new product raises the revenue, the best loads change, and they may weigh less or more.
3. None of them on every instance: its revenue matches and its weight equals, rather than exceeds, the single-objective
   weight. The known oracle catches it, as the lightest tie test shows, and so does the pseudo-oracle.

</details>

### Further reading

- Matthias Ehrgott, *Multicriteria Optimization*, 2nd edition, Springer, 2005: lexicographic optimization among the
  other ways to combine objectives.

> **Practice it**
>
> - Python: Multi-objective MIP with optimality exercise (coming soon)
> - Java: Multi-objective MIP with optimality exercise (coming soon)

---

<a id="ch-mip-no-optimality"></a>

## Testing a single-objective mixed-integer program without optimality guaranteed

A mixed-integer program (MIP) can take hours to solve to proven optimality once its instance grows, and a load planner
cannot wait hours before the aircraft closes. The pipeline has to answer in time, even when the best load has not been
proven best yet. It gives the solver a time limit and, when the limit is reached, returns the best load found so far,
the [incumbent](../appendix/glossary.md#incumbent). A test can no longer ask for the optimum. What can it still ask for?

### The contract

The solver knows more than its incumbent. Branch-and-bound also keeps a
[dual bound](../appendix/glossary.md#dual-bound): a value proven to be at least the optimal revenue. The contract adds
it to the `result` as a sixth field, `bound`, and `status` gains a value:

| `status` | `picked`, totals, `objective_value` | `bound` |
|---|---|---|
| `OPTIMAL` | A load proven the best | Equals `objective_value` |
| `FEASIBLE` | A feasible load, perhaps not the best | At least `objective_value` |
| `INFEASIBLE` | No meaning | No meaning |

`INFEASIBLE` means proven infeasible. The pipeline checks the committed pallets before the solver starts and, when they
fit, hands them to the solver as its first incumbent: a result is then always either a feasible load or proven
infeasibility, and no status such as "no load found yet" exists. The distance between the two is the
[optimality gap](../appendix/glossary.md#optimality-gap), `(bound − objective_value) / bound` for a positive bound.

### What survives

- **Unchanged:** the load checks of the [unknown oracle](#mip-unknown-oracle), which never needed the optimum, and the
  expected status of the [known oracle](#mip-known-oracle), since the committed pallets decide it at any size.
- **When `status` is `OPTIMAL`:** every oracle of the single-objective chapter, as before. A test on an instance small
  enough to finish well inside the time limit may expect `OPTIMAL`.
- **Otherwise, weakened into bounds:** `objective_value ≤ bound`, and the gap the pipeline reports equals the one
  computed from those two fields. On small instances, enumeration supplies the optimum between them, as
  [Figure: an incumbent and its bound](#fig-bounds) shows.

In [Pseudocode: time-limit bound test](#pseudo-time-limit-bound-test), `mip_solver(time_limit=…)` is the pipeline with
its solver stopped at the given limit.

<a id="fig-bounds"></a>

**Figure: an incumbent and its bound**

<p align="center">
  <img src="assets/mip-no-optimality-bounds.svg" width="720"
       alt="A number line of revenue. On the left, the incumbent's objective value, the revenue of the load returned. On
the right, the proven bound. Between them, the optimum, unknown on a large instance, and the optimality gap spanning the
distance from incumbent to bound">
</p>

<a id="pseudo-time-limit-bound-test"></a>

**Pseudocode: time-limit bound test**

```
// pseudocode: time-limit-bound-test
reference = enumeration_solver().solve(items, weight_capacity, volume_capacity)
candidate = mip_solver(time_limit=1 second).solve(items, weight_capacity, volume_capacity)

expect (candidate.status == INFEASIBLE) == (reference.status == INFEASIBLE)
if reference.status == OPTIMAL:
    expect candidate.objective_value <= reference.objective_value
    expect reference.objective_value <= candidate.bound
```

**The relations do not survive.** Metamorphic relations are theorems about the optimum, and an incumbent is not the
optimum. A [heuristic](../appendix/glossary.md#heuristic) with no bound at all is the extreme case: take a greedy one
that sorts products by revenue per tonne and loads each while it fits.

<a id="pseudo-greedy-relation-test"></a>

**Pseudocode: greedy relation test**

```
// pseudocode: greedy-relation-test
a = item(name="A", weight=3, volume=1, revenue=10)
d = item(name="D", weight=2, volume=1, revenue=7)

before = greedy_solver().solve([a],    weight_capacity=3, volume_capacity=10)   // loads A: 10
after  = greedy_solver().solve([a, d], weight_capacity=3, volume_capacity=10)   // loads D first, then nothing fits: 7

expect after.objective_value >= before.objective_value                          // fails: 7 < 10
```

D earns 3.5 per tonne and A 3.3, so the greedy method loads D, and the tonne left takes nothing. The optimum with D
available is still 10, one pallet of A. The heuristic dropped to 7 while behaving exactly as designed, so the failure is
in the test, which asked an incumbent for a theorem about optima.

### Where this stops working

> [!WARNING]
> A bound test passes whenever the bound is loose, so it shows far less than the optimality tests it replaces.

- **A loose or wrong bound passes.** `objective_value ≤ bound` holds for any bound large enough, including a wrong one.
- **A large instance's bound cannot be checked independently.** Enumeration confirms it only on small instances.
- **A poor load passes.** The committed pallets alone satisfy every weakened check. Without an approximation guarantee
  there is no floor to assert, so solution quality is better tracked as a benchmark over time, the average gap on a
  fixed set of instances, than as a pass/fail test.

### Check yourself

1. A solver reaches its 60-second limit and returns `FEASIBLE` with a 3% gap. Should the exact-value assertion of
   situation 6 apply to it?
2. On the same small instance, the pipeline reports 12 revenue and enumeration reports 10. Is that a bug?
3. Why does the pipeline hand the committed pallets to the solver before it starts?

<details>
<summary>Answers</summary>

1. No. It applies only when the status is `OPTIMAL`; for `FEASIBLE`, assert the load checks and the bounds.
2. Yes. No feasible load beats the optimum, so either the load is infeasible or its revenue is misreported, and the load
   checks show which.
3. So that the solver always has a feasible incumbent when the committed pallets fit: the result is then either a
   feasible load or proven infeasibility.

</details>

### Further reading

- Laurence A. Wolsey, *Integer Programming*, 2nd edition, Wiley, 2020: primal and dual bounds, and how branch-and-bound
  closes the gap between them.
- David P. Williamson and David B. Shmoys, *The Design of Approximation Algorithms*, Cambridge University Press, 2011:
  where approximation guarantees, the floor a heuristic test can assert, come from.

> **Practice it**
>
> - Python: Single-objective MIP without optimality exercise (coming soon)
> - Java: Single-objective MIP without optimality exercise (coming soon)

---

<a id="ch-multi-no-optimality"></a>

## Testing a multi-objective mixed-integer program without optimality guaranteed

The second objective picks the lightest load among those with the best revenue. Under a time limit, the best revenue
itself may be unproven, and the second level has to choose from loads whose revenue is only as good as the first level
managed. Each level can stop early, so each needs its own promise.

### The contract

The `result` of the multi-objective chapter reports each level separately:

- `revenue_status` and `revenue_bound`: whether the revenue was proven the best, and a proven upper bound on it.
- `weight_status` and `weight_bound`: whether the weight was proven the lowest, and a proven lower bound on it.

`objective_value` and `total_weight` stay the revenue and the weight of the load returned. Internally, the second level
searches the loads that earn at least the revenue the first level found. The load returned may earn more, and
`weight_bound` remains valid for it: a bound over a larger set of loads also holds over the smaller one.

### What survives

- **Unchanged:** the load checks and the expected status from the committed pallets.
- **Always:** `objective_value ≤ revenue_bound` and `total_weight ≥ weight_bound`.
- **When `revenue_status` is `OPTIMAL`:** the revenue relations and oracles of the single-objective chapter.
- **Only when both statuses are `OPTIMAL`:** the claim that the load is the lightest among the loads with the best
  revenue, and with it every oracle of the multi-objective chapter. A proven revenue is not enough: a second level
  stopped early can return a heavier load than the lightest.

<a id="pseudo-level-bounds-test"></a>

**Pseudocode: level bounds test**

```
// pseudocode: level-bounds-test
result = mip_solver(time_limit=1 second).solve(items, weight_capacity, volume_capacity)

expect result.objective_value <= result.revenue_bound
expect result.total_weight >= result.weight_bound
if result.revenue_status == OPTIMAL and result.weight_status == OPTIMAL:
    expect result.objective_value == result.revenue_bound
    expect result.total_weight == result.weight_bound
```

The limits of [Where this stops working](#where-this-stops-working) apply to each level: a loose bound passes, and a
large instance's bounds cannot be checked independently.

### Check yourself

1. `revenue_status` is `OPTIMAL` and `weight_status` is `FEASIBLE`. May a test assert that the revenue equals the
   single-objective optimum? That the weight is the lowest possible?
2. Why is `weight_bound` still valid when the load returned earns more than the first level found?
3. Which assertion of the lightest tie test survives when both levels stop at `FEASIBLE`?

<details>
<summary>Answers</summary>

1. The revenue, yes: it was proven. The weight, no: assert only `total_weight ≥ weight_bound`.
2. The bound holds for every load earning at least the first level's revenue, and the loads earning at least the
   returned revenue are among them.
3. Only the feasibility half: the load checks and the two bounds. The revenue of 6, the weight of 2 and the two pallets
   of B all assume proven levels.

</details>

> **Practice it**
>
> - Python: Multi-objective MIP without optimality exercise (coming soon)
> - Java: Multi-objective MIP without optimality exercise (coming soon)

---

<a id="ch-dss-testing"></a>

## Testing a decision-support system

A decision-support system promises its users a decision, not an algorithm: behind its [interface](#ch-interface),
the load may come from enumeration, a heuristic or a solver, and the choice may change. Its tests therefore see only
what the interface returns.

A decision-support system is more than its optimization model. Data arrives from other systems, business rules turn it
into model parameters, the model computes a decision, and the decision flows back to the people and systems that act
on it. Each of these parts can break. For most of them, the expected output is cheap to write down: you know what a
data check or a business rule should return before running it. The model is the exception, because its expected
output is the very thing it exists to compute. The chapter will map each part of the system to the kind of test that
fits it.

The chapter will also sort the oracles of the model chapters by what survives behind an interface. The contract,
the load checks, the known oracle, the metamorphic relations and differential testing only need the system's output.
A solver's bounds and gaps need the solver itself.

---

<a id="ch-conclusion"></a>

## Conclusion

A test is an experiment with an expected answer, and each chapter of this section is a way of obtaining that answer, up
to the case where the answer is the very thing the model computes.

- **Test the promise, not the mechanism** ([Interface vs implementation](#ch-interface)). What a unit does outlives how
  it does it.
- **A unit test is a small experiment** ([Unit testing](#ch-unit-testing)). One behavior, fixed inputs and a stated
  prediction.
- **Nothing tests the test** ([Writing good tests](#ch-clear-tests)). A test must be obviously correct at a glance.
- **Red first shows the cause** ([Test-driven development](#ch-tdd)). A test that failed before the code existed shows
  that the code made it pass.
- **Record the calls you cannot observe** ([Mocks](#ch-mocks)). When a behavior is a call to another system, a mock
  keeps the record the test checks.
- **Keep what only your program uses real** ([Integration testing](#ch-integration)). Mock what others observe, and let
  the real files and databases show where units disagree.
- **Test the pipeline through its contract** ([Testing an optimization model](#ch-model-testing)). The status, the load
  and its totals are the promise; the algorithm behind them is not.
- **Sort the checks by what the test knows**
  ([Testing a single-objective mixed-integer program with optimality guaranteed](#ch-mip-optimal)). A known answer, a
  second implementation, or only conditions every answer meets.
- **A second objective settles ties**
  ([Testing a multi-objective mixed-integer program with optimality guaranteed](#ch-multi-optimal)). Once the lightest
  load must win, a test may assert which load comes back.
- **Without optimality, checking is cheaper than solving**
  ([Testing a single-objective mixed-integer program without optimality guaranteed](#ch-mip-no-optimality)). The cheap
  checks survive, and the rest weaken into bounds.
- **Each level keeps its own promise**
  ([Testing a multi-objective mixed-integer program without optimality guaranteed](#ch-multi-no-optimality)). A claim
  about the weight needs both levels proven.
- **Behind an interface, only the output counts** ([Testing a decision-support system](#ch-dss-testing)). The techniques
  that read the output survive a hidden algorithm; the ones that need the solver do not.

With the system tested, the next section puts it in front of its users.

---

[← Book contents](../../README.md) · [Next section: 06 Deploying decision-support software →](../06-deployment/README.md)
