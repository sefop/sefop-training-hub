# SEFOP Training Hub

This hub is part of [SEFOP](https://github.com/sefop) and serves two audiences:
1. **Operations research scientists** who want to ship decision-support software with professional standards.
2. **Engineering managers** who lead the teams building them.

The hub is written as a small practical book that moves from general to particular: what decision-support software is
and when a company needs it, how its lifecycle differs from that of ordinary software, and then one section per phase
of that lifecycle. Chapters explain the ideas in a language-agnostic way, and some end with exercises in code.

## Start here

| If you… | Start with |
|---|---|
| **write the optimization models** | [Section 05 — Testing decision-support software](book/05-testing/README.md) |
| **inherited code that is hard to change** | [Section 07 — Evolving existing decision-support software](book/07-evolving-existing-code/README.md) |
| **lead the team that builds them** | [Section 02](book/02-do-you-need-dss/README.md) and [Section 08](book/08-leading-the-team/README.md) are planned; meanwhile, read [Brownfield adoption](book/07-evolving-existing-code/01-brownfield-adoption.md) |
| **are new to software engineering** | The [Learning Roadmap](book/appendix/learning-roadmap.md), a sequenced reading path from version control to agentic development |

---

## [Section 01 — Introduction](book/01-introduction/README.md)

What decision-support software is, why it often ends up hard to maintain, and how this book is organized.
*Planned.*

- What decision-support software is
- What goes wrong, and why
- AI coding assistants as amplifiers
- How to read this book

## [Section 02 — When a company needs decision-support software and an OR team](book/02-do-you-need-dss/README.md)

Whether a decision deserves software, who should build it, and where the team sits. *Planned.*

- When a decision deserves software
- Do you need an in-house team?
- Your team in the organization
- From proof of concept to funded project

## [Section 03 — The lifecycle of decision-support software](book/03-lifecycle/README.md)

The phases every piece of software goes through, and how each one differs for decision-support software. *Planned.*

- The software development lifecycle
- How decision-support software differs
- The map of this book

## [Section 04 — Designing decision-support software](book/04-designing/README.md)

How to draw boundaries between data, business rules, the model, and the solver. *Planned.*

- The parts of a decision-support system
- Separate the model from the solver
- Keep data out of the formulation
- Keep business rules visible
- Design for reproducibility

## [Section 05 — Testing decision-support software](book/05-testing/README.md)

How to test decision-support software, and above all its optimization model, whose correct answer is the very thing it
computes.

| # | Chapter | Audience | Status |
|:---:|---|---|---|
| 01 | [What to test in decision-support software](book/05-testing/01-what-to-test-in-decision-support-software.md) | Scientists & Engineering Managers | Coming soon |
| 02 | [Why optimization models are hard to test](book/05-testing/02-why-optimization-models-are-hard-to-test.md) | Scientists & Engineering Managers | Ready |
| 03 | [Test the contract, not the algorithm](book/05-testing/03-test-the-contract-not-the-algorithm.md) | Scientists & Engineering Managers | Ready |
| 04 | [Oracles you write by hand](book/05-testing/04-oracles-you-write-by-hand.md) | Scientists | Ready |
| 05 | [Metamorphic relations](book/05-testing/05-metamorphic-relations.md) | Scientists | Ready |
| 06 | [Differential testing](book/05-testing/06-differential-testing.md) | Scientists | Ready |
| 07 | [When optimality is not guaranteed](book/05-testing/07-when-optimality-is-not-guaranteed.md) | Scientists | Ready |
| 08 | [Duality as an oracle](book/05-testing/08-duality-as-an-oracle.md) | Scientists | Coming soon |
| 09 | [Testing a Pareto front](book/05-testing/09-testing-a-pareto-front.md) | Scientists | Coming soon |

## [Section 06 — Delivering and operating decision-support software](book/06-delivering/README.md)

How to get changes into production safely and notice when decisions degrade. *Planned.*

- Version control for code, data, and models
- Continuous integration
- Environments and packaging
- Releasing a new model safely
- Monitoring decisions in production

## [Section 07 — Evolving existing decision-support software](book/07-evolving-existing-code/README.md)

How to change code you did not write without breaking what already works.

| # | Chapter | Audience | Status |
|:---:|---|---|---|
| 01 | [Brownfield adoption](book/07-evolving-existing-code/01-brownfield-adoption.md) | Scientists & Engineering Managers | Draft (older format) |
| 02 | [Protocol to fix a bug](book/07-evolving-existing-code/02-protocol-to-fix-a-bug.md) | Scientists & Engineering Managers | Draft (older format) |

## [Section 08 — Leading the team](book/08-leading-the-team/README.md)

How to staff and lead a team of scientists building production software. *Planned.*

- How to staff your team
- From science to software: the mindset change
- Introducing engineering practices to a team that resists them
- Training scientists in software engineering

## [Section 09 — AI-assisted development of decision-support software](book/09-ai-assisted-development/README.md)

How to use AI coding assistants on models without accepting unverified code. *Planned.*

- Why fundamentals matter more with AI
- Tests as the guardrail for AI-written models
- Giving an assistant the context of your model
- Evaluating AI workflows

---

## Appendix

- [Learning Roadmap](book/appendix/learning-roadmap.md) — books, courses, and videos in a suggested order.
- [Practice Repositories](book/appendix/practice-repositories.md) — language-specific exercises for the chapters.
- [Glossary](book/appendix/glossary.md) — every software engineering term used in the book, defined once.

## Workshops

Slides and material from past and upcoming talks live in [workshops](workshops/).

## For Questions

Go here https://github.com/orgs/sefop/discussions.
