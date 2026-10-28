# INFORMS Annual Meeting 2026: slide plan

**Length:** 15 minutes, questions after. **Slides:** 0 to 7. **Budget:** about 12:30, 2:30 spare.

Slide 0 shows only the title. Every other slide has two supporting bullets for its title, and one
bullet that leads to the next slide. The screen shows the title and the supporting bullets; the
speaker says the connection, so the next slide is never given away.

Slides 1 to 3 build the problem; slide 4 introduces SEFOP as the answer, and slides 5 and 6 each give
the audience one idea to apply to their own decision-support system.

## 0. SEFOP: software engineering for optimization in the agentic AI era (0:15)

Title only.

## 1. Recurring decisions need decision-support software (1:15)

- Operations research (OR) brings value through decisions.
- A decision required again and again (cargo load plans, crew recovery, shift schedules) needs
  software that runs for years: decision-support software (DSS).
- **Next:** That software must stay right while it changes, and that is where DSS struggles.

## 2. What goes wrong in DSS, and what it costs (1:30)

- Weak practices around the model (notebooks, no automated tests, manual deployment) make it run on
  one machine only, hard to maintain, feared to change, and rewritten instead of evolved.
- The cost: lost business value, as systems stall within a year or turn legacy, and weak foundations
  that keep agentic AI from delivering its full potential.
- **Next:** Why do the foundations decide what AI delivers?

## 3. Agentic AI amplifies whatever foundations it finds (1:30)

- DORA (2025), Google's annual survey of software teams: AI's primary role is an amplifier.
- Strong foundations: faster at good quality. Weak foundations: faster, with more technical debt
  (shortcuts that make later changes costly).
- **Next:** OR teams need those foundations, built for their kind of software.

## 4. SEFOP: a software engineering framework for optimization programs (1:30)

- A free, open framework: a training curriculum on software engineering for OR, and practice
  repositories in Python and Java.
- Four capabilities: Train, Lead, Deliver, and Go Agentic.
- **Next:** Two ideas from it you can apply to your own system this week.

## 5. Design: achieving modularization in DSS (2:30)

- Keep data, business rules, formulation and solver apart, so each one can change without touching
  the others.
- Every run says what it knows: a proven optimum, a plan that may not be the best, or no plan. Bad
  input is an error, never "infeasible".
- **Next:** Once the model states what it promises, a test can check it.

## 6. Testing: ideas for verifying DSS at scale (2:30)

- No optimum needed: relax a constraint (more capacity, more crew, a longer horizon) and the
  objective must not get worse; tighten one and it must not improve.
- It catches what a solver run hides: a constraint with a flipped sign still reports "optimal", and
  fails this test.
- **Next:** These ideas are the foundations the amplifier needs.

## 7. The amplifier is on: make what it amplifies strong (1:30)

- DORA (2025) names the practices that amplify AI's benefits (name the two or three this talk
  showed, after checking the report).
- This week: write one relation for your own model, and keep its test in human hands.
- **QR code:** github.com/sefop.

## Questions to prepare

- Is DORA evidence about OR teams? (No: it surveys software teams; the talk uses it as an analogy.)
- Where are the templates the abstract mentions?
- What about time limits and optimality gaps? (The relation holds between proven optima; with a gap,
  compare bounds: the new run's upper bound must not fall below the old run's best solution.)
- Isn't this just ordinary software engineering? (No: in OR the right output is usually unknown, so
  tests check how the output moves when the input moves.)
- How does this apply to one-off research code?
- How do you judge whether a new model is better before users see it? (Run old and new on the same
  instances, explain every difference, then run the new one alongside live operations.)
