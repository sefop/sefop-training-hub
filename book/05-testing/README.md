# Section 05 — Testing decision-support software

## Introduction

Software engineers test code by comparing its output with an answer they already know. Most of a decision-support
system fits that habit: the expected output of a data check or a business rule is easy to write down. The optimization
model breaks it: the answer you would compare against is the very thing the model exists to compute. This section
starts with what to test across the whole system, then explains how to test the model anyway, in short chapters, each
built around one idea.

### Out of scope

- **How to write tests in a particular language or test framework.** The chapters use pseudocode; the runnable
  exercises in the [practice repositories](../appendix/practice-repositories.md) cover the tooling.
- **How fast the model solves.** These chapters ask whether a model computes the right decision, not how quickly.
  Run time and solution quality in production belong to
  [Section 06 — Deploying decision-support software](../06-deployment/README.md).
- **Testing the predictive models that feed a formulation.** When demand or travel times come from a forecast,
  measuring its accuracy is a machine-learning topic; this section tests the optimization side.

## Chapters

| # | Chapter | After it you can… | Status |
|:---:|---|---|---|
| 01 | [What to test in decision-support software](#01--what-to-test-in-decision-support-software) | Name the parts of a decision-support system that need tests, and choose the kind of test for each | Coming soon |
| 02 | [Why optimization models are hard to test](#02--why-optimization-models-are-hard-to-test) | Name the oracle problem and explain why the usual way of testing fails for a MIP | Ready |
| 03 | [Test the contract, not the algorithm](#03--test-the-contract-not-the-algorithm) | Write tests that keep passing when someone swaps the solver | Ready |
| 04 | [Oracles you write by hand](#04--oracles-you-write-by-hand) | Choose a small, systematic set of instances whose answers you work out yourself | Ready |
| 05 | [Metamorphic relations](#05--metamorphic-relations) | Test a model without knowing its optimal value | Ready |
| 06 | [Differential testing](#06--differential-testing) | Use a second implementation to find mistakes in the formulation | Ready |
| 07 | [When optimality is not guaranteed](#07--when-optimality-is-not-guaranteed) | Decide which tests survive when the solver is a heuristic | Ready |
| 08 | [Duality as an oracle](#08--duality-as-an-oracle) | Check an LP's optimum with a certificate instead of re-solving | Coming soon |
| 09 | [Testing a Pareto front](#09--testing-a-pareto-front) | Test a multi-objective model that has no single optimum | Coming soon |

The chapters build on each other. Chapter 01 maps the whole system. Chapters 02–03 set up the vocabulary. Chapters
04–06 present three kinds of oracle, each covering a gap the previous one leaves open. Chapter 07 revisits all three
under a weaker promise. Read them in order the first time.

## The running example: a knapsack

Chapters 02–09 use the same problem, so that the testing ideas change while the model stays still.

A catalogue of items, each with a cost, a volume, and a calorie count. Each item can be taken more than once, up to a
maximum quantity. The task: choose how many units of each item to take so that total calories is maximized, subject
to a cost budget and a volume budget.

Let $I$ be the set of items. For each item $i \in I$, let $c_i$ be its cost, $v_i$ its volume, and $k_i$ its calorie
count, all fixed, **non-negative** parameters. Let $u_i$ be its maximum quantity, $C$ the cost budget, and $V$ the
volume budget. The decision variable $x_i$ is the quantity of item $i$ selected.

$$
\begin{aligned}
\max_{x} \quad & \sum_{i \in I} k_i x_i \\
\text{s.t.} \quad & \sum_{i \in I} c_i x_i \le C \\
& \sum_{i \in I} v_i x_i \le V \\
& 0 \le x_i \le u_i, \quad x_i \in \mathbb{Z}, \quad \forall i \in I
\end{aligned}
$$

The feasible region can be empty. If $C < 0$, no $x$ satisfies the cost constraint, not even $x = 0$ — this is where
the non-negativity of $c_i$ matters, since it puts every attainable total cost at zero or above. The instance then has
no solution at all, and a correct solver must report that rather than return some $x$ anyway.

### A two-item instance

| Item | Cost $c_i$ | Volume $v_i$ | Calories $k_i$ | Max quantity $u_i$ |
|:---:|:---:|:---:|:---:|:---:|
| A | 2 | 1 | 10 | 1 |
| B | 1 | 2 | 6 | 1 |

with cost budget $C = 2$ and volume budget $V = 2$:

$$
\begin{aligned}
\max_{x} \quad & 10 x_A + 6 x_B \\
\text{s.t.} \quad & 2 x_A + x_B \le 2 \\
& x_A + 2 x_B \le 2 \\
& x_A, x_B \in \{0, 1\}
\end{aligned}
$$

[Chapter 02](#02--why-optimization-models-are-hard-to-test) solves it by hand.

## How to read the pseudocode

Chapters show tests as short, language-agnostic pseudocode, so the ideas transfer to any language. The conventions:

```
a = item(name="A", cost=2, volume=1, calories=10, max_quantity=1)

result = solve([a], cost_budget=2, volume_budget=2)

expect result.feasible == true
expect result.total_calories == 10
```

- `solve(items, cost_budget, volume_budget)` runs whichever solver is under test. When a chapter needs a specific
  one, it writes `enumeration_solver().solve(...)` or `mip_solver().solve(...)`.
- `result` has five fields: `feasible`, `quantities` (item name → units chosen), `total_calories`, `total_cost`, and
  `total_volume`. When `feasible` is false, the other fields carry no meaning.
- `expect` marks an assertion: the test fails if the condition is false. `==` on numbers means equal within a small
  numerical tolerance.

## Practice

Every chapter ends with a **Practice it** box linking to runnable exercises.

- **Python:** [training-testing-python — exercise 5](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md),
  which implements this knapsack with two solvers and ends with an untested shortest-path solver for you to test.
- **Java:** coming soon.

All practice repositories are listed in the [appendix](../appendix/practice-repositories.md).

---

## 01 — What to test in decision-support software

A decision-support system is more than its optimization model. Data arrives from other systems, business rules turn it
into model parameters, the model computes a decision, and the decision flows back to the people and systems that act
on it. Each of these parts can break. For most of them, the expected output is cheap to write down: you know what a
data check or a business rule should return before running it. The model is the exception, because its expected
output is the very thing it exists to compute. The chapter will map each part of the system to the kind of test that
fits it, and explain why the rest of this section, chapters 02–09, concentrates on the model.

> **Practice it**
>
> - Python: coming soon
> - Java: coming soon

---

## 02 — Why optimization models are hard to test

An [automated test](../appendix/glossary.md#automated-test) is a small program that runs your code on a known input
and checks the output against an expected answer. The textbook example is a calculator: `add(2, 3)` should return 5,
and you know that without reading a single line of `add`. The test is cheap to write because the expected answer is
cheap to compute.

Now try the same with a MIP. To write `expect result.total_calories == ???`, you need the optimal value. For any
instance large enough to be interesting, computing that value independently means solving the very problem the model
exists to solve. The test needs the answer before the code can provide it.

Whatever decides whether an output is correct is called a [test oracle](../appendix/glossary.md#test-oracle). For the
calculator, the oracle is arithmetic you already know. The difficulty of building an oracle when the correct output is
expensive, or impossible, to compute independently has a name in the software testing literature: the
[oracle problem](../appendix/glossary.md#oracle-problem).

You already know this asymmetry from optimization. Checking that a solution is *feasible* is cheap: substitute $x$
into each constraint. Proving that it is *optimal* is expensive: you need a matching bound, which is exactly what
branch-and-bound spends most of its time building. An oracle for feasibility is easy to write. An oracle for
optimality runs into the same wall your solver does.

The oracle problem is a reason to choose a testing technique deliberately, not a reason to skip testing. A model is
software: it gets refactored, its data changes, and eventually someone swaps its solver. Chapters 04–06 present three
kinds of oracle that work around the problem, each at a different cost.

The simplest oracle is a person. Take the [two-item instance](#a-two-item-instance): each $x_i \in \{0, 1\}$,
so there are $2 \times 2 = 4$ candidate selections, few enough to list.

| $x_A$ | $x_B$ | Cost (≤ 2) | Volume (≤ 2) | Calories | Feasible? |
|:---:|:---:|:---:|:---:|:---:|---|
| 0 | 0 | 0 | 0 | 0 | yes |
| 1 | 0 | 2 | 1 | 10 | yes |
| 0 | 1 | 1 | 2 | 6 | yes |
| 1 | 1 | 3 | 3 | 16 | no — both budgets exceeded |

The best feasible selection is $x_A = 1$, $x_B = 0$, worth 10 calories. Nobody needed a solver to produce that answer,
so it can serve as the expected value of a test:

```
a = item(name="A", cost=2, volume=1, calories=10, max_quantity=1)
b = item(name="B", cost=1, volume=2, calories=6,  max_quantity=1)

result = solve([a, b], cost_budget=2, volume_budget=2)

expect result.feasible == true
expect result.total_calories == 10
```

The price of a human oracle grows fast. The number of candidate selections is $\prod_{i \in I} (u_i + 1)$: 4 for this
instance, but $4^{30} \approx 1.2 \times 10^{18}$ for 30 items that can each be taken up to 3 times. A person can
only be the oracle at teaching scale, which is exactly how [chapter 04](#04--oracles-you-write-by-hand) uses one.

### Check yourself

1. For the calculator, what plays the role of the test oracle?
2. In the two-item instance, the cost budget rises from 2 to 3 and the volume budget stays at 2. What is the optimal
   calorie total?
3. How many candidate selections does an instance with three items and maximum quantities 1, 2, and 4 have?

<details>
<summary>Answers</summary>

1. Arithmetic you already know: you compute 2 + 3 in your head, independently of the code.
2. Still 10. Taking both items now fits the cost budget (3 ≤ 3) but uses volume 3 > 2, so item A alone remains best.
3. $2 \times 3 \times 5 = 30$.

</details>

### Where this stops working

> [!WARNING]
> The knapsack does not fully honour the claim of this chapter.

It is only *weakly* NP-hard: a pseudo-polynomial dynamic
program solves it exactly, so a cheap independent oracle does exist for this particular problem. The oracle problem
bites hardest on general MIPs, where no such shortcut is available. The knapsack is used here because it is small
enough to reason about by hand, not because it is the hardest case.

> **Practice it**
>
> - Python: [training-testing-python — exercise 5, Setup](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md#setup)
> - Java: coming soon

### Further reading

- Barr et al., ["The Oracle Problem in Software Testing: A Survey"](https://ieeexplore.ieee.org/document/6963470),
  IEEE Transactions on Software Engineering, 2015 — the survey that names and organizes the problem.
- [Test oracle](https://en.wikipedia.org/wiki/Test_oracle), Wikipedia — a short overview.

---

## 03 — Test the contract, not the algorithm

The function that "solves" a knapsack could be a brute-force enumeration, a greedy heuristic, a dynamic program, or a
call to a commercial or open-source MIP solver. That choice changes over time: today enumeration is fast enough;
next year the catalogue has thousands of items and someone swaps in a MIP solver.

When tests check *how* the answer was computed, a legitimate swap turns them red even though nothing a user cares about
got worse. A [regression](../appendix/glossary.md#regression) — a behavior that used to work and no longer does —
never happened, yet the tests report one. Teams in that situation learn to rewrite tests with every change, or to
ignore red tests altogether. Both defeat the purpose of having tests.

A [contract](../appendix/glossary.md#contract) is the promise a piece of code makes to its callers: what it needs as
input and what it guarantees as output, and nothing about how. Everything else — the algorithm, its running time, its
internal data structures — is an [implementation detail](../appendix/glossary.md#implementation-detail).

For the knapsack, the contract fits in one sentence: *given a catalogue of items and two budgets, return the
calorie-maximizing selection if one exists, or report that the instance is infeasible.* Two clauses make it precise:

1. When `feasible` is false, the other result fields carry no meaning.
2. When several selections tie for the best calorie total, any one of them may be returned.

You already make this separation in optimization. The formulation says *what* the optimal solution is; branch-and-bound,
cutting planes, or enumeration say *how* to find it. That is why you can swap solvers without rewriting the model. A
contract test checks the formulation's promise, so it runs unchanged against every solver that keeps it.

In code, a contract usually lives in an [abstraction](../appendix/glossary.md#abstraction): a named interface with a
single method, `solve`, that several implementations fulfil. In the Python exercise it is an abstract class with two
implementations, one enumerating every selection and one calling the HiGHS solver.

Writing contract tests first has a useful side effect. Each test is a question about the contract — "what does `solve`
promise when nothing is affordable?" — so the contract must be made explicit before any solver exists. It also pushes
the design toward modularity: a component that can be tested without looking at its internals is, by construction, a
component whose internals do not leak into its interface.

The same instance from [chapter 02](#02--why-optimization-models-are-hard-to-test), tested two ways. First, a test
coupled to the algorithm:

```
solver = enumeration_solver()
result = solver.solve([a, b], cost_budget=2, volume_budget=2)

expect solver.combinations_checked == 4      # how the answer was found
expect result.total_calories == 10
```

Replace `enumeration_solver()` with `mip_solver()` and this test breaks: a MIP solver never enumerates combinations,
so there is no count to check. The optimum is still 10, yet the test fails.

Second, a test against the contract:

```
for solver in [enumeration_solver(), mip_solver()]:
    result = solver.solve([a, b], cost_budget=2, volume_budget=2)

    expect result.feasible == true
    expect result.total_calories == 10
```

This test only calls `solve` and reads the promised fields. Running it against two very different solvers is itself
the evidence that it asserts on the contract: if it depended on either algorithm's internals, one of the two would
fail.

### Check yourself

1. Is "the solver finishes in under one second" part of the knapsack contract as stated above?
2. Two selections tie at 5 calories. Solver A returns one of them and solver B returns the other. Which contract test
   should fail?
3. Which assertion is about the contract: (a) `result.total_cost <= cost_budget`, or (b) "the MIP model has two
   constraints"?

<details>
<summary>Answers</summary>

1. No. Running time is an implementation detail here. If users need a time guarantee, it has to be written into the
   contract explicitly.
2. None. Clause 2 of the contract allows any optimal selection, so the test should assert only the calorie total.
3. (a). The number of constraints describes how one solver models the problem, not what `solve` promises.

</details>

### Where this stops working

> [!WARNING]
> Contract tests are a trade-off, not a free win.

They tell you *that* a solver is wrong, not *why*: a failing situation
does not point at the line that caused it. Tests written against an algorithm's internals — say, the table a dynamic
program fills — catch bugs earlier and closer to their cause. They are legitimate, as long as everyone agrees that they
may be deleted together with the algorithm they test. Keep them separate from the contract tests. What contract tests
buy in exchange is a suite that survives a solver swap, which in a production pipeline happens more often than most
test suites assume.

> **Practice it**
>
> - Python: [training-testing-python — exercise 5, Practice: the contract](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md#practice-the-contract)
> - Java: coming soon

### Further reading

- Robert C. Martin, ["Search for a Path"](https://blog.cleancoder.com/uncle-bob/2016/10/26/DijkstrasAlg.html) — the
  same idea applied to Dijkstra's shortest-path algorithm: tests written against the contract, ordered from degenerate
  cases up to complex ones.
- Vladimir Khorikov, *Unit Testing: Principles, Practices and Patterns* — discusses the same distinction under the
  names *observable behavior* and *implementation details*.

---

## 04 — Oracles you write by hand

[Chapter 02](#02--why-optimization-models-are-hard-to-test) showed that a person can solve a two-item instance by
hand. The harder question is *which* instances to write. Small instances picked at random tend to cover whatever comes
to mind first, which is usually the ordinary case. Bugs, however, cluster at the edges: an empty catalogue, a budget of
exactly zero, two items that tie. Without a method, those edges are left to luck.

This chapter uses the first of three oracle families that the rest of the section builds on:

| Oracle | How it decides whether an output is correct | Chapter |
|---|---|:---:|
| [Specified oracle](../appendix/glossary.md#specified-oracle) | The expected answer is stated in advance, worked out by a person | 04 |
| [Metamorphic relation](../appendix/glossary.md#metamorphic-relation) | A relation between two runs must hold, whatever their answers are | 05 |
| [Pseudo-oracle](../appendix/glossary.md#pseudo-oracle) | A second, independent implementation must agree | 06 |

A fourth kind comes for free in every test: an [implicit oracle](../appendix/glossary.md#implicit-oracle) catches what
is wrong in any program at all — a crash, a hang, a corrupted result. A solver that raises an error fails its test
regardless of what was asserted.

A specified oracle only needs a person and a small instance. To choose the instances, two standard techniques help:

- **[Equivalence partitioning](../appendix/glossary.md#equivalence-partitioning)** splits the input space into classes
  expected to behave the same way, then tests one instance per class.
- **[Boundary value analysis](../appendix/glossary.md#boundary-value-analysis)** adds instances exactly on the border
  between two classes, where behavior changes character.

If you have done sensitivity analysis, you have seen this structure. As you vary a right-hand side, the optimal basis
stays the same over a range, then changes at a breakpoint. The ranges are equivalence classes; the breakpoints are
boundary values. You would never probe sensitivity only in the middle of each range, and the same holds for tests.

Applied to the knapsack, the two techniques produce the table below, ordered from the simplest instance to the most
involved:

| # | Situation | Expected behavior |
|:---:|---|---|
| 1 | No items at all | Nothing to pick: a feasible, zero-calorie empty selection. |
| 2 | Negative cost budget | Even the empty selection violates the budget: infeasible. |
| 3 | Negative volume budget | The mirror of situation 2, for volume. |
| 4 | Budgets of exactly zero | The boundary between 2–3 and the rest: the empty selection still fits, but nothing can be added. |
| 5 | An item that may not be taken | An item with maximum quantity zero is ignored, however attractive its calories. |
| 6 | Nothing individually affordable | Every item exceeds a budget on its own; the empty selection is still feasible, worth zero. |
| 7 | Unique optimum | One item dominates the other; the basic case. |
| 8 | Only the cost budget binds | The optimum exhausts the cost budget and leaves volume unused. |
| 9 | Only the volume budget binds | The mirror of situation 8. |
| 10 | Both budgets bind at once | The optimum exhausts both budgets simultaneously. |
| 11 | Several optimal selections | Two interchangeable items tie; only the shared calorie total is asserted, never which item was picked. |
| 12 | More than one unit of an item | Quantities are genuine integers, not 0/1 choices in disguise. |
| 13 | One item individually unaffordable | An expensive item is excluded without disturbing the rest of the selection. |

Read situations 2 and 3 against 4 and 6. All four produce a zero-calorie answer of some kind, and only two of them are
infeasible. That distinction is exactly what a boundary is for.

Take one row of the table, situation 2, written as a specified-oracle test:

```
r = item(name="R", cost=1, volume=1, calories=10, max_quantity=5)

result = solve([r], cost_budget=-1, volume_budget=5)

expect result.feasible == false
```

The expected answer was derived by hand, without a solver: costs are non-negative, so every selection — including
taking nothing — costs at least 0, which is more than −1. No feasible selection exists. Notice what the test does
*not* assert: quantities and calories. The [contract](#03--test-the-contract-not-the-algorithm) says those fields
carry no meaning when the instance is infeasible, so asserting them would test a promise that was never made.

### Check yourself

1. One item with cost 1, a cost budget of 0, and a volume budget of 0. Feasible or infeasible?
2. Which situation would fail for a solver that treats every item as a take-it-or-leave-it (0/1) choice?
3. Why does situation 11 assert only the calorie total and not the quantities?

<details>
<summary>Answers</summary>

1. Feasible. The empty selection costs 0, which fits a budget of 0 (situation 4).
2. Situation 12.
3. The contract allows any optimal selection when several tie, so the chosen quantities may legitimately differ.

</details>

### Where this stops working

> [!WARNING]
> Thirteen situations pin down thirteen points in an input space that is effectively unbounded, and every one of them
> required a person to work out the answer first.

That is the ceiling of a specified oracle: it does not scale to a
catalogue of thousands of items, and it is not meant to. Its job is to fix expected behavior across a representative
slice of the input space. Two further assumptions are worth naming: the instances are small enough to solve by hand,
and the solver promises exact optimality. [Chapter 07](#07--when-optimality-is-not-guaranteed) drops the second one.

> **Practice it**
>
> - Python: [training-testing-python — exercise 5, Practice: situation tables](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md#practice-situation-tables)
> - Java: coming soon

### Further reading

- Maurício Aniche, *Effective Software Testing: A developer's guide* — covers equivalence partitioning and boundary
  analysis in depth, under the name specification-based testing.
- Barr et al., ["The Oracle Problem in Software Testing: A Survey"](https://ieeexplore.ieee.org/document/6963470),
  2015 — where specified, derived, and implicit oracles are defined.

---

## 05 — Metamorphic relations

Every expected answer in [chapter 04](#04--oracles-you-write-by-hand) required a person to work it out first. That
caps testing at instances small enough to enumerate by hand. The instances you care about in practice — a real
catalogue, a real network — are far beyond that, and no one can tell you their optimal value.

A [metamorphic relation](../appendix/glossary.md#metamorphic-relation) is a relation that must hold between the
outputs of two related runs, even when you know neither output. The recipe has three steps:

1. Take an instance, any instance.
2. Transform it in a way whose effect on the optimum you can prove.
3. Solve both versions and check that the relation holds.

In the survey's vocabulary, a metamorphic relation is a *derived* oracle: it derives correctness from a relation
rather than from a known answer.

You already prove relations like these as theorems. Relaxing a constraint cannot make the optimal value worse — the
same reasoning that makes an LP relaxation a valid bound. A metamorphic relation turns such a theorem into a test. For
the knapsack, four of them hold on every instance:

| Transformation | Relation on the optimal calorie total | Why it holds |
|---|---|---|
| Add an item to the catalogue | Never decreases | Every previous selection is still available, with the new item at quantity zero. |
| Raise the cost or volume budget | Never decreases | Relaxing a constraint only enlarges the feasible region. |
| Multiply every calorie count by $k > 0$ | Scales by exactly $k$ | The feasible region is unchanged; only the objective is rescaled. |
| Cap an item's maximum quantity at zero | Equals the value with that item removed | An item that may not be taken cannot take part in any selection. |

None of the four compares the selected quantities. A transformation can turn a near-tie into an exact tie, and the
[contract](#03--test-the-contract-not-the-algorithm) never promised which selection wins among equals.

Written as a test, the first relation — raising a budget never decreases the optimum — looks like this:

```
a = item(name="A", cost=2, volume=1, calories=10, max_quantity=2)
b = item(name="B", cost=1, volume=2, calories=6,  max_quantity=1)
c = item(name="C", cost=3, volume=1, calories=14, max_quantity=1)

before = solve([a, b, c], cost_budget=5, volume_budget=4)
after  = solve([a, b, c], cost_budget=8, volume_budget=4)

expect after.total_calories >= before.total_calories
```

The optimum of the first instance happens to be 26 calories (two units of A plus one of B), but the test never needs
to know that. The same three lines work unchanged on a catalogue of four thousand items, which is what makes
metamorphic relations the part of this toolkit that scales.

### Check yourself

1. You double every item's cost. Does the optimal calorie total never decrease, never increase, or neither?
2. A broken solver always returns a feasible, empty selection worth 0 calories. Which of the four relations does it
   violate?
3. You remove an item from the catalogue. What happens to the optimal calorie total?

<details>
<summary>Answers</summary>

1. Never increases. With non-negative costs, every selection that fits the doubled costs also fit the original ones,
   so the feasible region can only shrink.
2. None of them: 0 ≥ 0, 0 = k × 0, and 0 = 0. See the next section.
3. It never increases — the reverse of adding an item.

</details>

### Where this stops working

- **Consistency is not correctness.** A solver that always answers 0 satisfies all four relations. Metamorphic
  relations check that runs agree with each other, not that any single run is right, so they complement the specified
  oracles of chapter 04 rather than replace them.
- **They are theorems about the optimal value.** They hold for a solver that promises exact optimality. A heuristic can
  violate them without being broken, as [chapter 07](#07--when-optimality-is-not-guaranteed) shows.
- **Numerical tolerance.** "Scales by exactly $k$" means within a small tolerance once calorie counts are real numbers.

> **Practice it**
>
> - Python: [training-testing-python — exercise 5, Practice: metamorphic relations](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md#practice-metamorphic-relations)
> - Java: coming soon

### Further reading

- T. Y. Chen et al., "Metamorphic Testing: A Review of Challenges and Opportunities," *ACM Computing Surveys*, 2018 —
  a broad review of the technique and where it has been applied.

---

## 06 — Differential testing

The relations of [chapter 05](#05--metamorphic-relations) check that runs are consistent with each other, but a model
can be consistently wrong. The mistakes that matter most in practice live in the formulation: a coefficient attached to
the wrong sum, a budget applied to the wrong constraint, an index set that silently drops an item. The solver then
optimizes the wrong model faithfully.

It is worth being precise here. A mature MIP solver such as HiGHS is very unlikely to compute a wrong optimum for the
model it was given. The realistic risk is that the model does not say what you meant.

A [pseudo-oracle](../appendix/glossary.md#pseudo-oracle) is a second, independent implementation of the same contract.
[Differential testing](../appendix/glossary.md#differential-testing) runs both implementations on the same inputs and
compares their outputs. For small knapsack instances, brute-force enumeration makes a good pseudo-oracle: it is slow,
but correct by inspection. When it disagrees with the MIP solver, the disagreement points at the formulation.

This is the disciplined version of a sanity check most modelers already run informally — "let me compare my new model
against brute force on a toy case." Three details turn that habit into a reliable test:

1. **Generate many instances instead of picking a few.** Hundreds of small random instances explore corners that
   nobody would think to write by hand, including infeasible ones if the generator draws negative budgets.
2. **Fix the [random seed](../appendix/glossary.md#random-seed).** Reproducibility works here the way it does in a
   controlled experiment: the same inputs must always produce the same outputs. A failure that vanishes on the retry
   cannot be investigated, so the test must also report the instance that failed.
3. **Compare only what the contract promises.** Feasibility and the calorie total, never the selected quantities. When
   several selections tie, the [contract](#03--test-the-contract-not-the-algorithm) allows the two implementations to
   return different ones.

In code, the comparison over generated instances looks like this:

```
rng = random_generator(seed=20260908)

repeat 200 times:
    items = a list of rng.integer(1, 4) items, each with
                cost = rng.integer(0, 5),  volume = rng.integer(0, 5),
                calories = rng.integer(0, 20),  max_quantity = rng.integer(1, 3)
    cost_budget   = rng.integer(-1, 8)
    volume_budget = rng.integer(-1, 8)

    reference = enumeration_solver().solve(items, cost_budget, volume_budget)
    candidate = mip_solver().solve(items, cost_budget, volume_budget)

    expect candidate.feasible == reference.feasible
    if reference.feasible:
        expect candidate.total_calories == reference.total_calories
```

The largest generated instance has 4 items with up to 4 quantity values each, so enumeration checks at most
$4^4 = 256$ selections. The reference stays cheap.

What does this catch that chapter 04 does not? Suppose the formulation mistakenly uses each item's volume in the cost
constraint. Some of the thirteen hand-written situations will catch that mistake and some will not, because they were
chosen to cover the contract, not this particular error. A sweep over 200 generated instances is far more likely to hit
one that exposes it. Neither approach guarantees detection; the difference is how reliably each one finds a mistake
that nobody anticipated.

### Check yourself

1. The candidate selects item E and the reference selects item F. Both are worth 5 calories. Should the test fail?
2. Why is the random seed fixed rather than drawn fresh on every run?
3. Why is enumeration a good reference for 4 items but not for 50?

<details>
<summary>Answers</summary>

1. No. The contract allows any optimal selection when several tie; only feasibility and the calorie total are compared.
2. So that a failure reproduces on the next run and can be investigated.
3. The number of selections grows as $\prod_i (u_i + 1)$ — already about $1.3 \times 10^{30}$ for 50 items with up to
   3 units each.

</details>

### Where this stops working

- **The reference must stay tractable.** Differential testing against enumeration lives in the same small-instance
  regime as chapter 04. It broadens coverage considerably within that regime; it does not reach the large instances
  where you would most want an answer.
- **The two implementations must be independent.** If both share the same misunderstanding of the problem — say, both
  treat every item as a 0/1 choice — they agree with each other and are both wrong. A pseudo-oracle only protects
  against mistakes the two implementations do not have in common.

> **Practice it**
>
> - Python: [training-testing-python — exercise 5, Practice: differential testing](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md#practice-differential-testing)
> - Java: coming soon

### Further reading

- William M. McKeeman, "Differential Testing for Software," *Digital Technical Journal*, 1998 — the paper that named
  the technique.
- [Hypothesis](https://hypothesis.readthedocs.io/) — a [property-based testing](../appendix/glossary.md#property-based-testing)
  library for Python. It generates instances like the loop above and, when one fails, automatically
  [shrinks](../appendix/glossary.md#shrinking) it to the smallest input that still fails, which on generated instances
  is most of the debugging work.

---

## 07 — When optimality is not guaranteed

Every expected answer in [chapter 04](#04--oracles-you-write-by-hand) and every relation in
[chapter 05](#05--metamorphic-relations) assumes that the solver returns a truly optimal answer. That assumption fails
for a [heuristic](../appendix/glossary.md#heuristic): a method that gives up the guarantee of optimality on purpose, in
exchange for finishing in reasonable time on instances too large to solve exactly.

It also fails, less visibly, for an exact MIP solver with a time limit. When the clock runs out, the solver returns its
best incumbent and an optimality gap. From the contract's point of view, that solver is a heuristic. Testing either one
against "did you find the exact optimum" fails it for doing precisely what it was designed to do.

Start again from the [contract](#03--test-the-contract-not-the-algorithm). A heuristic's contract is weaker:

- return a *feasible* selection, or report infeasibility when no selection exists;
- its calorie total is at most the optimum;
- if, and only if, the method carries an approximation guarantee, its calorie total is at least a known fraction of the
  optimum.

A test survives exactly as far as it checks something this weaker contract still promises. This is the asymmetry from
[chapter 02](#02--why-optimization-models-are-hard-to-test) coming back: tests that rely on *feasibility* survive
untouched, because checking feasibility never needed the optimum. Tests that rely on *optimality* must be weakened into
bounds, or dropped.

**Specified oracles (chapter 04).** One reasonable sorting of the thirteen situations:

| Verdict | Situations | Why |
|---|:---:|---|
| Unchanged | 1, 2, 3, 4, 6 | The feasible region is empty or holds a single selection (the empty one), so any correct solver is forced to the same answer. |
| Weakened | 5, 8, 9, 10, 13 | The feasibility half survives — the capped item and the unaffordable item stay at zero, and budgets are respected. The claims about the optimal total or about which budget binds do not. |
| Lose their purpose | 7, 11, 12 | They exist to check which value is optimal. Weakened to feasibility, they only repeat the rows above. |

**Metamorphic relations (chapter 05).** These are theorems about the optimal value, not about algorithms, so they do
not transfer automatically. A perfectly correct heuristic can violate them — the worked example below shows one. What
survives is applying a feasibility check to every transformed instance.

**Differential testing (chapter 06).** It survives in weakened form. Keep the exact reference and compare
`candidate.feasible == reference.feasible` and `candidate.total_calories <= reference.total_calories`, plus a floor
if the heuristic has a guarantee.

Take a greedy heuristic that sorts items by calories per unit of cost and takes each one while it still fits. One item, a
cost budget of 2, and a volume budget of 10 that never binds:

```
a = item(name="A", cost=2, volume=1, calories=10, max_quantity=1)
d = item(name="D", cost=1, volume=1, calories=6,  max_quantity=1)

before = greedy_solver().solve([a],    cost_budget=2, volume_budget=10)   # takes A: 10 calories
after  = greedy_solver().solve([a, d], cost_budget=2, volume_budget=10)   # takes D first (6 per unit of cost
                                                                          # beats 5), then A no longer fits: 6
expect after.total_calories >= before.total_calories                      # fails: 6 < 10
```

The relation "adding an item never decreases the optimum" still holds for the optimum itself, which stays at 10. It is
the heuristic that dropped to 6, and it did so while behaving exactly as designed. The test that fits its weaker
contract is a bound against an exact reference:

```
exact = enumeration_solver().solve([a, d], cost_budget=2, volume_budget=10)

expect after.feasible == exact.feasible
expect after.total_calories <= exact.total_calories
```

### Check yourself

1. A MIP solver reaches its 60-second time limit and returns an incumbent with a 3% gap. Should the exact-value
   assertion of situation 7 apply to it?
2. Does situation 2 (negative cost budget → infeasible) still hold for a heuristic?
3. On the same instance, a heuristic reports 12 calories and enumeration reports 10. Is that a bug?

<details>
<summary>Answers</summary>

1. No. Under a time limit the solver is a heuristic for contract purposes: assert feasibility and a bound, or use
   instances small enough to guarantee it finishes.
2. Yes. No feasible selection exists, so any correct solver must report infeasibility.
3. Yes. No feasible selection can beat the optimum, so either the heuristic's selection is infeasible or its totals are
   miscomputed.

</details>

### Where this stops working

- **Bounds are weak tests.** "At most the optimum" is satisfied by returning the empty selection every time. Without an
  approximation guarantee there is no floor to assert. One practical option is to track solution quality as a
  benchmark over time — the average gap to the exact reference, say — rather than as a pass/fail test.
- **An exact reference is still needed** for the weakened differential test, so it remains limited to small instances,
  as in [chapter 06](#06--differential-testing).

> **Practice it**
>
> - Python: [training-testing-python — exercise 5, Your turn: shortest path](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md#your-turn-shortest-path) — apply chapters 04–06 to an untested solver
> - Java: coming soon

### Further reading

- David P. Williamson and David B. Shmoys, *The Design of Approximation Algorithms* (Cambridge University Press, 2011)
  — where approximation guarantees, the floor a heuristic test can assert, come from.

---

## 08 — Duality as an oracle

[Chapter 02](#02--why-optimization-models-are-hard-to-test) argued that checking feasibility is cheap while proving
optimality is expensive. Linear programming is the exception worth a chapter of its own. By strong duality, a primal
feasible solution and a dual feasible solution with equal objective values prove each other optimal. A test can
therefore ask the solver for both, and verify optimality with a few matrix-vector products — an oracle that checks
rather than computes.

> **Practice it**
>
> - Python: [training-testing-python — exercise 4](https://github.com/sefop/training-testing-python/tree/main/exercises/4-testing-lp-single-objective) (in preparation)
> - Java: coming soon

---

## 09 — Testing a Pareto front

With two or more objectives, a solver returns a set of trade-offs rather than one answer, and most of the assertions in
this section have nothing to compare against. The chapter will cover properties that a correct Pareto front must satisfy
regardless of the instance — for example, that no returned solution dominates another, and that the ends of the front
agree with the corresponding lexicographic single-objective optima.

> **Practice it**
>
> - Python: [training-testing-python — exercise 6](https://github.com/sefop/training-testing-python/tree/main/exercises/6-testing-mip-multi-objective) (in preparation)
> - Java: coming soon

---

## What this section does not cover

- **Performance and scale.** No chapter tests how fast a solver is or how large an instance it handles.
- **Input validation.** Items are never checked for nonsense values such as a negative cost. Every infeasible
  instance in this section comes from the budgets, never from a malformed item.
- **Continuous and multi-objective models**, until chapters 08 and 09.

---

[← Book contents](../../README.md) · [Next section: 06 Deploying decision-support software →](../06-deployment/README.md)
