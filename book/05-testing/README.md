# Section 05 — Testing decision-support software

## Introduction

Testing matters in the [software development
lifecycle](../appendix/glossary.md#software-development-lifecycle) because it serves both abilities
a team needs: [learning quickly](../03-software-development-lifecycle/README.md#ch-learning) and
[adapting quickly](../03-software-development-lifecycle/README.md#ch-adapting). For learning, a test
is how the scientific method reaches code: it writes a hypothesis about what the code must do in a
form anyone can check, and running it is the experiment that confirms or refutes it. For adapting,
testing is one of two pillars. Design is the other: it keeps each change small and confined to one
part, as [the design section](../04-design/README.md) shows. An [automated test
suite](../appendix/glossary.md#test-suite) then shows, on every change, that everything that worked
before still works. With both pillars in place, a team can change working code as often as the
business asks. Decision-support software adds one difficulty ordinary software rarely poses: the
correct answer of its optimization model is hard to know in advance.

### Verification vs validation

A model reaches its users through two translations: a business problem becomes a mathematical model,
and the mathematical model becomes code. [Validation](../appendix/glossary.md#validation) checks the
first translation and asks *are we building the right model?*, a business question.
[Verification](../appendix/glossary.md#verification) checks the second and asks *are we building the
model right?*, a software question: does the code do what the mathematical model says? [Figure:
verification and validation](#fig-verification-validation) places each question on its translation.

<a id="fig-verification-validation"></a>

**Figure: verification and validation**

<p align="center">
  <img src="assets/intro-verification-validation.svg" width="760"
       alt="A chain of three boxes joined by arrows labeled translation: a business problem, a
decision to support; a mathematical model, max c transpose x subject to A x at most b; and code,
model.py or Model.java. A muted brace under the first translation reads validation, are we building
the right model, a business question. An emphasized brace under the second translation reads
verification, are we building the model right, a software question, this section">
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

Functional tests come in three levels, told apart by how much of the program each one runs. A [unit
test](../appendix/glossary.md#unit-test) checks one small piece of code in isolation. An
[integration test](../appendix/glossary.md#integration-test) combines several units and checks that
they work together. An [end-to-end test](../appendix/glossary.md#end-to-end-test) runs the whole
application in a real-world scenario, the way its users would.

<a id="fig-test-pyramid"></a>

**Figure: test pyramid**

<p align="center">
  <img src="assets/unit-test-pyramid.svg" width="640"
       alt="A pyramid of three levels of functional tests: unit tests at the wide base, integration
tests in the middle, end-to-end tests at the narrow top. Cost per test rises toward the top, speed
rises toward the base, and the base holds the most tests">
</p>

Take a small program that reads a user's records, computes their income and tax, and reports the
result. [Figure: test levels](#fig-test-levels) draws it once per level and colors what a single
test of that level runs.

<a id="fig-test-levels"></a>

**Figure: test levels**

<p align="center">
  <img src="assets/unit-test-levels.svg" width="780"
       alt="The same example program drawn three times, as six functions in three modules with data
flowing downward: read_user and read_db in reading data, calculate_income and calculate_tax in
business logic, create_report and display_report in processing results. Unit tests: each function is
highlighted on its own. Integration tests: two groups are highlighted, reading data, and business
logic together with processing results. End-to-end tests: the whole program is highlighted as one">
</p>

As [Figure: test pyramid](#fig-test-pyramid) shows, each step up runs more of the program, so each
test costs more to write and runs slower. A healthy suite holds many unit tests, fewer integration
tests and a handful of end-to-end tests.

### Out of scope

- **Performance and scale.** No chapter tests how fast a solver is or how large an instance it
  handles.
- **Input validation.** Items are never checked for nonsense values such as a negative weight: every
  infeasible instance in this section comes from the capacities, never from a malformed item.
- **Several objectives.** Models with more than one objective are not covered yet.
- **Validation.** Whether a model captures the right decision is a business question, not covered in
  this book.
- **Reviewing a formulation.** Checking the mathematics of a model on paper is not covered: the
  tests here check the output of solving it.

[Interface vs implementation](#ch-interface) separates what a unit promises from how it keeps the
promise, and every later chapter tests the promise. [Unit testing](#ch-unit-testing), [Writing good
tests](#ch-clear-tests) and [Test-driven development](#ch-tdd) test one unit on its own.
[Mocks](#ch-mocks) and [Integration testing](#ch-integration) take a test beyond the unit, to the
systems it calls and the files it reads. [Testing an optimization model](#ch-model-testing) then
meets the difficulty specific to decision-support software and sets up the contract. [Test
oracles](#ch-oracles) shows three ways to decide whether `run` kept it, and [Testing a mixed-integer
program without optimality guaranteed](#ch-mip-no-optimality) what remains of it when optimality is
not guaranteed. [Testing a decision-support system](#ch-dss-testing) applies them to the whole
system behind its interface. Read them in order: each chapter uses only what the chapters before it
defined.

<a id="ch-interface"></a>

## Interface vs implementation

Every unit of code has two parts. Its [interface](../appendix/glossary.md#interface) says what the
unit does: its name, the inputs it accepts, and the outputs and errors it returns. Programmers also
call it the signature, the application programming interface (API), the
[contract](../appendix/glossary.md#contract), or the
[abstraction](../appendix/glossary.md#abstraction). Its implementation is how the unit does it, and
everything in it is an [implementation detail](../appendix/glossary.md#implementation-detail). Any
code that calls the unit is one of its *clients*. Implementation details include any
[private](../appendix/glossary.md#public-and-private) method the unit calls, such as `is_finite` in
the figure: no client can call it, so it can change freely. [Figure: interface and
implementation](#fig-interface-implementation) marks the parts on the calculator's `add`.

<a id="fig-interface-implementation"></a>

**Figure: interface and implementation**

<p align="center">
  <img src="assets/interface-implementation.svg" width="780"
       alt="The pseudocode of add and its private helper is_finite, in one color with comments in
green, and three braces on the right. The first brace, in blue, marks the interface: the line public
add(a, b) returns number and the comments stating its promises (the sum, commutativity, identity, an
invalid-input error, an overflow error), labeled what the unit does, also called signature, API,
contract or abstraction, its comments are part of it, visible to every client. The second brace, in
orange, marks the implementation: the input checks that call is_finite, the sum, the overflow check
and the return, labeled how the unit does it, hidden from clients, one of many possible behind the
interface. The third brace, in orange, marks the private method is_finite(x), labeled also an
implementation detail, clients cannot call it">
</p>

Two design practices follow from the split. The interface states what the unit does and never how,
and the comments that state its promises belong to it as much as its first line does. The
implementation stays hidden from the clients, so it can change, or give way to a different
implementation, without any client noticing.

A wall socket shows the same split. [Figure: socket](#fig-socket) draws it: the socket is the
interface, a fixed shape that delivers a fixed voltage. Behind the wall, the power may come from a
gas plant, a wind farm or solar panels; that is the implementation, and the utility can change it at
any time. The lamp, the laptop and the phone are the clients, and they rely on the socket alone.
Telling the interface from the implementation is foundational knowledge, in
[design](../04-design/README.md) as much as in [testing](#ch-unit-testing).

<a id="fig-socket"></a>

**Figure: socket**

<p align="center">
  <img src="assets/interface-socket.svg" width="780"
       alt="The electricity service in three zones. Left, in orange, the implementation hidden
behind the wall: a gas plant, a wind farm and solar panels wired to one line. Middle, in blue, the
interface: a socket on the wall. Right, in green, the clients: a lamp, a laptop and a phone plugged
into the socket">
</p>

<a id="ch-unit-testing"></a>

## Unit testing

A unit test sits at the base of the pyramid: it checks one unit of code, such as a function, on its
own, and runs in milliseconds.

### What to test

An interface has one or more *behaviors*, and each one is something to test. The interface in
[Figure: interface and implementation](#fig-interface-implementation) promises five:

1. **The base case**, also called the [happy path](../appendix/glossary.md#happy-path):
   `add(3, 4) = 7`.
2. **Commutativity**: `add(3, 4) = add(4, 3)`.
3. **Identity**: `add(3, 0) = 3`.
4. **Invalid input**: `add("3", 4)` fails with an invalid-input error.
5. **Overflow**: adding the largest representable number to itself fails with an overflow error.

A behavior may need more than one case: identity holds for 3, and also for a negative number and a
very large one.

### How to write a unit test

A unit test's name says what it checks, in three parts: the unit, the behavior and case, and the
expected result. `test__add__given_two_numbers__returns_their_sum` tests `add`, given two ordinary
numbers, and expects their sum. When it fails, its name alone reports which behavior broke.

The body follows the [arrange, act, assert (AAA)](../appendix/glossary.md#arrange-act-assert)
pattern: *arrange* the objects and inputs the test needs, *act* by calling the unit once, and
*assert* that the result meets the expectation. In the pseudocode, `expect` makes the assertion: the
test fails if its condition is false.

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

A unit test is a scientific experiment in miniature, and it holds every part an experiment in a
laboratory holds. The table finds each part in [Pseudocode: add test](#pseudo-add-test).

| Part of the experiment | In Pseudocode: add test |
|---|---|
| Hypothesis | The name: `add`, given two numbers, returns their sum |
| Controlled conditions | *Arrange*: a new `Calculator` and the fixed inputs 1 and 2 |
| Intervention | *Act*: one call, `calculator.add(1, 2)` |
| Observation | `result`, the value the call returns |
| Prediction checked against the observation | *Assert*: `expect result == 3` |
| Conclusion | The test passes, and the evidence supports the hypothesis; or it fails, and refutes it |

The parts carry the principles of [the scientific
method](../03-software-development-lifecycle/README.md#ch-learning) with them. The hypothesis is
testable, because the assertion states it as an objective, measurable condition. The conditions are
controlled, because the test runs one unit on its own, with inputs it fixes itself, so a failure has
one cause: `add`. And the experiment is reproducible: anyone can run it again, on any machine, and
get the same result.

### Where to place the test

Test code lives apart from production code, in a folder tree that mirrors it, so each module's tests
sit at the same place in the tests tree as the module does in the source tree.

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

How do you know you tested every behavior? The starting point is [code
coverage](../appendix/glossary.md#code-coverage): a tool records which lines of the production code
the tests run, and reports the rest. [Pseudocode: add coverage](#pseudo-add-coverage) marks each
line of `add` for a suite that holds only the happy-path test.

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
> The pseudocode is illustrative: a coverage tool reports the same pattern for `add` written in a
> real language, over more lines.

The three lines that never run belong to the invalid-input and overflow behaviors. Add a test for
each, and every line runs: coverage reaches 100%. Now delete the commutativity test. Coverage stays
at 100%, because the happy-path test already runs every line the commutativity test runs. Coverage
points at lines no test runs; it cannot point at a behavior no test checks. Use it to find what is
missing, and use the list of behaviors to decide when you are done.

### Exercise: a calculator

The exercise lives in the practice repositories: test the calculator's `divide` the way this part
tested `add`.

> **Practice it**
>
> - Python: [Unit testing exercise](https://github.com/sefop/training-testing-python/tree/main/src/unit_tests_and_coverage)
> - Java: [Unit testing exercise](https://github.com/sefop/sefop-training-java/tree/main/src/main/java/unit_tests_and_coverage)

<a id="ch-clear-tests"></a>

## Writing good tests

[Unit testing](#ch-unit-testing) gave a test its structure and its name; the practices below tell a
good test from a bad one.

### Complete and concise

A test is *complete* when its body holds everything a reader needs to understand its result, and
*concise* when it holds nothing else. [Pseudocode: cluttered test](#pseudo-cluttered-test) fails
both ways: the constructor arguments play no part in addition, and the numbers that decide the
result hide inside helper functions.

<a id="pseudo-cluttered-test"></a>

**Pseudocode: cluttered test**

```
// pseudocode: cluttered-test
public test__add__given_two_numbers__returns_their_sum()
    calculator = Calculator(precision=10, rounding="half-even", log_file="calc.log")
    result = calculator.add(first_operand(), second_operand())
    expect result == 5
```

[Pseudocode: concise test](#pseudo-concise-test) keeps the numbers that matter in view and drops the
rest.

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

[Pseudocode: method test](#pseudo-method-test) checks three behaviors of `add` at once. When it
fails, its name cannot say which behavior broke, and the first failing `expect` stops the test, so
the ones after it go unchecked.

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

[Pseudocode: behavior tests](#pseudo-behavior-tests) splits it into one test per behavior, each
named for the behavior it checks. A name that needs the word "and" describes two behaviors, and
belongs to two tests.

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

Production code must handle any input, so it needs logic: loops, conditions, arithmetic. A test
handles a few chosen inputs, so it needs none, and each piece of logic it carries is a computation
its reader must run in their head. [Pseudocode: logic test](#pseudo-logic-test) loops over six pairs
of numbers and computes each expected value with `a + b`, the very operation `add` performs. The
test repeats the implementation instead of checking it.

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

[Pseudocode: concise test](#pseudo-concise-test) is straight-line code with a literal expected
value: a reader checks that 2 plus 3 is 5 at a glance.

### Clear failure messages

When a test fails, its failure message is often the first thing a reader sees, and sometimes the
only one. A good message states the inputs, the expected value and the actual value. So far,
`expect` has taken a condition; it also takes a message after a comma, which the test reports when
the condition is false. [Pseudocode: vague failure](#pseudo-vague-failure) reduces the comparison to
true or false before asserting it, so its failure reads only "expected true, got false".

<a id="pseudo-vague-failure"></a>

**Pseudocode: vague failure**

```
// pseudocode: vague-failure
public test__add__given_two_numbers__returns_their_sum()
    calculator = Calculator()
    result = calculator.add(2, 3)
    expect (result == 5) is true
```

[Pseudocode: clear failure](#pseudo-clear-failure) fails with "add(2, 3) returned 6, expected 5",
which points at the broken behavior before anyone opens the test.

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

Production code follows [don't repeat yourself (DRY)](../appendix/glossary.md#dont-repeat-yourself):
each piece of knowledge lives in one place, so a change is one edit. Test code follows [descriptive
and meaningful phrases (DAMP)](../appendix/glossary.md#descriptive-and-meaningful-phrases) instead:
a little repetition is welcome when it lets each test be read on its own. [Pseudocode: too-DRY
tests](#pseudo-too-dry-tests) shares its calculator and its numbers across the file, so to check
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

[Pseudocode: behavior tests](#pseudo-behavior-tests) repeats `calculator = Calculator()` and its
numbers in every test, and each test reads on its own.

### Further reading

- Titus Winters, Tom Manshreck and Hyrum Wright, *Software Engineering at Google*, O'Reilly, 2020,
  chapter 12, "Unit Testing": the source of these five practices, each shown on tests from a code
  base of Google's size.
- Vladimir Khorikov, *Unit Testing: Principles, Practices and Patterns*, Manning, 2020, chapter 3,
  "The anatomy of a unit test": the same ground from another angle, on one behavior per test, no
  branching in tests, and setup shared between tests.

<a id="ch-tdd"></a>

## Test-driven development

[Test-driven development (TDD)](../appendix/glossary.md#test-driven-development) writes each test
before the code it checks. In the terms of the scientific experiment in [Unit
testing](#ch-unit-testing), it states the hypothesis before it builds the experiment: the test says
what the code must do while that code does not exist yet.

### The cycle: red, green, refactor

TDD advances in short cycles of three steps, named after the colors a test tool shows:

1. **Red.** Write one test for the next requirement, run it, and watch it fail.
2. **Green.** Write the minimum code that makes it pass.
3. **Refactor.** Improve the code while every test keeps passing. Changing code without changing
   what it does is called [refactoring](../appendix/glossary.md#refactoring).

Then the next requirement starts the next cycle. [Figure: TDD cycle](#fig-tdd-cycle) draws the loop.

<a id="fig-tdd-cycle"></a>

**Figure: TDD cycle**

<p align="center">
  <img src="assets/tdd-cycle.svg" width="520"
       alt="A loop of three steps. Red: write a failing test. Green: make it pass with the minimum
code. Refactor: improve the code, tests still pass. An arrow labeled next requirement leads from
refactor back to red">
</p>

### Why each step matters

**Red shows that the test can fail.** A test that has never failed has never been shown to test
anything: it may check the wrong value, or not run at all. Watching it fail first is the evidence
that it can tell working code from missing code.

**Red, then green, shows causality.** The test failed, one change was made, and now the test passes:
that change is why it passes. This is the causality principle of [the scientific
method](../03-software-development-lifecycle/README.md#ch-learning) applied to code: change one
thing at a time, so the result shows what caused it. A test written after the code passes on its
first run, and cannot tell whether the code made it pass or whether it would have passed anyway.

**Green with the minimum code keeps every line accountable.** Each line of production code exists
because a test demanded it, so no line goes untested and no behavior is built that nobody asked for.

**Refactor is safe because the tests check the interface.** The tests pin down what the code does,
never how, as [Interface vs implementation](#ch-interface) set out. The code can change shape
underneath them, and a test that turns red means a promise broke, not that the code merely moved.

### A linear expression example

A linear expression has the form $a_0 + a_1 x_1 + \dots + a_n x_n$: a scalar $a_0$, and a
coefficient $a_i$ for each variable $x_i$. The class `LinearExpression` represents one. The scalar
and the coefficients are floating-point numbers, and each variable is identified by its name, a
string. For example:

| Expression | Scalar | Coefficients |
|---|---|---|
| $0$ | 0.0 | none |
| $1 + 2x$ | 1.0 | `"x"`: 2.0 |
| $-1 - x + 2y$ | -1.0 | `"x"`: -1.0, `"y"`: 2.0 |

This example builds the scalar part test-first, in three cycles, with these requirements:

- An expression built with no arguments has scalar 0.0.
- An expression built with a scalar has that scalar.
- Adding a value to the scalar increases the scalar by that value.

**Cycle 1.** [Pseudocode: empty expression test](#pseudo-empty-expression-test) states the first
requirement. It is red: `LinearExpression` does not exist yet.

<a id="pseudo-empty-expression-test"></a>

**Pseudocode: empty expression test**

```
// pseudocode: empty-expression-test
public test__linear_expression__given_no_arguments__has_scalar_zero()
    expression = LinearExpression()
    expect expression.scalar() == 0.0
```

The minimum code that turns it green returns a constant, as [Pseudocode: constant
scalar](#pseudo-constant-scalar) shows. It looks like cheating, and on purpose: one test demands no
more than this, and the next test will force the real code.

<a id="pseudo-constant-scalar"></a>

**Pseudocode: constant scalar**

```
// pseudocode: constant-scalar
class LinearExpression
    public scalar() returns number
        return 0.0
```

**Cycle 2.** [Pseudocode: scalar-only test](#pseudo-scalar-only-test) states the second requirement.
It is red: the constant 0.0 is not 3.0.

<a id="pseudo-scalar-only-test"></a>

**Pseudocode: scalar-only test**

```
// pseudocode: scalar-only-test
public test__linear_expression__given_a_scalar__has_that_scalar()
    expression = LinearExpression(scalar = 3.0)
    expect expression.scalar() == 3.0
```

To pass both tests, the expression must keep the scalar it receives, with 0.0 when it receives none.
[Pseudocode: stored scalar](#pseudo-stored-scalar) does that, and the constant is gone. The refactor
step finds nothing to improve yet, and a cycle may end that way.

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

**Cycle 3.** [Pseudocode: add scalar test](#pseudo-add-scalar-test) states the third requirement. It
is red: `add_scalar` does not exist yet.

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

The scalar part is done. The variables are the exercise: building an expression with a term, adding
a term to a variable that is already present, merging two expressions, and reading back the
variables and their coefficients, one cycle at a time.

### Further reading

- Kent Beck, *Test-Driven Development: By Example*, Addison-Wesley, 2002: the book that named the
  cycle, worked through at the same small step size as this chapter.

> **Practice it**
>
> - Python: [Test-driven development exercise](https://github.com/sefop/training-testing-python/tree/main/src/test_driven_development)
> - Java: [Test-driven development exercise](https://github.com/sefop/sefop-training-java/tree/main/src/main/java/test_driven_development)

<a id="ch-mocks"></a>

## Mocks

A unit test checks the behaviors a unit promises through its
[interface](../appendix/glossary.md#interface). A unit rarely works alone: it calls another unit,
its [dependency](../appendix/glossary.md#dependency), to do part of its work. A behavior may be
visible in a returned value or error, in an outgoing call, or in both: `add` returns a sum, while a
nightly planning job asks a notifier to wake someone up. The earlier tests checked the first kind.
The second raises a problem: a unit test must not make an external call for real.

### Why the real dependency stays out of the test

A test runs many times a day, on developers' laptops and on shared servers. When a dependency's
calls reach a person or an external system, every run would wake a real person or write to a real
system. That system may also be slow, or out of reach from the machine that runs the test. And
whatever record it keeps lives outside the program, where the test has no dependable way to read it.

### What a mock is

A [mock](../appendix/glossary.md#mock) is a stand-in that the test puts in place of the dependency.
It accepts the same calls as the real one, does nothing else, and records every call it receives,
with its arguments. The unit receives it the way it would receive the real dependency, from outside,
through [dependency injection](../appendix/glossary.md#dependency-injection). After acting, the test
asserts on the record.

[Figure: real notifier and mock](#fig-mocks-real-vs-mock) sets the two side by side. They share the
same [interface](#ch-interface); only what sits behind it differs.

<a id="fig-mocks-real-vs-mock"></a>

**Figure: real notifier and mock**

<p align="center">
  <img src="assets/mocks-real-vs-mock.svg" width="700"
       alt="Two notifiers side by side with the same interface on top, notify(message), joined by an
equals sign. Left, the real notifier: behind the interface, in orange, its implementation connects
to the SMS service and sends the text, and an arrow leaves the object to a phone, labeled a real
person is woken up. Right, the mock notifier: behind the same interface, in green, only a record of
the calls it received, notify with the message Instance 2026-09-26: no feasible plan exists, labeled
sends nothing. Caption: same interface, the unit that calls notify cannot tell them apart">
</p>

Nothing more is needed to build one. [Pseudocode: recording notifier](#pseudo-recording-notifier) is
a complete mock of a notifier: it keeps the messages it is asked to send, and sends none.

<a id="pseudo-recording-notifier"></a>

**Pseudocode: recording notifier**

```
// pseudocode: recording-notifier
class RecordingNotifier implements Notifier
    private messages = empty list

    public notify(message)
        append message to messages
```

Test tools build such an object for any interface, so tests rarely write one by hand. The pseudocode
writes `notifier = mock(Notifier)` to create one, and reads its record with two assertions:

- `expect notifier.notify called once with "<message>"` holds when exactly one call was made, with
  that argument.
- `expect notifier.notify never called` holds when no call was made.

### A worked example

Every night, a planning job solves tomorrow's plan. When the model reports that no feasible plan
exists, someone must act before morning, so the job notifies the planner on call. [Pseudocode:
nightly planner](#pseudo-nightly-planner) receives the result of the solve and the notifier; it
never calls the solver itself.

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

The notification is the behavior, so the test checks the notification. [Pseudocode: infeasible
notifies test](#pseudo-infeasible-notifies-test) hands `NightlyPlanner` a mock and an infeasible
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

A feasible night must stay quiet. [Pseudocode: feasible silent test](#pseudo-feasible-silent-test)
asserts that no notification was sent, which only a record of calls can show.

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

Mock the dependencies whose calls reach people or external systems. Those calls are behaviors a
client relies on, so checking them checks the [interface](#ch-interface). Keep the unit's own
internal parts real. A test that mocks them checks how the unit does its work, and breaks the day
that work is reorganized, even though no promise changed.

### Further reading

- Vladimir Khorikov, *Unit Testing: Principles, Practices and Patterns*, Manning, 2020, chapters 5,
  "Mocks and test fragility", and 9, "Mocking best practices": when a mock protects a test and when
  it makes the test brittle.
- Titus Winters, Tom Manshreck and Hyrum Wright, *Software Engineering at Google*, O'Reilly, 2020,
  chapter 13, "Test Doubles": the other kinds of stand-ins, such as stubs and fakes, and when to
  prefer the real dependency.

> **Practice it**
>
> - Python: [Mocks exercise](https://github.com/sefop/training-testing-python/tree/main/src/mocks)
> - Java: [Mocks exercise](https://github.com/sefop/sefop-training-java/tree/main/src/main/java/mocks)

<a id="ch-integration"></a>

## Integration testing

The [integration test](../appendix/glossary.md#integration-test) is the middle level of [Figure:
test pyramid](#fig-test-pyramid). A program's units do not only call each other: they also meet real
things outside the program, such as files, databases and other systems, and many bugs live in that
meeting. A file written in one format and read in another, a folder that is not where the code
expects it: a unit test with a [mock](../appendix/glossary.md#mock) cannot see such bugs, because
the mock stands exactly where the bug is. An integration test runs the units together with those
real dependencies.

### Which dependencies stay real

Not every dependency should be real in an integration test. The rule depends on who else can see it.

- A [managed dependency](../appendix/glossary.md#managed-dependency) is used only by your program,
  such as its own files or its own database. It stays real: how the program uses it is an
  implementation detail, and only the real one shows whether that detail works.
- An [unmanaged dependency](../appendix/glossary.md#unmanaged-dependency) is observed by other
  people or systems, such as the notifier. It stays a mock, as in [Mocks](#ch-mocks): a test must
  not wake a real person, and the call itself is the behavior to check.

[Figure: real and mocked dependencies](#fig-integration-dependencies) applies the rule to the
nightly planner.

<a id="fig-integration-dependencies"></a>

**Figure: real and mocked dependencies**

<p align="center">
  <img src="assets/integration-dependencies.svg" width="720"
       alt="NightlyPlanner in the middle of an integration test. On the left, in green, the results
file: a managed dependency, only this program uses it, so the test keeps it real. On the right, in
purple, the notifier: an unmanaged dependency, people observe it, so the test replaces it with a
mock">
</p>

### What an integration test covers

An integration test is slower and costlier than a unit test, so it covers one happy path per
scenario, through every real dependency. The edge cases stay in unit tests, with one exception: an
edge case that only the real dependency can produce, such as tonight's file being missing, belongs
in an integration test.

### A worked example

The nightly planner no longer receives the result of the solve as an argument. The solve job saves
each night's result to a file with a `ResultsWriter`, and the planner reads it back with its own
`ResultsReader`. They are two units, owned by two teams, and they share no code: each one encodes
its own idea of the file's format. [Pseudocode: nightly planner with
reader](#pseudo-nightly-planner-with-reader) shows the planner.

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

[Pseudocode: infeasible night integration test](#pseudo-infeasible-night-integration-test) writes a
real file with the real writer, runs the planner with the real reader, and keeps only the notifier a
mock.

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

Suppose the solve job's team changes how it writes the status, `Infeasible` instead of `infeasible`,
and updates its own tests to match. The writer's tests pass, and so do the reader's, each against
its own idea of the format. Only this test, which joins the two, fails.

### Further reading

- Vladimir Khorikov, *Unit Testing: Principles, Practices and Patterns*, Manning, 2020, chapters 8,
  "Why integration testing?", and 10, "Testing the database": the rule for managed and unmanaged
  dependencies, and how many integration tests to write.
- Titus Winters, Tom Manshreck and Hyrum Wright, *Software Engineering at Google*, O'Reilly, 2020,
  chapter 14, "Larger Testing": tests beyond the unit, and the gaps in unit tests they close.

> **Practice it**
>
> - Python: [Integration testing exercise](https://github.com/sefop/training-testing-python/tree/main/src/integration_testing)
> - Java: [Integration testing exercise](https://github.com/sefop/sefop-training-java/tree/main/src/main/java/integration_testing)

---

<a id="ch-model-testing"></a>

## Testing an optimization model

Every test so far compared an output with an expected value that someone could work out before
running the code: `add(2, 3)` is 5, and a notification carries a known message. An optimization
model breaks that assumption, because its expected output is the very thing it exists to compute.

Before jumping into the details, lets clarify some things first. Testing an optimization model can
mean two different things:
1. Given some instance data, test the formulation is coded correctly.
2. Given some instance data, test the output of the solved model is correct.

What should we do? the difference is subtle, but very important. Both are plausible, indeed. Let's
go back to the first principles to answer the question.

Testing the formulation is possible, but I advise against it. This idea has 2 flaws. The first flaw
is that it assumes there is a formulation coded in the first place, which might not necessarily be
true in some situations. For example, if you are solving a problem with a heuristic or
metaheuristic, then there is no formulation coded. The second flaw is that it does not test the
public behavior of interest (the optimization model output). The formulation is indeed, an
implementation detail. Thus, we should only test the output of the solved model. That is the correct
public behavior that (should) be offered by this abstraction. If the abstraction is promising that a
particular solver is being used (Gurobi, XPress, Cplex, etc.), that is a design problem (known as a
leaky abstraction).

<a id="model-difficulties"></a>

### Why an optimization model is harder to test

Six properties of an optimization model make its output harder to test than the output of the
calculator.

<a id="difficulty-oracle"></a>

**The oracle problem.** Whatever decides whether an output is correct is called a [test
oracle](../appendix/glossary.md#test-oracle). For the calculator, the oracle is arithmetic you
already know: 2 plus 3 is 5, worked out without reading a line of `add`. For an optimization model,
writing `expect result.objective_value == ???` needs the optimal value, and for an instance large
enough, computing it independently means solving the problem the model exists to solve. The
difficulty has a name in the software testing literature: the [oracle
problem](../appendix/glossary.md#oracle-problem). [Figure: the oracle problem](#fig-oracle-problem)
sets the two situations side by side.

<a id="fig-oracle-problem"></a>

**Figure: the oracle problem**

<p align="center">
  <img src="assets/model-testing-oracle-problem.svg" width="760"
       alt="Two tests side by side. Left, an ordinary test: the inputs 2 and 3 go into add, which
returns 5, and the expected value 5 comes from arithmetic done in your head, so the two can be
compared. Right, a test of an optimization model on a large instance: the instance goes into the
model and its solver, which returns an objective value, but the expected value is a question mark,
because the only way to compute it is to solve the same problem again">
</p>

<a id="difficulty-uniqueness"></a>

**The answer may not be unique.** A model instance can have a single optimal solution, or several
that tie at the same objective value. Which one comes back depends on the solver, its settings, even
the order of the input. A test cannot know in advance which of the optimal solutions it will
receive, nor whether there is more than one.

<a id="difficulty-infeasible"></a>

**An empty feasible region is an answer.** Constraints can contradict each other: one demands
$x \ge 2$ while another allows at most $x \le 1$. Then no solution exists, and "infeasible" is the
correct output, not a failure. A correct model must say so rather than return a solution, and a test
must treat that statement as an answer to check, like any other.

<a id="difficulty-floating-point"></a>

**Numbers are floating point.** A computer stores most decimal numbers approximately: 0.1 + 0.2 is
not exactly 0.3. A solver computes with that finite precision, and it accepts a constraint as
satisfied when it is violated by less than a small tolerance. Two correct answers can therefore
differ in their last digits, an objective value can come back as 25.999999998 instead of 26, and a
constraint $x \le 10$ can be met at 10.000000001. Equality can only mean equality within a
tolerance.

<a id="difficulty-optimality"></a>

**Optimality may not be guaranteed.** A [heuristic](../appendix/glossary.md#heuristic) gives up the
guarantee of optimality on purpose, in exchange for speed on large instances. An exact solver
stopped by a time limit does the same without announcing it: it returns the best solution found so
far, which need not be the best one. For such solvers, "the optimal value" is not something the
output promises, and two runs may even return different solutions.

<a id="difficulty-algorithm"></a>

**The algorithm may change.** An optimization model can be solved with many algorithms, such as a
commercial-solver, a heuristic, a metaheuristic, dynamic programming, etc. Thus, the tests should
not use leaked information from the algorithm to assert correctness.

<a id="model-cargo"></a>

### A cargo model example

For the next parts of the section we are going to use this example. The full definition of the cargo
loading system is written in [the
appendix](../appendix/running-example.md#an-optimization-model-for-this-problem). for one cargo
flight, the question is what cargo to load to maximize revenue and respect operational constraints.
The model is is a [mixed-integer program](../appendix/glossary.md#mixed-integer-program) (MIP).

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

<a id="model-contract"></a>

### The optimization contract

[Interface vs implementation](#ch-interface) showed that a caller relies on what the abstraction
promises, never on how it keeps the promise. What, then, does the cargo model promise to its caller?
Let's write these promises explicitly before testing them.

The cargo model sits behind one class, `Optimization`, with a single public method, `run`. It
receives an `Instance` object and returns a `Solution` object. [Pseudocode: optimization
contract](#pseudo-optimization-contract) defines the three classes and the method. A comment
starting with `requires` states what the caller must provide, and one starting with `returns` what
the method guarantees; `or null` means the method may return no object at all.

<a id="pseudo-optimization-contract"></a>

**Pseudocode: optimization contract**

```
// pseudocode: optimization-contract
class Product
    public name
    public weight                        // per pallet
    public volume                        // per pallet
    public revenue                       // per pallet
    public committed_quantity            // pallets that must fly, 0 by default

class Instance
    public products                      // list of Product
    public weight_capacity
    public volume_capacity

class Solution
    public picked                        // product name -> whole number of pallets, 0 when left behind
    public objective_value               // revenue of the load
    public total_weight                  // weight of the load
    public total_volume                  // volume of the load

class Optimization
    // requires: instance is not null
    // returns:  a Solution filled with the load found, or null when the optimization phase
    //           could not provide a feasible solution
    // raises:   an error if instance is null
    public run(instance) returns Solution or null
```

A caller writes two lines, as shown in [Pseudocode: optimization usage](#pseudo-optimization-usage):

<a id="pseudo-optimization-usage"></a>

**Pseudocode: optimization usage**

```
// pseudocode: optimization-usage
optimization = Optimization()
solution = optimization.run(instance)
```

Note that the contract says nothing about the algorithm behind `run`, and nothing about why the
optimization module could fail to provide one. This design is deliberate on purpose, we don't want
to **leak implementation details** to the contract.

Behind `run`, five private steps make up the *optimization phase*, as [Figure: the optimization
phase](#fig-model-pipeline) shows: receive the instance, build the model, solve it, assemble the
solution, and return it. They are implementation details: a caller cannot reach them and does not
know anything about them.

<a id="fig-model-pipeline"></a>

**Figure: the optimization module**

<p align="center">
  <img src="assets/model-testing-pipeline.svg" width="420"
       alt="A vertical diagram. An Instance at the top enters the class Optimization through its
only public method, run, shown in blue: run takes an Instance and returns a Solution. Inside the
class, five private steps in orange run from top to bottom: receive the instance, build the model,
solve, assemble the solution, return the solution, labeled private implementation details. A
Solution leaves at the bottom">
</p>

So what does this contract offers? There are two types of promises: software promises (derived from
the software design) and mathematical promises (derived from optimization theory).

**Software promises**:
1. There is a single public method called `run` which receives a non-null `Instance` object.
2. If the provided `Instance` is null, then an error is going to be thrown by the program.
3. If the provided `Instance` is not null, this method returns an `Solution` object. The `Solution`
   object could
be null, which means a solution could not be found. It its `non-null`, it means a feasible solution
was found.

Mathematical promises varies if the underlying algorithm solving the model guarantees optimality or
not. The promises that hold for any algorithm come first; those that hold only when optimality is
guaranteed follow from it. Mathematical promises usually are implicit and not written as concrete
comments in the abstraction, nonetheless, I think it would be a good idea to write them as comments
in your project.

Assume a model as $\max \{ f(x) : x \in X \}$, where $f$ is the objective and $X$ the feasible set,
and let $z = f(x)$ for the objective value of a solution $x$. A first run solves $(f, X')$ and
returns $x'$ with $z' = f(x')$; a second run solves $(f, X'')$ and returns $x''$ with
$z'' = f(x'')$. Every relation between two runs assumes that both returned a solution. In a test,
$=$ means equal within the tolerance of [floating point numbers](#difficulty-floating-point).

**Mathematical promises without optimality guarantees**:

1. **Valid solution.**

   $x' \in X'$ and $z' = f(x')$: the solution is feasible, and its value is reported correctly.

   *Cargo model example tests:*
   - every product's quantity is a whole number of pallets.
   - every committed pallet is loaded.
   - the total weight is at most $W$, and the total volume at most $V$.
   - `objective_value` equals $\sum_i r_i x'_i$, and the reported totals equal $\sum_i w_i x'_i$ and
     $\sum_i v_i x'_i$.

2. **No solution from an empty feasible set.**

   If $X' = \emptyset$, no solution is returned.

   *Cargo model example tests:*
   - the committed pallets alone weigh more than the payload capacity, $\sum_i w_i l_i > W$, thus
     the output is `null`.
   - the committed pallets alone take more room than the hold, $\sum_i v_i l_i > V$:=, thus the
     output is `null`.

**Mathematical promises with optimality guaranteed**:

Every promise below follows from optimality: assume the optimal objective function value is $z^*$.

3. **Existence & optimality.**

   If $X' \ne \emptyset$, then the optimal value returned should be $z^*$.

   *Cargo model example tests:*
   - no products at all: an empty load worth zero revenue.
   - the committed pallets fill one capacity exactly and fit the other: the committed load is the
     actual solution.
   - no pallets committed, and every product exceeds a capacity on its own: an empty load worth
     zero.
   - one uncommitted product with positive revenue, whose weight and volume allow $m \ge 2$ pallets:
     exactly $m = \lfloor \min(W / w, V / v) \rfloor$ whole pallets are loaded.
   - two products, and only one pallet fits in total: the higher-revenue pallet is loaded.
   - an instance whose unique optimum fills the payload exactly and leaves volume unused: that load.
   - the mirror case, a unique optimum that fills the hold exactly and leaves payload unused: that
     load.
   - a unique optimum that fills both capacities exactly: that load.
   - two equal-revenue pallets that each fit, but not together: either one, with the same revenue.
   - an uncommitted product too heavy to fly on its own: left behind, and the rest of the load is
     unaffected.

4. **Permutation invariance.**
    - If a second instance is a reordering of the first instance data, then $z' = z'' = z^*$,
      even when $x'' \ne x'$. It generalizes the commutativity property in the addition operation for an
    optimization model.

   *Cargo model example tests:*
   - the products listed in reverse order: the same revenue in both solutions.

5. **Objective changed, feasible set unchanged**.
   - Assume $X'' = X'$.
   - If $f'' = k f'$ with $k > 0$, then $z'' = k z'$.
   - If $f''(x) \ge f'(x)$ for every $x \in X'$, then $z'' \ge z'$.

   *Cargo model example tests:*
   - every revenue multiplied by $k > 0$: the revenue is multiplied by $k$.
   - one product's revenue raised: the revenue does not fall.
   - several revenues raised by different amounts: the revenue does not fall.

6. **Feasible set expanded, objective does not worsen**.
   - Assume $X'' \supseteq X'$, then, $z'' \ge z'$.

   *Cargo model example tests:* the revenue does not fall when
   - the payload capacity is raised.
   - the hold capacity is raised.
   - a new, uncommitted product is added.
   - a committed pallet is released.

7. **Feasible set reduced, objective does not improve**.
   - Assume $X'' \subseteq X'$, then, $z'' \le z'$.
   - If $x' \in X''$, then $z'' = z'$.

   *Cargo model example tests:* the revenue does not rise when
   - the payload capacity is lowered.
   - the hold capacity is lowered.
   - an uncommitted product is removed.
   - one more pallet is committed.

   It stays the same when exactly the pallets the first run loaded are committed.


<a id="model-what-to-test"></a>

### Testing the black box

A test builds an `Instance`, calls `run`, and checks one promise of [the contract](#model-contract)
on what comes back. It runs the real solver: a stand-in that returns a fixed answer could never show
whether the answer is right. [Figure: testing the black box](#fig-black-box-test) shows the two
shapes such a test takes: one run checked against one promise, or two runs checked against a
relation between them.

<a id="fig-black-box-test"></a>

**Figure: testing the black box**

<p align="center">
  <img src="assets/model-testing-black-box.svg" width="760"
       alt="Three columns: arrange, act, assert. Top row, one run: an Instance goes into
Optimization, drawn as a dark black box whose only visible part is its public method run, and the
Solution that comes out, or null, is checked against one promise, behaviors 1 to 3. Bottom row, two
runs: an Instance and a transformed copy each go through run, and a relation between the two
solutions is checked, behaviors 4 to 7, for example that the second objective value is at least the
first. A note says the test sees only what goes into run and what comes out of it">
</p>

Such a test is a [unit test](../appendix/glossary.md#unit-test), even though five private steps and
a solver run behind `run`. A unit test checks one unit of behavior, quickly and in isolation from
other tests, and one unit of behavior can span several pieces of code: here, everything `run` does
to keep one promise. The solver could be a library inside the program, and each test builds its own
model, so no test affects another. The test could become an [integration
test](../appendix/glossary.md#integration-test) in two cases: when its instance is large enough to
make it slow, and when the solver checks its license against a server outside the program.

---

<a id="ch-oracles"></a>

## Test oracles

The tests defined before require different levels of reasoning of the expected behavior. The
artifact that provides the expected behavior in a test is known as a [test
oracle](../appendix/glossary.md#test-oracle). For a valid solution, that knowledge is direct: a load
is checked against the constraints by substituting it into them. The test oracle is the definition
of the constraints itself, and a test derives the expected result by implementing that definition.

A direct test of **Existence & optimality** requires the optimal value of the problem, which is not
known in advance for a given instance. The optimal value has a precise mathematical definition, but
computing it can be very expensive: for an instance large enough, it means solving the model again.
This is the [oracle problem](#difficulty-oracle), and this chapter explores three ways around it:
the known oracle, the pseudo-oracle and metamorphic relations.

<a id="mip-known-oracle"></a>

### Known oracle

A [known oracle](../appendix/glossary.md#known-oracle) is the expected answer, worked out before the
test runs by a method that does not use the code under test: by hand, from a formula, or from a
published result. The test compares the output with that answer.

In the following example there is nothing commited and chocolate fits at most once by weight and
water at most once by volume, so
each $x_i \in \{0, 1\}$ and there are $2 \times 2 = 4$ candidate loads, few enough to list:

| $x_A$ | $x_B$ | Weight (≤ 2) | Volume (≤ 2) | Revenue | Feasible? |
|:---:|:---:|:---:|:---:|:---:|---|
| 0 | 0 | 0 | 0 | 0 | yes |
| 1 | 0 | 2 | 1 | 10 | yes |
| 0 | 1 | 1 | 2 | 6 | yes |
| 1 | 1 | 3 | 3 | 16 | no, both capacities exceeded |

The best feasible load is $x_A = 1$, $x_B = 0$, worth a revenue of 10. Nobody needed a solver to
produce that answer, so it can serve as the expected value of a test:

<a id="pseudo-two-pallet-test"></a>

**Pseudocode: two-pallet test**

```
// pseudocode: two-pallet-test
a = Product(name="A", weight=2, volume=1, revenue=10)
b = Product(name="B", weight=1, volume=2, revenue=6)
instance = Instance(products=[a, b], weight_capacity=2, volume_capacity=2)

solution = Optimization().run(instance)

expect solution != null
expect solution.objective_value == 10
```

**No solution from an empty feasible set** has a known oracle too: whether the committed pallets
alone exceed a capacity is one sum over them. That shortcut belongs to this model: every pallet
weighs something and takes room, so the committed pallets alone are the lightest and smallest load
allowed.

<a id="mip-pseudo-oracle"></a>

### Pseudo-oracle

A hand-worked answer covers only a few cases. A
[pseudo-oracle](../appendix/glossary.md#pseudo-oracle) checks many more: it is a second, independent
implementation of the same contract, whose steps can be inspected even if it is slow. [Differential
testing](../appendix/glossary.md#differential-testing) runs both on the same inputs and compares
their outputs: a disagreement means one of them is wrong.

Here the second implementation is an `EnumerationSolver`: a class that exists only in the tests, has
a `run` method with the same contract, and tries every candidate load. It is slow, but correct by
inspection, and it only makes sense for instances small enough to enumerate. A MIP solver such as
Gurobi is very unlikely to compute a wrong optimum for the model it was given; the realistic risk is
that the code builds a different model from the one on paper, and a disagreement with enumeration
points at that.

This is the disciplined version of a sanity check most modelers already run by hand, comparing a new
model with brute force on a toy case. Three details turn that habit into a reliable test:

1. **Generate many instances instead of picking a few.** Hundreds of small random instances explore
   corners that nobody would think to write by hand, including ones with no feasible load whenever
   the generator commits more cargo than the aircraft can carry.
2. **Fix the [random seed](../appendix/glossary.md#random-seed).** The same inputs must always
   produce the same outputs, as in a controlled experiment. A failure that vanishes on the retry
   cannot be investigated, so the test must also report the instance that failed.
3. **Compare only what the contract promises.** Whether a Solution came back and its objective
   value, never `picked`: when several loads tie, the contract allows the two implementations to
   return different ones. An equal value proves the load optimal only together with the checks of a
   valid solution: a load that misreports its revenue could match the optimum by accident.

<a id="pseudo-differential-sweep"></a>

**Pseudocode: differential sweep**

```
// pseudocode: differential-sweep
rng = random_generator(seed=42)

repeat 200 times:
    products = a list of rng.integer(1, 4) products, each with
                   weight  = rng.integer(1, 5),  volume             = rng.integer(1, 5),
                   revenue = rng.integer(0, 20), committed_quantity = rng.integer(0, 2)
    instance = Instance(products,
                        weight_capacity=rng.integer(0, 8),
                        volume_capacity=rng.integer(0, 8))

    reference = EnumerationSolver().run(instance)
    candidate = Optimization().run(instance)

    expect (candidate == null) == (reference == null)
    if reference != null:
        expect candidate.objective_value == reference.objective_value
```

Weights and volumes start at 1, so no product fits more than 8 times, and enumeration checks at most
$9^4 = 6561$ loads. The reference stays cheap.

What does this catch that the known oracle does not? Suppose the code mistakenly uses each product's
volume in the weight constraint. Some hand-picked instances catch that mistake and some do not,
because they were chosen to cover the contract, not this particular error. A sweep over 200
generated instances is far more likely to hit one that exposes it. Neither guarantees detection; the
difference is how reliably each one finds a mistake nobody anticipated.

The two implementations must be independent: if both share the same misunderstanding, say both treat
every product as a 0/1 choice, they agree with each other and are both wrong.

<a id="mip-metamorphic-relations"></a>

### Metamorphic relations

In instances where using a test oracle is impractical, such as a large MIP, we can exploit
mathematical properties of related runs to assert some expected behavior. These are called
[metamorphic relations](../appendix/glossary.md#metamorphic-relation).

A classical example is the $sin(x)$ function. We know that for some values like $x=0,30,45,60,90$
computing $sin(x)$ is easy. For some other values like $x=17$ is not that simple. For cases like
these we can exploit a metamorphic relation of the sin function: $\sin(x + \pi) = -\sin(x)$, which
is easy to verify visually:

<a id="fig-sine-relation"></a>

**Figure: a metamorphic relation of the sin function**

<p align="center">
  <img src="assets/oracles-sine-relation.svg" width="520"
       alt="The unit circle with a right triangle for a small angle x: its hypotenuse is a radius of
length 1, and its vertical side, sin(x), rises from the horizontal axis to the point (cos x, sin x).
The same triangle is drawn for the angle x + pi, opposite through the center: it has the same
hypotenuse and the same angle x at the center, so its vertical side, sin(x + pi), has the same
length but points down to (-cos x, -sin x). Hence sin(x + pi) = -sin(x)">
</p>

How to transform this metamorphic relation into a test? Take two related runs an assert the
mathematical properties of both runs. In the case of the example above, it would be:

<a id="pseudo-sine-relation-test"></a>

**Pseudocode: sine relation test**

```
// pseudocode: sine-relation-test
x = 17

first  = sin(x)
second = sin(x + π)

expect second == -first
```

In the context of a MIP, two consecutive optimal runs share some implicit properties, which are
the ones listed at the end of the optimization contract:

- Permutation invariance
- Objective changed, feasible set unchanged
- Feasible set expanded, objective does not worsen
- Feasible set reduced, objective does not improve


<a id="mip-oracle-reach"></a>

### When to use each oracle

[Figure: the reach of each oracle](#fig-oracle-classes) places the three oracles along the size of
the instance.

<a id="fig-oracle-classes"></a>

**Figure: the reach of each oracle**

<p align="center">
  <img src="assets/oracles-classes.svg" width="760"
       alt="A horizontal axis of instance size, from tiny to large, with three bands.
Hand-calculated optimal values, the known oracle, reach only tiny instances. Enumeration, the
pseudo-oracle, reaches small ones. Metamorphic relations between two runs apply at every size">
</p>

- **Known oracle: selected small cases.** The price of a human oracle grows fast. The capacities
  allow at most $m_i = \lfloor \min(W / w_i, V / v_i) \rfloor$ pallets of product $i$, so the
  candidate loads number $\prod_{i \in I} (m_i - l_i + 1)$: 4 for the example instance, but
  $4^{30} \approx 1.2 \times 10^{18}$ for 30 products that each fit up to 3 times. A person can only
  be the oracle at teaching scale. A few handpicked small instances often cover the ordinary case,
  but bugs cluster at the boundaries where behavior changes, so choose boundary cases deliberately:
  that is why the example tests for **No solution from an empty feasible set** and **Existence &
  optimality** in [The optimization contract](#model-contract) sit on boundaries. The
  empty-feasible-set sum is this model's exception: it holds at any size.
- **Pseudo-oracle: many small cases.** The reference must stay tractable, so differential testing
  against enumeration lives in the same small-instance regime as the known oracle. It broadens
  coverage within that regime but does not reach the large instances.
- **Metamorphic relations: any size.** The instances that matter in practice, a real booking list on
  a real aircraft, are beyond both, and for them a test knows nothing about the answer. The
  relations still hold. Checking a valid solution also applies at every size: it takes one pass over
  the products.


The three are complementary: known answers check selected cases, enumeration checks many small
cases, and metamorphic relations check properties at any size.

### Further reading

- Barr et al., ["The Oracle Problem in Software Testing: A
  Survey"](https://ieeexplore.ieee.org/document/6963470), IEEE Transactions on Software Engineering,
  2015: the survey that names the oracle problem and sorts oracles by mechanism.
- Maurício Aniche, *Effective Software Testing: A developer's guide*, Manning, 2022: choosing test
  inputs at the boundaries where behavior changes, in depth, under the name specification-based
  testing.
- T. Y. Chen et al., "Metamorphic Testing: A Review of Challenges and Opportunities," *ACM Computing
  Surveys*, 2018: a broad review of the technique and where it has been applied.
- William M. McKeeman, "Differential Testing for Software," *Digital Technical Journal*, 1998: the
  paper that named the technique.

The following exercise implements every example test of
[The optimization contract](#model-contract), each with the oracle that fits it.

> **Practice it**
>
> - Python: Oracles exercise (coming soon)
> - Java: Oracles exercise (coming soon)

---

<a id="ch-mip-no-optimality"></a>

## Testing a mixed-integer program without optimality guaranteed

A mixed-integer program (MIP) can take hours to solve to proven optimality once its instance grows,
and a load planner cannot wait hours before the aircraft closes. The optimization phase has to
answer in time, even when the best load has not been proven best yet: its solver stops at a time
limit and returns the best load found so far, the [incumbent](../appendix/glossary.md#incumbent).
The contract can then no longer promise the optimum, and [Pseudocode: time-limited
contract](#pseudo-time-limited-contract) says so.

<a id="pseudo-time-limited-contract"></a>

**Pseudocode: time-limited contract**

```
// pseudocode: time-limited-contract
class Optimization
    // requires: instance is not null
    // returns:  a Solution, which is feasible but may not be optimal,
    //           or null when the optimization phase could not provide a feasible solution
    public run(instance) returns Solution or null
```

What can a test still ask for?

### What survives

A test can only check a promise the contract still makes. Without optimality, that leaves the two
behaviors of [The optimization contract](#model-contract) that hold for any algorithm:

- **Behavior 1, a valid solution.** Its checks apply unchanged to every Solution `run` returns: they
  never needed the optimum.
- **Behavior 2, no solution from an empty feasible set.** An instance whose committed pallets exceed
  a capacity has no feasible load, so `run` must return `null`. The converse is gone: a phase
  stopped early may return `null` on an instance that does have a feasible load, and the contract
  allows it.

Behaviors 3 to 7 follow from optimality, so they no longer hold. The relations of behaviors 4 to 7
are theorems about the optimum, and an incumbent is not the optimum. A
[heuristic](../appendix/glossary.md#heuristic) shows it most plainly: take a greedy one that sorts
products by revenue per tonne and loads each while it fits.

<a id="pseudo-greedy-relation-test"></a>

**Pseudocode: greedy relation test**

```
// pseudocode: greedy-relation-test
a = Product(name="A", weight=3, volume=1, revenue=10)
d = Product(name="D", weight=2, volume=1, revenue=7)

before = GreedyOptimization().run(Instance(products=[a],    weight_capacity=3, volume_capacity=10))   // loads A: 10
after  = GreedyOptimization().run(Instance(products=[a, d], weight_capacity=3, volume_capacity=10))   // loads D: 7

expect after.objective_value >= before.objective_value                                                // fails: 7 < 10
```

`GreedyOptimization` keeps the time-limited contract: its loads are feasible and may not be optimal.
D earns 3.5 per tonne and A 3.3, so it loads D, and the tonne left takes nothing. The optimum with D
available is still 10, one pallet of A. The heuristic dropped to 7 while behaving exactly as
designed, so the failure is in the test, which asked a load that may not be optimal for a theorem
about optima.

### Measuring quality instead

The two surviving tests cannot tell a good load from a poor one: the committed pallets alone pass
both. Quality is still worth watching, but it needs a different tool. A
[benchmark](../appendix/glossary.md#benchmark) runs `run` on a fixed set of instances and records
how far each load falls short, every time the code changes, so that a change for the worse shows up
and gets investigated rather than failing a build.

The shortfall is measured against a number the test computes itself. Drop the requirement that
pallets be whole, and the model becomes its [linear
relaxation](../appendix/glossary.md#linear-relaxation), a linear program that solves fast even for
large instances; its best revenue is at least the best revenue of whole pallets.
`lp_relaxation_value(instance)` is a helper that exists only in the tests and computes it. The
*upper-bound gap* of a load is then $(z_{\text{LP}} - z) / z_{\text{LP}}$, where $z$ is the load's
revenue and $z_{\text{LP}}$ the value of the relaxation. On an instance small enough to enumerate,
`EnumerationSolver` gives the optimum $z^*$, and the *exact gap* $(z^* - z) / z^*$ can be measured
as well. [Figure: the gap a benchmark measures](#fig-bounds) places the three values on one line.

<a id="fig-bounds"></a>

**Figure: the gap a benchmark measures**

<p align="center">
  <img src="assets/mip-no-optimality-bounds.svg" width="720"
       alt="A number line of revenue. On the left, the incumbent's objective value, the revenue of
the load returned. On the right, the value of the linear relaxation, computed by the test. Between
them, the optimum, unknown on a large instance and computed by enumeration on a small one. The
upper-bound gap spans the distance from the incumbent to the relaxation">
</p>

[Pseudocode: quality benchmark](#pseudo-quality-benchmark) keeps the two gaps apart, since they
measure different things, and counts the `null` returns separately, since the contract allows them
and they have no gap. It holds no `expect`: it reports, and a person reads the report.

<a id="pseudo-quality-benchmark"></a>

**Pseudocode: quality benchmark**

```
// pseudocode: quality-benchmark
upper_bound_gaps = empty list
exact_gaps       = empty list
null_count       = 0

for each instance in the fixed benchmark instances:
    solution = Optimization().run(instance)
    if solution == null:
        null_count = null_count + 1
    else:
        bound = lp_relaxation_value(instance)
        add (bound − solution.objective_value) / bound to upper_bound_gaps
        if the instance is small enough to enumerate:
            optimum = EnumerationSolver().run(instance).objective_value
            add (optimum − solution.objective_value) / optimum to exact_gaps

report the average of upper_bound_gaps, the average of exact_gaps, and null_count
```

### Where this stops working

- **The relaxation can be loose.** The upper-bound gap includes the distance between the relaxation
  and the optimum, so it overstates how far a load falls short, sometimes by a lot.
- **Exact gaps exist only for small instances.** On a large one, only the upper-bound gap is
  available.

### Check yourself

1. `run` reaches its time limit and returns a Solution. Should the two-pallet test's exact-value
   assertion apply to it?
2. On the same small instance, `Optimization` reports 12 revenue and `EnumerationSolver` reports 10.
   Is that a bug?
3. `run` returns `null` on an instance whose committed pallets fit. Does that break the time-limited
   contract?

<details>
<summary>Answers</summary>

1. No. The contract does not promise an optimal load, so check behavior 1, and track the load's
   quality in the benchmark.
2. Yes. No feasible load beats the optimum, so either the load is infeasible or its revenue is
   misreported, and the checks of behavior 1 show which.
3. No. `null` means only that the phase could not provide a feasible solution. The contract forces
   `null` on an instance with no feasible load, but it never forces a Solution.

</details>

### Further reading

- Laurence A. Wolsey, *Integer Programming*, 2nd edition, Wiley, 2020: linear relaxations, the
  bounds they give, and how branch-and-bound closes the gap between a load and its bound.
- David P. Williamson and David B. Shmoys, *The Design of Approximation Algorithms*, Cambridge
  University Press, 2011: where approximation guarantees, a floor a heuristic test could assert,
  come from.

> **Practice it**
>
> - Python: MIP without optimality exercise (coming soon)
> - Java: MIP without optimality exercise (coming soon)

---

<a id="ch-dss-testing"></a>

## Testing a decision-support system

A decision-support system promises its users a decision, not an algorithm: behind its
[interface](#ch-interface), the load may come from enumeration, a heuristic or a solver, and the
choice may change. Its tests therefore see only what the interface returns.

A decision-support system is more than its optimization model. Data arrives from other systems,
business rules turn it into model parameters, the model computes a decision, and the decision flows
back to the people and systems that act on it. Each of these parts can break. For most of them, the
expected output is cheap to write down: you know what a data check or a business rule should return
before running it. The model is the exception, because its expected output is the very thing it
exists to compute. The chapter will map each part of the system to the kind of test that fits it.

The chapter will also sort the oracles of the model chapters by what survives behind an interface.
All of them already treat `Optimization` as a black box: they need only the instance and what `run`
returns.

---

<a id="ch-conclusion"></a>

## Conclusion

A test is an experiment with an expected answer, and each chapter of this section is a way of
obtaining that answer, up to the case where the answer is the very thing the model computes.

- **Test the promise, not the mechanism** ([Interface vs implementation](#ch-interface)). What a
  unit does outlives how it does it.
- **A unit test is a small experiment** ([Unit testing](#ch-unit-testing)). One behavior, fixed
  inputs and a stated prediction.
- **Nothing tests the test** ([Writing good tests](#ch-clear-tests)). A test must be obviously
  correct at a glance.
- **Red first shows the cause** ([Test-driven development](#ch-tdd)). A test that failed before the
  code existed shows that the code made it pass.
- **Record the calls you cannot observe** ([Mocks](#ch-mocks)). When a behavior is a call to another
  system, a mock keeps the record the test checks.
- **Keep what only your program uses real** ([Integration testing](#ch-integration)). Mock what
  others observe, and let the real files and databases show where units disagree.
- **Test the pipeline through its contract** ([Testing an optimization model](#ch-model-testing)).
  `run` and the Solution it returns are the promise; the five private steps behind them are not.
- **Sort the checks by what the test knows** ([Test oracles](#ch-oracles)). A known answer, a second
  implementation, or only conditions every answer meets.
- **Without optimality, test what is still promised** ([Testing a mixed-integer program without
  optimality guaranteed](#ch-mip-no-optimality)). Load validity and `null` on an impossible instance
  remain tests; solution quality is tracked over time as a benchmark.
- **Behind an interface, only the output counts** ([Testing a decision-support
  system](#ch-dss-testing)). The techniques that read the output survive a hidden algorithm; the
  ones that need the solver do not.

With the system tested, the next section puts it in front of its users.

---

## Ideas to develop

- Testing models with a [second objective](../appendix/running-example.md#ev-second-objective), with
  and without optimality.

---

[← Book contents](../../README.md) · [Next section: 06 Deploying decision-support software
→](../06-deployment/README.md)
