# Rethinking the embedded Operations Research team: from project to product, and how to get there

**Event:** AGIFORS Annual Symposium, 2026-10-25  
**Speaker:** Francisco Zenteno  
**Length:** 20 minutes  
**Target presentation time:** ~18 minutes


---

## Governing thought

**An OR team that owns a decision-support product has to operate as a specialized software development team.**

---

## Storyline

1. **Context:** Embedded OR teams increasingly own software that makes recurring decisions.
2. **Problem:** The value of the mathematics is constrained by the engineering around it.
3. **Thesis:** The OR team therefore needs to operate as a specialized software development team.
4. **Evidence:** Software-engineering literature shows that quality and throughput are not opposing goals, and one OR team experienced the same pattern.
5. **Why specialized:** OR software inherits normal software-engineering needs and adds challenges unique to decision-support systems.
6. **How:** Build the right team, keep end-to-end product ownership, and develop the right level of software-engineering capability across roles.
7. **SEFOP:** Package these practices so OR teams do not have to work them out from scratch.
8. **Conclusion:** The organizational shift is from project delivery to continuous ownership of decision products.

---

# 01 <Repeats the title here>

- **Content:**
  - Title, name, affiliation, github.com/sefop.
- **Visual:** Title slide.
- **Source:** —


---

## 02 One-time analysis v/s decision-support system

- **Content:**
  1. Operations Research (OR) turns data + business rules + mathematics into a decision.
  2. If this decision is needed at some cadence (like annual fleet composition, monthly crew sequences, or daily crew recovery) --> then
  the OR solution becomes a software product: a decision-support system (DSS).
  3. The business value comes from building a sustainable decision-making tool.


---

## 03 DSS tend to have weak software practices surrounding model

- **Content:**
  1. **Cultural root cause:** OR scientists are not trained in software engineering, and often do not see why they should be.
  2. **Technical root cause:** a DSS has challenges that ordinary business software does not.
  3. **Evidence:** a survey of 168 modelers found code and documentation debt widespread, and mostly introduced deliberately.
- **Visual:** Two columns, "cultural" and "technical", above a callout: "168 modellers: debt widespread, mostly deliberate."
- **Source:** [SEFOP README, "Why: what goes wrong and why"](https://github.com/sefop#why-what-goes-wrong-and-why);
  [Section 01](../../book/01-introduction/README.md) (two root causes); Vidoni & Cunico (2022).


---

## 04 The value of this product is constrained by the software used to deliver it

- **Content:**
    1. What happens to software with weak foundations? 
       - Difficulty to maintain, test and/or deploy.
       - Applications eventually need to be rewritten rather than evolved, so the investment restarts instead of compounding.
- **Visual:** A progress-over-time chart, after Ousterhout's tactical vs. strategic programming. Vertical axis: progress; horizontal axis: time
  (years). Three illustrative curves, not data:
  - **Curve 1, short-lived system (about 1 year):** starts steepest, then flattens quickly as each change costs more (a logarithmic shape). When
    further progress is no longer economically viable, the system is rewritten or discarded (consequence 4).
  - **Curve 2, legacy system (a few years):** survives the short term, but stalls once the original authors leave. Changes become very
    expensive, and the curve flattens.
  - **Curve 3, strategic system:** built with proper practices from the beginning. Slower at first, because it invests in its foundations, then
    a steady line (y = x) that overtakes curves 1 and 2 and stays economically efficient for its whole life.
  - Callout where curve 3 overtakes the others: "The early speed of curves 1 and 2 was temporary."
- **Source:** [SEFOP README, "Why: what goes wrong and why"](https://github.com/sefop#why-what-goes-wrong-and-why);
  [Section 01](../../book/01-introduction/README.md) (four symptoms); Ousterhout, *A Philosophy of Software Design* (tactical vs. strategic
  programming).


---

## 05 To unlock the full value the OR team has to operate as a specialized software development team

- **Content:**
  1. Some of these special needs:
     - the SDLC of a DSS has some parts that require both SE (software engineering) and OR disciplines to interact:
     - The SDLC has typically these phases: business need -> elicitation -> user stories -> design -> development -> testing -> integration
     to dev environment -> deployment -> monitoring.
     - Some example phases that requires specialized knowledge: how to design a system like this? how to make it solver agnostic?
     how to automatically test if a MIP model is working correctly? how to prepare for potentially multiple algorithms? How should the
     CI pipeline look? how to set an experimentation infrastructure? what to monitor in production?
  2. These special needs are required from DSS because the DSS is software at the end of the day.
  3. This requires addressing both the cultural and technical challenges mentioned earlier.


---

## 06 Has it been done? yes

- **Content:**
  1. Describe the case from the DSI paper: 15-month project turning a pilot into a better system
  2. In one four-scientist team over 15 months, throughput moved from **1.0× → 2.3×** after adopting engineering practices.
  3. Software quality improved as well: unit testing coverage rose 42 pp, and code smells fell by ~2/3.
  4. This is consistent with a broader software-engineering principle: mature engineering organizations do 
  not treat throughput and quality as opposing objectives.
- Visual: TDB
- Source: cite the paper from DSI, Accelerate, Modern SOfrtwre Engineering, Google Book?


---

# 07 AI-coding assistants make this transition more urgent

1. AI-coding assistants act as an amplifier of current software engineering practices (DORA, 2025)
   - Teams with strong foundations move faster at higher quality
   - Teams with weak foundations ship more software with higher technical debt
2. AI-coding assistants are already in use: the switch is on.
3. Thus, solid engineering practices are the prerequisite to capture the value from agentic development
**Visual**: TDB, maybe split screen with the same **AI multiplier** entering both sides.

---

## 08 An embedded OR team should deliberately sit at the strong-practices end of the spectrum

- **Content:**
  1. Software practices form a spectrum:
     - **Left, no practices:** the team works like a consultant delivering a project, measured by being on time and on budget.
     Its software caps the value the model can deliver.
     - **Right, strong software engineering practices:** the team works like a "software factory" running a product, measured by the business outcomes
       it keeps producing. Its practices unlock the full value of the model.
  2. Both ends aim, in good faith, for the full value of the model, but only software prepared for it can deliver it.
  3. The position should be deliberate, and it should point right.
  4. Own what determines the product value; borrow the rest from supporting teams (ie, maybe you should not have cyberseccurity in your team, but rely on the company's)
  5. Staffing needs: engineering managers, product owners, software developers, architects, scientists
- **Visual:** A horizontal spectrum with "project / consultant" on the left and "product / software factory" on the right; a cluster of dots near the
  left; a bold arrow pointing right; "How do we get there?" underneath.


---

## 09 How to get there? SEFOP can help

- **Content:**
  1. SEFOP (Software Engineering Framework for Optimization Programs) exists so OR teams do not have to work this out from scratch.
  2. **Train:** an open book for OR scientists, with no software engineering background assumed, plus language-specific practice repositories.
  3. **Lead:** guidance for the managers who lead these teams.
  4. **Deliver:** reference implementations.
  5. **Go Agentic:** AI-assisted development.
  6. Open and under construction; feedback welcome.
- **Visual:** Four tiles with a QR code to github.com/sefop.
- **Source:** show github.com/sefop.


---

## 10 Conclusion

- **Content:**
  1. **A recurring OR decision demands software practices**: It has to remain testable, maintainable and deployable during its lifetime.
  2. **Software engineering is part of the OR capability**: Embedded OR teams need the skills, ownership, and practices to engineer the product.
  3. **AI makes this capability more important, not less**: AI can accelerate development, but strong engineering practices provide the foundation
     that makes that acceleration safe and sustainable.
  4. Bonus: SEFOP is a framework that can help you make this transition.

---


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
