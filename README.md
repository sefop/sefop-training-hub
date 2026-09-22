# SEFOP Training Hub

This hub is part of [SEFOP](https://github.com/sefop) and serves two audiences:
1. **Operations research scientists** who want to ship decision-support software (DSS) with professional standards.
2. **Engineering managers** who lead the teams building them.

The hub is written as a practical e-book that moves from general to particular: what decision-support software is
and when a company needs it, how its lifecycle differs from that of ordinary software, and then one section per phase
of that lifecycle. Chapters explain the ideas in a language-agnostic way, and some end with exercises in code.

> [!NOTE]
> This book is under construction. Nothing is definitive yet.

---

## Book contents

| # | Section | Questions it answers |
|:---:|---|---|
| 01 | [Introduction](book/01-introduction/README.md) | • What is decision-support software, and how does it differ from a one-off analysis?<br>• Why does decision-support software so often become hard to maintain?<br>• Why do AI coding assistants make engineering practices more important, not less? |
| 02 | [Do you need DSS?](book/02-do-you-need-dss/README.md) | • Does this decision deserve software, or is a one-off analysis or a spreadsheet enough?<br>• Should we build an in-house OR team, or rely on vendors and consultants?<br>• Where should the team sit in the organization, and whom should it report to? |
| 03 | [Software development lifecycle](book/03-software-development-lifecycle/README.md) | • What phases does software go through, from idea to retirement?<br>• What makes each phase different for decision-support software than for ordinary software?<br>• Which section of this book addresses each difference? |
| 04 | [Design](book/04-design/README.md) | • What are the parts of a decision-support system, and where do the boundaries between them go?<br>• How do I swap solvers without rewriting the model?<br>• How do I make the same inputs always produce the same decision? |
| 05 | [Testing](book/05-testing/README.md) | • What should I test in a decision-support system?<br>• How do I test a model when I don't know its optimal answer?<br>• Which tests still work when the solver is a heuristic? |
| 06 | [Deployment](book/06-deployment/README.md) | • How do I deploy a model, with its solver and data, so it delivers a usable decision on every run?<br>• How do I release a new model without putting current decisions at risk?<br>• What should I measure in production to know whether the decisions are still good? |
| 07 | [Working with legacy DSS](book/07-working-with-legacy-dss/README.md) | • How do I improve code I did not write without breaking what already works?<br>• Is this bug worth fixing?<br>• How do I fix a bug so it stays fixed? |
| 08 | [Leading the team](book/08-leading-the-team/README.md) | • Which roles does my team need, and which expertise should it borrow instead of hiring?<br>• What changes when scientists start shipping production software?<br>• How do I introduce engineering practices to a team that resists them? |
| 09 | [AI-assisted development](book/09-ai-assisted-development/README.md) | • Why do engineering fundamentals matter more, not less, when an AI assistant writes the code?<br>• How do I check model code that an assistant wrote?<br>• How do I know whether an AI workflow actually improves my results? |

---

## Appendix

- [Learning Roadmap](book/appendix/learning-roadmap.md) — a suggested order to learn software engineering for building decision-support software.
- [Practice Repositories](book/appendix/practice-repositories.md) — language-specific exercises for the chapters.
- [Glossary](book/appendix/glossary.md) — every software engineering term used in the book, defined once.

## Workshops

Slides and material from past and upcoming talks live in [workshops](workshops/).

## For Questions

Go here https://github.com/orgs/sefop/discussions.
