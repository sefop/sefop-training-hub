# Section 01 — Introduction

## Introduction

Operations research creates business value by helping organizations make better decisions. That value reaches the
business through **decision-support software**: software that runs repeatedly to turn data, mathematical models, and
business rules into recurring decisions. This section explains what that software is, why it often ends up hard to
maintain, and how an organization can solve the problems that arise in decision-support software.

### Out of scope

- **How to apply any practice.** This section argues why the practices matter; Sections 03–09 explain how.

## Chapters

| # | Chapter | After it you can… | Status |
|:---:|---|---|---|
| 01 | [What decision-support software is](#01--what-decision-support-software-is) | Tell decision-support software apart from a one-off analysis, and place a system on the strategic, tactical, or operational level | Ready |
| 02 | [What goes wrong, and why](#02--what-goes-wrong-and-why) | Recognize the symptoms of weak engineering in decision-support software, and name its two root causes | Ready |
| 03 | [AI coding assistants as amplifiers](#03--ai-coding-assistants-as-amplifiers) | Explain why AI assistants raise the value of engineering practices instead of replacing them | Ready |
| 04 | [How to read this book](#04--how-to-read-this-book) | Say what each section covers, and where the material that is not in this book lives | Ready |

Read them in order. Chapter 01 defines what the book is about, chapter 02 states the problem the rest of the book
addresses, chapter 03 places that problem in today's context, and chapter 04 maps the nine sections.

---

## 01 — What decision-support software is

After this chapter you can tell decision-support software apart from a one-off analysis, and place a system on the
strategic, tactical, or operational level.

### The problem

Operations research turns data, business needs, and mathematics into a decision. Training and literature in the field
concentrate on the first half of that sentence: how to formulate a problem, and how to solve it. What happens to the
decision afterwards — who runs the model next month, on which machine, with whose data — gets far less attention.

That omission would be harmless if every decision were made once. Many are not. A study that recommends where to open
two distribution centers ends when the company opens them. A model that schedules next week's deliveries is asked the
same question every week, with new data, for as long as the network exists. The second kind of work cannot be
delivered as a report and closed.

### The idea

Two shapes of work, told apart by how often the decision is needed:

- A **project** delivers a decision once. It ends with a deliverable — a report, a recommendation, a number — and the
  model that produced it can be retired along with it.
- A **product** delivers a recurring decision. It does not end. Somebody owns it for as long as the business needs the
  decision.

The software behind a product is a [decision-support system](../appendix/glossary.md#decision-support-system), or DSS:
software that runs repeatedly to turn data, mathematical models, and business rules into decisions the business acts
on.

The distinction moves where the value sits. A project is worth the quality of the single decision it delivered. A
product is worth the quality of the decisions it keeps delivering, next month and three years from now. So the value
of a product depends on how cheaply it can keep running and keep changing — and that is a property of the software,
not of the formulation. A correct model inside a system nobody can run is worth nothing.

Recurring decisions are usually placed on three levels, by how far ahead they commit the business:

1. **Strategic** — decisions that shape assets and commitments, with a horizon of years.
2. **Tactical** — decisions that allocate capacity the business already has, over weeks or months.
3. **Operational** — decisions that run the business now, within days or hours.

The level sets the cadence of the decision, and the cadence sets how much of the run has to happen without a person
present.

### Worked example

Four systems, one per cadence:

| Decision | Level | Cadence | What the cadence forces on the software |
|---|---|---|---|
| Extraction plan of a mine | Strategic | Annual | An analyst can run it by hand and inspect the result, but the run must be reproducible years later, when the plan is audited |
| Shift schedules of a retail store | Tactical | Monthly | Whoever is on duty must be able to run it; the business rules change more often than the model does |
| Delivery plan of a transportation network | Tactical | Weekly | The run is scheduled rather than launched by a person; a failed run must still leave the business with a usable plan |
| Recovery of an airline's operation after a weather disruption | Operational | Daily, and within the day | The run is unattended and bounded by a time limit; an answer that arrives late is worth nothing, because the disruption has moved |

The pattern across the four rows: the shorter the cadence, the less a person can be in the loop, and the more the
system has to handle by itself — scheduling, bad input, a run that does not finish. The mine plan tolerates a
scientist babysitting the solver once a year. The airline recovery does not.

That is an observation about these four systems rather than a law. The cadence is the strongest driver of what the
software must do on its own, but it is not the only one: a monthly run that feeds a regulator can demand more
engineering than a daily run used by one planner.

### Check yourself

1. A consultancy delivers a study recommending two new warehouse locations. The client builds them and never runs the
   model again. Project or product?
2. The same client now asks for the study to be re-run every quarter, as demand shifts. What changes for the software?
3. Place "recover the operation after a storm" on the three levels, and say what its cadence implies about the run.

<details>
<summary>Answers</summary>

1. A project. The decision is made once, the deliverable is the recommendation, and the model can be retired with it.
2. The decision becomes recurring, so the model becomes a product: somebody has to own it, the data has to arrive the
   same way every quarter, and the result has to be reproducible when the numbers change. Nothing about the
   formulation changes; everything about the software around it does.
3. Operational, with a daily and intra-day cadence. The run has to complete unattended, inside a time limit, and
   still return something usable when the solver does not finish.

</details>

### Where this stops working

The line between project and product is not always sharp, and drawing it too early costs money in both directions.

- **A genuine one-off analysis is not decision-support software.** Engineering it as a product — tests, deployment,
  monitoring — spends money that the single decision will never return.
- **A time-boxed proof of concept is a project even when it looks like a product.** It exists to find out whether the
  value is there. The decision to turn it into a product comes afterwards, and belongs to
  [Section 02](../02-do-you-need-dss/README.md).
- **The dangerous case is the one in between:** a spreadsheet or a script that quietly became recurring, and that
  nobody owns. It is a product by cadence and a project by construction, which is how most of the trouble in
  [chapter 02](#02--what-goes-wrong-and-why) starts.

---

## 02 — What goes wrong, and why

After this chapter you can recognize the symptoms of weak engineering in decision-support software, and name the two
root causes behind them.

### The problem

Decision-support software that was built without engineering practices announces itself the same way across
companies and industries:

1. **The code runs on one machine only** — the author's — and nobody is quite sure what else it needs.
2. **Peers cannot extend it**, and after a few months neither can the person who wrote it.
3. **Developers are afraid to modify it**, because nothing tells them whether a change broke a result.
4. **The system is eventually rewritten rather than evolved**, and the knowledge inside it is rebuilt from scratch.

These symptoms rarely reach the business as software problems. They arrive as "that change takes three weeks", "only
one person can run the model", or "the numbers moved and we do not know why".

### The idea

The causes divide into two groups, following the framing of
[Kanewala & Bieman (2014)](https://doi.org/10.1016/j.infsof.2014.05.006) for scientific software.

**Cultural.** Operations research scientists are trained deeply in mathematics and rarely in software engineering, and
often do not see why the practices should apply to them. The consequence is visible in the literature.
[Ackoff (1979)](https://doi.org/10.1057/jors.1979.22) already observed operations research becoming identified with
its models rather than with implementing and maintaining them.
[Vidoni (2021)](https://doi.org/10.1080/01605682.2020.1865848) argues the field needs an "Operations Research
Engineering" practice of its own. [Vidoni & Cunico (2022)](https://doi.org/10.1007/s12532-022-00225-1) surveyed 168
modellers and found [technical debt](../appendix/glossary.md#technical-debt) in code and documentation to be
widespread — and, in most cases, introduced deliberately. The last finding is the one that matters for a manager: the
debt is not an accident of ignorance, it is a choice made under delivery pressure.

**Technical.** A decision-support system is a mixture of two disciplines, and the mixture raises questions ordinary
business software never has to answer.

![A decision-support system as one system holding software components and applied mathematics side by side](assets/02-dss-software-and-mathematics.svg)

- **How do you test an optimization model automatically,** when the expected answer is the very thing the model
  computes? → [Section 05](../05-testing/README.md)
- **How do you design the system so the solver can be replaced** without rewriting the formulation? →
  [Section 04](../04-design/README.md)
- **How do you compare one formulation against another** on real data, before the change reaches the business? →
  [Section 06](../06-deployment/README.md)

Neither cause is sufficient on its own. A scientist who wants to engineer well still hits the technical questions,
and a software engineer who knows the answers to none of the mathematics cannot supply them either. That is the
argument [Section 08](../08-leading-the-team/README.md) picks up.

### Worked example

What does weak engineering cost, in practice? Think of a system's total progress — features delivered, decisions
supported, questions the business can now ask — against time.

![Total progress against time for three systems: solid foundations, legacy system, and short-lived system](assets/02-progress-over-time.png)

*Illustrative, after Ousterhout (2018).*

Three trajectories, all of them common:

1. **Solid foundations.** The first months are slower: boundaries between data, rules, and model; automated tests;
   a repeatable way to run it. The slope after that stays roughly constant, because each change costs about what the
   last one did.
2. **Legacy system.** The start is fast, and for a year or two nothing looks wrong. Then the original developers move
   on. Nobody can say what the code does or why, each change takes longer than the one before, and the curve flattens
   without ever quite stopping.
3. **Short-lived system.** The fastest start of the three, and the shortest life. Within about a year the system
   cannot absorb the changes the business asks for, and the organization rewrites it or decommissions it — losing the
   modelling knowledge inside it.

The three curves are drawn to make a qualitative point, not from measured data. What they claim is an ordering — the
foundations path overtakes the others if the system lives long enough — not a crossover date.

### Check yourself

1. A planner says "only Ana can run the model". Which of the four symptoms is that, and what does it predict about
   what happens when Ana changes jobs?
2. The survey finding is that most technical debt is introduced *deliberately*. Why does that change how a manager
   should respond to it?
3. Your system is a six-week proof of concept that will be thrown away. Which trajectory should you aim for?

<details>
<summary>Answers</summary>

1. Symptom 1, and partly 2: the system runs on one machine and in one head. When Ana leaves, the system does not stop
   working, but changing it becomes a rewrite — which is symptom 4 arriving on schedule.
2. Training alone does not fix a deliberate choice. If debt is taken on under delivery pressure, the answer is to
   change what the team is rewarded for and to make the cost visible, which is the subject of
   [Section 08](../08-leading-the-team/README.md).
3. The short-lived one. It is the right trajectory when the system's life is shorter than the time the foundations
   would take to pay back.

</details>

### Where this stops working

Not every system deserves foundations, and this chapter is not an argument that it does.

- **Short-lived systems are sometimes the correct choice.** A prototype built to answer one question, and discarded
  afterwards, should be built fast and cheap.
- **The curves say nothing about when the crossover happens.** It depends on the team, on how often the business
  changes its mind, and on how long the system lives. Anyone who quotes you a date for it is guessing.
- **The symptoms are signals, not proof.** Code that runs on one machine may simply be new. What makes the four
  symptoms serious is the combination, and the cadence behind it:
  [chapter 01](#01--what-decision-support-software-is) explains why a recurring decision cannot live with them.

---

## 03 — AI coding assistants as amplifiers

After this chapter you can explain why AI coding assistants raise the value of engineering practices instead of
replacing them.

### The problem

More than 70% of scientific programmers already write code with LLM-based tools
([O'Brien & Eisty, 2026](https://www.computer.org/csdl/magazine/cs/2026/01/11482007/2fJHVugY5UY)). Whether an
assistant belongs in the workflow is no longer the decision in front of a team; what to do about it is.

The difficulty is sharper here than in ordinary business software. When an assistant writes a web page badly, the
page breaks, or the number on it is visibly absurd. When an assistant writes a constraint badly, the model returns a
plan: feasible, optimal for the formulation as written, and wrong. A mistaken constraint reads exactly like a correct
one, and the cheap check that would expose it — comparing against the right answer — is the thing
[chapter 02](#02--what-goes-wrong-and-why) named as the technical half of the problem.

### The idea

An assistant does not raise or lower the quality of a team's engineering. It multiplies what is already there. The
[2025 DORA report](https://dora.dev/research/2025/dora-report/), which surveys software teams at large, describes the
same pattern outside operations research: teams with strong practices deliver faster at the same quality, while teams
with weak ones ship more, and more fragile, output.

| Practice around the assistant | What the assistant changes | Result |
|---|---|---|
| [Automated tests](../appendix/glossary.md#automated-test), [continuous integration](../appendix/glossary.md#continuous-integration), clear boundaries | More code written per week, each change checked automatically | Sustainable acceleration: faster delivery at the quality the team already had |
| Manual checking, or none; unclear design | More code written per week, checked at the same manual rate as before | Accelerated [technical debt](../appendix/glossary.md#technical-debt): more output, and more of it unverified |

The mechanism behind both rows is the same, and it is worth stating plainly: an assistant reduces the cost of
*writing* code. It does not reduce the cost of *deciding whether the code is right*. Where that decision is
automated, the team can absorb the extra volume. Where it is a person reading a diff, or a planner noticing a strange
plan, the volume arrives anyway and the checking does not keep up.

This is an argument about where the bottleneck sits, not a measurement of any particular team. The DORA pattern is
consistent with it; it does not prove it for operations research specifically.

### Worked example

Two teams get the same request — *no truck may be loaded above 90% of its volume* — and both ask an assistant to
write the constraint. Both have working code in minutes. What differs is when they find out whether it is right.

| | Team A: tests and CI | Team B: manual checking |
|---|---|---|
| Constraint written | In minutes | In minutes |
| First signal | The test suite runs on the commit; two tests fail because the objective dropped on instances where it should not have | The run produces a plan, and the plan looks plausible |
| Cost of the signal | Minutes, and the change is still in the author's head | Weeks, if a planner questions a route; otherwise never |
| What gets learned | The constraint was applied to every truck, including the ones exempt by contract | That the plan "feels tighter than it used to" |

Team B is not slower at writing code than Team A. It is slower at finding out, and the assistant widened that gap by
making the writing part faster on both sides.

### Check yourself

1. An assistant is asked to make a failing test pass, and edits the test's expected value instead of the code. Which
   practice catches that, and which one does not?
2. A team with no automated tests adopts an assistant and triples the amount of code it produces per sprint. What has
   actually improved?
3. Why is an assistant riskier on the formulation than on the script that loads the input data?

<details>
<summary>Answers</summary>

1. Code review of the test change catches it; a green test suite does not, because the suite is now checking the
   wrong thing. Tests written by a person, and reviewed changes to them, are the defense —
   [Section 09](../09-ai-assisted-development/README.md) treats this in detail.
2. The rate of writing. Nothing about the rate of verifying, which is what decides whether the extra code is an asset
   or a liability.
3. Because the loader has a cheap oracle and the formulation does not. You know what a correctly parsed row looks
   like; you do not know the optimal objective value without solving the problem
   ([Section 05](../05-testing/README.md)).

</details>

### Where this stops working

- **The evidence is not from operations research.** DORA surveys software teams broadly. The mechanism transfers
  because the oracle problem makes verification *more* expensive here, not less — but that is an inference, not a
  measurement of OR teams.
- **The size of the effect is not stable.** Assistants change quickly. The ordering in the table is the durable
  claim; any specific multiplier is not.
- **A throwaway prototype genuinely benefits from raw speed.** If the code will be discarded next month, unverified
  output is a smaller liability than the time spent verifying it.

How to capture the acceleration without accepting the risk is the subject of
[Section 09](../09-ai-assisted-development/README.md).

---

## 04 — How to read this book

After this chapter you can say what each section of the book covers, and where the material that is deliberately not
in this book lives.

This book is one part of SEFOP, the Software Engineering Framework for Optimization Programs, which develops four
capabilities: **Train** (the skills a team needs), **Lead** (how such a team is staffed and led), **Deliver**
(working reference implementations), and **Go Agentic** (getting business value out of AI coding assistants). The
book covers Train and Lead. Deliver and Go Agentic live in sibling repositories at
[github.com/sefop](https://github.com/sefop). That division is why the chapters here use pseudocode rather than a
language: runnable code belongs to the repositories built for it, and the exercises that go with these chapters are
listed in the [practice repositories appendix](../appendix/practice-repositories.md).

### The book in nine sections

1. **01 — Introduction** (this section) — what decision-support software is, why its engineering is usually the weak
   half, and what that weakness costs.
2. **[02 — When a company needs decision-support software and an OR team](../02-do-you-need-dss/README.md)** —
   whether a recurring decision justifies software at all, whether to build the team in-house or buy from a vendor,
   and where the team belongs in the organization.
3. **[03 — The lifecycle of decision-support software](../03-software-development-lifecycle/README.md)** — the phases
   every piece of software passes through, and the twist each phase takes when the software produces decisions. It
   is the map for the sections that follow.
4. **[04 — Designing decision-support software](../04-design/README.md)** — drawing boundaries between data,
   business rules, the formulation, and the solver, so that each can change without breaking the others.
5. **[05 — Testing decision-support software](../05-testing/README.md)** — how to test a model whose correct answer
   is the very thing it computes: oracles worked out by hand, metamorphic relations, and differential testing.
6. **[06 — Deploying decision-support software](../06-deployment/README.md)** — getting a model, its solver, and its
   data into production, planning for runs that end badly, and measuring whether the decisions stay good.
7. **[07 — Working with legacy decision-support software](../07-working-with-legacy-dss/README.md)** — changing a
   system you inherited without breaking what already works, and fixing a bug so that it stays fixed.
8. **[08 — Leading the team](../08-leading-the-team/README.md)** — which expertise the team owns and which it
   borrows, and how to change what a team of scientists treats as part of the job.
9. **[09 — AI-assisted development of decision-support software](../09-ai-assisted-development/README.md)** — working
   with coding assistants on model code without accepting output nobody has verified.

Three references sit outside the sections and are meant to be used rather than read: the
[glossary](../appendix/glossary.md), which defines every software engineering term the book uses; the
[learning roadmap](../appendix/learning-roadmap.md), a suggested order for learning the practices; and the
[practice repositories](../appendix/practice-repositories.md), where the runnable exercises live.

---

[← Book contents](../../README.md) · [Next section: 02 When a company needs decision-support software and an OR team →](../02-do-you-need-dss/README.md)
