# 05 — Metamorphic relations

> **Audience:** Scientists · **Prerequisites:** [04](04-oracles-you-write-by-hand.md) · **~8 min read**

After this chapter you can test a model on instances whose optimal value nobody knows.

## The problem

Every expected answer in [chapter 04](04-oracles-you-write-by-hand.md) required a person to work it out first. That
caps testing at instances small enough to enumerate by hand. The instances you care about in practice — a real
catalogue, a real network — are far beyond that, and no one can tell you their optimal value.

## The idea

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
[contract](03-test-the-contract-not-the-algorithm.md) never promised which selection wins among equals.

## Worked example

One relation — raising a budget never decreases the optimum:

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

## Check yourself

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

## Where this stops working

- **Consistency is not correctness.** A solver that always answers 0 satisfies all four relations. Metamorphic
  relations check that runs agree with each other, not that any single run is right, so they complement the specified
  oracles of chapter 04 rather than replace them.
- **They are theorems about the optimal value.** They hold for a solver that promises exact optimality. A heuristic can
  violate them without being broken, as [chapter 07](07-when-optimality-is-not-guaranteed.md) shows.
- **Numerical tolerance.** "Scales by exactly $k$" means within a small tolerance once calorie counts are real numbers.

> **Practice it**
> - Python: [training-testing-python — exercise 5, Practice: metamorphic relations](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md#practice-metamorphic-relations)
> - Java: coming soon

## Further reading

- T. Y. Chen et al., "Metamorphic Testing: A Review of Challenges and Opportunities," *ACM Computing Surveys*, 2018 —
  a broad review of the technique and where it has been applied.

---

[← 04 Oracles you write by hand](04-oracles-you-write-by-hand.md) · [Next: 06 Differential testing →](06-differential-testing.md)
