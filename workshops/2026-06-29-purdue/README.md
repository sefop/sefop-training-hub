# Software Engineering for Optimization Practitioners
**Secquoia Lab — Purdue University**
**June 29, 2026 | 09:00–17:00**

> Anchored on David Farley's *Modern Software Engineering* and the [SEFOP framework](https://github.com/sefop).

---

## Schedule

| Time | Session |
|------|---------|
| 09:00–09:45 | Block 1: What is Software Engineering? |
| 09:45–10:00 | Break |
| 10:00–10:45 | Block 2: Optimize for Learning |
| 10:45–11:00 | Break |
| 11:00–11:45 | Block 3: Optimize for Managing Complexity |
| 11:45–12:30 | Break / transition |
| 12:30–13:30 | Lunch |
| 13:30–17:00 | Afternoon: SEFOP in practice — TDD exercise |

---

## Block 1 — What is Software Engineering? (09:00–09:45)

### 1. Welcome and framing
- a) Logistics (schedule, wifi, repo link)
- b) Who am I — presenter introduction
- c) Framing slide: *(two points — "you" and "software developer" — with an arrow pointing from you toward the software developer)* — "I can give you the bicycle, but I can't ride it for you"

### 2. The pain stories *(show of hands after each)*
- a) "It worked 6 months ago" — can't reproduce your own results before a deadline
- b) "Works on my machine" — advisor or collaborator can't run your code
- c) "I changed the solver and everything broke" — no separation between model and infrastructure
- d) **Science case:** Geoffrey Chang (Scripps Institute, 2006) — retracted 5 high-impact papers on membrane protein structures because a sign error in a data-processing script had corrupted all results for years
- e) **Industry case:** Ariane 5 rocket explosion (1996) — a reused software component caused an unhandled overflow exception; the rocket self-destructed 37 seconds after launch, destroying a $370M payload
- f) Interactive question: *"Raise your hand if any version of the first three has happened to you"*

### 3. A different type of engineering
- a) In civil or mechanical engineering, design and construction are separate phases: you design a bridge, then you build it
- b) In software, construction is essentially free — the code *is* the blueprint and the product simultaneously
- c) The bottleneck is not building, it's **discovering what to build and how**
- d) Software engineering is fundamentally a **creative discovery process** — you rarely know the full solution before you start writing it
- e) Therefore, the most important thing to optimize is **your ability to learn and adapt**: short feedback loops, cheap experiments, easy rollback
- f) Farley's definition: applying an empirical, scientific approach to finding efficient, effective solutions to practical problems

### 4. The two core challenges
- a) Learning and discovering what to build (working under uncertainty)
- b) Managing the complexity of what we build
- c) The core property we want from our software: **the ability to change quickly** — because in research, you are always learning and your code must keep up
- d) Speed of change without discipline creates chaos — keep complexity at a manageable scale so changing one thing doesn't break everything else
- e) These two challenges are in tension: the practices we'll cover today resolve that tension

### 5. Why not just use AI coding assistants?
- a) AI assistants amplify the engineering practices already present in a team — they don't replace them
- b) Good practices → AI makes you faster; bad practices → AI generates more mess, faster
- c) Link to [DORA report](https://dora.dev/): teams with strong engineering foundations benefit most from AI tools; teams without them see neutral or negative outcomes
- d) Interactive question: *"Are you using AI coding assistants today? Do you feel more productive or more confused?"*

---

## Block 2 — Optimize for Learning (10:00–10:45)

> Farley Part II: Ch. 4 (Iterative), Ch. 5 (Feedback), Ch. 6 (Incrementalism), Ch. 7 (Empiricism), Ch. 8 (Experimental)

### 1. Working iteratively and incrementally (Farley Ch. 4 + Ch. 6)
- a) Agile vs. waterfall
- b) Iteration drives learning — analogy to gradient descent: each step gives you information to take a better next step; the iteration strategy (Farley Fig. 4.3): Design → Develop → Test → Release — analogous to the scientific method: theory, prediction, experiment, observation
- c) Benefits of small incremental iterations: easier to build, test, and review; each increment is a checkpoint you can always return to; limits the blast radius of mistakes — a small change that breaks something is easy to find and fix; example: implement a greedy heuristic first, verify it works, then layer in the MIP solver *(show image describing this incremental process)*
- d) Git as an example of working iteratively and incrementally: commits as checkpoints, branches as experiments, history as a lab notebook

### 2. Empiricism and experimentation (Farley Ch. 5 + Ch. 7 + Ch. 8)
- a) **In code:** static analysis tools catch errors before you even run the program (linters, type checkers)
- b) **In automated tests:** run your assumptions against reality automatically
- c) CI/CD: how continuous integration and delivery automate the Test → Release steps so feedback is instant
- d) Reproducibility is empiricism applied to software: same inputs must always produce same outputs
- e) Virtual environments + declared dependencies = reproducible science
- f) Interactive question: *"If I gave you a fresh laptop right now, how long would it take to run your experiments?"*
- g) Test types: unit, integration, end-to-end
- h) Properties of a good test (analogous to a good scientific experiment): reproducible, fast, isolated, meaningful
- i) Git branches as a laboratory: try a new approach without destroying what works

---

## Block 3 — Optimize for Managing Complexity (11:00–11:45)

> Farley Part III: Ch. 9 (Modularity), Ch. 10 (Cohesion), Ch. 11 (Separation of Concerns), Ch. 12 (Information Hiding), Ch. 13 (Coupling)

### 1. Cohesion and coupling (Farley Ch. 10 + Ch. 13)
- a) Cohesion: things that change together should live together — a module should have one reason to change
- b) Coupling: things that don't change together should not depend on each other
- c) High cohesion + low coupling = the goal; low cohesion + high coupling = the mess most research code is in
- d) Interactive question: *"If you change how your data is loaded, how many other files do you have to touch?"*

### 2. Modularity (Farley Ch. 9)
- a) A module is a unit of software that can be understood, built, and tested independently
- b) Modularity is what makes a system changeable — you can swap a module without touching the rest
- c) Test for modularity: can you change this piece without reading all the other pieces first?
- d) Example: a solver module that can be replaced without touching data loading or reporting

### 3. Separation of concerns (Farley Ch. 11)
- a) Keep data loading, business logic, and output separate — they change for different reasons
- b) A function that loads data, solves a model, and prints results has three concerns — and three reasons to break
- c) Applied to optimization: model formulation ≠ solver call ≠ results reporting
- d) Dependency injection as the mechanism: pass dependencies in from the outside — the component declares what it needs, it doesn't decide what it gets
- e) Python example:

```python
# Without DI — solver is hardcoded
class Engine:
    def solve(self, instance):
        solver = GurobiSolver()
        return solver.solve(instance)

# With DI — solver is injected
class Engine:
    def __init__(self, solver):
        self.solver = solver

    def solve(self, instance):
        return self.solver.solve(instance)

engine = Engine(solver=GreedySolver())
engine = Engine(solver=MIPSolver())
```

- f) The Engine doesn't know or care which solver it uses — concerns are fully separated

### 4. Information hiding and abstraction (Farley Ch. 12)
- a) Hide implementation details behind a simple interface — callers shouldn't need to know how something works, only what it does
- b) Abstraction lets you change the internals without breaking the callers
- c) Example: a `solve(instance)` function that hides whether it uses Gurobi, HiGHS, or a heuristic

### 5. YAGNI — You Aren't Gonna Need It
- a) Don't build for hypothetical future requirements — build for what you need today
- b) Every unnecessary abstraction adds complexity that someone has to understand and maintain
- c) Add structure when the pain of not having it is real, not when you imagine you might need it someday
- d) Interactive question: *"Have you ever built something 'just in case' that you never used?"*

---

## Afternoon — SEFOP in Practice (13:30–17:00)

> Students clone [`sefop/sefop-python-starter`](https://github.com/sefop/sefop-python-starter) and use TDD to extend the system.

*Details to be planned — exercise options:*
- Add a new solver component
- Add a new data loading mechanism

---

## Prerequisites for Students

- Python 3.12+ installed
- Git installed
- GitHub account
- A code editor (VS Code recommended)

---

## Resources

- [SEFOP GitHub](https://github.com/sefop)
- [sefop-python-starter](https://github.com/sefop/sefop-python-starter)
- *Modern Software Engineering* — David Farley (Addison-Wesley, 2021)
- [DORA Report](https://dora.dev/)
