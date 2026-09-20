# Rethinking the embedded Operations Research team: from project to product, and how to get there

**Event:** AGIFORS Annual Symposium, 2026-10-25  
**Speaker:** Francisco Zenteno  
**Length:** 20 minutes  


## Governing thought

**An OR team that owns a decision-support product has to operate as a specialized software development team.**


# 01 <Repeats the title here>

- **Content:**
  - Title, name, affiliation, github.com/sefop.
- **Visual:** Title slide.
- **Source:** —


## 02 Working in a project v/s developing a product

- **Content:**
  1. Operations Research (OR) turns data + business rules + mathematics into a decision.
  2. If this decision is needed at some cadence (like annual fleet composition, monthly crew sequences, or daily crew recovery) --> then
  the OR solution becomes a software product: a decision-support system (DSS).
  3. The business value comes from building a sustainable decision-making product over the entire lifetime of the business need.


## 03 DSS often have weak software practices surrounding strong mathematics

- **Content:**
  1. **Cultural root cause:** OR scientists are typically trained deeply in applied mathematics, but not in software engineering.
  2. **Technical root cause:** a DSS has unique challenges deriving from the usage of applied mathematics. (examples: how to automatically test an optimization model? 
     how to design the system to be solver-agnostic?)
  3. **Evidence:** a survey of 168 modelers found code and documentation debt widespread, and mostly introduced deliberately.
- **Visual:** Two columns, "cultural" and "technical", above a callout: "168 modelers: debt widespread, mostly deliberate."

- **Source:** [SEFOP README, "Why: what goes wrong and why"](https://github.com/sefop#why-what-goes-wrong-and-why);
  [Section 01](../../book/01-introduction/README.md) (two root causes); Vidoni & Cunico (2022).


## 04 Weak software puts a ceiling on the value the product can deliver

- **Content:**
  1. Weak foundations make systems harder to maintain, test, deploy, and adapt.
  2. Short-term delivery speed can be misleading if every later change becomes more expensive.
  3. Eventually, systems may need to be rewritten instead of evolved, so the investment restarts instead of compounding.
  
- **Visual:** A progress-over-time chart, after Ousterhout's tactical vs. strategic programming. Vertical axis: progress; horizontal axis: time
  (years). Three illustrative curves, not data:
  - **Curve 1, short-lived system (about 1 year):** starts steepest, then flattens quickly as each change costs more (a logarithmic shape). When
    further progress is no longer economically viable, the system is rewritten or discarded.
  - **Curve 2, legacy system (a few years):** survives the short term, but stalls once the original authors leave. Changes become very
    expensive, and the curve flattens.
  - **Curve 3, strategic system:** built with proper practices from the beginning. Slower at first, because it invests in its foundations, then
    a steady line (y = x) that overtakes curves 1 and 2 and stays economically efficient for its whole life.
  - Callout where curve 3 overtakes the others: "The early speed of curves 1 and 2 was temporary."
- **Source:** *A Philosophy of Software Design* (tactical vs. strategic programming). Label this as illustratrive.


## 05 To unlock the full value the OR team has to operate as a specialized software development team

- **Content:**
  1. A DSS contains both **decision logic** and **software-engineering responsibilities**.
  2. Some critical problems sit exactly at the intersection: model testing, solver integration, experimentation, CI, and monitoring decision quality.
  3. Therefore, neither a traditional OR team nor a generic software team is sufficient on its own.

- **Visual:** Two overlapping circles: **Operations Research** and **Software Engineering**. The overlap contains examples showed at the right, such as:
  - solver-agnostic architecture
  - multiple-algorithms design (ex: enumeration / MIP / heuristics depending on instance size)
  - reproducible experiments
  - automatic testing of the solution of an optimization model
  - decision-quality monitoring in production


## 06 Case of study: strengthening the engineering foundation led to throughput and quality improving together

- **Content:**
  1. Describe the case from the DSI paper: 15-month project turning a pilot into a better system
  2. In one four-scientist team over 15 months, throughput moved from **1.0× → 2.3×** after adopting engineering practices.
  3. Software quality improved as well: unit testing coverage rose 42 pp, and code smells fell by ~2/3.
  4. This is consistent with a broader software-engineering principle: mature engineering organizations do 
  not treat throughput and quality as opposing objectives.
- Source: cite the paper from DSI, Accelerate, Modern SOfrtwre Engineering, Google Book?
**Visual**: TBD.

# 07 AI-coding assistants make this transition more urgent

1. AI-coding assistants act as an amplifier of current software engineering practices (DORA, 2025)
   - Teams with strong foundations move faster at higher quality
   - Teams with weak foundations ship more software with higher technical debt
2. AI-coding assistants are already in use: **the switch is on**.
3. Strong engineering practices are therefore the prerequisite for capturing the value of agentic development sustainably.
**Visual**: TDB, maybe split screen with the same **AI multiplier** entering both sides.


## 08 The destination is product ownership, not project delivery

- **Content:**
  1. **Project mindset:** deliver the model or project and optimize for completion.
  2. **Product mindset:** continuously own the business outcome and the software that produces it.
  3. An embedded OR team should deliberately move toward the product end of the spectrum.

- **Visual:** Horizontal spectrum:
  - left: **Project / Consultant**
  - right: **Product / Continuous ownership**
  - bold arrow pointing right

  Supporting contrast:
  - **Project:** completion, handoff, short-term delivery
  - **Product:** outcomes, iteration, long-term ownership


## 09 The team owns the decision product, but it does not need to do everything itself

- **Content:**
  1. **Own:** business interaction, formulation, testing strategy, software quality, delivery responsibility, and production behavior of the DSS.
  2. **Borrow:** infrastructure, cybersecurity, cloud platforms, reliability expertise, and other specialist capabilities.
  3. Within the team, skills should overlap—but roles remain specialized.

- **Visual:** Three-layer operating model:
  - **Core embedded OR product team:** OR scientists, software developers, engineering manager, product owner / product manager
  - **Platform capabilities:** infrastructure, cloud, developer platforms
  - **Enabling expertise:** cybersecurity, reliability, specialist coaching

  Bottom message: **Borrow expertise. Keep product ownership.**

- **Source:** Skelton & Pais, *Team Topologies*; SEFOP leadership material.


## 10 OR scientists need enough software engineering to build effectively inside a software team

- **Content:**
  1. Scientists need the engineering skills closest to their daily work: version control, automated testing, CI, clean design, reproducibility, and code review.
  2. They do not need equal depth everywhere: deployment, infrastructure, and production operations can remain primarily software-developer responsibilities.
  3. The objective is **overlap, not role replacement**: enough shared knowledge for scientists and developers to build the decision product together.

- **Visual:** Three skill zones:
  - **Core for OR scientists:** version control, testing, CI, clean code, reproducibility, code review
  - **Shared working knowledge:** architecture, monitoring, deployment concepts, production behavior
  - **Developer-led expertise:** CD, infrastructure, production operations, platform integration

  Bottom message: **Shared understanding ≠ equal expertise**

- **Source:** SEFOP learning roadmap and team-role material.


## 11 SEFOP packages the practices needed to make this transition repeatable

- **Content:**
  1. SEFOP exists so OR teams do not have to rediscover these practices independently.
  2. **Train:** software-engineering education tailored to OR scientists.
  3. **Lead:** guidance for managers leading embedded OR product teams.
  4. **Deliver:** reference implementations and engineering patterns.
  5. **Go Agentic:** AI-assisted development built on top of a strong engineering foundation.
  6. Open and under construction; feedback welcome.

- **Visual:** Four tiles:
  - **TRAIN**
  - **LEAD**
  - **DELIVER**
  - **GO AGENTIC**

  Include QR code / `github.com/sefop`.

- **Source:** `github.com/sefop`.


## 12 Conclusion

- **Content:**
  1. **A recurring OR decision demands software practices:** the system has to remain testable, maintainable, adaptable, and deployable throughout its lifetime.
  2. **Software engineering is part of the OR capability:** embedded OR teams need the skills, ownership, and practices to engineer the product—not just the formulation.
  3. **AI makes this capability more important, not less:** strong engineering foundations determine whether AI accelerates sustainable delivery or technical debt.

- **Visual:** Three takeaways at the top, then the closing transformation:

  **FROM**  
  Project → Model → Handoff

  **TO**  
  Product → Team → Continuous ownership

  Footer:
  **SEFOP — a framework that can help teams make the shift.**


## References

- Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps.* IT Revolution.
- Humble, J., & Farley, D. (2010). *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation.* Addison-Wesley.
- Kersten, M. (2018). *Project to Product: How to Survive and Thrive in the Age of Digital Disruption with the Flow Framework.* IT Revolution.
- O'Brien & Eisty (2026). *Computing in Science & Engineering.* https://www.computer.org/csdl/magazine/cs/2026/01/11482007/2fJHVugY5UY
  **[fill in: authors' initials and title]**
- Ousterhout, J. (2018). *A Philosophy of Software Design.* Yaknyam Press.
- Skelton, M., & Pais, M. (2019). *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution.
- Vidoni, M., & Cunico, M. L. (2022). On technical debt in mathematical programming: An exploratory study. *Mathematical Programming Computation.*
  https://doi.org/10.1007/s12532-022-00225-1
- Winters, T., Manshreck, T., & Wright, H. (2020). *Software Engineering at Google: Lessons Learned from Programming Over Time.* O'Reilly.
- DORA (2025). *State of AI-assisted Software Development.* https://dora.dev/research/2025/dora-report/
- SEFOP: https://github.com/sefop
