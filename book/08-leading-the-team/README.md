# Section 08 — Leading the team

## Introduction

Section 02 decides whether a company needs an operations research team. This section covers leading one once it exists.
**The difference this section addresses:** a team building decision-support software is usually made of scientists,
trained and rewarded for the quality of their models rather than the quality of their software. Leading it means
changing what the team treats as part of the job, without losing the scientific strength that made it valuable.

### Ideas to develop

- **Why practitioners resist, and what changes their behavior.** Build on the DSI 2026 paper *Why software engineering
  practices are slow to spread among operations research practitioners and what changes that behavior*, and on the change-management
  half of [Brownfield adoption](../07-working-with-legacy-dss/README.md#01--brownfield-adoption), which is planned to move here.
  Its four themes: make the problem visible, make change the easy path, make it theirs, and know your terrain.
- **Report quality and throughput together.** Showing that delivery speed did not drop is what defuses the belief that
  good practice and delivery pace trade off against each other.
- **Training as a lever.** The [Learning Roadmap](../appendix/learning-roadmap.md) and the
  [practice repositories](../appendix/practice-repositories.md) are the starting material for chapter 04.

### Out of scope

- **General people management** — hiring processes, performance reviews, compensation — except where decision-support
  software changes the answer.
- **Whether the team should exist, and where it sits.** That is [Section 02](../02-do-you-need-dss/README.md).

## Chapters

| # | Chapter | After it you can… | Status |
|:---:|---|---|---|
| 01 | [How to staff your team](#01--how-to-staff-your-team) | Name the kinds of contributor your team needs, and decide which expertise to own and which to borrow | Ready |
| 02 | [From science to software: the mindset change](#02--from-science-to-software-the-mindset-change) | Explain what changes when scientists start shipping production software | Coming soon |
| 03 | [Introducing engineering practices to a team that resists them](#03--introducing-engineering-practices-to-a-team-that-resists-them) | Plan a change in practice that lasts beyond your own involvement | Coming soon |
| 04 | [Training scientists in software engineering](#04--training-scientists-in-software-engineering) | Plan training for your team, and choose what to learn first | Coming soon |

Chapter 01 decides who is on the team. Chapters 02–04 are about what happens next: what the work feels like from the
inside, how to change practice in a team that did not ask for it, and what to train first.

---

## 01 — How to staff your team

Suppose you accept the diagnosis of [Section 01](../01-introduction/README.md#what-goes-wrong-and-why): your
team's mathematics is strong and the software around it is weak. The obvious fix is to hire software developers.

On its own, that fix disappoints. The developer does not know the mathematics, so the formulation — the part where
correctness is hardest to establish — stays with the scientists, and stays untested. The developer takes the work
nobody argues about: the database, the deployment scripts, the interface. The team now has two vocabularies and a
handoff between them, and the weakest part of the system is on the far side of that handoff.

The mistake is treating "software engineering" as one skill that one hire supplies. It is several, and they do not all
belong in the same person, or even in the same team.

A more useful way to staff the team is to position the contributors against the two disciplines the product needs,
operations research and software engineering.

<!-- TODO figure: the two overlapping circles, software engineering and operations research.
![Two overlapping circles, software engineering and operations research, with developers on the software engineering side, OR engineers in the overlap, and scientists on the operations research side](assets/01-contributors-se-or.svg)
-->

1. **Developers** work on what is unrelated to the mathematics: the database, the data pipelines, the deployment, the
   interfaces people use. They need no operations research to do it well.
2. **OR engineers** live in the overlap. They know enough of both disciplines to set the scientific development
   needs — how to test an optimization model, how to keep the system solver-agnostic, how to run an experiment that
   compares two formulations. Their job is to make the scientists' work engineerable, not to do it for them.
3. **Scientists** hold the modelling, and are trained in the parts of software engineering their work actually
   requires: the [software development lifecycle](../03-software-development-lifecycle/README.md), gathering
   requirements from the business, [automated testing](../appendix/glossary.md#automated-test),
   [test-driven development](../appendix/glossary.md#test-driven-development), basic design, and
   [continuous integration](../appendix/glossary.md#continuous-integration).

The third point is the one most teams get wrong in both directions. Scientists do not need everything a software
engineer knows, and sending them to a generic curriculum wastes their time. They do need a bounded subset, and
without it no amount of hiring will make the model maintainable, because the model stays theirs.

That still leaves the question of size. Take a team of four scientists that owns one decision-support system: what
must the team hold, and what can it get from elsewhere in the company?

| Own | Borrow |
|---|---|
| **Business interaction** — what the decision has to achieve, and what a good plan looks like | **Cybersecurity** — threat review, access policy, dependency scanning |
| **Product behavior** — the formulation, the business rules, what the system promises its users | **Infrastructure** — servers, containers, the platform the run happens on |
| **Software quality** — tests, design, and the state the code is allowed to reach | **Reliability** — on-call practice, incident response, alerting standards |
| **CI/CD** — how a change gets from a laptop to production, and how it gets rolled back | **UI/UX** — how planners see and interrogate a plan |

The left column is what the product *is*. Give away any of it and the team stops owning the decisions the business
depends on — the formulation drifts from the business rules, or quality becomes something a separate group signs off
on after the fact. The right column is expertise your organization has already paid for and that no OR team can match
by itself.

So the answer to "how large does my team have to be?" is smaller than it first looks: borrow expertise from your
organization, and keep product ownership.

### Check yourself

1. Your infrastructure group offers to take over the deployment pipeline, including deciding when a model version
   goes live. Own or borrow?
2. You can make one hire. The system has no automated tests, and nobody on the team knows how to test a MIP. Which of
   the three kinds of contributor do you look for?
3. Your company has no platform group and no security function. What does the OWN/BORROW table become?

<details>
<summary>Answers</summary>

1. Borrow the pipeline, own the decision. Who builds and runs the machinery is infrastructure; *when* a new model
   version is allowed to produce decisions is product behavior, and it stays with the team.
2. An OR engineer. A developer would build the pipeline but not answer the testing question, and the scientists
   cannot answer it without somebody who knows both sides. See [Section 05](../05-testing/README.md) for the
   substance of that work.
3. It collapses into one column, and the team's capacity has to absorb it. That is a real cost to state out loud
   when the system is funded, not a reason to pretend the work does not exist.

</details>

### Where this stops working

- **Small teams.** With one or two scientists there is nothing to distribute; the same people cover every row of the
  OWN column, and the only lever left is training.
- **Nothing to borrow from.** A company with no platform, security, or design function leaves the team with a choice
  between owning that work and accepting the risk knowingly. Both are defensible; drifting into the second without
  saying so is not.
- **OR engineers are hard to hire.** The overlap is thin in the market, and most teams grow their own from scientists
  who take to the engineering side. Chapter 04 is about that path.
- **A bought system changes the answer.** If a vendor owns the formulation, the team is not staffing a product; it is
  managing a supplier, which is [Section 02](../02-do-you-need-dss/README.md).

---

## 02 — From science to software: the mindset change

A model written for a study is judged by what it shows. The same model inside a decision-support system is judged by
what it keeps doing: whether it runs on somebody else's machine, whether a change can be made safely next year,
whether the result can be reproduced when a planner disputes it. The chapter will name the habits that transfer from
research practice — experiment design, reproducibility, skepticism about results — and the ones that have to be
added, and will be honest about what the change costs the individual scientist in the short term.

---

## 03 — Introducing engineering practices to a team that resists them

Resistance to engineering practice is usually rational from where the team stands: the practices cost time now and
pay later, and nobody is measured on later. The chapter will treat adoption as a change-management problem rather
than a technical one, around four themes — make the problem visible, make change the easy path, make it theirs, and
know your terrain — drawing on the change-management material currently in
[Section 07](../07-working-with-legacy-dss/README.md#01--brownfield-adoption), which is planned to move here.

---

## 04 — Training scientists in software engineering

Chapter 01 claims scientists need a bounded subset of software engineering. This chapter will say which subset, in
what order, and how to tell whether the training took. It will build the sequence on the
[Learning Roadmap](../appendix/learning-roadmap.md) and the
[practice repositories](../appendix/practice-repositories.md), and will cover the part managers usually skip: giving
the team work where the new practice is the only way through, so the training does not evaporate on contact with the
next deadline.

---

[← Book contents](../../README.md) · [Next section: 09 AI-assisted development of decision-support software →](../09-ai-assisted-development/README.md)
