# Rethinking the embedded OR team as a specialized software team

**Event:** AGIFORS Annual Symposium, 2026-10-25  
**Speaker:** Francisco Zenteno Smith  
**Length:** 20 minutes  


## Governing thought

**An OR team that owns a decision-support product has to operate as a specialized software development team.**


## 01 Rethinking the embedded OR team as a specialized software team

- **Content:**
  - AGIFORS Annual Symposium 2026
  - Title (as above)
  - Francisco Zenteno Smith, Senior Operations Research Scientist, American Airlines
  - AGIFORS Annual Symposium · October 25, 2026
  - Disclaimer: "Every comment here represents my own opinion, and does not necessarily represent an American Airlines statement"
- **Visual:** Title slide.
- **Hook:** Before that claim can mean anything: what is an OR team actually building?


## 02 Working in a project v/s building a product

- **Content:**
  1. Operations Research (OR) turns data + business needs + mathematics into a decision.
  2. A **project** delivers a one-time decision: analyze, hand off, move on.
  3. A **product** is needed when the decision is required recurrently, and someone has to own it for its whole life:
     - Plan the annual fleet composition
     - Generate the monthly crew schedules
     - Recover from irregular operations
  4. That product is a decision-support system (DSS), and its business value comes from being sustainable over the lifetime of the
     business need.

- **Visual:** Horizontal spectrum:
  - left: **Project / Consultant**
  - right: **Product / Continuous ownership**
  - bold arrow pointing right

  Supporting contrast:
  - **Project:** completion, handoff, short-term delivery
  - **Product:** outcomes, iteration, long-term ownership

- **Speaker notes:**
  - This is the premise, not the argument. State it once, here, and spend the rest of the talk on the team
    the product needs.
- **Hook:** Sustainability is a property of the software, not of the mathematics. So how good is ours?


## 03 DSS often has weak software practices surrounding the mathematics

- **Content:**
  1. **Cultural reasons:** Scientists are trained deeply in mathematics, but not in software engineering (SE). They don't know the
     benefits of SE, or they don't think it is for them.
  2. **Technical reasons:** DSS has unique challenges deriving from the mixture of applied mathematics and SE. For example:
     - How to automatically test an optimization model?
     - How to design the system to be solver-agnostic?
- **Visual:** A decision-support system diagram made of two parts, "Software components" and "Applied mathematics". Two columns,
  "Cultural reasons" and "Technical reasons", carry the points above.
- **Speaker notes:**
  - Open by naming the cracks out loud, so the room recognizes them before any claim is made:
    - The model only one person can run, and that person is on vacation.
    - The notebook that feeds a production decision every Monday, and nobody dares refactor it.
    - The result nobody can reproduce, because the input file was overwritten.
  - Those are the symptoms. The two columns are the causes.
- **Source:** Vidoni, Cunico & Vecchietti (2018, 2020); Vidoni (2021); Vidoni & Cunico (2022); Kanewala & Bieman (2014).
- **Hook:** Weak practices are common. The question nobody asks is what they cost.


## 04 Weak software practices constrain the potential business value a DSS can deliver

- **Content:**
  1. What happens to weak software?
  2. Harder to test, deploy and maintain.
  3. Short-term delivery is misleading as it hides technical debt.
  4. At some point it can't sustain progress economically: might get re-written or decommissioned.

- **Visual:** A progress-over-time chart, after Ousterhout's tactical vs. strategic programming. Vertical axis: "Total progress";
  horizontal axis: "Time". Three curves, labelled illustrative:
  - **Solid foundations:** slower at first, then a steady line that overtakes the other two.
  - **Legacy system**
  - **Short-lived system**
- **Speaker notes:**
  - Short-lived system: seems to provide significant value, but soon (maybe 1 year?) progress stalls as it can't support changes
    efficiently.
  - Legacy system: started fine; after a couple of years the initial developers left. Now it is unclear how it works, or making a
    change is very difficult. At some point it has to be re-written to continue supporting the business.
- **Source:** *A Philosophy of Software Design* (tactical vs. strategic programming). These curves are illustrative.
- **Hook:** So what kind of team keeps a DSS strong over its whole lifetime?


## 05 How to unlock the full value of the DSS? operate as a specialized software development team

- **Content:**
  1. The obvious answer is to hire developers. It is not enough.
  2. Developers alone can't solve problems that need the mathematics: how to automatically test an optimization model? how to
     design the system to be solver-agnostic?
  3. Scientists alone can't solve problems that need engineering: architecture, CI, reproducible experiments.
  4. The hard problems sit at the intersection, so the team needs specialists in both.

- **Visual:** Two overlapping circles: **Operations Research** and **Software Engineering**. The overlap holds the hard problems
  from slide 3.
  - **Software Engineering only (developers):** traditional skills to tackle problems unrelated to OR (ex: design a database).
  - **Operations Research only (scientists):** trained in some SE elements: SDLC, elicitation, agile, OOP, basics of design,
    automated testing, TDD, CI.
  - **Intersection (specialists):** build the OR-tailored engineering the scientists work inside: testing for optimization models,
    design that keeps the system solver-agnostic, architecture for a DSS.
- **Hook:** Specialists on both sides sounds like a team nobody will fund. Does it need every skill itself?


## 06 The OR team owns the product, but it does not need to hold every skill itself

- **Content:**
  1. **Own:** business interaction, formulation, testing strategy, software quality, delivery responsibility, and production
     behavior of the DSS. Nobody else can: the knowledge of the decision lives naturally in the OR scientists.
  2. **Borrow:** infrastructure, cybersecurity, cloud platforms, reliability expertise, and other specialist capabilities.

- **Visual:** Three-layer operating model:
  - **Core embedded OR product team:** OR scientists, software developers, engineering manager, product owner / product manager
  - **Platform capabilities:** infrastructure, cloud, developer platforms
  - **Enabling expertise:** cybersecurity, reliability, specialist coaching

  Bottom message: **Borrow expertise. Keep product ownership.**

  Footnote: *This slide draws the boundary around the team. The next one sets the depth each scientist needs inside it.*

- **Source:** Skelton & Pais, *Team Topologies*; SEFOP leadership material.
- **Hook:** The boundary is drawn. Inside it, how much software engineering does a scientist actually need?


## 07 OR scientists need enough software engineering to build inside a software team

- **Content:**
  1. Scientists need the engineering skills closest to their daily work: automated testing, reproducibility, clean design, and
     code review.
  2. They do not need equal depth everywhere: deployment, infrastructure, and production operations stay primarily developer-led.
  3. The objective is **overlap, not role replacement**: enough shared knowledge for scientists and developers to build the
     decision product together.

- **Visual:** Three skill zones:
  - **Core for OR scientists:** automated testing, reproducible experiments, clean code, code review, tracking changes (version
    control)
  - **Shared working knowledge:** architecture, monitoring, how deployment works, production behavior
  - **Developer-led expertise:** automated build and release pipelines (CI/CD), infrastructure, production operations, platform
    integration

  Bottom message: **Shared understanding ≠ equal expertise**

- **Source:** SEFOP learning roadmap and team-role material.
- **Hook:** That is the target. What happens to a real team that trains its scientists this way?


## 08 Case study: strengthening the engineering of a DSS improved throughput and quality

- **Content:**
  - 15-month case study · 4 OR scientists · from pilot → DSS
  - **Before:** throughput 1x; software quality: low test coverage, code smells unattended.
  - **After (15 months transformation):** throughput 2.3x (+130%); software quality: +42pp in test coverage, 2/3 reduction in code
    smells.
  - What changed: heavy training of SE to OR scientists; refactoring the system for OR needs.
  - Speed and quality moved together: this is the "solid foundations" curve from slide 4.
  - Where this team sits: four scientists, no developers yet. This is the first leg of the team from slide 5, not the destination.
- **Visual:** Before / after table (throughput and software quality).
- **Speaker notes:**
  - Say aloud what the case shows: foundations and speed are not opposed (1x → 2.3x, +42pp coverage), and training the scientists
    is enough to start moving.
  - Say aloud what it is: the first leg, walked on its own. The destination is still the team from slide 5 — developers,
    scientists trained in what they need, and specialists building the OR-tailored engineering.
  - Every team walks this leg first, whatever it decides to staff afterwards.
- **Source:** Zenteno Smith (2026), *Why software engineering practices are slow to spread among operations research practitioners
  and what changes that behavior*.
- **Hook:** Fifteen months of engineering. The obvious 2026 objection: why bother, when AI writes the code?


## 09 Can't AI-coding assistants take care of this?

- **Content:**
  1. The 2026 objection: why spend 15 months on engineering when AI writes the code? Because AI multiplies what you already have —
     and the team in slide 8 just changed what it had.
  2. **Strong engineering practices** (CI/CD, architecture, automated testing) × AI = sustainable acceleration: faster delivery +
     higher quality.
  3. **Weak engineering practices** (manual processes, unclear design, manual testing or absence) × AI = accelerated technical
     debt: more output + more risk.
  4. So the engineering foundation your team can build and maintain matters more now, not less — and that depends on who is in the
     team.
- **Visual:** Split screen with the same **AI multiplier** entering both sides. Label the strong side with slide 8's "after"
  numbers and the weak side with its "before".
- **Source:** DORA Research 2025, *State of AI-assisted Software Development* (Google Cloud, 2025).
- **Hook:** AI multiplies what you already have. So what does your team already have?


## 10 Which of the three is your team missing?

- **Content:**
  1. Slide 5 named three kinds of contributor. Ask the question about your own team:
  2. **Developers:** who builds the parts of the system that are not mathematics?
  3. **Scientists trained in the software engineering they need:** automated testing, reproducibility, clean design, code review.
  4. **Specialists at the intersection:** who builds the OR-tailored engineering the scientists work inside — testing for
     optimization models, design that keeps the system solver-agnostic?
  5. Most teams are missing one. Name which, and that is where the next hire or the next training goes.

- **Visual:** The Venn diagram from slide 5, repeated, with one checkbox per region for the audience to answer silently.

  Bottom message: **Name the one you are missing.**

- **Speaker notes:**
  - Pause here. This is the only moment in the talk that is about their team rather than about OR teams in general.
  - Most OR teams start with scientists only. That is a default, not a decision (an observation from experience, not a survey
    result).
- **Hook:** You have just named a gap. Where do you get the material to close it?


## 11 How do you build that team? SEFOP packages the practices

- **Content:**
  1. SEFOP exists so OR teams do not have to rediscover these practices independently.
  2. **Train:** software-engineering education tailored to OR scientists. Status: [confirm before 2026-10-25]
  3. **Lead:** guidance for managers leading embedded OR product teams. Status: [confirm before 2026-10-25]
  4. **Deliver:** reference implementations and engineering patterns. Status: [confirm before 2026-10-25]
  5. **Go Agentic:** AI-assisted development built on top of a strong engineering foundation. Status: [confirm before 2026-10-25]
  6. Open and under construction; feedback welcome.

- **Visual:** Four tiles:
  - **TRAIN**
  - **LEAD**
  - **DELIVER**
  - **GO AGENTIC**

  Each tile carries a status tag (available / in progress / planned), set from what exists on the day of the talk.

  Include QR code / `github.com/sefop`.

- **Source:** `github.com/sefop`.
- **Hook:** That is the offer. Here is what to remember even if you never open it.


## 12 Conclusion

- **Content:**
  1. **A recurring OR decision is a product.**
  2. **Products need engineering practices:** the system has to remain testable, maintainable, adaptable, and deployable
     throughout its lifetime.
  3. **The OR team has to own the product, and it takes three kinds of contributor:** developers, scientists trained in the
     software engineering they need, and specialists building the OR-tailored engineering the scientists work inside. Nobody else
     can own it, because the knowledge of the decision lives naturally in OR scientists.
  4. **AI makes this more important, not less:** strong engineering foundations determine whether AI accelerates sustainable
     delivery or technical debt.

- **Visual:** Four takeaways at the top, then the closing transformation:

  **FROM**  
  Project → Model → Handoff

  **TO**  
  Product → Team → Continuous ownership

  Footer:
  **SEFOP — a framework that can help teams make the shift.**
- **Hook:** — (final slide; the audience answers this one, not another slide)


## References

- Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps.* IT Revolution.
- Humble, J., & Farley, D. (2010). *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment
  Automation.* Addison-Wesley.
- Kanewala, U., & Bieman, J. M. (2014). **[fill in: title and venue]**
- Kersten, M. (2018). *Project to Product: How to Survive and Thrive in the Age of Digital Disruption with the Flow Framework.* IT
  Revolution.
- O'Brien & Eisty (2026). *Computing in Science & Engineering.*
  https://www.computer.org/csdl/magazine/cs/2026/01/11482007/2fJHVugY5UY
  **[fill in: authors' initials and title]**
- Ousterhout, J. (2018). *A Philosophy of Software Design.* Yaknyam Press.
- Skelton, M., & Pais, M. (2019). *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution.
- Vidoni, M., Cunico, M. L., & Vecchietti, A. (2018, 2020). **[fill in: titles and venues]**
- Vidoni, M. (2021). **[fill in: title and venue]**
- Vidoni, M., & Cunico, M. L. (2022). On technical debt in mathematical programming: An exploratory study. *Mathematical
  Programming Computation.*
  https://doi.org/10.1007/s12532-022-00225-1
- Winters, T., Manshreck, T., & Wright, H. (2020). *Software Engineering at Google: Lessons Learned from Programming Over Time.*
  O'Reilly.
- DORA (2025). *State of AI-assisted Software Development.* https://dora.dev/research/2025/dora-report/
- Zenteno Smith, F. (2026). *Why software engineering practices are slow to spread among operations research practitioners and
  what changes that behavior.* **[fill in: venue]**
- SEFOP: https://github.com/sefop
