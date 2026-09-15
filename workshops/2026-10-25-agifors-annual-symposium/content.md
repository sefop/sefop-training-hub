# Rethinking the embedded Operations Research team: from project to product

**Event:** AGIFORS Annual Symposium, 2026-10-25 · **Speaker:** Francisco Zenteno · **Length:** 20 minutes, 14 slides

> [!NOTE]
> Storyline draft. Items marked **[fill in]** need data from the case study before the slides are built.

---

## Governing thought

**An OR team that owns a decision-support product has to operate as a specialized software development team.**

## SCQA summary

- **Situation.** Embedded OR teams deliver value through software that runs on a cadence.
- **Complication.** Most of these teams are still managed like consultants delivering projects.
The business value of the decision-support system is constrained by the software practices used to deliver it.
- **Question.** What has to change for an embedded OR team to deliver long-term value?
- **Answer.** The governing thought above: why it is urgent, how to get there, and evidence that it works.

## Argument structure

0. **Context (slides 2–3).** What decision-support software is, with airline examples, and why its business value is
   constrained by the software used to deliver it.
1. **Thesis (slide 4).** The governing thought.
2. **Why now (slides 5–7).** All software is built by discovery. AI coding assistants amplify whatever practices a team
   has. So the team should deliberately sit at the strong-practices end of the spectrum.
3. **How (slides 8–12).** Operate as a specialized software development team: the DSS differences it must handle, the
   roles and skills it needs, what it owns and borrows, how to train scientists, and SEFOP.
4. **Proof (slide 13).** A case study, framed with Accelerate's throughput metrics.
5. **Close (slide 14).** Recap and two asks.

## Timing

| Block | Slides | Time |
|---|:---:|:---:|
| Open and thesis | 1–4 | 4:00 |
| Why now | 5–7 | 3:50 |
| How | 8–12 | 6:10 |
| Proof | 13 | 1:30 |
| Close | 14 | 1:00 |
| **Total** | | **16:30** (3:30 buffer) |

---

## 01 — Rethinking the Embedded OR Team : from project to product

- **Content:** Title, name, affiliation, github.com/sefop.
- **Visual:** Title slide.
- **Source:** —
- **Time:** 0:30

**Speaker notes.** Good morning. I'm Francisco Zenteno. For the next twenty minutes I want to argue one idea about how
embedded OR teams should be organized, show you one team where it worked, and leave you with a framework to try it.

---

## 02 — Decision-support software turns data, models, and business rules into decisions an airline makes on a cadence

- **Content:** Decision-support software (DSS) is software that runs repeatedly to turn data, mathematical models, and
  business rules into recurring decisions. Four airline examples, one per cadence:
  - **Annual (strategic):** the fleet and network plan.
  - **Monthly (tactical):** crew rosters.
  - **Weekly (tactical):** aircraft maintenance routing.
  - **Daily (operational):** recovering from irregular operations.

  "The value is not in producing one analysis. It is in building a sustainable decision-making tool."
- **Visual:** Four tiles on a strategic → operational axis, from annual to daily.
- **Source:** [SEFOP README](https://github.com/sefop) (definition, quote, daily-recovery example);
  [Section 01](../../book/01-introduction/README.md). The annual, monthly, and weekly examples are adapted for this
  audience.
- **Time:** 1:10

**Speaker notes.** Let me set the context first. This talk is about one kind of OR team: an embedded team that builds
decision-support software. By that I mean software that runs repeatedly and turns data, mathematical models, and
business rules into decisions. You know the examples. Once a year, the fleet and network plan. Every month, crew
rosters. Every week, maintenance routing. Every day, recovering the operation after a storm closes a hub. None of these
ends at a report. The model runs again next cycle, and the cycle after that. So the value is not in one analysis. It is
in a tool the airline can rely on, cycle after cycle.

---

## 03 — The business value of a decision-support system is constrained by the software used to deliver it

- **Content:** The mathematics is the core of a DSS, but the software practices around it are usually weak. There are
  two root causes:
  - **Cultural:** OR scientists are not trained in software engineering, and often do not see why they should be.
  - **Technical:** decision-support software has challenges that ordinary business software does not.

  Evidence: a survey of 168 modellers found code and documentation debt widespread, and mostly introduced deliberately.
  Consequence: this style of software does not maximize the business value of the DSS.
- **Visual:** A funnel: the model's potential value on the left, a narrow neck labeled "software," and the value the
  business receives on the right.
- **Source:** [SEFOP README, "Why: what goes wrong and why"](https://github.com/sefop#why-what-goes-wrong-and-why);
  [Section 01](../../book/01-introduction/README.md) (two root causes); Vidoni & Cunico (2022).
- **Time:** 1:20

**Speaker notes.** Now the problem. In these systems, we put our best effort into the mathematics, and rightly so: it
is the core. The software around it usually gets far less care. There are two reasons. The first is cultural. Most of
us were trained to formulate and solve models, not to engineer software, and many of us do not see why we should. The
second is technical. Decision support raises problems that ordinary business software does not have, such as testing a
model when you do not know the right answer. This is not only anecdote. Vidoni and Cunico surveyed 168 modellers and
found code and documentation debt widespread, and mostly introduced on purpose. Here is the consequence I want you to
keep in mind. A model can be excellent, but the business receives only the value its software is able to deliver.

---

## 04 — An OR team that owns a decision-support product has to operate as a specialized software development team

- **Content:** The governing thought, plus a preview of the three blocks: why it is urgent, how to get there, and
  evidence that it works.
- **Visual:** A pyramid with the governing thought on top and three boxes underneath.
- **Source:** —
- **Time:** 1:00

**Speaker notes.** Here is my answer up front. If an OR team owns a decision-support product, it has to operate as a
specialized software development team. Not only the model: the pipeline, the releases, the automatic tests, and the
conversation with the business. The talk has three parts. First, why this is urgent now. Second, how to get there:
the roles, what the team owns, and how to train scientists. Third, one team where it worked.

---

## 05 — All software is built by discovery, so teams must learn fast and adapt fast, and decision-support software is no exception

- **Content:** No software team knows the right product up front. It learns what users need by releasing and
  observing. Two capabilities keep that loop fast:
  - **Learn fast:** short iterations with feedback from users (agile).
  - **Adapt fast:** every change built, tested, and ready to release automatically (CI/CD, continuous integration and
    delivery).

  In DSS, the loop discovers the formulation too: an objective and constraints the business cannot state precisely.
- **Visual:** A loop, learn (agile) → adapt (CI/CD) → release → learn, with a small tag: "DSS: the formulation is
  discovered too."
- **Source:** Humble & Farley, *Continuous Delivery*;
  [Section 03](../../book/03-software-development-lifecycle/README.md) (requirements row; iteration as gradient
  descent).
- **Time:** 1:10

**Speaker notes.** Let me start with something that is true for all software, not only ours. Nobody gets the product
right on the first try. Software teams learn what users need by releasing something and watching what happens. Two
capabilities decide how fast that loop turns. The first is learning fast: short iterations with real feedback, which
is what agile is for. The second is adapting fast: every change is built, tested, and ready to release automatically.
Humble and Farley call this continuous delivery. Decision support is no exception. If anything, our loop carries one
more unknown, because we are also discovering the formulation. I think of it as gradient descent: each release gives
the gradient for the next step.

---

## 06 — AI coding assistants make this need more urgent

- **Content:** More than 70% of scientific programmers already write code with LLM-based tools. The 2025 DORA report
  describes an AI assistant as an amplifier of the practices around it.
  - **Team with strong practices** (tests, CI/CD, code review): AI output is checked automatically, so the team moves
    faster at good quality.
  - **Team with weak practices:** AI output is not verified, so the team ships more code and more technical debt,
    faster.

  *Accelerate*: in high-performing teams, throughput and stability rise together.
- **Visual (visual A):** A split screen with the same AI multiplier arrow on both sides: on the left, a solid foundation
  and a rising line; on the right, a weak foundation and a growing stack of debt.
- **Source:** [2025 DORA report](https://dora.dev/research/2025/dora-report/); O'Brien & Eisty (2026); Forsgren,
  Humble & Kim, *Accelerate*; [Section 01](../../book/01-introduction/README.md);
  [Section 09](../../book/09-ai-assisted-development/README.md).
- **Time:** 1:20

**Speaker notes.** This is not a new argument, but AI changes its urgency. More than 70% of scientific programmers
already use LLM-based tools to write code. The 2025 DORA report describes these assistants as amplifiers: they
multiply whatever practices are already there. Picture two teams with the same assistant. The first has tests, a
pipeline, and code review, so every suggestion is checked before it reaches production, and the team gets faster
without losing quality. The second has none of that. It also gets faster, but at producing debt. For decision support
there is an extra risk: a wrong formulation looks just as plausible as a right one. Same multiplier, different
foundation. Keep this picture in mind. I will come back to it.

---

## 07 — An embedded OR team should deliberately sit at the strong-practices end of the spectrum

- **Content:** A spectrum of software practices.
  - **Left, no practices:** the team works like a consultant delivering a project. Its software can sustain only
    short-term value.
  - **Right, strong software engineering practices:** the team works like a "software factory" running a product, with
    practices that make long-term value achievable.

  Most teams sit closer to the left. The position should be a deliberate choice, not an accident, and it should point
  right. Closing question: how do we get there?
- **Visual:** A horizontal spectrum with "project / consultant" on the left and "product / software factory" on the
  right; a cluster of dots near the left; a bold arrow pointing right; "How do we get there?" underneath.
- **Source:** Kersten, *Project to Product*; abstract.
- **Time:** 1:20

**Speaker notes.** Put the last three slides together. Value is capped by software, all software is built by discovery,
and AI amplifies whatever practices you have. Now picture a spectrum. On the left, a team with no software practices.
It works like a consultant: it delivers a project and moves on. On the right, a team with strong software engineering
practices. It runs a product. Mik Kersten's *Project to Product* describes this shift: a project is measured by being
on time and on budget, while a product is measured by the business outcomes it keeps producing. Both ends aim, in good
faith, for long-term value, but only software prepared for it can deliver. In my experience, most OR teams sit closer
to the left, and not by choice. That is an observation, not a survey result. My point is that the position should be
deliberate, and it should point right. So the question becomes: how do we get there?

---

## 08 — Getting there means operating as a specialized software development team, because decision-support software differs in three ways

- **Content:** General software engineering practices are necessary, but not sufficient. DSS differs from ordinary
  business software in three ways:
  - **Testing:** the expected output is the very thing the model computes (the oracle problem).
  - **Operation:** run time and solution quality vary with each instance.
  - **Failure:** a failure can be a silently worse decision rather than a crash.
- **Visual:** Three columns, each with an icon: an unknown answer, a variable stopwatch, a silent downward arrow.
- **Source:** [Section 03](../../book/03-software-development-lifecycle/README.md) (difference table);
  [Section 05](../../book/05-testing/README.md); [Section 06](../../book/06-deployment/README.md).
- **Time:** 1:20

**Speaker notes.** My answer is to treat the embedded OR team as a software development team, but a specialized one.
Why specialized? Because a general software team would miss three things. First, testing. In ordinary software you
know the expected output. In ours, the expected output is the thing the model computes, so we need other ways to check
it. Second, operation. The same code can take ten seconds on one instance and an hour on the next. Third, failure. A
decision-support system may never crash. It may quietly produce a worse schedule. Handling these needs both OR
knowledge and software engineering in the same team.

---

## 09 — A specialized team combines four roles whose skills overlap by design

- **Content:** Skills as rows, and a 5-level axis on each row: Beginner · Basic · Intermediate · Advanced · Expert.
  Each role is a shape placed at its level: ▲ OR scientist · ● software developer · ■ engineering manager · ◆ product
  manager.

  | Skill | ▲ OR scientist | ● Developer | ■ Eng. manager | ◆ Product manager |
  |---|:---:|:---:|:---:|:---:|
  | Formulation & solving | 5 | 2 | 3 | 2 |
  | Model testing (no known optimum) | 5 | 3 | 2 | 1 |
  | Clean code & code review | 3 | 5 | 3 | 1 |
  | CI (tests on every change) | 3 | 5 | 4 | 1 |
  | CD & operations | 2 | 5 | 4 | 1 |
  | Monitoring decision quality in production | 4 | 4 | 3 | 3 |
  | Quality & flow metrics | 2 | 3 | 5 | 2 |
  | Business consulting & prioritization | 3 | 1 | 3 | 5 |

  Two callouts: "The scientist writes code, so knows CI, but the developer owns CD." "If the engineering manager does
  not care about quality metrics, the team will not either."
- **Visual:** Eight horizontal axes with role shapes placed on each; the overlaps are visible where shapes cluster.
- **Source:** [Section 08](../../book/08-leading-the-team/README.md) (roles to weigh).
- **Time:** 1:30

**Speaker notes.** What does that team look like? I see four roles. Each row here is a skill, and each shape is a role
placed at its level, from beginner on the left to expert on the right. Notice two things. First, every role is expert in
something different: the scientist in formulation and model testing, the developer in code and delivery, the
engineering manager in quality and flow metrics, and the product manager in the business. Second, the skills overlap on
purpose. The scientist writes code, so the scientist needs continuous integration, but not deep knowledge of
deployment, because the developer owns that. And the engineering manager has to know CI/CD and care about quality. If
the manager does not track those metrics, the team will not either. These levels are my judgment from practice, not
survey data.

---

## 10 — Own what determines the product's value; borrow the rest from platform and enabling teams

- **Content:** Three tiers of capabilities, not roles.
  - **Own (stream-aligned team):** product management, business consulting and formulation, engineering practices and
    CI/CD.
  - **Borrow as a service (platform team):** infrastructure and cloud.
  - **Borrow as coaching (enabling team):** cybersecurity, reliability specialists.
- **Visual:** Three concentric rings, with the OR team in the center.
- **Source:** Skelton & Pais, *Team Topologies*.
- **Time:** 1:20

**Speaker notes.** A specialized team does not mean doing everything alone. *Team Topologies* gives us the vocabulary.
A stream-aligned team (a team that owns one product from end to end) is the OR team. It must own what determines the
product's value: product management, the conversation with the business, and the path from a code change to a release.
It borrows the rest. A platform team provides infrastructure as a service. An enabling team, such as corporate
cybersecurity, helps the OR team build a capability and then steps back. You can borrow expertise, but not
responsibility. The trade-off is cognitive load, and the book is explicit that a team can only hold so much.

---

## 11 — Scientists learn software engineering fastest when it is tailored to the problems they already solve

- **Content:**
  - **Learn in order:** version control → automated testing → CI → software design → deployment. Each step builds on
    the one before.
  - **Tailor it to OR:** generic courses do not cover testing a model without a known optimum, reproducible runs with a
    solver and data, or keeping data, rules, model, and solver separate so each can change.
  - **Practice in code:** short exercises with immediate feedback, such as unit testing, test-driven development, and
    mutation testing.
- **Visual:** A staircase from Beginner to Advanced, with OR-specific steps highlighted.
- **Source:** [Learning Roadmap](../../book/appendix/learning-roadmap.md);
  [Practice Repositories](../../book/appendix/practice-repositories.md);
  [Section 04](../../book/04-design/README.md); [Section 05](../../book/05-testing/README.md);
  [Section 08](../../book/08-leading-the-team/README.md) (training as a lever).
- **Time:** 1:10

**Speaker notes.** The scientists are the primary role for this change, so how do we train them? Three lessons. First,
order matters. Start with version control, then automated tests, then continuous integration, and only then design
and deployment. Each step makes the next one make sense. Second, generic software courses leave a gap. They teach you
to test code whose answer you know. They do not teach you to test a model whose answer you do not know, or to make a
solver run reproducible. That part has to be tailored to OR. Third, reading is not enough. Scientists change their
habits by writing tests against real models, with fast feedback.

---

## 12 — SEFOP packages software engineering tailored for OR teams

- **Content:** SEFOP (Software Engineering Framework for Optimization Programs), four dimensions:
  - **Train:** an open book for OR scientists, plus language-specific practice repositories.
  - **Lead:** guidance for the managers who lead these teams.
  - **Deliver:** reference implementations.
  - **Go Agentic:** AI-assisted development (`sefop-agentic`).
- **Visual:** Four tiles with a QR code to github.com/sefop.
- **Source:** [Section 01](../../book/01-introduction/README.md) (where the book sits in SEFOP).
- **Time:** 0:50

**Speaker notes.** SEFOP is the framework I am building so other teams do not have to work this out from scratch. It has
four dimensions. Train and Lead live in an open book, written for OR scientists and the managers who lead them, with no
software engineering background assumed, and with practice repositories in code. Deliver lives in reference
implementations. Go Agentic covers AI-assisted development. It is open and under construction, and I would welcome your
feedback.

---

## 13 — It has been done: in 15 months, a 4-scientist team reached 2.3x, then 4.1x throughput while code quality held

- **Content:**
  - **Throughput:** deployments / PRs merged per period **[fill in: exact unit and baseline period]**. Baseline 1.0x →
    2.3x after adopting engineering practices → 4.1x after adding agentic development.
  - **Code quality:** unit-test coverage **[fill in]**, number of integration tests **[fill in]**, SonarQube code smells
    **[fill in]**.
  - **Limits:** one team, no control group. The team adopted some of the practices SEFOP now describes; SEFOP itself
    did not exist yet.
- **Visual (visual A, mirrored):** The strong-practices side of slide 6, now with real data: a throughput index over 15
  months with two phase markers, and a small quality panel beside it.
- **Source:** Case study; Forsgren, Humble & Kim, *Accelerate* (throughput metrics).
- **Time:** 1:30

**Speaker notes.** Has this been tried? Yes. Here is one team: four scientists over fifteen months. I measured
throughput the way *Accelerate* recommends, by changes delivered: merged pull requests and deployments. After adopting
engineering practices, throughput reached 2.3 times the baseline. After adding agentic development on top, it reached
4.1 times. Over the same period, test coverage and the number of integration tests went up **[fill in]**, and code
smells **[fill in]**. Three caveats. This is one team, without a control group. Some of the gain likely comes from the
team maturing and the product stabilizing. And the team used some of the practices SEFOP now describes, but SEFOP did
not exist yet, so this case supports the practices, not the framework itself. Now look back at slide 6: this is the
left side of that picture. Same multiplier, different foundation.

---

## 14 — Leaders: staff and measure your OR team as a software team. Scientists: own one practice this quarter

- **Content:**
  - **Recap:** (1) The business value of DSS is capped by its software. (2) AI coding assistants make strong practices
    urgent. (3) Operate as a specialized software team: four roles, own the core, borrow the rest, and train scientists
    in software engineering tailored for OR.
  - **Leaders:** staff your OR team with the roles it needs, and measure quality and throughput together.
  - **Scientists:** pick one practice, for example a CI pipeline that runs your tests, and own it this quarter.
- **Visual:** The three-line recap on top; two columns of asks below; github.com/sefop in the footer.
- **Source:** —
- **Time:** 1:00

**Speaker notes.** To close. The business value of decision-support software is capped by the software that delivers
it. AI makes that cap tighter for teams without practices, and looser for teams with them. So an OR team that owns a
product has to operate as a specialized software team. Two asks. If you lead an OR team, staff it with the roles it
needs, and measure quality and throughput together. If you are a scientist, pick one practice and own it this quarter.
A pipeline that runs your tests on every change is a good first one. Thank you.

---

## Parking lot

Slides removed in revision 3, kept here so they can be placed later.

- **Google, value over time** (old slide 06). Title: "Owning a product means owning its software for as long as it
  runs, so its practices must keep change cheap over time." *Software Engineering at Google* defines software
  engineering as "programming integrated over time." A DSS that runs weekly for five years spends most of its life in
  operation and maintenance. Visual: a short development bar next to a long operation bar, plus two cumulative value
  curves that diverge over time (illustrative). Source: Winters, Manshreck & Wright; `book/03`.
- **Handoff loop** (old slide 05). Title: "The team that discovers the formulation has to own the product, because every
  handoff breaks the loop that improves it." Answers the objection "why not hand the software to IT?" Visual: an
  iteration loop cut by a handoff wall. Source: `book/03`; *Team Topologies*.
- **Deployment pipeline** (old slide 11). Title: "The deployment pipeline is the capability that turns ownership into
  repeatable delivery." Pipeline with OR-specific stages: contract tests → model checks without a known optimum → safe
  release → monitoring of decision quality. Source: *Continuous Delivery*; `book/05`, `book/06`.

---

## References

- Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps.* IT Revolution.
- Humble, J., & Farley, D. (2010). *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment
  Automation.* Addison-Wesley.
- Kersten, M. (2018). *Project to Product: How to Survive and Thrive in the Age of Digital Disruption with the Flow
  Framework.* IT Revolution.
- O'Brien & Eisty (2026). *Computing in Science & Engineering.*
  https://www.computer.org/csdl/magazine/cs/2026/01/11482007/2fJHVugY5UY **[fill in: authors' initials and title]**
- Skelton, M., & Pais, M. (2019). *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT
  Revolution.
- Vidoni, M., & Cunico, M. L. (2022). On technical debt in mathematical programming: An exploratory study.
  *Mathematical Programming Computation.* https://doi.org/10.1007/s12532-022-00225-1
- Winters, T., Manshreck, T., & Wright, H. (2020). *Software Engineering at Google: Lessons Learned from Programming
  Over Time.* O'Reilly.
- DORA (2025). *State of AI-assisted Software Development.* https://dora.dev/research/2025/dora-report/
- SEFOP: https://github.com/sefop
