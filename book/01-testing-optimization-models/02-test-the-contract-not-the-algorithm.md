# 02 — Test the contract, not the algorithm

> **Audience:** Scientists & Engineering Managers · **Prerequisites:** [01](01-why-optimization-models-are-hard-to-test.md) · **~8 min read**

After this chapter you can write tests that keep passing when someone replaces the algorithm behind your model.

## The problem

The function that "solves" a knapsack could be a brute-force enumeration, a greedy heuristic, a dynamic program, or a
call to a commercial or open-source MIP solver. That choice changes over time: today enumeration is fast enough;
next year the catalogue has thousands of items and someone swaps in a MIP solver.

When tests check *how* the answer was computed, a legitimate swap turns them red even though nothing a user cares about
got worse. A [regression](../appendix/glossary.md#regression) — a behavior that used to work and no longer does —
never happened, yet the tests report one. Teams in that situation learn to rewrite tests with every change, or to
ignore red tests altogether. Both defeat the purpose of having tests.

## The idea

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

## Worked example

The same instance from [chapter 01](01-why-optimization-models-are-hard-to-test.md), tested two ways. First, a test
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

## Check yourself

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

## Where this stops working

Contract tests are a trade-off, not a free win. They tell you *that* a solver is wrong, not *why*: a failing situation
does not point at the line that caused it. Tests written against an algorithm's internals — say, the table a dynamic
program fills — catch bugs earlier and closer to their cause. They are legitimate, as long as everyone agrees that they
may be deleted together with the algorithm they test. Keep them separate from the contract tests. What contract tests
buy in exchange is a suite that survives a solver swap, which in a production pipeline happens more often than most
test suites assume.

> **Practice it**
> - Python: [training-testing-python — exercise 5, Practice: the contract](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md#practice-the-contract)
> - Java: coming soon

## Further reading

- Robert C. Martin, ["Search for a Path"](https://blog.cleancoder.com/uncle-bob/2016/10/26/DijkstrasAlg.html) — the
  same idea applied to Dijkstra's shortest-path algorithm: tests written against the contract, ordered from degenerate
  cases up to complex ones.
- Vladimir Khorikov, *Unit Testing: Principles, Practices and Patterns* — discusses the same distinction under the
  names *observable behavior* and *implementation details*.

---

[← 01 Why optimization models are hard to test](01-why-optimization-models-are-hard-to-test.md) · [Next: 03 Oracles you write by hand →](03-oracles-you-write-by-hand.md)
