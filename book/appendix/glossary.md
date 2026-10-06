# Glossary

Software engineering terms used in this book, each defined once. Chapters link here the first time
they use a term.

---

## Abstraction

Another name for [interface](#interface), used when the stress is on what it hides: how something
is done stays behind what it does. A cargo loading solver abstraction exposes one method, `solve`,
and several implementations, a MIP solver or a heuristic, can stand behind it. It is what lets you
swap solvers without rewriting the code that calls them.

## Adapter pattern

A [design pattern](#design-pattern) in which a small class translates between the interface a system
expects and the one it is given, such as a reader that turns a CSV file into the system's own
objects. Each outside source gets its own adapter, and the rest of the system never sees the
source's format.

## Agile

A way of organizing software development around short feedback loops: release a small change, learn
from the people who use it, and feed the lesson into the next change. Its value is the loop, not its
meetings or vocabulary. Contrast with [waterfall](#waterfall).

## Arrange, act, assert

The three-part body of a unit test, abbreviated AAA: arrange the objects and inputs the test needs,
act by calling the unit once, and assert that the result meets the expectation.

## Automated test

A small program that runs your code on a known input and checks the output against an expected
answer, without a person looking at the result. A collection of them is a [test suite](#test-suite).

## Benchmark

A fixed set of instances run repeatedly to track a measure of quality over time, such as the gap to
a bound. A change is investigated rather than failed.

## Boundary value analysis

Choosing test inputs exactly on the border between two
[equivalence classes](#equivalence-partitioning), where behavior changes character — for example,
committed cargo that exactly fills an aircraft, between a commitment that does not fit (infeasible)
and one that leaves room to spare. Think of the breakpoints in sensitivity analysis.

## Branch

A separate line of work in version control where a change is made without touching the shared code.
When the change is ready, it is merged back, usually through a [pull request](#pull-request).

## Clean architecture

An [architecture](#software-architecture) that arranges a system in four concentric rings (entities,
use cases, interface adapters, frameworks and drivers) and allows dependencies to point only inward,
so that file formats, databases and web frameworks can change without touching the business logic.

## Code complexity

How much a person has to hold in mind to understand what a piece of code does: how many branches,
how many interacting parts, how much hidden state. Every change starts with understanding the code
it touches, so complexity makes every change slower and riskier.

## Code coverage

The share of your code's lines (or branches) that the test suite executes. Useful as a signal of
what is untested; misleading as a goal, because executing a line is not the same as checking that it
is right.

## Cohesion

How closely the elements inside one module of a system belong together. A cohesive module serves one
purpose, so a single kind of change touches it and nothing else. Aim for high cohesion; contrast
with [coupling](#coupling).

## Composition root

The one place in a program, usually its entry point, where every concrete module is built and
connected to the modules that use it. With [dependency injection](#dependency-injection), it is the
only code that knows which concrete classes were chosen.

## Contract

Another name for [interface](#interface), used when the stress is on the promise a piece of code
makes to its callers: what it requires as input, what it returns and what the caller may conclude
from each result, and which errors it raises. It says nothing about how the code gets there. The
cargo optimization contract returns one of four statuses: `optimal`, `feasible`, `infeasible` and
`not_found`. Contrast with [implementation detail](#implementation-detail).

## Continuous delivery

Keeping the software in a state where any change that passed
[continuous integration](#continuous-integration) can be released on demand, through an automated
path rather than a manual procedure. Often written together with continuous integration as CI/CD.

## Continuous integration

Running the build and the [test suite](#test-suite) automatically on every change, so a change that
breaks something is found in minutes instead of at the next release. Abbreviated CI.

## Coordinator

The module that runs an [optimization pattern](#optimization-pattern): it builds the input of each
[solution provider](#solution-provider) it calls, runs the sequence, the loop or the choice, and
returns one result. Seen from outside, it is itself a solution provider.

## Coupling

How much one module of a system depends on another. Two modules are tightly coupled when a change to
one forces a change to the other. Aim for low coupling; contrast with [cohesion](#cohesion).

## Decision-support system

Software that runs repeatedly to turn data, mathematical models, and business rules into decisions
the business acts on. Abbreviated DSS. A one-off study that answers a question once is not one: what
makes a system decision-support software is that the decision recurs and somebody owns the software
that produces it.

## Dependency

Another unit of code that a unit calls to do part of its work. A planning job that notifies people
through a notifier depends on the notifier.

## Dependency injection

Passing a module the modules it depends on from outside, instead of letting it create them itself. A
class that receives its solver can be given a different one, or a fake one in a test, without
editing the class. See [composition root](#composition-root).

## Dependency inversion principle

The rule that high-level policy should not depend on low-level details; both should depend on an
[abstraction](#abstraction). An optimization module depends on a solution-provider interface, and
each solver implements it, instead of the module calling one solver library directly. The D in
[SOLID](#solid).

## Derived oracle

A [test oracle](#test-oracle) that decides correctness from something other than a known expected
answer — for example, a [metamorphic relation](#metamorphic-relation) between two runs, or agreement
with a [pseudo-oracle](#pseudo-oracle).

## Descriptive and meaningful phrases

The rule that test code should favor readability over the removal of repetition: each test states
its own setup and values, even when other tests repeat them, so it can be read on its own.
Abbreviated DAMP. Contrast with [don't repeat yourself](#dont-repeat-yourself), the rule for
production code.

## Design pattern

A named, reusable solution to a problem that recurs in software design, such as
[strategy](#strategy-pattern) or [adapter](#adapter-pattern). Patterns save reinventing a solution
and give a team a shared vocabulary for describing a design.

## Differential testing

Running two independent implementations of the same [contract](#contract) on the same inputs and
comparing their outputs. A disagreement means at least one of them is wrong.

## Don't repeat yourself

The rule that each piece of knowledge, such as a business rule or an output format, should live in
exactly one place in the code, so that changing it means one edit. Abbreviated DRY.

## Duality

The pairing of every linear program with a second one, its dual, whose optimal value bounds the
first. By strong duality, a feasible solution and a feasible dual solution with equal objective
values are both optimal, so the pair certifies optimality without solving the problem again.

## End-to-end test

A [functional test](#functional-test) that runs the whole application in a real-world scenario, the
way its users would. The slowest and costliest kind of test, so a suite holds only a few.

## Equivalence partitioning

Splitting the space of possible inputs into classes that are expected to behave the same way, then
testing one input per class instead of many redundant ones.

## Evaluator

The module of an [iterated solve](#iterated-solve) that receives the answer of a
[solution provider](#solution-provider) and returns three things: the answer made complete, whether
it is acceptable as a final answer to the original instance, and feedback for the next round. It can
be a second optimization model, a simulation or a check of rules.

## Flaky test

A test that passes on some runs and fails on others without any change to the code, often because it
depends on randomness, timing, or external state. Fixing the [random seed](#random-seed) removes one
common cause.

## Functional test

A test that checks whether a program provides its services correctly: given these inputs, it returns
this output or raises this error. Contrast with [non-functional test](#non-functional-test).

## Happy path

The base case of a unit's behavior: ordinary, valid inputs and the result they should produce, with
nothing going wrong.

## Heuristic

A method that gives up the guarantee of an optimal answer on purpose, in exchange for speed. An
exact MIP solver stopped by a time limit behaves like one from the point of view of its
[contract](#contract): both return a load with the status `feasible`, never `optimal`.

## Implementation detail

Anything about how code produces its result that is not part of its [contract](#contract): the
algorithm, running time, internal data structures. Tests that assert on implementation details break
when the implementation legitimately changes. A fact the caller acts on, such as whether a load is
proven optimal, is not an implementation detail and belongs in the contract.

## Implicit oracle

A [test oracle](#test-oracle) that catches failures wrong in any program at all, such as a crash,
without knowing anything about the expected answer. A hang counts once the test sets a time limit
that turns it into a failure.

## Incremental development

Building a system one part at a time, each part finished and released before the next begins: one
region live before all regions. Contrast with [iterative development](#iterative-development); most
teams need both.

## Incumbent

The best feasible solution a solver has found so far. A solver stopped by a time limit returns its
incumbent, which need not be optimal.

## Information hiding

Keeping each module's [implementation details](#implementation-detail) behind an
[interface](#interface), so that the rest of the system knows what the module does but never how.
Introduced by David Parnas in 1972.

## Integration test

A [functional test](#functional-test) that combines several units and checks that they work
together, for example that one unit reads data in the shape the next one expects.

## Interface

Everything a module of a system offers to the code that calls it, without saying how it is carried
out: for each operation, its name, inputs and output, and the promises that go with them. Also
called [contract](#contract), signature or [abstraction](#abstraction). Code that depends only on an
interface keeps working when the implementation behind it changes.

## Interface segregation principle

The rule that no module of a system should depend on functions it does not use. A module that writes
the plan needs the load, so it should not depend on an interface that also exposes the solver's log.
The I in [SOLID](#solid).

## Iterated solve

An [optimization pattern](#optimization-pattern) in which a [solution provider](#solution-provider)
and an [evaluator](#evaluator) run in a loop: the provider answers, the evaluator judges the answer
and sends feedback, and the provider answers again. Its [coordinator](#coordinator) keeps the best
acceptable answer, and returns `optimal` or `infeasible` only when the loop holds a proof about the
original instance.

## Iterative development

Building the whole system in a rough form first and improving it on every pass, instead of trying to
get it right the first time, such as a formulation revised after users react to its first plans.
Contrast with [incremental development](#incremental-development).

## Known oracle

A [test oracle](#test-oracle) that knows the expected answer before the run, for example an optimal
value worked out by hand for a small instance. Called a [specified oracle](#specified-oracle) in the
testing literature.

## Leaky abstraction

An [abstraction](#abstraction) that lets its implementation show through, so that callers come to
depend on details it was meant to hide. An optimization module whose callers must know which solver
it uses is one.

## Legacy system

Software that is difficult to change safely — not because it is old, but because it lacks the safety
mechanisms, such as a [test suite](#test-suite), that make change possible.

## Lexicographic optimization

Optimizing several objectives in a fixed order of priority: the first objective is optimized, then
the second is optimized among the solutions that keep the first at its optimum, and so on. Also
called hierarchical optimization.

## Linear program

An optimization model whose objective and constraints are linear and whose variables are continuous.
Abbreviated LP. Solvers find a provably optimal solution, and [duality](#duality) certifies it.

## Linear relaxation

The [linear program](#linear-program) obtained from a
[mixed-integer program](#mixed-integer-program) by dropping the requirement that variables take
integer values. Every integer solution is also a solution of the relaxation, so its optimal value
bounds the optimal value of the mixed-integer program: from above for a maximization.

## Liskov substitution principle

The rule that any implementation of an interface must be usable wherever the interface is expected:
it accepts everything the [contract](#contract) accepts and keeps everything the contract promises.
A heuristic that labels its load `optimal` takes the right input, returns the right record and
breaks the principle. The L in [SOLID](#solid).

## Managed dependency

A [dependency](#dependency) outside the program that only the program itself uses, such as its own
files or its own database. Integration tests use the real one, because how the program uses it is an
implementation detail. Contrast with [unmanaged dependency](#unmanaged-dependency).

## Metamorphic relation

A relation that must hold between the outputs of two related runs, even when neither output is
known. Example: raising a capacity never decreases the optimal value.

## Mixed-integer program

A [linear program](#linear-program) in which some or all variables must take integer values, such as
a number of whole pallets. Abbreviated MIP. Integrality makes the problem much harder to solve and
removes the certificate of optimality that duality gives a linear program.

## Mock

A stand-in for a [dependency](#dependency), created by a test, that records the calls it receives
from the unit under test so the test can check them. Used when the behavior under test is a call to
another system, such as sending a message. One kind of [test double](#test-double).

## Modularity

Building a system from modules with clear boundaries, so that each module can be understood, tested
and replaced on its own. It keeps a change small: a new requirement touches one module and leaves
the others as they were.

## Module

Any piece of code with a boundary around it: a function, a class, or a group of them. The rest of
the system reaches a module only through its [interface](#interface). In some programming languages
the word also names a source file; this book uses the general meaning.

## Monitoring

Collecting and watching signals from software while it runs in production, so that the team learns
about a problem from the system rather than from its users. For decision-support software the
signals include the quality of the decisions, not only whether the program ran.

## Mutation testing

Deliberately introducing small bugs ("mutants") into the code and checking whether the test suite
notices. Mutants that survive point at behavior the tests do not really check.

## Non-functional test

A test that checks how well a program provides its services rather than whether it provides them
correctly: security, speed, usability, availability, scalability. Contrast with
[functional test](#functional-test).

## Object-oriented programming

Organizing a program around objects that hold data together with the operations allowed on it,
instead of around procedures that pass data between them. Abbreviated OOP.

## Open-closed principle

The rule that a module of a system should be open for extension and closed for modification: new
behavior is added by adding code, not by editing code that works. A new heuristic arrives as a new
class behind the solution-provider interface, and the existing solver class is not touched. The O in
[SOLID](#solid).

## Optimization pattern

A named, recurring way to arrange the algorithms of the optimization module of a
[decision-support system](#decision-support-system), by analogy with a
[design pattern](#design-pattern). This book names four: [single solve](#single-solve),
[sequential solve](#sequential-solve), [iterated solve](#iterated-solve) and
[selected solve](#selected-solve).

## Oracle problem

The difficulty of building a [test oracle](#test-oracle) when the correct output is expensive, or
impossible, to compute independently of the code under test. Optimization models are a prime
example.

## Pinned environment

A record of the exact version of every library a program depends on, used to rebuild the same
environment on any machine. It makes a result on one machine a result on every machine.

## Property-based testing

Writing tests as properties that must hold for all inputs of some kind, then letting a library
generate many inputs to check them. When a generated input fails, the library usually
[shrinks](#shrinking) it.

## Pseudo-oracle

A second, independent implementation of the same [contract](#contract), used as the reference in
[differential testing](#differential-testing). Brute-force enumeration is a typical pseudo-oracle
for small instances.

## Public and private

Markers that say who may use a function or a piece of data. Anything may call a public function;
only the code around a private one, such as the rest of its class, may. Keeping details private is
how [information hiding](#information-hiding) is enforced.

## Pull request

A proposal to merge a [branch](#branch) into the shared code, shown as the exact lines it changes so
that a reviewer and [continuous integration](#continuous-integration) can check it first.

## Random seed

The starting value of a pseudo-random number generator. The same seed always produces the same
sequence of numbers, which makes a test that uses random instances reproducible — the software
equivalent of a controlled experiment.

## Refactoring

Changing the internal structure of code without changing what it does, to make the next change
cheaper. The [test suite](#test-suite) is what tells you the behavior did not move.

## Regression

A behavior that used to work and no longer does, usually introduced by a later change. Catching
regressions early is the main job of an automated test suite.

## Selected solve

An [optimization pattern](#optimization-pattern) in which one of several
[solution providers](#solution-provider) is chosen for each instance. It is the
[strategy pattern](#strategy-pattern) applied to the optimization module. Also called algorithm
selection.

## Sequential solve

An [optimization pattern](#optimization-pattern) in which several
[solution providers](#solution-provider) run in a row, the answer of one becoming part of the input
of the next, so that each solves a different problem. The whole is not guaranteed to be optimal,
even when every provider's answer is. Also called hierarchical planning.

## Shrinking

Automatically reducing a failing generated input to the smallest input that still fails, so that a
person can understand the failure. A feature of [property-based testing](#property-based-testing)
libraries.

## Signature

Another name for [interface](#interface).

## Single responsibility principle

The rule that a module of a system should have only one reason to change. A responsibility is an
axis of change, such as the input format or the formulation, not a task the code performs. The S in
[SOLID](#solid).

## Single solve

An [optimization pattern](#optimization-pattern) in which one
[solution provider](#solution-provider), exact or heuristic, handles every instance.

## Software architecture

The design of a whole system: the few large decisions about its modules and their boundaries that
are expensive to reverse later.

## Software development lifecycle

The phases a piece of software passes through during its life: working out what is needed, planning,
design, building, testing, deployment, operation and evolution. Abbreviated SDLC.

## SOLID

Five design principles collected by Robert C. Martin:
[single responsibility](#single-responsibility-principle), [open-closed](#open-closed-principle),
[Liskov substitution](#liskov-substitution-principle),
[interface segregation](#interface-segregation-principle) and
[dependency inversion](#dependency-inversion-principle). Each one raises [cohesion](#cohesion),
lowers [coupling](#coupling), or both.

## Solution provider

A module that takes the record of the problem it solves and returns a result under the optimization
[contract](#contract).
An exact provider can prove optimality or infeasibility; a heuristic provider searches without
proving, so it never returns `optimal`.

## Specified oracle

A [test oracle](#test-oracle) in which the expected answer is stated in advance. The book calls it a
[known oracle](#known-oracle).

## Static analysis

Checking code without running it, for type errors, unused variables or suspicious constructs, so
that a class of mistakes is caught before the program runs at all.

## Strategy pattern

A [design pattern](#design-pattern) that puts a family of interchangeable algorithms behind one
interface, so the code using them can choose one at run time, such as a MIP solver or a heuristic
chosen for each instance.

## Technical debt

The future cost of a shortcut taken today: code, tests, or documentation left in a state that makes
the next change more expensive. Like financial debt, it can be a deliberate and reasonable choice —
as long as somebody knows it was taken and what the interest is.

## Test double

An object that stands in for a real dependency during a test. A _stub_ returns fixed answers, a
_fake_ is a simpler working version of the dependency, and a _mock_ records how it was called so the
test can check it.

## Test-driven development

Writing the [automated test](#automated-test) before the code that makes it pass, in short cycles.
Abbreviated TDD. The test comes first so that it describes the behavior wanted, rather than the
behavior that happened to be built.

## Test oracle

Whatever decides whether an output is correct. For a calculator, it is arithmetic you already know.
See also [oracle problem](#oracle-problem).

## Test suite

The full collection of [automated tests](#automated-test) for a codebase, usually run together with
a single command.

## Testability

How easily each module of a system can be checked on its own, quickly, without running the others. A
function that takes values and returns values is highly testable; one that reads files and calls a
solver in the middle of its logic is not.

## Unified Modeling Language

A standard notation for drawing software, abbreviated UML. This book uses a simplified form: a box
per class or interface, members marked `+` for public and `-` for private, and a hollow arrowhead
from a class to the interface it implements.

## Unit test

A [functional test](#functional-test) that checks one small piece of code, such as a function, in
isolation. The fastest and cheapest kind of test, so a suite holds many. The unit is a unit of
behavior: it may be a single function, or several pieces of code that together keep one promise, as
long as the test stays fast and shares nothing with other tests.

## Unmanaged dependency

A [dependency](#dependency) outside the program that other people or systems observe, such as a
notification service. Tests replace it with a [mock](#mock), because the calls it receives are
behavior others rely on. Contrast with [managed dependency](#managed-dependency).

## Validation

Checking that a model is the right one for the decision it supports: a business question, "are we
building the right model?". Contrast with [verification](#verification).

## Verification

Checking that software does what its specification says; for a model, checking that the code
implements the mathematical model correctly: "are we building the model right?". Contrast with
[validation](#validation).

## Waterfall

A development process that runs each phase once, in order (all requirements, then all design, then
all building, then testing and release), so that feedback from users arrives only at the end.
Contrast with [agile](#agile).
