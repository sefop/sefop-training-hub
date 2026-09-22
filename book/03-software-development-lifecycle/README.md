# Section 03 — The lifecycle of decision-support software

> **Status:** planned. No chapters yet; this page collects the ideas the section will develop. Working titles may
> change before the first chapter is written.

## Introduction

### Motivation

Every piece of software moves through the same broad phases: someone states what it must do, designs it, builds and
tests it, deploys it, and then maintains it for as long as it is used. That sequence is the **software development
lifecycle**. Decision-support software moves through the same phases, but each phase has a twist that ordinary business
software does not. This section names those differences. It is the map of the book: each section after this one takes
one phase and addresses its difference.

### Ideas to develop

- **A difference table**, one row per phase. These are working hypotheses, to be checked against the literature and
  against practice before the chapter is written:

  | Phase | Ordinary business software | Decision-support software | Section |
  |---|---|---|:---:|
  | Requirements | Stated as features the business can describe | Partly an objective and constraints the business cannot state precisely; the formulation is discovered by iterating | 04 |
  | Design | Logic is mostly business rules | Data, business rules, the model, and the solver change at different speeds and are owned by different people | 04 |
  | Testing | The expected output is known in advance | The expected output is the very thing the model computes (the oracle problem) | 05 |
  | Deployment and operation | Same input, same output, in predictable time | Run time and solution quality vary with each instance; a failure can be a silently worse decision rather than a crash | 06 |
  | Maintenance | Code written as a product from the start | Code often grows out of a research prototype or a notebook | 07 |
  | People | Built by software engineers | Built by scientists trained in modelling, not in software engineering | 08 |

- **Iteration as gradient descent.** Each pass through the lifecycle gives information for the next, the way each step
  of gradient descent uses the gradient at the current point. A formulation is rarely right on the first pass, which is
  why the lifecycle of decision-support software is a loop rather than a line.
- **The lifecycle does not end at deployment.** A model that runs weekly for five years spends most of its life in
  operation and maintenance, not in development.

### Out of scope

- **A comparison of process frameworks** such as Scrum or Kanban. The section describes phases, not a particular way
  of running them.

## Who this section is for

Scientists and managers alike. Read it before Sections 04–09 if you want to see how they fit together; skip it if you
arrived for a specific practice.

## Planned chapters

| # | Working title | After it you can… |
|:---:|---|---|
| 01 | The software development lifecycle | Name the phases software goes through, from idea to retirement, and what each phase produces |
| 02 | How decision-support software differs | Explain, phase by phase, what makes decision-support software different than ordinary business software |
| 03 | The map of this book | Find the section that addresses each difference |

---

[← Book contents](../../README.md) · [Next section: 04 Designing decision-support software →](../04-design/README.md)
