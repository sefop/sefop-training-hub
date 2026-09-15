# Rethinking the embedded Operations Research team: from project to product

**Event:** AGIFORS Annual Symposium, 2026-10-25 · **Speaker:** Francisco Zenteno · **Length:** 20 minutes, 14 slides

> [!NOTE]
> Storyline draft. Items marked **[fill in]** need data from the case study before the slides are built.

---

## Governing thought

**An OR team that owns a decision-support product has to operate as a specialized software development team.**

## SCQA summary

- **Situation.** Embedded OR teams deliver value through software that runs on a cadence (decision-support systems, or DSS).
- **Complication.** A DSS usually has weak software engineering practices, especially those that surround the mathematics. The business value of the
  DSS is constrained by the software practices used to deliver it.
- **Question.** What has to change for an embedded OR team to unlock the maximum value of its DSS from a software perspective?
- **Answer.** The governing thought above: why it is urgent, how to get there, and evidence that it works.

## Argument structure

0. **Context (slides 2–4).** Decision-support software delivers value only if it keeps working; most is built with weak software practices; and those
   practices constrain its business value.
1. **Thesis (slide 5).** The governing thought.
2. **Why now (slides 6–8).** AI coding assistants amplify whatever practices a team has. Decision-support software needs everything ordinary software
   needs, plus three things it does not. So the team should deliberately sit at the strong-practices end of the spectrum.
3. **How (slides 9–12).** Operate as a specialized software development team: the roles and skills it needs, what it owns and borrows, how to train
   scientists, and SEFOP.
4. **Proof (slide 13).** A case study, framed with Accelerate's throughput metrics.
5. **Close (slide 14).** Recap and two asks.

## Timing

| Block | Slides | Time |
|---|:---:|:---:|
| Open, context, and thesis | 1–5 | 5:10 |
| Why now | 6–8 | 4:10 |
| How | 9–12 | 4:50 |
| Proof | 13 | 1:30 |
| Close | 14 | 1:00 |
| **Total** | | **16:40** (3:20 buffer) |

---

## 01 — Rethinking the embedded OR Team as a specialized software development team

- **Content:**
  - Title, name, affiliation, github.com/sefop.
- **Visual:** Title slide.
- **Source:** —
- **Time:** 0:30

---

## 02 — An airline's decision-support software delivers value only if it keeps working, cycle after cycle

- **Content:**
  1. Decision-support software (DSS) runs repeatedly to turn data, mathematical models, and business rules into recurring decisions.
  2. Airlines run DSS at every cadence:
     - **Annual (strategic):** the fleet and network plan.
     - **Monthly (tactical):** crew rosters.
     - **Weekly (tactical):** aircraft maintenance routing.
     - **Daily (operational):** recovering from irregular operations.
  3. None of these ends at a report: the model runs again next cycle, and the cycle after that.
  4. "The value is not in producing one analysis. It is in building a sustainable decision-making tool."
- **Visual:** Four tiles on a strategic → operational axis, from annual to daily.
- **Source:** [SEFOP README](https://github.com/sefop) (definition, quote, daily-recovery example);
  [Section 01](../../book/01-introduction/README.md). The annual, monthly, and weekly examples are adapted for this audience.
- **Time:** 1:10

---

## 03 — Most decision-support systems are built with weak software practices, for cultural and technical reasons

- **Content:**
  1. The mathematics is the core of a DSS, and it gets the team's best effort and training.
  2. **Cultural root cause:** OR scientists are not trained in software engineering, and often do not see why they should be.
  3. **Technical root cause:** a DSS has challenges that ordinary business software does not.
  4. **Evidence:** a survey of 168 modellers found code and documentation debt widespread, and mostly introduced deliberately.
- **Visual:** Two columns, "cultural" and "technical", above a callout: "168 modellers: debt widespread, mostly deliberate."
- **Source:** [SEFOP README, "Why: what goes wrong and why"](https://github.com/sefop#why-what-goes-wrong-and-why);
  [Section 01](../../book/01-introduction/README.md) (two root causes); Vidoni & Cunico (2022).
- **Time:** 1:00

---

## 04 — Weak software practices constrain the business value of a decision-support system

- **Content:**
  1. Code works on one machine but is difficult to reproduce elsewhere, so results are hard to trust or rerun.
  2. Systems are difficult for peers, and even for their original authors, to maintain or extend, so the DSS adapts slowly when the business changes.
  3. Developers are afraid of modifying the system because the consequences are unpredictable, so improvements do not ship.
  4. Applications eventually need to be rewritten rather than evolved, so the investment restarts instead of compounding.
  5. However good the model, the business receives only the value its software can deliver.
- **Visual:** A funnel: the model's potential value on the left, a narrow neck made of the four consequences, and the value the business receives on
  the right.
- **Source:** [SEFOP README, "Why: what goes wrong and why"](https://github.com/sefop#why-what-goes-wrong-and-why);
  [Section 01](../../book/01-introduction/README.md) (four symptoms).
- **Time:** 1:10

---

## 05 — To unlock full value the OR team has to operate as a specialized software development team

- **Content:**
  1. A DSS is a product, and the team that owns it owns its software responsibilities.
  2. Those responsibilities go beyond the model: automatic tests, the pipeline, releases, and the conversation with the business.
  3. The talk supports this in three blocks:
     - **Why now:** AI coding assistants, what makes DSS different, and where the team should sit.
     - **How:** roles and skills, what to own and what to borrow, training, and SEFOP.
     - **Proof:** one team where it worked.
- **Visual:** A pyramid with the governing thought on top and three boxes underneath.
- **Source:** —
- **Time:** 1:00

---

## 06 — AI coding assistants make strong software practices more urgent

- **Content:**
  1. More than 70% of scientific programmers already write code with LLM-based tools.
  2. An AI assistant amplifies the practices around it (2025 DORA report).
  3. **Team with strong practices** (tests, CI/CD, code review): AI output is checked automatically, so the team moves faster at good quality.
  4. **Team with weak practices:** AI output is not verified, so the team ships more code and more technical debt, faster.
  5. In a DSS the risk is higher: a wrong formulation looks just as plausible as a right one.
  6. *Accelerate*: in high-performing teams, throughput and stability rise together.
- **Visual (visual A):** A split screen with the same AI multiplier arrow on both sides: on the left, a solid foundation and a rising line; on the
  right, a weak foundation and a growing stack of debt. Caption: "Same multiplier, different foundation."
- **Source:** [2025 DORA report](https://dora.dev/research/2025/dora-report/); O'Brien & Eisty (2026); Forsgren, Humble & Kim, *Accelerate*;
  [Section 01](../../book/01-introduction/README.md); [Section 09](../../book/09-ai-assisted-development/README.md).
- **Time:** 1:20

---

## 07 — Decision-support software needs everything ordinary software needs, plus three things it does not

- **Content:**
  1. Like all software, a DSS is built by discovery: nobody gets it right on the first try.
     - **Learn fast:** short iterations with user feedback (agile).
     - **Adapt fast:** every change built, tested, and ready to release automatically (CI/CD).
     - In a DSS, even the formulation is discovered this way.
  2. **Testing:** the expected output is the very thing the model computes (the oracle problem). How do you test an optimization model when you do not
     know the optimum? You need other checks, such as feasibility, or how the optimum should move when the input changes.
  3. **Operation:** run time and solution quality vary with each instance. The same code can take ten seconds on one instance and an hour on the next.
  4. **Failure:** a failure can be a silently worse decision rather than a crash.
  5. Handling these differences needs OR knowledge and software engineering in the same team.
- **Visual:** A base bar labeled "all software: learn fast (agile) · adapt fast (CI/CD)", with three columns on top of it, each with an icon: an
  unknown answer, a variable stopwatch, a silent downward arrow.
- **Source:** Humble & Farley, *Continuous Delivery*; [Section 03](../../book/03-software-development-lifecycle/README.md) (requirements row;
  difference table); [Section 05](../../book/05-testing/README.md); [Section 06](../../book/06-deployment/README.md).
- **Time:** 1:30

---

## 08 — An embedded OR team should deliberately sit at the strong-practices end of the spectrum

- **Content:**
  1. Software practices form a spectrum:
     - **Left, no practices:** the team works like a consultant delivering a project, measured by being on time and on budget. Its software caps the
       value the model can deliver.
     - **Right, strong software engineering practices:** the team works like a "software factory" running a product, measured by the business outcomes
       it keeps producing. Its practices unlock the full value of the model.
  2. Both ends aim, in good faith, for the full value of the model, but only software prepared for it can deliver it.
  3. Most OR teams sit closer to the left, and not by choice (an observation, not a survey result).
  4. The position should be deliberate, and it should point right: that is where the value cap from slide 4 is lifted.
  5. How to get there: operate as a specialized software development team.
- **Visual:** A horizontal spectrum with "project / consultant" on the left and "product / software factory" on the right; a cluster of dots near the
  left; a bold arrow pointing right; "How do we get there?" underneath.
- **Source:** Kersten, *Project to Product*; abstract.
- **Time:** 1:20

---

## 09 — A specialized team combines four roles whose skills overlap by design

- **Content:**
  1. Four roles: ▲ OR scientist · ● software developer · ■ engineering manager · ◆ product manager.
  2. Each role is the expert in something different: the scientist in formulation and model testing, the developer in code and delivery, the
     engineering manager in quality and flow metrics, the product manager in the business.
  3. Skills overlap on purpose:
     - The scientist writes code, so knows CI, but the developer owns CD.
     - The engineering manager knows CI/CD and cares about quality. If the manager does not track quality metrics, the team will not either.
  4. Skill levels, from 1 to 5 (Beginner · Basic · Intermediate · Advanced · Expert), reflect judgment from practice, not survey data:

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

- **Visual:** Eight horizontal axes, one per skill, with the role shapes placed on each; the overlaps are visible where shapes cluster.
- **Source:** [Section 08](../../book/08-leading-the-team/README.md) (roles to weigh).
- **Time:** 1:30

---

## 10 — Own what determines the product's value; borrow the rest from platform and enabling teams

- **Content:**
  1. The OR team is a stream-aligned team: it owns one product from end to end.
  2. **Own:** product management, business consulting and formulation, engineering practices and CI/CD.
  3. **Borrow as a service (platform team):** infrastructure and cloud.
  4. **Borrow as coaching (enabling team):** cybersecurity and reliability specialists, who help the team build a capability and then step back.
  5. You can borrow expertise, but not responsibility.
  6. The limit is cognitive load: a team can only hold so much.
- **Visual:** Three concentric rings, with the OR team in the center.
- **Source:** Skelton & Pais, *Team Topologies*.
- **Time:** 1:20

---

## 11 — Scientists learn software engineering fastest when it is tailored to the problems they already solve

- **Content:**
  1. Scientists are the primary role for this change.
  2. Order matters: version control → automated testing → CI → software design → deployment. Each step makes the next one make sense.
  3. Generic courses teach you to test code whose answer you know. OR scientists also need to learn:
     - Testing a model without a known optimum.
     - Reproducible runs with a solver and data.
     - Keeping data, rules, model, and solver separate, so each can change.
  4. Reading is not enough: habits change by writing tests against real models, with fast feedback (exercises in unit testing, test-driven
     development, and mutation testing).
- **Visual:** A staircase from Beginner to Advanced, with OR-specific steps highlighted.
- **Source:** [Learning Roadmap](../../book/appendix/learning-roadmap.md); [Practice Repositories](../../book/appendix/practice-repositories.md);
  [Section 04](../../book/04-design/README.md); [Section 05](../../book/05-testing/README.md); [Section 08](../../book/08-leading-the-team/README.md)
  (training as a lever).
- **Time:** 1:10

---

## 12 — SEFOP packages software engineering tailored for OR teams

- **Content:**
  1. SEFOP (Software Engineering Framework for Optimization Programs) exists so OR teams do not have to work this out from scratch.
  2. **Train:** an open book for OR scientists, with no software engineering background assumed, plus language-specific practice repositories.
  3. **Lead:** guidance for the managers who lead these teams.
  4. **Deliver:** reference implementations.
  5. **Go Agentic:** AI-assisted development (`sefop-agentic`).
  6. Open and under construction; feedback welcome.
- **Visual:** Four tiles with a QR code to github.com/sefop.
- **Source:** [Section 01](../../book/01-introduction/README.md) (where the book sits in SEFOP).
- **Time:** 0:50

---

## 13 — It has been done: in 15 months, a 4-scientist team reached 2.3x, then 4.1x throughput while code quality held

- **Content:**
  1. One team: four scientists over 15 months.
  2. Throughput measured as *Accelerate* recommends, by changes delivered: deployments / PRs merged per period
     **[fill in: exact unit and baseline period]**.
     - Baseline 1.0x → 2.3x after adopting engineering practices → 4.1x after adding agentic development.
  3. Code quality held: unit-test coverage **[fill in]**, number of integration tests **[fill in]**, SonarQube code smells **[fill in]**.
  4. Same AI multiplier as slide 6, on a strong foundation.
  5. Limits:
     - One team, no control group.
     - Some of the gain likely comes from the team maturing and the product stabilizing.
     - The team adopted some of the practices SEFOP now describes, but SEFOP did not exist yet, so the case supports the practices, not the framework
       itself.
- **Visual (visual A, mirrored):** The strong-practices side of slide 6, now with real data: a throughput index over 15 months with two phase markers,
  and a small quality panel beside it.
- **Source:** Case study; Forsgren, Humble & Kim, *Accelerate* (throughput metrics).
- **Time:** 1:30

---

## 14 — Leaders: staff and measure your OR team as a software team. Scientists: own one practice this quarter

- **Content:**
  1. The business value of a DSS is capped by its software practices.
  2. AI coding assistants make strong practices urgent, and a DSS needs specialized ones.
  3. Operate as a specialized software team: four roles, own the core, borrow the rest, and train scientists in software engineering tailored for OR.
  4. **Leaders:** staff your OR team with the roles it needs, and measure quality and throughput together.
  5. **Scientists:** pick one practice, for example a CI pipeline that runs your tests on every change, and own it this quarter.
- **Visual:** The three-line recap on top; two columns of asks below; github.com/sefop in the footer.
- **Source:** —
- **Time:** 1:00

---

## Parking lot

Slides removed in revision 3, kept here so they can be placed later.

- **Google, value over time** (old slide 06). Title: "Owning a product means owning its software for as long as it runs, so its practices must keep
  change cheap over time." *Software Engineering at Google* defines software engineering as "programming integrated over time." A DSS that runs weekly
  for five years spends most of its life in operation and maintenance. Visual: a short development bar next to a long operation bar, plus two
  cumulative value curves that diverge over time (illustrative). Source: Winters, Manshreck & Wright; `book/03`.
- **Handoff loop** (old slide 05). Title: "The team that discovers the formulation has to own the product, because every handoff breaks the loop that
  improves it." Answers the objection "why not hand the software to IT?" Visual: an iteration loop cut by a handoff wall. Source: `book/03`; *Team
  Topologies*.
- **Deployment pipeline** (old slide 11). Title: "The deployment pipeline is the capability that turns ownership into repeatable delivery." Pipeline
  with OR-specific stages: contract tests → model checks without a known optimum → safe release → monitoring of decision quality. Source: *Continuous
  Delivery*; `book/05`, `book/06`.

---

## References

- Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps.* IT Revolution.
- Humble, J., & Farley, D. (2010). *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation.* Addison-Wesley.
- Kersten, M. (2018). *Project to Product: How to Survive and Thrive in the Age of Digital Disruption with the Flow Framework.* IT Revolution.
- O'Brien & Eisty (2026). *Computing in Science & Engineering.* https://www.computer.org/csdl/magazine/cs/2026/01/11482007/2fJHVugY5UY
  **[fill in: authors' initials and title]**
- Skelton, M., & Pais, M. (2019). *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution.
- Vidoni, M., & Cunico, M. L. (2022). On technical debt in mathematical programming: An exploratory study. *Mathematical Programming Computation.*
  https://doi.org/10.1007/s12532-022-00225-1
- Winters, T., Manshreck, T., & Wright, H. (2020). *Software Engineering at Google: Lessons Learned from Programming Over Time.* O'Reilly.
- DORA (2025). *State of AI-assisted Software Development.* https://dora.dev/research/2025/dora-report/
- SEFOP: https://github.com/sefop
