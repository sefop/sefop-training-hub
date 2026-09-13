# 06 — Differential testing

> **Audience:** Scientists · **Prerequisites:** [03](03-test-the-contract-not-the-algorithm.md), [05](05-metamorphic-relations.md) · **~9 min read**

After this chapter you can use a slow, obviously correct implementation to catch mistakes in the formulation you hand
to a solver.

## The problem

The relations of [chapter 05](05-metamorphic-relations.md) check that runs are consistent with each other, but a model
can be consistently wrong. The mistakes that matter most in practice live in the formulation: a coefficient attached to
the wrong sum, a budget applied to the wrong constraint, an index set that silently drops an item. The solver then
optimizes the wrong model faithfully.

It is worth being precise here. A mature MIP solver such as HiGHS is very unlikely to compute a wrong optimum for the
model it was given. The realistic risk is that the model does not say what you meant.

## The idea

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
   several selections tie, the [contract](03-test-the-contract-not-the-algorithm.md) allows the two implementations to
   return different ones.

## Worked example

Comparing two implementations over generated instances:

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

## Check yourself

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

## Where this stops working

- **The reference must stay tractable.** Differential testing against enumeration lives in the same small-instance
  regime as chapter 04. It broadens coverage considerably within that regime; it does not reach the large instances
  where you would most want an answer.
- **The two implementations must be independent.** If both share the same misunderstanding of the problem — say, both
  treat every item as a 0/1 choice — they agree with each other and are both wrong. A pseudo-oracle only protects
  against mistakes the two implementations do not have in common.

> **Practice it**
> - Python: [training-testing-python — exercise 5, Practice: differential testing](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md#practice-differential-testing)
> - Java: coming soon

## Further reading

- William M. McKeeman, "Differential Testing for Software," *Digital Technical Journal*, 1998 — the paper that named
  the technique.
- [Hypothesis](https://hypothesis.readthedocs.io/) — a [property-based testing](../appendix/glossary.md#property-based-testing)
  library for Python. It generates instances like the loop above and, when one fails, automatically
  [shrinks](../appendix/glossary.md#shrinking) it to the smallest input that still fails, which on generated instances
  is most of the debugging work.

---

[← 05 Metamorphic relations](05-metamorphic-relations.md) · [Next: 07 When optimality is not guaranteed →](07-when-optimality-is-not-guaranteed.md)
