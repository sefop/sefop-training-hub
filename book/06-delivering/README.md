# Section 06 — Delivering and operating decision-support software

> **Status:** planned. No chapters yet; this page collects the ideas the section will develop. Working titles may
> change before the first chapter is written.

A decision-support system creates value only while it runs in production, often every day or every week, against data
it has never seen. **The difference this section addresses:** ordinary software usually fails loudly, with an error or a
crash. Decision-support software can fail silently: the solver hits its time limit, the gap widens, or the data drifts,
and the system still returns a plan, just a worse one. Delivery and operation are about getting changes into production
safely and noticing when the decisions degrade.

## Who this section is for

Scientists who deploy and run their models, and engineering managers responsible for systems the business depends on.

## Planned chapters

| # | Working title | After it you can… |
|:---:|---|---|
| 01 | Version control for code, data, and models | Know exactly which code, data, and solver version produced any past decision |
| 02 | Continuous integration | Run your tests automatically on every change, before it reaches production |
| 03 | Environments and packaging | Run the system identically on any machine |
| 04 | Releasing a new model safely | Compare a new model against the current one on real data before switching |
| 05 | Monitoring decisions in production | Detect infeasible runs, time-limit hits, growing gaps, and drift in solution quality |

## Ideas to develop

- **Version control** (tracking every change to your files so you can recover any past state) works like a lab notebook
  for code. For decision-support software it also has to cover the data snapshot and the solver version behind each
  decision.
- **Continuous integration** (CI: running the build and the tests automatically on every change) turns the tests of
  Section 05 from a habit into a system that enforces itself. Solver licenses and long solve times make CI harder for
  decision-support software; the chapter should show how to test with small instances and open-source solvers.
- **Shadow runs.** Before switching models, run the new one alongside the current one on the same data for a few
  cycles, and compare their decisions and objective values. The switch then rests on a measured delta, not on hope.
- **Log enough to reproduce any run:** the instance, the random seed, the solver version, the time limit, and the gap.
- **Track quality over time as a benchmark,** not only as pass/fail tests. Section 05, chapter 07 suggests tracking the
  average gap to an exact reference for heuristics; production monitoring extends that idea.
- **Containers** (packages that bundle code with everything it needs to run) make a model run the same way on a laptop,
  a CI server, and production.

## What this section will not cover

- **Specific cloud providers or deployment platforms.** The practices are meant to transfer across them.

---

[← Book contents](../../README.md) · [Next section: 07 Evolving existing decision-support software →](../07-evolving-existing-code/README.md)
