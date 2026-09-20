# Rethinking the embedded Operations Research team: from project to product, and how to get there

**Event:** AGIFORS Annual Symposium, 2026-10-25  
**Speaker:** Francisco Zenteno Smith  
**Length:** 20 minutes  


## Governing thought

**An OR team that owns a decision-support product has to operate as a specialized software development team.**


## 01 Rethinking the embedded Operations Research team: from project to product, and how to get there

- **Content:**
  - AGIFORS Annual Symposium 2026
  - Title (as above)
  - Francisco Zenteno Smith, Senior Operations Research Scientist, American Airlines
  - AGIFORS Annual Symposium · October 25, 2026
  - Disclaimer: "Every comment here represents my own opinion, and does not necessarily represent an American Airlines statement"
- **Visual:** Title slide.
- **Source:** —


## 02 Working in a project v/s building a product

- **Content:**
  1. Operations Research (OR) turns data + business needs + mathematics into a decision.
  2. If the decision is required recurrently:
     - Plan the annual fleet composition
     - Generate the monthly crew schedules
     - Recover from irregular operations
  3. The OR solution becomes a software product, particularly, a decision-support system (DSS).
  4. The business value comes from building a sustainable decision-making product over the lifetime of the business need.


## 03 DSS often has weak software practices surrounding the mathematics

- **Content:**
  1. **Cultural reasons:** Scientists are trained deeply in mathematics, but not in software engineering (SE). They don't know the benefits of SE, or they don't think it is for them.
  2. **Technical reasons:** DSS has unique challenges deriving from the mixture of applied mathematics and SE. For example:
     - How to automatically test an optimization model?
     - How to design the system to be solver-agnostic?
- **Visual:** A decision-support system diagram made of two parts, "Software components" and "Applied mathematics". Two columns, "Cultural reasons" and "Technical reasons", carry the points above.
- **Source:** Vidoni, Cunico & Vecchietti (2018, 2020); Vidoni (2021); Vidoni & Cunico (2022); Kanewala & Bieman (2014).


## 04 Weak software practices constraints the potential business value a DSS can deliver

- **Content:**
  1. What happens to weak software?
  2. Harder to test, deploy and maintain.
  3. Short-term delivery is misleading as it hides technical debt.
  4. At some point it can't sustain progress economically: might get re-written or decommissioned.

- **Visual:** A progress-over-time chart, after Ousterhout's tactical vs. strategic programming. Vertical axis: "Total progress"; horizontal axis: "Time". Three curves, labelled illustrative:
  - **Solid foundations:** slower at first, then a steady line that overtakes the other two.
  - **Legacy system**
  - **Short-lived system**
- **Speaker notes:**
  - Short-lived system: seems to provide significant value, but soon (maybe 1 year?) progress stalls as it can't support changes efficiently.
  - Legacy system: started fine; after a couple of years the initial developers left. Now it is unclear how it works, or making a change is very difficult. At some point it has to be re-written to continue supporting the business.
- **Source:** *A Philosophy of Software Design* (tactical vs. strategic programming). These curves are illustrative.


## 05 How to unlock the full value of the DSS? operate as a specialized software development team

- **Content:**
  1. **Software engineering (developers):** developers with traditional skills to tackle problems unrelated to OR (ex: design a database).
  2. **Operations research (scientists):** scientists trained in some SE elements: SDLC, elicitation, agile, OOP, basics of design, automated testing, TDD, CI.
  3. **Intersection (specialists):** specialists in SE and OR to solve hard problems at the intersection: architecture, design, automated testing.

- **Visual:** Two overlapping circles: **Operations Research** and **Software Engineering**, with the three roles above attached to the left circle, the right circle, and the overlap.


## 06 Case of study: strengthening the engineering of a DSS improved throughput and quality

- **Content:**
  - 15-month case study · 4 OR scientists · from pilot → DSS
  - **Before:** throughput 1x; software quality: low test coverage, code smells unattended.
  - **After (15 months transformation):** throughput 2.3x (+130%); software quality: +42pp in test coverage, 2/3 reduction in code smells.
  - What changed: heavy training of SE to OR scientists; refactoring the system for OR needs.
- **Visual:** Before / after table (throughput and software quality).
- **Source:** Zenteno Smith (2026), *Why software engineering practices are slow to spread among operations research practitioners and what changes that behavior*.


## 07 AI-coding assistants make this transition more urgent: they amplify existing practices

- **Content:**
  1. AI-coding assistants act as an amplifier of current software engineering practices.
  2. **Strong engineering practices** (CI/CD, architecture, automated testing) × AI = sustainable acceleration: faster delivery + higher quality.
  3. **Weak engineering practices** (manual processes, unclear design, manual testing or absence) × AI = accelerated technical debt: more output + more risk.
- **Visual:** Split screen with the same **AI multiplier** entering both sides.
- **Source:** DORA Research 2025, *State of AI-assisted Software Development* (Google Cloud, 2025).


## 08 Product ownership as a deliberate choice

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


## 09 The OR team owns the product, but it does not need all the skills needed in the team

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


## 10 OR scientists need some SE skills and specialized infrastructure to be effective developers

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


## 11 How to get there? SEFOP packages the training materials to make this transition

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
- Kanewala, U., & Bieman, J. M. (2014). **[fill in: title and venue]**
- Kersten, M. (2018). *Project to Product: How to Survive and Thrive in the Age of Digital Disruption with the Flow Framework.* IT Revolution.
- O'Brien & Eisty (2026). *Computing in Science & Engineering.* https://www.computer.org/csdl/magazine/cs/2026/01/11482007/2fJHVugY5UY
  **[fill in: authors' initials and title]**
- Ousterhout, J. (2018). *A Philosophy of Software Design.* Yaknyam Press.
- Skelton, M., & Pais, M. (2019). *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution.
- Vidoni, M., Cunico, M. L., & Vecchietti, A. (2018, 2020). **[fill in: titles and venues]**
- Vidoni, M. (2021). **[fill in: title and venue]**
- Vidoni, M., & Cunico, M. L. (2022). On technical debt in mathematical programming: An exploratory study. *Mathematical Programming Computation.*
  https://doi.org/10.1007/s12532-022-00225-1
- Winters, T., Manshreck, T., & Wright, H. (2020). *Software Engineering at Google: Lessons Learned from Programming Over Time.* O'Reilly.
- DORA (2025). *State of AI-assisted Software Development.* https://dora.dev/research/2025/dora-report/
- Zenteno Smith, F. (2026). *Why software engineering practices are slow to spread among operations research practitioners and what changes that behavior.* **[fill in: venue]**
- SEFOP: https://github.com/sefop
