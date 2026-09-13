# 08 — Testing a Pareto front

> **Audience:** Scientists · **Prerequisites:** [03](03-oracles-you-write-by-hand.md), [04](04-metamorphic-relations.md) · **Status: coming soon**

After this chapter you will be able to test a multi-objective model, where there is no single optimal value to compare
against.

## Planned content

With two or more objectives, a solver returns a set of trade-offs rather than one answer, and most of the assertions in
this part have nothing to compare against. The chapter will cover properties that a correct Pareto front must satisfy
regardless of the instance — for example, that no returned solution dominates another, and that the ends of the front
agree with the corresponding lexicographic single-objective optima.

> **Practice it**
> - Python: [training-testing-python — exercise 6](https://github.com/sefop/training-testing-python/tree/main/exercises/6-testing-mip-multi-objective) (in preparation)
> - Java: coming soon

---

[← 07 Duality as an oracle](07-duality-as-an-oracle.md) · [Part 01 overview](README.md) · [Book contents](../../README.md)
