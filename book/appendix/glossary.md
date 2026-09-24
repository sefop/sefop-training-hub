# Glossary

Software engineering terms used in this book, each defined once. Chapters link here the first time they use a term.

---

## Abstraction

A named interface that hides how something is done behind what it does. A cargo loading solver abstraction exposes one
method, `solve`, and several implementations — enumeration, a MIP solver — can stand behind it. It is what lets you
swap solvers without rewriting the code that calls them.

## Agile

A way of organizing software development around short feedback loops: release a small change, learn from the
people who use it, and feed the lesson into the next change. Its value is the loop, not its meetings or vocabulary.
Contrast with [waterfall](#waterfall).

## Automated test

A small program that runs your code on a known input and checks the output against an expected answer, without a person
looking at the result. A collection of them is a [test suite](#test-suite).

## Boundary value analysis

Choosing test inputs exactly on the border between two [equivalence classes](#equivalence-partitioning), where behavior
changes character — for example, committed cargo that exactly fills an aircraft, between a commitment that does not
fit (infeasible) and one that leaves room to spare. Think of the breakpoints in sensitivity analysis.

## Branch

A separate line of work in version control where a change is made without touching the shared code. When the
change is ready, it is merged back, usually through a [pull request](#pull-request).

## Code complexity

How much a person has to hold in mind to understand what a piece of code does: how many branches, how many
interacting parts, how much hidden state. Every change starts with understanding the code it touches, so complexity
makes every change slower and riskier.

## Code coverage

The share of your code's lines (or branches) that the test suite executes. Useful as a signal of what is untested;
misleading as a goal, because executing a line is not the same as checking that it is right.

## Contract

The promise a piece of code makes to its callers: what it needs as input and what it guarantees as output, and nothing
about how it gets there. Contrast with [implementation detail](#implementation-detail).

## Continuous delivery

Keeping the software in a state where any change that passed [continuous integration](#continuous-integration) can be
released on demand, through an automated path rather than a manual procedure. Often written together with continuous
integration as CI/CD.

## Continuous integration

Running the build and the [test suite](#test-suite) automatically on every change, so a change that breaks something
is found in minutes instead of at the next release. Abbreviated CI.

## Decision-support system

Software that runs repeatedly to turn data, mathematical models, and business rules into decisions the business acts
on. Abbreviated DSS. A one-off study that answers a question once is not one: what makes a system decision-support
software is that the decision recurs and somebody owns the software that produces it.

## Derived oracle

A [test oracle](#test-oracle) that decides correctness from something other than a known expected answer — for example,
a [metamorphic relation](#metamorphic-relation) between two runs, or agreement with a
[pseudo-oracle](#pseudo-oracle).

## Differential testing

Running two independent implementations of the same [contract](#contract) on the same inputs and comparing their
outputs. A disagreement means at least one of them is wrong.

## Equivalence partitioning

Splitting the space of possible inputs into classes that are expected to behave the same way, then testing one input
per class instead of many redundant ones.

## Flaky test

A test that passes on some runs and fails on others without any change to the code, often because it depends on
randomness, timing, or external state. Fixing the [random seed](#random-seed) removes one common cause.

## Heuristic

A method that gives up the guarantee of an optimal answer on purpose, in exchange for speed. An exact MIP solver stopped
by a time limit behaves like one from the point of view of its [contract](#contract).

## Implementation detail

Anything about how code produces its result that is not part of its [contract](#contract): the algorithm, running time,
internal data structures. Tests that assert on implementation details break when the implementation legitimately
changes.

## Implicit oracle

A [test oracle](#test-oracle) that catches failures wrong in any program at all — a crash, a hang, a corrupted result —
without knowing anything about the expected answer. Every test gets one for free.

## Incremental development

Building a system one part at a time, each part finished and released before the next begins: one region
live before all regions. Contrast with [iterative development](#iterative-development); most teams need both.

## Iterative development

Building the whole system in a rough form first and improving it on every pass, instead of trying to get it
right the first time, such as a formulation revised after users react to its first plans. Contrast with
[incremental development](#incremental-development).

## Legacy system

Software that is difficult to change safely — not because it is old, but because it lacks the safety mechanisms, such as
a [test suite](#test-suite), that make change possible.

## Metamorphic relation

A relation that must hold between the outputs of two related runs, even when neither output is known. Example: raising
a capacity never decreases the optimal value.

## Modularity

Building a system from parts with clear boundaries, so that each part can be understood, tested and replaced
on its own. It keeps a change small: a new requirement touches one part and leaves the others as they were.

## Monitoring

Collecting and watching signals from software while it runs in production, so that the team learns about a
problem from the system rather than from its users. For decision-support software the signals include the quality
of the decisions, not only whether the program ran.

## Mutation testing

Deliberately introducing small bugs ("mutants") into the code and checking whether the test suite notices. Mutants that
survive point at behavior the tests do not really check.

## Object-oriented programming

Organizing a program around objects that hold data together with the operations allowed on it, instead of around
procedures that pass data between them. Abbreviated OOP.

## Oracle problem

The difficulty of building a [test oracle](#test-oracle) when the correct output is expensive, or impossible, to compute
independently of the code under test. Optimization models are a prime example.

## Pinned environment

A record of the exact version of every library a program depends on, used to rebuild the same environment on
any machine. It makes a result on one machine a result on every machine.

## Property-based testing

Writing tests as properties that must hold for all inputs of some kind, then letting a library generate many inputs to
check them. When a generated input fails, the library usually [shrinks](#shrinking) it.

## Pseudo-oracle

A second, independent implementation of the same [contract](#contract), used as the reference in
[differential testing](#differential-testing). Brute-force enumeration is a typical pseudo-oracle for small instances.

## Pull request

A proposal to merge a [branch](#branch) into the shared code, shown as the exact lines it changes so that a
reviewer and [continuous integration](#continuous-integration) can check it first.

## Random seed

The starting value of a pseudo-random number generator. The same seed always produces the same sequence of numbers,
which makes a test that uses random instances reproducible — the software equivalent of a controlled experiment.

## Refactoring

Changing the internal structure of code without changing what it does, to make the next change cheaper. The
[test suite](#test-suite) is what tells you the behavior did not move.

## Regression

A behavior that used to work and no longer does, usually introduced by a later change. Catching regressions early is
the main job of an automated test suite.

## Shrinking

Automatically reducing a failing generated input to the smallest input that still fails, so that a person can understand
the failure. A feature of [property-based testing](#property-based-testing) libraries.

## Software development lifecycle

The phases a piece of software passes through during its life: working out what is needed, planning, design,
building, testing, deployment, operation and evolution. Abbreviated SDLC.

## Specified oracle

A [test oracle](#test-oracle) in which the expected answer is stated in advance — in this book, worked out by hand for a
small instance.

## Static analysis

Checking code without running it, for type errors, unused variables or suspicious constructs, so that a class
of mistakes is caught before the program runs at all.

## Technical debt

The future cost of a shortcut taken today: code, tests, or documentation left in a state that makes the next change
more expensive. Like financial debt, it can be a deliberate and reasonable choice — as long as somebody knows it was
taken and what the interest is.

## Test-driven development

Writing the [automated test](#automated-test) before the code that makes it pass, in short cycles. Abbreviated TDD.
The test comes first so that it describes the behavior wanted, rather than the behavior that happened to be built.

## Test oracle

Whatever decides whether an output is correct. For a calculator, it is arithmetic you already know. See also
[oracle problem](#oracle-problem).

## Test suite

The full collection of [automated tests](#automated-test) for a codebase, usually run together with a single command.

## Waterfall

A development process that runs each phase once, in order (all requirements, then all design, then all
building, then testing and release), so that feedback from users arrives only at the end. Contrast with
[agile](#agile).
