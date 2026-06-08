# Operations Research meets Software Engineering
**Secquoia Lab — Purdue University**
**June 29, 2026 | 09:00–17:00**

> Anchored on David Farley's *Modern Software Engineering* and the [SEFOP framework](https://github.com/sefop).

---

## Slide Index

| Slide | Content |
|-------|---------|
| 1 | Title — workshop title, presenter, QR code |
| 2 | About me |
| 3 | Schedule |
| 4 | Block 1 divider |
| 5 | Software Engineering rules and principles apply whether you know them or not |
| 6 | Software Engineering takes time to learn |
| 7 | Pre-workshop survey results |
| 8 | A different type of engineering |
| 9 | The two core challenges |
| 10 | Why not just use AI coding assistants? |
| 11 | Block 2 divider |
| 12 | Working iteratively and incrementally |
| 13 | Empiricism and experimentation |
| 14 | Block 3 divider |
| 15 | Cohesion and coupling |
| 16 | Modularity |
| 17 | Separation of concerns |
| 18 | Information hiding and abstraction |
| 19 | YAGNI |
| 20 | Afternoon divider |
| 21 | Thank you |

---

## `Slide 1` — Title

Francisco Zenteno Smith | Senior Operations Research Scientist — American Airlines
QR code → github.com/sefop

---

## `Slide 2` — About me

**Education**
- B.Sc. Industrial Engineering — Pontificia Universidad Católica de Chile
- M.Sc. Operations Research — Pontificia Universidad Católica de Chile
- M.Sc. Computer Science — University of California San Diego

**Experience**
- 10 years in applied Operations Research
- Senior Operations Research Scientist — American Airlines (DFW)

---

## `Slide 3` — Schedule

| Time | Session |
|------|---------|
| 09:00–09:45 | Block 1: Why learn Software Engineering? |
| 09:45–10:00 | Break |
| 10:00–10:45 | Block 2: Optimize for Learning |
| 10:45–11:00 | Break |
| 11:00–11:45 | Block 3: Optimize for Managing Complexity |
| 11:45–12:30 | Break / transition |
| 12:30–13:30 | Lunch |
| 13:30–17:00 | Afternoon: SEFOP in practice — TDD exercise |

---

## `Slide 4` — Block 1 divider: Why learn Software Engineering? (09:00–09:45)

---

### `Slide 5` — Software Engineering rules and principles apply whether you know them or not

**Some pain stories**

- a) "It worked 6 months ago" — can't reproduce your own results before a deadline
- b) "Works on my machine" — advisor or collaborator can't run your code
- c) "I changed the solver and everything broke" — no separation between model and infrastructure
- d) **Science case:** Geoffrey Chang (Scripps Institute, 2006) — retracted 5 high-impact papers on membrane protein structures because a sign error in a data-processing script had corrupted all results for years
- e) **Industry case:** Ariane 5 rocket explosion (1996) — a reused software component caused an unhandled overflow exception; the rocket self-destructed 37 seconds after launch, destroying a $370M payload
- f) Interactive question: *"Has any version of the first three happened to you?"*

### `Slide 6` — Software Engineering takes time to learn

- a) **Visual layout:** two labeled dots — "You today" at bottom left, "Software Engineer" at top right — with a small arrow pointing from "You today" toward "Software Engineer"
- b) A bicycle image centered or near the arrow
- c) Callout box: *"I can provide you the bicycle, but I can't ride it for you"*
- d) The bicycle will be a set of principles that apply in software engineering, and a repository where you can see a guided direction on how to learn these at your own pace.

### `Slide 7` — Pre-workshop survey results

**Left half — Experience ratings (1 = none, 5 = expert)**

| Practice | Avg. score |
|----------|-----------|
| Version control through Git | 2.9 |
| Object-Oriented Programming | 3.3 |
| Automated testing (e.g. unit tests) | 2.3 |
| Software design and modularity | 2.6 |
| CI/CD (e.g. GitHub Actions) | 2.1 |

**Right half — "What do you hope to learn from this workshop?"**

- "Best practices"
- "Best industrial practices"
- "How to coordinate between different parts of a repo and how to do proper docstring commenting"
- "How advanced techniques (e.g. large-scale optimization, advanced control) get integrated into modern enterprises"
- "SWE and Git best practices"

### `Slide 8` — Software Engineering: a different type of engineering

- a) In civil engineering, design and construction are separate phases: you design a bridge, then you build it
- b) In software, construction is essentially free — the code *is* the blueprint and the product simultaneously
- c) Key difference: SE lives in a world of imperfect information: the users don't know clearly what they need, don't know clearly how to specify it, building the software reveals unknown challenges, the users change their mind. In summary: SE is a **creative discovery process** — you rarely know the full solution before you start writing it
- e) Therefore, the most important thing to optimize is **your ability to learn and adapt quickly**:

### `Slide 9` — The Two Core Challenges

**Two-column layout:**

| Optimize for Learning *(→ Block 2)* | Optimize for Managing Complexity *(→ Block 3)* |
|-------------------------------------|------------------------------------------------|
| Short feedback loops | Keep code complexity low |
| Cheap experiments with the scientific method | Safety mechanisms to verify changes |
| Know quickly when something breaks | One change shouldn't break everything else |

### `Slide 10` — Why not just use AI coding assistants?

- a) AI assistants amplify the engineering practices already present in a team — they don't replace them
- b) Good practices → AI makes you faster; bad practices → AI generates more mess, faster
- c) Link to [DORA report](https://dora.dev/): teams with strong engineering foundations benefit most from AI tools; teams without them see neutral or negative outcomes
- d) Interactive question: *"Are you using AI coding assistants? Do you feel more productive or more confused?"*

---

## `Slide 11` — Block 2 divider: Optimize for Learning (10:00–10:45)

> Farley Part II: Ch. 4 (Iterative), Ch. 5 (Feedback), Ch. 6 (Incrementalism), Ch. 7 (Empiricism), Ch. 8 (Experimental)

### `Slide 12` — Working iteratively and incrementally (Farley Ch. 4 + Ch. 6)

- a) Agile vs. waterfall
- b) Iteration drives learning — analogy to gradient descent: each step gives you information to take a better next step; the iteration strategy (Farley Fig. 4.3): Design → Develop → Test → Release — analogous to the scientific method: theory, prediction, experiment, observation
- c) Benefits of small incremental iterations: easier to build, test, and review; each increment is a checkpoint you can always return to; limits the blast radius of mistakes — a small change that breaks something is easy to find and fix; example: implement a greedy heuristic first, verify it works, then layer in the MIP solver *(show image describing this incremental process)*
- d) Git as an example of working iteratively and incrementally: commits as checkpoints, branches as experiments, history as a lab notebook

### `Slide 13` — Empiricism and experimentation (Farley Ch. 5 + Ch. 7 + Ch. 8)

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

## `Slide 14` — Block 3 divider: Optimize for Managing Complexity (11:00–11:45)

> Farley Part III: Ch. 9 (Modularity), Ch. 10 (Cohesion), Ch. 11 (Separation of Concerns), Ch. 12 (Information Hiding), Ch. 13 (Coupling)

### `Slide 15` — Cohesion and coupling (Farley Ch. 10 + Ch. 13)

- a) Cohesion: things that change together should live together — a module should have one reason to change
- b) Coupling: things that don't change together should not depend on each other
- c) High cohesion + low coupling = the goal; low cohesion + high coupling = the mess most research code is in
- d) Interactive question: *"If you change how your data is loaded, how many other files do you have to touch?"*

### `Slide 16` — Modularity (Farley Ch. 9)

- a) A module is a unit of software that can be understood, built, and tested independently
- b) Modularity is what makes a system changeable — you can swap a module without touching the rest
- c) Test for modularity: can you change this piece without reading all the other pieces first?
- d) Example: a solver module that can be replaced without touching data loading or reporting

### `Slide 17` — Separation of concerns (Farley Ch. 11)

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

### `Slide 18` — Information hiding and abstraction (Farley Ch. 12)

- a) Hide implementation details behind a simple interface — callers shouldn't need to know how something works, only what it does
- b) Abstraction lets you change the internals without breaking the callers
- c) Example: a `solve(instance)` function that hides whether it uses Gurobi, HiGHS, or a heuristic

### `Slide 19` — YAGNI — You Aren't Gonna Need It

- a) Don't build for hypothetical future requirements — build for what you need today
- b) Every unnecessary abstraction adds complexity that someone has to understand and maintain
- c) Add structure when the pain of not having it is real, not when you imagine you might need it someday
- d) Interactive question: *"Have you ever built something 'just in case' that you never used?"*

---

## `Slide 20` — Afternoon divider: SEFOP in Practice (13:30–17:00)

> Students clone [`sefop/sefop-python-starter`](https://github.com/sefop/sefop-python-starter) and use TDD to extend the system.

*Details to be planned — exercise options:*
- Add a new solver component
- Add a new data loading mechanism

## `Slide 21` — Thank you

QR code → github.com/sefop

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
