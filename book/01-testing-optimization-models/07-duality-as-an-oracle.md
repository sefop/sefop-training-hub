# 07 — Duality as an oracle

> **Audience:** Scientists · **Prerequisites:** [01](01-why-optimization-models-are-hard-to-test.md), [02](02-test-the-contract-not-the-algorithm.md) · **Status: coming soon**

After this chapter you will be able to check a linear program's claimed optimum with a certificate, instead of solving
it a second time.

## Planned content

[Chapter 01](01-why-optimization-models-are-hard-to-test.md) argued that checking feasibility is cheap while proving
optimality is expensive. Linear programming is the exception worth a chapter of its own. By strong duality, a primal
feasible solution and a dual feasible solution with equal objective values prove each other optimal. A test can
therefore ask the solver for both, and verify optimality with a few matrix-vector products — an oracle that checks
rather than computes.

> **Practice it**
> - Python: [training-testing-python — exercise 4](https://github.com/sefop/training-testing-python/tree/main/exercises/4-testing-lp-single-objective) (in preparation)
> - Java: coming soon

---

[← 06 When optimality is not guaranteed](06-when-optimality-is-not-guaranteed.md) · [Next: 08 Testing a Pareto front →](08-testing-a-pareto-front.md)
