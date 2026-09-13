# 06 — When optimality is not guaranteed

> **Audience:** Scientists · **Prerequisites:** [03](03-oracles-you-write-by-hand.md), [04](04-metamorphic-relations.md), [05](05-differential-testing.md) · **~9 min read**

After this chapter you can decide which of your tests still apply when the solver is a heuristic, or a MIP solver
stopped by a time limit.

## The problem

Every expected answer in [chapter 03](03-oracles-you-write-by-hand.md) and every relation in
[chapter 04](04-metamorphic-relations.md) assumes that the solver returns a truly optimal answer. That assumption fails
for a [heuristic](../appendix/glossary.md#heuristic): a method that gives up the guarantee of optimality on purpose, in
exchange for finishing in reasonable time on instances too large to solve exactly.

It also fails, less visibly, for an exact MIP solver with a time limit. When the clock runs out, the solver returns its
best incumbent and an optimality gap. From the contract's point of view, that solver is a heuristic. Testing either one
against "did you find the exact optimum" fails it for doing precisely what it was designed to do.

## The idea

Start again from the [contract](02-test-the-contract-not-the-algorithm.md). A heuristic's contract is weaker:

- return a *feasible* selection, or report infeasibility when no selection exists;
- its calorie total is at most the optimum;
- if, and only if, the method carries an approximation guarantee, its calorie total is at least a known fraction of the
  optimum.

A test survives exactly as far as it checks something this weaker contract still promises. This is the asymmetry from
[chapter 01](01-why-optimization-models-are-hard-to-test.md) coming back: tests that rely on *feasibility* survive
untouched, because checking feasibility never needed the optimum. Tests that rely on *optimality* must be weakened into
bounds, or dropped.

**Specified oracles (chapter 03).** One reasonable sorting of the thirteen situations:

| Verdict | Situations | Why |
|---|:---:|---|
| Unchanged | 1, 2, 3, 4, 6 | The feasible region is empty or holds a single selection (the empty one), so any correct solver is forced to the same answer. |
| Weakened | 5, 8, 9, 10, 13 | The feasibility half survives — the capped item and the unaffordable item stay at zero, and budgets are respected. The claims about the optimal total or about which budget binds do not. |
| Lose their purpose | 7, 11, 12 | They exist to check which value is optimal. Weakened to feasibility, they only repeat the rows above. |

**Metamorphic relations (chapter 04).** These are theorems about the optimal value, not about algorithms, so they do
not transfer automatically. A perfectly correct heuristic can violate them — the worked example below shows one. What
survives is applying a feasibility check to every transformed instance.

**Differential testing (chapter 05).** It survives in weakened form. Keep the exact reference and compare
`candidate.feasible == reference.feasible` and `candidate.total_calories <= reference.total_calories`, plus a floor
if the heuristic has a guarantee.

## Worked example

A greedy heuristic that sorts items by calories per unit of cost and takes each one while it still fits. One item, a
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

## Check yourself

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

## Where this stops working

- **Bounds are weak tests.** "At most the optimum" is satisfied by returning the empty selection every time. Without an
  approximation guarantee there is no floor to assert. One practical option is to track solution quality as a
  benchmark over time — the average gap to the exact reference, say — rather than as a pass/fail test.
- **An exact reference is still needed** for the weakened differential test, so it remains limited to small instances,
  as in [chapter 05](05-differential-testing.md).

> **Practice it**
> - Python: [training-testing-python — exercise 5, Your turn: shortest path](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md#your-turn-shortest-path) — apply chapters 03–05 to an untested solver
> - Java: coming soon

## Further reading

- David P. Williamson and David B. Shmoys, *The Design of Approximation Algorithms* (Cambridge University Press, 2011)
  — where approximation guarantees, the floor a heuristic test can assert, come from.

---

[← 05 Differential testing](05-differential-testing.md) · [Next: 07 Duality as an oracle →](07-duality-as-an-oracle.md)
