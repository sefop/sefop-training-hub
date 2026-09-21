# Rethinking the embedded OR team as a specialized software team

**Event:** AGIFORS Annual Symposium, 2026-10-25  
**Speaker:** Francisco Zenteno Smith  
**Length:** 20 minutes  
**Deck:** `agifors-sefop.pptx` (11 slides) — this file records what the deck currently says.


## Governing thought

**An OR team that owns a decision-support product has to operate as a specialized software development team.**


## 01 Rethinking the embedded OR team as a specialized software team

- **Content:**
  - AGIFORS Annual Symposium 2026
  - Title (as above)
  - Francisco Zenteno Smith, Senior Operations Research Scientist, American Airlines
  - Disclaimer: "Every comment here represents my own opinion, and does not represent an American Airlines statement"
- **Visual:** Title slide.
- **Speaker notes:**
  - Hook: what is an OR team building?


## 02 Working in a project v/s building a product

- **Content:**
  1. Operations Research (OR) turns data + business needs + mathematics → decision.
  2. A **project** delivers a one-time decision.
  3. A **product** delivers a recurring decision (and someone must own it).
  4. Examples:
     - Plan the annual fleet composition
     - Generate the monthly crew schedules
     - Recover from irregular operations
  5. These products are also known as **decision-support systems (DSS)**.
  6. Its business value comes from being sustainable over the lifetime of the business need.

- **Visual:** Three statements across the top. Below them an **Examples:** label and three icon + text rows, one per
  example. A bracket to the right of the examples points to the callout **"These products are also known as
  decision-support systems (DSS)"**. Full-width closing line at the bottom: *its business value comes from being
  sustainable over the lifetime of the business need.*
- **Speaker notes:**
  - Hook: sustainability is a software property, how good is it in DSS?


## 03 DSS often has weak software practices surrounding the applied mathematics

- **Content:**
  1. **Cultural reasons:** Scientists are trained deeply in mathematics, but not in software engineering (SE). They
     don't know the benefits of SE, or they don't think it is for them.
  2. **Technical reasons:** DSS has unique challenges deriving from the mixture of applied mathematics and SE:
     - How to automatically test an optimization model?
     - How to design the system to be solver-agnostic?
     - How to set an experimentation platform?
- **Visual:** Left: a **decision-support system** diagram, a single box whose contents are split into two labelled
  parts — **Software components** (square marker) and **Applied mathematics** (circle marker). Right: two stacked
  blocks, **Cultural reasons** and **Technical reasons**, with the three technical questions listed underneath.
- **Speaker notes:**
  - Some cracks: using Jupyter notebooks; lack of automatic tests.
  - Hook: what is the price we pay because of these weak practices?
- **Source:** Vidoni, Cunico & Vecchietti (2018, 2020); Vidoni (2021); Vidoni & Cunico (2022); Kanewala & Bieman (2014).


## 04 Weak software practices constrain the potential business value a DSS can deliver

- **Content:**
  1. What happens to weak software?
  2. Harder to test, deploy and maintain.
  3. Short-term delivery includes significant technical debt.
  4. At some point becomes unsustainable: rewrite or decommission.

- **Visual:** A progress-over-time chart, after Ousterhout's tactical vs. strategic programming. Vertical axis:
  "Total progress"; horizontal axis: "Time". Three labelled curves:
  - **Solid foundations**
  - **Legacy system**
  - **Short-lived system**
- **Speaker notes:**
  - Short-lived system: soon (maybe 1 year?) progress stalls as it can't support changes efficiently.
  - Legacy system: started fine; after a couple of years the initial developers left. Now it is unclear how it works,
    or making a change is very difficult.
  - Hook: so how to strengthen the weak practices?
- **Source:** *A Philosophy of Software Design* (John Ousterhout). These curves are illustrative.


## 05 Operate as a specialized software development team to unlock the full value of a DSS

- **Content:** Three kinds of contributor, placed against the two disciplines:
  1. **Developers** — to tackle problems unrelated to OR: design a database, data, deployments.
  2. **OR Engineers** — to set scientific development needs: optimization model testing, solver-agnostic design,
     experimentation suite, among others.
  3. **Scientists** — trained in some SE elements: SDLC, elicitation, agile, OOP, basics of design, automated testing,
     TDD, CI.

- **Visual:** Two overlapping circles stacked vertically on the left — **Software Engineering** on top, **Operations
  Research** below. Three leader lines run from the diagram to the three labels on the right: *Developers* from the
  Software Engineering circle, *OR Engineers* from the overlap, *Scientists* from the Operations Research circle.
- **Speaker notes:**
  - The obvious fix? To hire developers — but that does not work.
  - OR should not know everything about SE, just what it needs.
  - OR engineers help scientists develop properly.
  - Hook: then my science team will grow 10x? What is the actual scope I need?


## 06 The OR team owns the product, but it does not need to hold every skill itself

- **Content:**
  1. **OWN:** business interaction, product behavior, software quality, CI/CD.
  2. **BORROW:** cybersecurity, infrastructure, reliability expertise, UI/UX.
  3. Bottom message: **Borrow expertise from your organization. Keep product ownership.**

- **Visual:** Two rounded cards side by side, each with a header (**OWN**, **BORROW**) above a rule and four items
  beneath. A full-width rounded banner at the bottom carries the closing message.
- **Speaker notes:**
  - Hook: OK, what happens now when we train scientists in software engineering?


## 07 Case study: strengthening the engineering of a DSS improved throughput and quality

- **Content:**
  - 15-month case study · 4 OR scientists · from pilot → DSS
  - **Before:** throughput 1x; software quality: low test coverage, code smells unattended.
  - **After (15 months transformation):** throughput 2.3x (+130%); software quality: +42pp in test coverage, 2/3
    reduction in code smells.
  - What changed: heavy training of SE to OR scientists; refactoring the system for OR needs.
- **Visual:** Before / after comparison across two rows (throughput and software quality), with a ✕ on the before
  column and a ✓ on the after column, and a **15 months transformation** label between them. The two "what changed"
  items sit underneath.
- **Speaker notes:**
  - Every team walks this leg first, whatever it decides to staff afterwards.
  - Hook: 15 months of engineering. Why bother, when AI writes the code?
- **Source:** Zenteno Smith (2026), *Why software engineering practices are slow to spread among operations research
  practitioners and what changes that behavior*.


## 08 AI-coding assistants require the engineering investment urgently: they amplify your practices

- **Content:**
  1. **Strong engineering practices** (automated testing, CI/CD, architecture) × AI = **↗ Sustainable acceleration** —
     faster delivery + higher quality.
  2. **Weak engineering practices** (manual testing or absence, manual processes, unclear design) × AI =
     **↘ Accelerated technical debt** — more output + more risk.
- **Visual:** Two stacked cards on the left, **Strong engineering practices** and **Weak engineering practices**, each
  holding three icon + label items. The same **AI** chip enters both rows through a `×`, and an `=` leads to a result
  card on the right: *↗ Sustainable acceleration* above, *↘ Accelerated technical debt* below, each with its one-line
  consequence.
- **Speaker notes:**
  - Hook: AI multiplies what you already have. So what does your team already have?
- **Source:** DORA Research 2025, *State of AI-assisted Software Development* (Google Cloud, 2025).


## 09 A reflection: what could you improve in your team structure and practices?

- **Content:** The three contributors from slide 05, restated as a question about the audience's own team:
  1. **Developers** — to tackle problems unrelated to OR: design a database, data, deployments.
  2. **OR Engineers** — to set scientific development needs: optimization model testing, solver-agnostic design,
     experimentation suite, among others.
  3. **Scientists** — trained in some SE elements: SDLC, elicitation, agile, OOP, basics of design, automated testing,
     TDD, CI.

- **Visual:** The slide 05 diagram repeated unchanged, under the reflection title.
- **Speaker notes:**
  - Pause here. This is the only moment in the talk that is about their team rather than about OR teams in general.
  - Hook: if you identified a gap in OR Engineers or scientists' training… how do you close that gap?


## 10 How do you build that team? SEFOP packages practices and training materials

- **Content:**
  1. **S**oftware **E**ngineering **F**ramework for **O**ptimization **P**rograms — open-source.
  2. Four tiles: **Train**, **Lead**, **Deliver**, **Go agentic**.
  3. `github.com/sefop`

- **Visual:** The SEFOP expansion line under the title, then a 2×2 grid of icon tiles (Train, Lead / Deliver, Go
  agentic) on the left. A large QR code fills the right half, with `github.com/sefop` underneath it.
- **Speaker notes:**
  - SEFOP exists so OR teams do not have to rediscover these practices independently.
- **Source:** `github.com/sefop`.


## 11 Conclusions

- **Content:**
  1. A recurring decision is a product. Product is software.
  2. Software needs proper engineering practices to unlock its full business value.
  3. The OR team has to own the lifecycle of the product, with its specific software & scientific needs.
  4. AI-coding assistants need proper engineering first to unlock full potential.

- **Visual:** Four numbered circles down the left, each with its statement on the right.
- **Speaker notes:** — (final slide; the audience answers this one, not another slide)


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
