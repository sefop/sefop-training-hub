# INFORMS Annual Meeting 2026: slide plan

**Length:** 15 minutes, questions after. **Slides:** 0 to 9. **Budget:** about 13:30, 1:30 spare.

Slide 0 shows only the title. Every other slide has two supporting bullets for its title, and one
bullet that leads to the next slide. The screen shows the title and the supporting bullets; the
speaker says the connection, so the next slide is never given away.

One bug threads the talk: a constraint with its sign flipped, introduced on slide 4 and caught on
slide 8. After SEFOP is introduced, slides 7 and 8 each give the audience one idea to apply to their
own decision-support system.

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

## 3. Agentic AI amplifies whatever foundations it finds (1:15)

- DORA (2025), Google's annual survey of software teams: AI's primary role is an amplifier.
- Strong foundations: faster at good quality. Weak foundations: faster, with more technical debt
  (shortcuts that make later changes costly).
- **Next:** Its potential is enormous for a team that can tell a right model from a wrong one.

## 4. Applied correctly means you can check what it writes (1:15)

- An assistant lowers the cost of writing code, not of knowing it is right: flip the sign of one
  constraint and the solver still reports "optimal".
- Asked to make a failing test pass, it may change the expected value instead of the model, so
  people own the tests.
- **Next:** Why is OR not ready to check its own code today?

## 5. Why the engineering half is the thinner half (1:30)

- Cultural: OR scientists are trained in mathematics, rarely in software engineering. Vidoni &
  Cunico (2022), surveying 168 modelers: technical debt is widespread and mostly deliberate.
- Technical: where OR meets software, questions have no obvious answer, such as how to design a
  model so it can change safely, and how to test it without knowing the optimum.
- **Next:** These questions need answers written for OR teams.

## 6. SEFOP: a software engineering framework for optimization programs (1:15)

- A free, open framework: a training curriculum on software engineering for OR, and practice
  repositories in Python and Java.
- Four capabilities: Train, Lead, Deliver, and Go Agentic (in progress, contributions welcome).
- **Next:** Two ideas from it you can apply to your own system this week.

## 7. Design idea: keep the model separate, and make its answer honest (2:00)

- Keep data, business rules, formulation and solver apart, so each one can change without touching
  the others.
- Every run says what it knows: a proven optimum, a plan that may not be the best, or no plan. Bad
  input is an error, never "infeasible".
- **Next:** Once the model states what it promises, a test can check it.

## 8. Testing idea: find one relation your model must obey (2:00)

- No optimum needed: relax a constraint (more capacity, more crew, a longer horizon) and the
  objective must not get worse; tighten one and it must not improve.
- On small instances solved to optimality, the correct model passes and slide 4's flipped sign
  fails.
- **Next:** These ideas are the foundations the amplifier needs.

## 9. The amplifier is on: make what it amplifies strong (1:15)

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
