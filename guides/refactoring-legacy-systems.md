# Refactoring a Legacy Decision-Support System [In Construction]

## What is a legacy system?

A legacy system is any piece of software that is difficult to change safely — not because it is old, but because it lacks the safety mechanisms that make change possible. The clearest signal: **no automated tests**. Without tests, you cannot know whether a change broke something until it breaks in production. This guide will help you build those mechanisms and use them to modernize a system incrementally.

---

## For managers — understanding the process

Refactoring a legacy system is not a single project with a fixed end date. It is a staged process of adding safety, then improving structure, then extending capability. Each phase delivers value independently — you do not need to complete all four before the system improves.

### The four phases

| Phase | Goal | Outcome |
|-------|------|---------|
| 1. Assess | Understand what the system does and where the risk is | A written map of inputs, outputs, and high-risk areas |
| 2. Protect | Add a safety net before touching anything | Automated tests that lock current behavior |
| 3. Restructure | Improve structure without changing behavior | Cleaner, more modular code; tests still pass |
| 4. Extend | Add new capability on the improved foundation | New features built with confidence |

### What "done" looks like at each phase

- **Assess:** The team can explain, in plain language, what the system does and which parts are most likely to break when changed.
- **Protect:** Running the test suite takes less than a few minutes and confirms the system still behaves as it did before any change.
- **Restructure:** A developer unfamiliar with the system can locate the relevant code for a given behavior in under 10 minutes.
- **Extend:** New features are built alongside new tests, and the test suite grows with the system.

### Signals that the team is stuck

- **Stuck in Assess:** The system has no clear owner and no one can describe its full behavior. Escalate to find the person who built it or who uses it most.
- **Stuck in Protect:** Tests are hard to write because the code is tightly tangled. This is normal — see Phase 3 for targeted untangling techniques.
- **Stuck in Restructure:** Changes keep breaking tests. This usually means behavior was accidentally changed rather than just structure. Roll back and retry in smaller steps.
- **Stuck in Extend:** The new capability requires touching too many parts of the system at once. Return to Phase 3 and extract the relevant module before extending it.

---

## For scientists — step-by-step playbook

### Phase 1: Assess

**Goal:** Build a shared understanding of what the system does before touching a single line of code.

1. **Identify the entry points.** Where does the system start? What triggers it — a script call, a scheduled job, a user action?
2. **Map inputs and outputs.** What data goes in? What comes out? Where does each live (files, databases, APIs)?
3. **Find the high-risk areas.** Which parts of the code are changed most often? Which parts does everything else depend on? These are your highest priority to protect.
4. **Document current behavior informally.** Write down (even in plain text) what the system is supposed to do. You do not need formal specs — just enough to know what "correct" looks like.

> You are done with Phase 1 when you can hand the above to a colleague and they can understand the system without running it.

---

### Phase 2: Protect

**Goal:** Add a safety net — a set of automated tests that capture what the system does today, right or wrong — before changing anything.

1. **Write characterization tests.** A characterization test calls the system with real or representative inputs and records the output. It does not assert what the output *should* be — it asserts what it *is*. This locks current behavior so you know immediately if a change breaks something.
2. **Do not fix bugs yet.** If the system produces wrong output, record that wrong output as the expected result for now. Fixing bugs before you have a safety net is how regressions happen.
3. **Start with the highest-risk areas** identified in Phase 1. You do not need 100% coverage — you need coverage of the parts most likely to break.
4. **Set up a basic automated run.** Configure a CI tool (e.g. GitHub Actions) to run your tests automatically on every change. If you do not have CI, a simple script that runs the tests locally is enough to start.

> You are done with Phase 2 when you can make a change, run the tests, and know within minutes whether you broke something.

---

### Phase 3: Restructure

**Goal:** Improve the structure of the code without changing its behavior. Tests from Phase 2 are your safety net — if they break, you changed behavior, not just structure.

1. **Extract functions.** If a block of code does more than one thing, split it. Each function should do exactly one thing and be nameable in a single verb phrase.
2. **Separate concerns.** Data loading, business logic, and output should live in separate places. A function that reads a file, runs a calculation, and writes a report has three reasons to break — split it into three.
3. **Rename for clarity.** Variable names like `x`, `df2`, or `temp` are a maintenance cost. Rename to reflect what the thing actually represents.
4. **Delete dead code.** If a function is never called, delete it. If a variable is never used, delete it. Dead code creates confusion and false leads.
5. **Run tests after every change.** Do not restructure for an hour and then run tests. Change one thing, run tests, commit. Short cycles catch problems immediately.

> You are done with Phase 3 when a developer unfamiliar with the system can read the code and understand what it does without running it.

---

### Phase 4: Extend

**Goal:** Add new capability using the improved foundation, with tests as a design tool.

1. **Write the test before the code.** Describe what the new behavior should do as a test. Watch it fail. Then write the code to make it pass. This is called test-driven development (TDD) and it ensures you only write code that is actually needed.
2. **Keep your characterization tests.** The tests from Phase 2 still run. They ensure that adding new behavior does not break existing behavior.
3. **Add new tests for new behavior.** Every new feature should come with tests that describe what it does. These tests are documentation that never goes out of date.

> You are done with Phase 4 when the new capability is live, tested, and the test suite is larger than when you started.

---

## Further reading

These topics from the [learning roadmap](../roadmap.md) support each phase directly:

- **Automated Testing** (Intermediate #3) — foundations for Phases 2 and 4
- **Software Design** (Intermediate #4) — principles behind Phase 3 restructuring
- **Test-Driven Development** (Advanced #1) — the discipline behind Phase 4
- **Continuous Integration & Delivery** (Intermediate #6) — automating the test run in Phase 2
