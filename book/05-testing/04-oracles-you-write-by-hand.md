# 04 — Oracles you write by hand

> **Audience:** Scientists · **Prerequisites:** [02](02-why-optimization-models-are-hard-to-test.md), [03](03-test-the-contract-not-the-algorithm.md) · **~10 min read**

After this chapter you can choose a small, systematic set of instances, work out their answers by hand, and turn each
one into a contract test.

## The problem

[Chapter 02](02-why-optimization-models-are-hard-to-test.md) showed that a person can solve a two-item instance by
hand. The harder question is *which* instances to write. Small instances picked at random tend to cover whatever comes
to mind first, which is usually the ordinary case. Bugs, however, cluster at the edges: an empty catalogue, a budget of
exactly zero, two items that tie. Without a method, those edges are left to luck.

## The idea

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

## Worked example

One row of the table, situation 2, as a specified-oracle test:

```
r = item(name="R", cost=1, volume=1, calories=10, max_quantity=5)

result = solve([r], cost_budget=-1, volume_budget=5)

expect result.feasible == false
```

The expected answer was derived by hand, without a solver: costs are non-negative, so every selection — including
taking nothing — costs at least 0, which is more than −1. No feasible selection exists. Notice what the test does
*not* assert: quantities and calories. The [contract](03-test-the-contract-not-the-algorithm.md) says those fields
carry no meaning when the instance is infeasible, so asserting them would test a promise that was never made.

## Check yourself

1. One item with cost 1, a cost budget of 0, and a volume budget of 0. Feasible or infeasible?
2. Which situation would fail for a solver that treats every item as a take-it-or-leave-it (0/1) choice?
3. Why does situation 11 assert only the calorie total and not the quantities?

<details>
<summary>Answers</summary>

1. Feasible. The empty selection costs 0, which fits a budget of 0 (situation 4).
2. Situation 12.
3. The contract allows any optimal selection when several tie, so the chosen quantities may legitimately differ.

</details>

## Where this stops working

Thirteen situations pin down thirteen points in an input space that is effectively unbounded, and every one of them
required a person to work out the answer first. That is the ceiling of a specified oracle: it does not scale to a
catalogue of thousands of items, and it is not meant to. Its job is to fix expected behavior across a representative
slice of the input space. Two further assumptions are worth naming: the instances are small enough to solve by hand,
and the solver promises exact optimality. [Chapter 07](07-when-optimality-is-not-guaranteed.md) drops the second one.

> **Practice it**
> - Python: [training-testing-python — exercise 5, Practice: situation tables](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md#practice-situation-tables)
> - Java: coming soon

## Further reading

- Maurício Aniche, *Effective Software Testing: A developer's guide* — covers equivalence partitioning and boundary
  analysis in depth, under the name specification-based testing.
- Barr et al., ["The Oracle Problem in Software Testing: A Survey"](https://ieeexplore.ieee.org/document/6963470),
  2015 — where specified, derived, and implicit oracles are defined.

---

[← 03 Test the contract, not the algorithm](03-test-the-contract-not-the-algorithm.md) · [Next: 05 Metamorphic relations →](05-metamorphic-relations.md)
