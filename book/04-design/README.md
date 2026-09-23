# Section 04 — Designing decision-support software

> **Status:** planned. No chapters yet; this page collects the ideas the section will develop. Working titles may
> change before the first chapter is written.

## Introduction

A decision-support system is built from parts that change at different speeds. The data changes every run, business
rules change every few months, the formulation changes as the team learns the problem, and the solver may change once
in the system's life. **The difference this section addresses:** when those parts are tangled in one script, every
change to one of them risks breaking the others. Design is the practice of drawing boundaries between them.

### Ideas to develop

- **Modularity through solver swapping.** Modularity means building a system from parts that can be replaced one at a
  time. Operations research scientists already practise it when they swap a solver without touching the formulation;
  the chapters extend the same habit to data, rules, and output.
- **A tangled script as the starting point.** The Purdue 2026 workshop's
  [`code_smell.py`](../../workshops/2026-06-29-purdue/code_smell.py) mixes every concern in one place, so nothing can be
  tested without running everything else. Useful as a local illustration of what tangling looks like, not as the
  section's running example.
- **The shared running example.** The cargo loading system in
  [the appendix](../appendix/running-example.md) is what this section designs: the same decision Section 05 tests,
  surrounded by data loading, business rules, and reporting.
- **Design and testing reinforce each other.** A component that can be tested without looking at its internals is, by
  construction, a component whose internals do not leak into its interface (Section 05, chapter 03).
- **Reference implementations** in `sefop-python-starter`, `sefop-python-advanced`, and `sefop-java-advanced` can show
  each boundary in working code.
- **A trade-off to state honestly:** more boundaries mean more files and more indirection. For a two-week prototype, one
  script may be the right design.
- **Dependency injection**: develop this.
- SOLID principles
- Coupling and Cohesion

### Out of scope

- **User-interface design** and **enterprise architecture** beyond a single decision-support system.

## Planned chapters

| # | Working title | After it you can… |
|:---:|---|---|
| 01 | The parts of a decision-support system | Name the components of a system — data input, validation, business rules, model building, solving, and output — and draw the boundaries between them |
| 02 | Separate the model from the solver | Swap solvers without rewriting the model |
| 03 | Keep data out of the formulation | Load and validate data before it reaches the model, so the formulation only sees clean parameters |
| 04 | Keep business rules visible | Place business rules where the business can review them, apart from the mathematics |
| 05 | Design for reproducibility | Make the same inputs always produce the same decision, like a controlled experiment |
| 06 | Conclusion | Recall in one page where the boundaries of a decision-support system go, and what each one buys |

---

[← Book contents](../../README.md) · [Next section: 05 Testing decision-support software →](../05-testing/README.md)
