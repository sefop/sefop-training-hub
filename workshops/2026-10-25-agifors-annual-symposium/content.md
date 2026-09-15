# Rethinking the embedded Operations Research team: from project to product

**Event:** AGIFORS Annual Symposium, 2026-10-25 · **Speaker:** Francisco Zenteno · **Length:** 20 minutes, 15 slides

> [!NOTE]
> Storyline draft. Items marked **[fill in]** need data from the case study before the slides are built.

---

## Governing thought

**An OR team has to own its product, so it has to own the software responsibilities that come with it.**

## SCQA summary

- **Situation.** Embedded OR teams deliver value through software that runs on a cadence.
- **Complication.** Most of these teams are still managed like consultants delivering projects.
The business value of the decision-support system is constrained by the software practices used to deliver it.
- **Question.** What has to change for an embedded OR team to deliver long-term value?
- **Answer.** The governing thought above, proven in three steps and then operationalized.

## Argument structure

0. **Context (slides 2–3).** What decision-support software is, with airline examples, and why its business value is
   constrained by the software used to deliver it.
1. **Syllogism (slides 5–7).** The team has to own the product (link 1). Owning a product means owning its software for
   as long as it runs (link 2, Google). A team that owns the product but not the software caps its value
   (counterexample).
2. **What moving from project to product means (slides 8–11).** Kersten and the 0–1 scale, the DSS lifecycle, Team
   Topologies, and Continuous Delivery.
3. **Proof (slide 12).** The case study, framed with Accelerate's throughput metrics.
4. **How (slides 13–14).** Top-down and bottom-up change, then SEFOP.

## Timing

| Block | Slides | Time |
|---|:---:|:---:|
| Open | 1–4 | 4:00 |
| Syllogism | 5–7 | 4:00 |
| Project → product | 8–11 | 5:20 |
| Proof | 12 | 1:30 |
| How | 13–14 | 2:00 |
| Close | 15 | 1:00 |
| **Total** | | **17:50** (2:10 buffer) |

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
  - **Daily (operational):** recovering the operation after a weather disruption.

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

## 04 — An OR team has to own its product, so it has to own the software responsibilities that come with it

- **Content:** The governing thought, plus a preview of the three blocks: why ownership is unavoidable, what it means to
  move from project to product, and how to get there.
- **Visual:** A pyramid with the governing thought on top and three boxes underneath.
- **Source:** —
- **Time:** 1:00

**Speaker notes.** Here is my answer up front. If an OR team owns the product, it owns the software responsibilities
that come with it. Not only the model: the pipeline, the releases, the tests, and the conversation with the business.
The talk has three parts. First, I prove that claim in three steps. Second, I describe what moving from project to
product means, using five books most of you can pick up. Third, I show one case and a framework to make the change.

---

## 05 — The team that discovers the formulation has to own the product, because every handoff breaks the loop that improves it

- **Content:** Link 1. The business cannot state the objective and constraints precisely, so the formulation is
  discovered by iterating. Each release teaches the team something about the next one. When the model sits with one
  team and the software with another, every iteration crosses a handoff.
- **Visual:** A loop (formulate → build → release → learn), with a handoff wall cutting through it for the "split" case.
- **Source:** [Section 03](../../book/03-software-development-lifecycle/README.md) (requirements row; iteration as
  gradient descent); Skelton & Pais, *Team Topologies* (handoffs slow the flow of change).
- **Time:** 1:20

**Speaker notes.** The first objection I usually hear is: why not hand the software to IT? My answer comes from how OR
requirements work. In ordinary software, the business describes features. In decision-support, the business cannot
fully state its objective or its constraints. We discover the formulation by releasing, watching planners use the
result, and adjusting. I think of it as gradient descent: each pass gives the gradient for the next step. If the model
lives in one team and the software in another, the gradient is computed in one place and the step is taken in another.
*Team Topologies* makes the same point for any software: handoffs slow the flow of change. So the team that discovers
the formulation has to own the product.

---

## 06 — Owning a product means owning its software for as long as it runs, so its practices must keep change cheap over time

- **Content:** Link 2. *Software Engineering at Google* defines software engineering as "programming integrated over
  time." A decision-support system that runs weekly for five years spends most of its life in operation and
  maintenance, not in development. Without practices, the cost of each change grows and value flattens. With
  practices, change stays cheap and value keeps compounding.
- **Visual:** Top: a timeline in which development is a short bar and operation plus maintenance is a long one. Bottom:
  two curves of cumulative value over time that start together, then separate (illustrative, not data).
- **Source:** Winters, Manshreck & Wright, *Software Engineering at Google*;
  [Section 03](../../book/03-software-development-lifecycle/README.md) (the lifecycle does not end at deployment).
- **Time:** 1:20

**Speaker notes.** The second step. Google's book separates programming from software engineering with one variable:
time. Code you run once only has to work once. Code you run for years has to survive new data, new rules, new solvers,
and new people. An OR product is the second kind, and most of its life is operation and maintenance. What time does is
change the cost of change. Early on, the team with no tests and the team with a pipeline look the same. Sometimes the
first team even looks faster. Over months, one team's changes get riskier and slower, and the other team's stay
routine. These curves are illustrative, not data. If we own the product, we own that whole timeline, and that is where
the software responsibilities live.

---

## 07 — A team that builds a product without software practices caps its value, and AI now helps it pile up debt faster

- **Content:** The counterexample: a team that owns the product but not the software practices. Four symptoms: the code
  works on one machine only; peers, and even the original authors, struggle to extend it; developers fear modifying it;
  and it is eventually rewritten rather than evolved. The 2025 DORA report describes AI assistants as amplifiers of the
  practices around them.
- **Visual (visual A):** A multiplier arrow applied to a weak foundation, producing a growing stack of debt.
- **Source:** [Section 01](../../book/01-introduction/README.md) (four symptoms; AI as an amplifier);
  [2025 DORA report](https://dora.dev/research/2025/dora-report/).
- **Time:** 1:20

**Speaker notes.** Now the typical case. The team builds decision support, so it has a product, but it does not invest
in CI/CD (continuous integration and delivery: the automated path from a code change to a tested release) or in other
software practices. You probably recognize the symptoms. It runs on one laptop. Nobody wants to touch it. Eventually
someone proposes a rewrite. Every change gets slower, and that caps the value the product can deliver. Add AI coding
assistants to this team. The 2025 DORA report describes AI as an amplifier: strong practices get faster at good
quality, and weak practices ship more debt. Keep this picture in mind. I will come back to it.

---

## 08 — Projects end at handoff; products are funded and measured for as long as they create value

- **Content:** A scale from 0 to 1. At **0**, the team works like a consultant: it delivers a project, and its software
  can sustain only short-term value. At **1**, it works like a "software factory": it runs a product, with practices
  that make long-term value achievable. Most teams sit closer to 0. Below the scale, project vs product in four rows.
  **Funding:** fixed budget and scope vs ongoing investment in a value stream. **Success measure:** on time and on budget
  vs business outcomes. **Team:** assembled and disbanded vs stable. **Risk after delivery:** someone else's vs the
  team's.
- **Visual:** Across the top, a horizontal 0–1 scale with "consultant / project" at 0, "software factory / product" at
  1, and a cluster of dots near 0. Underneath, a two-column table.
- **Source:** Kersten, *Project to Product*; abstract.
- **Time:** 1:20

**Speaker notes.** Let me put a name on the change. I describe OR teams on a scale from 0 to 1. At 0, a team operates as
a consultant: it delivers a project and moves on, and its software can sustain only short-term value. At 1, it operates
as a software factory: it runs a product, with practices that make long-term value achievable. Both ends aim, in good
faith, for long-term value, but only software prepared for it can deliver. Mik Kersten's *Project to Product* gives this
scale its vocabulary. A project has a budget, a scope, and an end date, and it counts as a success if it arrives on time
and on budget. A product is funded as long as it creates value, it is measured by business outcomes, and the team stays
with it. Notice the last row. After delivery, a project's risk belongs to someone else, and a product's risk belongs to
the team. In my experience, most OR teams sit closer to 0. That is an observation, not a survey result.

---

## 09 — Owning a DSS means owning OR-specific responsibilities in every lifecycle phase

- **Content:** A condensed difference table.
  - **Testing:** the expected output is the very thing the model computes (the oracle problem).
  - **Operation:** run time and solution quality vary with each instance.
  - **Failure:** a failure can be a silently worse decision rather than a crash.
- **Visual:** Three rows: phase, ordinary software, decision-support software.
- **Source:** [Section 03](../../book/03-software-development-lifecycle/README.md) (difference table);
  [Section 05](../../book/05-testing/README.md); [Section 06](../../book/06-deployment/README.md).
- **Time:** 1:10

**Speaker notes.** This is why a general IT team cannot simply absorb these responsibilities for us. Decision support
is different from ordinary software in each phase. In testing, we usually do not know the correct answer in advance,
because the answer is what the model computes. In operation, the same code can take ten seconds on one instance and an
hour on the next. And a failure may never crash. It may quietly produce a worse schedule. Owning the product means
owning these differences. Most of them need OR knowledge to handle.

---

## 10 — Own what determines the product's value; borrow the rest from platform and enabling teams

- **Content:** Three tiers of capabilities, not roles.
  - **Own (stream-aligned team):** product management, business consulting and formulation, engineering practices and
    CI/CD.
  - **Borrow as a service (platform team):** infrastructure and cloud.
  - **Borrow as coaching (enabling team):** cybersecurity, reliability specialists.
- **Visual:** Three concentric rings, with the OR team in the center.
- **Source:** Skelton & Pais, *Team Topologies*.
- **Time:** 1:30

**Speaker notes.** Owning everything does not mean doing everything. *Team Topologies* gives us the vocabulary. A
stream-aligned team (a team that owns one product from end to end) is the OR team. It must own what determines the
product's value: product management, the conversation with the business, and the path from a code change to a release.
It borrows the rest. A platform team provides infrastructure as a service. An enabling team, such as corporate
cybersecurity, helps the OR team build a capability and then steps back. Two points. First, these are capabilities, not
headcount: a scientist can hold one. Second, you can borrow expertise, but not responsibility. The trade-off is
cognitive load, and the book is explicit that a team can only hold so much.

---

## 11 — The deployment pipeline is the capability that turns ownership into repeatable delivery

- **Content:** A deployment pipeline (the automated sequence every change passes through before release) with
  OR-specific stages: unit and contract tests → model checks that work without a known optimum → safe release →
  monitoring of decision quality in production.
- **Visual:** A left-to-right pipeline, with the OR-specific stages highlighted.
- **Source:** Humble & Farley, *Continuous Delivery*; [Section 05](../../book/05-testing/README.md);
  [Section 06](../../book/06-deployment/README.md).
- **Time:** 1:20

**Speaker notes.** If I had to pick one capability that makes ownership real, it would be the deployment pipeline.
Humble and Farley define it as the automated path every change follows, from commit to release. The principle I like
most from that book: if releasing hurts, do it more often, until it stops hurting. For an OR team, the pipeline needs
stages that ordinary software does not: tests that check a model without knowing its optimal answer, a release that
does not put current decisions at risk, and monitoring for decisions that quietly get worse. Our book covers each of
these stages.

---

## 12 — In 15 months, a 4-scientist team reached 2.3x, then 4.1x throughput, while code quality held

- **Content:**
  - **Throughput:** deployments / PRs merged per period **[fill in: exact unit and baseline period]**. Baseline 1.0x →
    2.3x after adopting engineering practices → 4.1x after adding agentic development.
  - **Code quality:** unit-test coverage **[fill in]**, number of integration tests **[fill in]**, SonarQube code smells
    **[fill in]**.
  - **Limits:** one team, no control group.
- **Visual (visual A, mirrored):** The same multiplier arrow as slide 7, now applied to a solid foundation. Beside it, a
  throughput index over 15 months with two phase markers and a small quality panel.
- **Source:** Case study; Forsgren, Humble & Kim, *Accelerate* (throughput metrics).
- **Time:** 1:30

**Speaker notes.** Does it pay off? Here is one team: four scientists over fifteen months. I measured throughput the way
*Accelerate* recommends, by changes delivered: merged pull requests and deployments. After adopting engineering
practices, throughput reached 2.3 times the baseline. After adding agentic development on top, it reached 4.1 times.
Over the same period, test coverage and the number of integration tests went up **[fill in]**, and code smells
**[fill in]**. Two caveats. This is one team, without a control group, and some of the gain likely comes from the team
maturing and the product stabilizing. Now compare this with slide 7: it is the same AI multiplier. The difference is the
foundation.

---

## 13 — Leaders set ownership from the top; scientists build it from the bottom

- **Content:** Top-down: leaders fund and measure the team as a product. Bottom-up: scientists are the primary role for
  the mindset change. Four themes that change practitioner behavior: make the problem visible, make change the easy path,
  make it theirs, and know your terrain.
- **Visual:** Two arrows meeting in the middle, with the four themes along the bottom arrow.
- **Source:** [Section 08](../../book/08-leading-the-team/README.md) (DSI 2026 paper on why OR practitioners resist
  software engineering practices).
- **Time:** 1:10

**Speaker notes.** A leader can declare that the team owns a product. That sets the direction, but it does not change
how code gets written on Tuesday. That change comes from the bottom, and the scientists are the primary role for it.
In a companion paper, we looked at why OR practitioners resist software engineering practices and what changes their
behavior. Four themes came out: make the problem visible, make the change the easy path, let the team make it their
own, and adapt to your terrain. Also report quality and throughput together. Showing that speed did not drop is what
defuses the belief that good practice slows delivery.

---

## 14 — SEFOP gives OR teams a path from project to product

- **Content:** SEFOP (Software Engineering Framework for Optimization Programs), four dimensions: **Train** (the
  training hub, a book for OR scientists and their managers), **Lead**, **Deliver** (reference implementations), and
  **Go Agentic** (`sefop-agentic`).
- **Visual:** Four tiles with a QR code to github.com/sefop.
- **Source:** [Section 01](../../book/01-introduction/README.md) (where the book sits in SEFOP).
- **Time:** 0:50

**Speaker notes.** SEFOP is the framework I am building so other teams do not have to work this out from scratch. It has
four dimensions. Train and Lead live in an open book, written for OR scientists and the managers who lead them, with no
software engineering background assumed. Deliver lives in reference implementations. Go Agentic covers AI-assisted
development. It is open and under construction, and I would welcome your feedback.

---

## 15 — Leaders: fund the product, not projects. Scientists: own one capability this quarter

- **Content:** **Leaders:** fund and measure your OR team as a product team. **Scientists:** pick one capability from
  slide 10, for example a CI pipeline that runs your tests, and own it this quarter. Callback: same multiplier,
  different foundation.
- **Visual:** Two columns, the asks, then the references strip.
- **Source:** —
- **Time:** 1:00

**Speaker notes.** Two asks. If you lead an OR team, fund and measure it as a product, not as a sequence of projects. If
you are a scientist, pick one capability and own it this quarter. A pipeline that runs your tests on every change is a
good first one. AI will multiply whatever foundation your team has. The question is what it multiplies. Thank you.

---

## References

- Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps.* IT Revolution.
- Humble, J., & Farley, D. (2010). *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment
  Automation.* Addison-Wesley.
- Kersten, M. (2018). *Project to Product: How to Survive and Thrive in the Age of Digital Disruption with the Flow
  Framework.* IT Revolution.
- Skelton, M., & Pais, M. (2019). *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT
  Revolution.
- Vidoni, M., & Cunico, M. L. (2022). On technical debt in mathematical programming: An exploratory study.
  *Mathematical Programming Computation.* https://doi.org/10.1007/s12532-022-00225-1
- Winters, T., Manshreck, T., & Wright, H. (2020). *Software Engineering at Google: Lessons Learned from Programming
  Over Time.* O'Reilly.
- DORA (2025). *State of AI-assisted Software Development.* https://dora.dev/research/2025/dora-report/
- SEFOP: https://github.com/sefop
