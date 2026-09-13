# 01 — What to test in decision-support software

> **Audience:** Scientists & Engineering Managers · **Prerequisites:** none · **Status: coming soon**

After this chapter you will be able to name the parts of a decision-support system that need tests, and say which kind
of test fits each one.

## Planned content

A decision-support system is more than its optimization model. Data arrives from other systems, business rules turn it
into model parameters, the model computes a decision, and the decision flows back to the people and systems that act
on it. Each of these parts can break. For most of them, the expected output is cheap to write down: you know what a
data check or a business rule should return before running it. The model is the exception, because its expected
output is the very thing it exists to compute. The chapter will map each part of the system to the kind of test that
fits it, and explain why the rest of this section, chapters 02–09, concentrates on the model.

> **Practice it**
> - Python: coming soon
> - Java: coming soon

---

[← Section 05 overview](README.md) · [Next: 02 Why optimization models are hard to test →](02-why-optimization-models-are-hard-to-test.md)
