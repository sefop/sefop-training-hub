# Glossary

Software engineering terms used in this book, each defined once. Chapters link here the first time they use a term.

---

### Abstraction

A named interface that hides how something is done behind what it does. A knapsack solver abstraction exposes one
method, `solve`, and several implementations — enumeration, a MIP solver — can stand behind it. It is what lets you
swap solvers without rewriting the code that calls them.

### Automated test

A small program that runs your code on a known input and checks the output against an expected answer, without a person
looking at the result. A collection of them is a [test suite](#test-suite).

### Boundary value analysis

Choosing test inputs exactly on the border between two [equivalence classes](#equivalence-partitioning), where behavior
changes character — for example, a budget of exactly zero, between negative budgets (infeasible) and positive ones.
Think of the breakpoints in sensitivity analysis.

### Code coverage

The share of your code's lines (or branches) that the test suite executes. Useful as a signal of what is untested;
misleading as a goal, because executing a line is not the same as checking that it is right.

### Contract

The promise a piece of code makes to its callers: what it needs as input and what it guarantees as output, and nothing
about how it gets there. Contrast with [implementation detail](#implementation-detail).

### Continuous delivery

Keeping the software in a state where any change that passed [continuous integration](#continuous-integration) can be
released on demand, through an automated path rather than a manual procedure. Often written together with continuous
integration as CI/CD.

### Continuous integration

Running the build and the [test suite](#test-suite) automatically on every change, so a change that breaks something
is found in minutes instead of at the next release. Abbreviated CI.

### Decision-support system

Software that runs repeatedly to turn data, mathematical models, and business rules into decisions the business acts
on. Abbreviated DSS. A one-off study that answers a question once is not one: what makes a system decision-support
software is that the decision recurs and somebody owns the software that produces it.

### Derived oracle

A [test oracle](#test-oracle) that decides correctness from something other than a known expected answer — for example,
a [metamorphic relation](#metamorphic-relation) between two runs, or agreement with a
[pseudo-oracle](#pseudo-oracle).

### Differential testing

Running two independent implementations of the same [contract](#contract) on the same inputs and comparing their
outputs. A disagreement means at least one of them is wrong.

### Equivalence partitioning

Splitting the space of possible inputs into classes that are expected to behave the same way, then testing one input
per class instead of many redundant ones.

### Flaky test

A test that passes on some runs and fails on others without any change to the code, often because it depends on
randomness, timing, or external state. Fixing the [random seed](#random-seed) removes one common cause.

### Heuristic

A method that gives up the guarantee of an optimal answer on purpose, in exchange for speed. An exact MIP solver stopped
by a time limit behaves like one from the point of view of its [contract](#contract).

### Implementation detail

Anything about how code produces its result that is not part of its [contract](#contract): the algorithm, running time,
internal data structures. Tests that assert on implementation details break when the implementation legitimately
changes.

### Implicit oracle

A [test oracle](#test-oracle) that catches failures wrong in any program at all — a crash, a hang, a corrupted result —
without knowing anything about the expected answer. Every test gets one for free.

### Legacy system

Software that is difficult to change safely — not because it is old, but because it lacks the safety mechanisms, such as
a [test suite](#test-suite), that make change possible.

### Metamorphic relation

A relation that must hold between the outputs of two related runs, even when neither output is known. Example: raising
a budget never decreases the optimal value.

### Mutation testing

Deliberately introducing small bugs ("mutants") into the code and checking whether the test suite notices. Mutants that
survive point at behavior the tests do not really check.

### Object-oriented programming

Organizing a program around objects that hold data together with the operations allowed on it, instead of around
procedures that pass data between them. Abbreviated OOP.

### Oracle problem

The difficulty of building a [test oracle](#test-oracle) when the correct output is expensive, or impossible, to compute
independently of the code under test. Optimization models are a prime example.

### Property-based testing

Writing tests as properties that must hold for all inputs of some kind, then letting a library generate many inputs to
check them. When a generated input fails, the library usually [shrinks](#shrinking) it.

### Pseudo-oracle

A second, independent implementation of the same [contract](#contract), used as the reference in
[differential testing](#differential-testing). Brute-force enumeration is a typical pseudo-oracle for small instances.

### Random seed

The starting value of a pseudo-random number generator. The same seed always produces the same sequence of numbers,
which makes a test that uses random instances reproducible — the software equivalent of a controlled experiment.

### Refactoring

Changing the internal structure of code without changing what it does, to make the next change cheaper. The
[test suite](#test-suite) is what tells you the behavior did not move.

### Regression

A behavior that used to work and no longer does, usually introduced by a later change. Catching regressions early is
the main job of an automated test suite.

### Shrinking

Automatically reducing a failing generated input to the smallest input that still fails, so that a person can understand
the failure. A feature of [property-based testing](#property-based-testing) libraries.

### Specified oracle

A [test oracle](#test-oracle) in which the expected answer is stated in advance — in this book, worked out by hand for a
small instance.

### Technical debt

The future cost of a shortcut taken today: code, tests, or documentation left in a state that makes the next change
more expensive. Like financial debt, it can be a deliberate and reasonable choice — as long as somebody knows it was
taken and what the interest is.

### Test-driven development

Writing the [automated test](#automated-test) before the code that makes it pass, in short cycles. Abbreviated TDD.
The test comes first so that it describes the behavior wanted, rather than the behavior that happened to be built.

### Test oracle

Whatever decides whether an output is correct. For a calculator, it is arithmetic you already know. See also
[oracle problem](#oracle-problem).

### Test suite

The full collection of [automated tests](#automated-test) for a codebase, usually run together with a single command.
