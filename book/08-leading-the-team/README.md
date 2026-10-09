# Section 08 — Leading the team

<a id="ch-introduction"></a>

## 1. Introduction

Section 02 decides whether a company needs an operations research team. This section covers leading
one once it exists. **The difference this section addresses:** a team building decision-support
software is usually made of scientists, trained and rewarded for the quality of their models rather
than the quality of their software. Leading it means changing what the team treats as part of the
job, without losing the scientific strength that made it valuable.

### Ideas to develop

- **Leadership at different levels of authority.** Distinguish what a technical lead can change in
  development and review, what a manager can change in priorities and time allocation, and what an
  organizational leader can support across projects. Make each role's available actions and limits
  explicit.
- **Complement project-level improvement.** [Section 07](../07-working-with-legacy-dss/README.md)
  addresses improving an inherited system and its team's practices from the position of a team
  member with some support and limited authority. This section develops the leadership conditions
  that enable and extend that work: staffing, incentives, training strategy, and adoption across
  projects.
- **Support strategic programming.**
  [Strategic programming](../appendix/glossary.md#strategic-programming) means investing in design
  while delivering working behavior to support future changes. Develop how leaders make room for
  that investment in estimates, review, and time allocation, building on
  [2. What design is for](../04-design/README.md#ch-design-purpose) in Section 04. Assess whether the
  practice is shared and repeatable as responsibility spreads beyond its original advocate.
- **Diagnose different barriers within the same team.** Unfamiliarity, uncertainty about how to
  start, delivery pressure, professional identity, and informal team norms call for different
  responses. Investigate both how existing practices arose and what keeps them in place.
- **Make improvement possible in everyday work.** Give people time, working examples, useful
  feedback, and a development process that makes safer practices easier to repeat. Make the cost of
  current practices visible through shared evidence and constructive review.
- **Connect engineering with scientific responsibility.** Develop how testing model behavior can
  support confidence in the mathematics, and how shared accomplishments and recognition can make
  engineering practices part of the team's own understanding of its job.
- **Understand support and informal authority.** Examine reporting lines, actual time allocation,
  and whose example colleagues follow. Explore when sufficient support allows improvement despite
  different priorities, when additional authority is needed, and how membership changes affect
  adoption. Avoid making full managerial alignment a universal prerequisite.
- **Report quality and delivery together.** Use evidence of safer changes and useful delivery to
  examine the perceived trade-off. Coverage, tool findings, and commit counts are partial
  indicators; they do not establish model correctness, business value, or independent expertise.
- **Distinguish adoption, mastery, and persistence.** Following a practice with an experienced
  reviewer's guidance differs from applying it independently. Plan how to share responsibility and
  assess whether practices persist when the original advocate's involvement decreases. Expect
  occasional shortcuts under pressure; aim for a better default and explicit handling of exceptions.
- **Training as a lever.** The [Learning Roadmap](../appendix/learning-roadmap.md) and the
  [practice repositories](../appendix/practice-repositories.md) are the starting material for
  [5. Training scientists in software engineering](#ch-training).

### Chapters

|  #  | Chapter                                                                                    | After it you can…                                                                                    | Status      |
| :-: | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ----------- |
|  1  | [Introduction](#ch-introduction)                                                           | Say what the section covers and how its chapters build on each other                                 | Ready       |
|  2  | [How to staff your team](#ch-staffing)                                                     | Name the kinds of contributor your team needs, and decide which expertise to own and which to borrow | Ready       |
|  3  | [From science to software: the mindset change](#ch-mindset)                                | Explain what changes when scientists start shipping production software                              | Coming soon |
|  4  | [Introducing engineering practices to a team that resists them](#ch-introducing-practices) | Plan a change in practice that lasts beyond your own involvement                                     | Coming soon |
|  5  | [Training scientists in software engineering](#ch-training)                                | Plan training for your team, and choose what to learn first                                          | Coming soon |
|  6  | [Conclusion](#ch-conclusion)                                                               | Recall in one page which expertise the team owns, and what it takes to change how it works           | Ready       |

---

<a id="ch-staffing"></a>

## 2. How to staff your team

Suppose you accept the diagnosis of [Section 01](../01-introduction/README.md#ch-what-goes-wrong):
your team's mathematics is strong and the software around it is weak. The obvious fix is to hire
software developers.

On its own, that fix disappoints. The developer does not know the mathematics, so the formulation —
the part where correctness is hardest to establish — stays with the scientists, and stays untested.
The developer takes the work nobody argues about: the database, the deployment scripts, the
interface. The team now has two vocabularies and a handoff between them, and the weakest part of the
system is on the far side of that handoff.

The mistake is treating "software engineering" as one skill that one hire supplies. It is several,
and they do not all belong in the same person, or even in the same team.

A more useful way to staff the team is to position the contributors against the two disciplines the
product needs, operations research and software engineering.

<!-- TODO figure: the two overlapping circles, software engineering and operations research.
<p align="center">
  <img src="assets/01-contributors-se-or.svg" width="560"
       alt="Software engineering and operations research as overlapping circles: developers on the software
       engineering side, OR engineers in the overlap, scientists on the operations research side">
</p>
-->

1. **Developers** work on what is unrelated to the mathematics: the database, the data pipelines,
   the deployment, the interfaces people use. They need no operations research to do it well.
2. **OR engineers** live in the overlap. They know enough of both disciplines to set the scientific
   development needs — how to test an optimization model, how to keep the system solver-agnostic,
   how to run an experiment that compares two formulations. Their job is to make the scientists'
   work engineerable, not to do it for them.
3. **Scientists** hold the modelling, and are trained in the parts of software engineering their
   work actually requires: the
   [software development lifecycle](../03-software-development-lifecycle/README.md), gathering
   requirements from the business, [automated testing](../appendix/glossary.md#automated-test),
   [test-driven development](../appendix/glossary.md#test-driven-development), basic design, and
   [continuous integration](../appendix/glossary.md#continuous-integration).

The third point is the one most teams get wrong in both directions. Scientists do not need
everything a software engineer knows, and sending them to a generic curriculum wastes their time.
They do need a bounded subset, and without it no amount of hiring will make the model maintainable,
because the model stays theirs.

That still leaves the question of size. Take a team of four scientists that owns one
decision-support system: what must the team hold, and what can it get from elsewhere in the company?

| Own                                                                                            | Borrow                                                                    |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Business interaction** — what the decision has to achieve, and what a good plan looks like   | **Cybersecurity** — threat review, access policy, dependency scanning     |
| **Product behavior** — the formulation, the business rules, what the system promises its users | **Infrastructure** — servers, containers, the platform the run happens on |
| **Software quality** — tests, design, and the state the code is allowed to reach               | **Reliability** — on-call practice, incident response, alerting standards |
| **CI/CD** — how a change gets from a laptop to production, and how it gets rolled back         | **UI/UX** — how planners see and interrogate a plan                       |

The left column is what the product _is_. Give away any of it and the team stops owning the
decisions the business depends on — the formulation drifts from the business rules, or quality
becomes something a separate group signs off on after the fact. The right column is expertise your
organization has already paid for and that no OR team can match by itself.

So the answer to "how large does my team have to be?" is smaller than it first looks: borrow
expertise from your organization, and keep product ownership.

### Check yourself

1. Your infrastructure group offers to take over the deployment pipeline, including deciding when a
   model version goes live. Own or borrow?
2. You can make one hire. The system has no automated tests, and nobody on the team knows how to
   test a MIP. Which of the three kinds of contributor do you look for?
3. Your company has no platform group and no security function. What does the OWN/BORROW table
   become?

<details>
<summary>Answers</summary>

1. Borrow the pipeline, own the decision. Who builds and runs the machinery is infrastructure;
   _when_ a new model version is allowed to produce decisions is product behavior, and it stays with
   the team.
2. An OR engineer. A developer would build the pipeline but not answer the testing question, and the
   scientists cannot answer it without somebody who knows both sides. See
   [Section 05](../05-testing/README.md) for the substance of that work.
3. It collapses into one column, and the team's capacity has to absorb it. That is a real cost to
   state out loud when the system is funded, not a reason to pretend the work does not exist.

</details>

### Where this stops working

- **Small teams.** With one or two scientists there is nothing to distribute; the same people cover
  every row of the OWN column, and the only lever left is training.
- **Nothing to borrow from.** A company with no platform, security, or design function leaves the
  team with a choice between owning that work and accepting the risk knowingly. Both are defensible;
  drifting into the second without saying so is not.
- **OR engineers are hard to hire.** The overlap is thin in the market, and most teams grow their
  own from scientists who take to the engineering side.
  [5. Training scientists in software engineering](#ch-training) is about that path.
- **A bought system changes the answer.** If a vendor owns the formulation, the team is not staffing
  a product; it is managing a supplier, which is [Section 02](../02-do-you-need-dss/README.md).

---

<a id="ch-mindset"></a>

## 3. From science to software: the mindset change

A model written for a study is judged by what it shows. The same model inside a decision-support
system is judged by what it keeps doing: whether it runs on somebody else's machine, whether a
change can be made safely next year, whether the result can be reproduced when a planner disputes
it. The chapter will name the habits that transfer from research practice — experiment design,
reproducibility, skepticism about results — and the ones that have to be added, and will be honest
about what the change costs the individual scientist in the short term.

---

<a id="ch-introducing-practices"></a>

## 4. Introducing engineering practices to a team that resists them

People on the same team can have different reasons for maintaining existing practices. The chapter
will develop how leaders diagnose those barriers and choose responses within their authority:
making costs visible, allocating time, making better practices easier, and connecting them with the
team's professional responsibilities. It will complement the project-level work in
[Section 07](../07-working-with-legacy-dss/README.md#ch-team-practices) by addressing leadership support
and adoption across projects, including how to assess whether improvements persist as the original
advocate's involvement decreases.

---

<a id="ch-training"></a>

## 5. Training scientists in software engineering

[2. How to staff your team](#ch-staffing) claims scientists need a bounded subset of software
engineering. This chapter will say which subset, in what order, and how to tell whether the training
took. It will build the sequence on the [Learning Roadmap](../appendix/learning-roadmap.md) and the
[practice repositories](../appendix/practice-repositories.md), and will cover the part managers
usually skip: giving the team work where the new practice is the only way through, so the training
does not evaporate on contact with the next deadline.

---

<a id="ch-conclusion"></a>

## 6. Conclusion

A team of scientists does not become a software team by hiring a software engineer. The formulation
is where correctness is hardest to establish, and it stays with the scientists — so the engineering
has to reach them rather than sit beside them.

- **Software engineering is several skills, not one** ([2. How to staff your team](#ch-staffing)).
  Developers take what is unrelated to the mathematics, OR engineers live in the overlap, and
  scientists learn a bounded subset of the rest.
- **Own the product, borrow the platform** ([2. How to staff your team](#ch-staffing)). Business
  interaction, product behavior, software quality and the path to production stay with the team;
  infrastructure, security, reliability and design come from elsewhere in the company.
- **The job changes, not only the toolkit**
  ([3. From science to software: the mindset change](#ch-mindset)). A model written for a study is
  judged by what it shows; the same model inside a system is judged by what it keeps doing.
- **Different barriers require different responses**
  ([4. Introducing engineering practices to a team that resists them](#ch-introducing-practices)).
  Diagnose what keeps current practices in place, then choose actions within your authority.
- **Training is the lever a manager actually controls**
  ([5. Training scientists in software engineering](#ch-training)). Choose a bounded curriculum,
  then give the team work where the new practice is the only way through.

The thread is the same one the section opened with: keep the scientific strength that made the team
valuable, and change what it treats as part of the job.

---

[← Book contents](../../README.md) ·
[Next section: 09 AI-assisted development of decision-support software →](../09-ai-assisted-development/README.md)
