# Operations Research meets Software Engineering
**Secquoia Lab — Purdue University**
**June 29, 2026 | 09:00–17:00**

> Anchored on David Farley's *Modern Software Engineering* and the [SEFOP framework](https://github.com/sefop).

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
| 09:00–09:50 | Block 1: Why learn Software Engineering? |
| 09:50–10:00 | Break |
| 10:00–10:50 | Block 2: Optimize for Learning |
| 10:50–11:00 | Break |
| 11:00–11:50 | Block 3: Unit Testing in Practice |
| 11:50–12:00 | Break |
| 12:00–13:00 | Lunch |
| 13:00–13:50 | Block 4: Optimize for Managing Complexity |
| 13:50–14:00 | Break |
| 14:00–17:00 | Putting it all together: SEFOP |

---

## `Slide 4` — Block 1 divider: Why learn Software Engineering?

---

### `Slide 5` — Software Engineering rules and principles apply whether you know them or not

**Some pain stories**

- a) **Academy case:** Geoffrey Chang (Scripps Institute, 2006) — retracted 5 high-impact papers on membrane protein structures because a sign error in a data-processing 
  script had corrupted all results for years
- b) **Industry case:** Ariane 5 rocket explosion (1996) — a reused software component caused an unhandled overflow exception; the rocket self-destructed 37 seconds 
  after launch, destroying a $370M payload
- On top of the economic impact, the psychological impact can result in stress, burnout, depression, leaving your job.
- Interactive question: *"Has any version of these first three happened to you?"*

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

- a) In civil engineering, design and construction are separate phases: you design a bridge, then you build it. It's very expensive to change the design in the middle of the construction.
- b) In software, construction is essentially free — the code *is* the blueprint and the product simultaneously
- c) Key difference: SE lives in a world of imperfect information: the users don't know clearly what they need, don't know clearly how to specify it, building the software reveals unknown challenges, the users change their mind. In summary: SE is a **creative discovery process** — you rarely know the full solution before you start writing it
- e) Therefore, the most important thing to optimize is **your ability to learn and adapt quickly**:

### `Slide 9` — The Two Core Challenges

**Two-column layout:**

| Optimize for Learning *(→ Block 2)* | Optimize for Adapting *(→ Block 3)* |
|-------------------------------------|------------------------------------------------|
| Short feedback loops | Keep code complexity low |
| Cheap experiments with the scientific method | Safety mechanisms to verify changes |
| Know quickly when something breaks | One change shouldn't break everything else |

### `Slide 10` — Why not just use AI coding assistants?

- a) Interactive question: *"Are you using AI coding assistants? What are your thoughts?
- b) AI assistants amplify the engineering practices already present in a team — they don't replace them
- c) Good practices → AI makes you faster; bad practices → AI generates more mess, faster
- d) Link to [DORA report](https://dora.dev/): teams with strong engineering foundations benefit most from AI tools; teams without them see neutral or negative outcomes


---

## `Slide 11` — Block 2 divider: Optimize for Learning

> Farley Part II: Ch. 4 (Iterative), Ch. 5 (Feedback), Ch. 6 (Incrementalism), Ch. 7 (Empiricism), Ch. 8 (Experimental)

### `Slide 12` — Working iteratively and incrementally (Farley Ch. 4 + Ch. 6)

- a) **The old way — Waterfall:** Plan everything → Build everything → Release once. Problem: you only discover what's wrong at the very end
- b) **Agile = Iterative + Incremental**
  - *Iterative:* "Don't try to get it all right from the beginning"
  - *Incremental:* "Don't build it all at once"
  - Link to the Agile Manifesto so the students can read it later.
- c) Image: Jeff Patton's Mona Lisa — ![Iterative vs Incremental](https://cms.gladwellacademy.com/storage/media/JeffPatton_Incremental-Iterative_MonaLisa.jpg)
- d) Each small unit of work follows this cycle: **Design → Develop → Test → Release → Learn**

### `Slide 13` — Working experimentally — applying the scientific method (Farley Ch. 5 + Ch. 7 + Ch. 8)

**Left half — The scientific method:**

```
Observation
    ↓
Question
    ↓
Hypothesis
    ↓
Set controlled experiment
    ↓
Test
    ↓
Conclusion    
```

**Right half — Principles:**

- **Skepticism** — don't trust; demand evidence. Assume it does not work until proven.
- **Evidence over authority** — it doesn't matter who wrote the code; only what the tests say.
- **Relevance** — the question must be worth asking; prove the experiment matters before running it.
- **Testability** — the hypothesis must be objective and measurable.
- **Reproducibility** — the experiment must produce the same results every time.
- **Causality** — the experiment variables must be controlled to show causality.

### `Slide 14` — Spot the principle (interactive exercise)

*"Which principle of the scientific method does each practice embody?"*

- a) **Branches + automated tests + PR** — You create a branch to isolate your change, run automated tests as your experiment checks, and open a PR as your conclusion. Only your change can affect the results.
  → *Causality + Testability*

- b) **`requirements.txt` + virtual environment** — You pin every dependency so the code runs identically on your machine, your colleague's machine, and CI.
  → *Reproducibility*

- c) **"My advisor wrote this function, it must be correct — no need to test it."**
  → *Evidence over authority (violated)*

- d) **`assert solution.is_feasible()` in a test** — You state your hypothesis in code: the solution must pass a concrete, measurable check.
  → *Testability*

- e) **"My heuristic seems faster than the MIP."** — No benchmark, no measurement, no comparison on the same instances.
  → *Testability (violated) — "seems" is not measurable*

- f) **You benchmark Gurobi vs. HiGHS but change the instance data at the same time.**
  → *Causality (violated) — you can't attribute any difference to the solver*

### `Slide 15` — Technologies that support experimentation

- a) **Static analysis** (linters, type checkers) — catch errors before you even run the program; *Skepticism* in automated form
- b) **Automated tests** (pytest) — run your assumptions against reality; a good test is reproducible, fast, isolated, and meaningful
- c) **CI/CD** (GitHub Actions) — automates the Test → Conclusion cycle so feedback is instant
- d) **Virtual environments + declared dependencies** — the engineering mechanism for *Reproducibility*; same inputs must always produce same outputs
- e) **Git branches** — an isolated laboratory; the PR is your conclusion; *Causality* made structural

---

## `Slide 16` — Block 3 divider: Unit Testing in Practice

### `Slide 17` — Unit Testing in Practice

[github.com/sefop/training-testing-python](https://github.com/sefop/training-testing-python)

---

## `Slide 18` — Block 4 divider: Optimize for Managing Complexity

> Farley Part III: Ch. 9 (Modularity), Ch. 10 (Cohesion), Ch. 11 (Separation of Concerns), Ch. 12 (Information Hiding), Ch. 13 (Coupling)

### `Slide 19` — Cohesion and coupling (Farley Ch. 10 + Ch. 13)

- a) Cohesion: things that change together should live together — a module should have one reason to change
- b) Coupling: things that don't change together should not depend on each other
- c) High cohesion + low coupling = the goal; low cohesion + high coupling = the mess most research code is in
- d) Interactive question: *"If you change how your data is loaded, how many other files do you have to touch?"*

### `Slide 20` — Modularity (Farley Ch. 9)

- a) A module is a unit of software that can be understood, built, and tested independently
- b) Modularity is what makes a system changeable — you can swap a module without touching the rest
- c) Test for modularity: can you change this piece without reading all the other pieces first?
- d) Example: a solver module that can be replaced without touching data loading or reporting

### `Slide 21` — Separation of concerns (Farley Ch. 11)

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

### `Slide 22` — Information hiding and abstraction (Farley Ch. 12)

- a) Hide implementation details behind a simple interface — callers shouldn't need to know how something works, only what it does
- b) Abstraction lets you change the internals without breaking the callers
- c) Example: a `solve(instance)` function that hides whether it uses Gurobi, HiGHS, or a heuristic

### `Slide 23` — YAGNI — You Aren't Gonna Need It

- a) Don't build for hypothetical future requirements — build for what you need today
- b) Every unnecessary abstraction adds complexity that someone has to understand and maintain
- c) Add structure when the pain of not having it is real, not when you imagine you might need it someday
- d) Interactive question: *"Have you ever built something 'just in case' that you never used?"*

---

## `Slide 24` — Putting it all together: SEFOP

> Students clone [`sefop/sefop-python-starter`](https://github.com/sefop/sefop-python-starter) and use TDD to extend the system.

*Details to be planned — exercise options:*
- Add a new solver component
- Add a new data loading mechanism

## `Slide 25` — Thank you

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
