# Section 06 — Deploying decision-support software

> **Status:** planned. No chapters yet; this page collects the ideas the section will develop. Working titles may
> change before the first chapter is written.

## Introduction

A decision-support system creates value only once it is **deployed**: installed and running where the business uses it,
a place called **production**, often every day or every week, against data it has never seen. **The difference this
section addresses:** deploying ordinary software means shipping code, and a failed deployment is usually loud, with an
error or a crash. Deploying decision-support software means shipping code together with a model, a solver and its
license, and the data that feeds them. A failed deployment can also be silent: the solver hits its time limit, the gap
widens, or the data drifts, and the system still returns a plan, just a worse one. A system that runs is not
necessarily a system that works.

This section answers two questions:

1. **How do you deploy decision-support software?** Chapters 01–04.
2. **What do you measure once it runs in production?** Chapters 05–06.

### Ideas to develop

#### How to deploy

- **Cadence drives the deployment shape.** Section 01's four examples run on four cadences. Working hypothesis: an
  annual mine plan can be a tool an analyst runs by hand, a weekly delivery plan fits a scheduled batch run, and the
  daily recovery of an airline's operation needs an on-demand service that answers in minutes. The shorter the cadence,
  the more of the deployment has to be automated.
- **The solver is part of the deployment.** Commercial solvers are licensed per machine or through a license server,
  which complicates containers (packages that bundle code with everything it needs to run) and servers that start and
  stop on demand. Pin the solver version: two versions can return different optimal solutions with the same objective
  value, which users see as the plan changing for no reason.
- **The time limit is a business decision, not a solver parameter.** It states how long the business can wait for a
  plan. When a run hits it, every option has a cost: return the best feasible solution found, reuse the last plan, run a
  simple heuristic, or stop and alert a person.
- **Continuous integration** (CI: running the build and the tests automatically on every change) turns the tests of
  Section 05 into a gate every change passes before it reaches production. Solver licenses and long solve times make CI
  harder for decision-support software; the chapter should show how to test with small instances and open-source
  solvers.
- **Shadow runs.** Before switching models, run the new one alongside the current one on the same data for a few
  cycles, and compare their decisions and objective values. The switch then rests on a measured delta, not on hope.
- **Artifacts**: we need a place to store the artifacts to have proper ways to revert a wrong deployment.

#### What to measure in production

- **The baseline from ordinary software.** The [DORA](https://dora.dev/) delivery metrics measure how often a team
  deploys, how long a change takes to reach production, how often a deployment fails, and how fast the team recovers.
  They still apply to decision-support software, but none of them says whether the decisions are good.
- **Four layers to monitor.** Working hypothesis: ordinary software monitoring covers the first layer; decision-support
  software needs all four.

  | Layer | Question it answers | Examples |
  |---|---|---|
  | Run | Did the run finish? | Exit status, run time, memory |
  | Solver | How did the solver behave? | Status (optimal, feasible, infeasible, time limit), gap, time to the first feasible solution |
  | Data | Does the input look like what the model expects? | Missing values, instance size, values outside their usual range |
  | Decision | Is the decision good, and is it used? | Objective value against a baseline, override rate, plan versus actual, business result |

- **Instances grow with the business.** More trucks, stores, or flights mean larger instances, and run time creeps up
  until the solver starts hitting its time limit. Track the trend of instance size and solve time, not only whether
  each run passed.
- **The objective value is an estimate, not the result.** It is what the model predicts the plan is worth. Compare the
  plan with what was actually executed, and with the outcome the business observed.
- **Override rate:** how often planners change the plan before acting on it. A rising rate may signal a business rule
  the model is missing, or trust the model has lost. Run-level monitoring sees neither.
- **Log enough to reproduce any run:** the code version, the data snapshot, the solver version, the parameters, the
  time limit, and the random seed. Version control (tracking every change to your files so you can recover any past
  state) covers the code; the data and the solver version need the same care.
- **Track quality over time as a benchmark,** not only as pass/fail tests. Section 05, chapter 07 suggests tracking the
  average gap to an exact reference for heuristics; production monitoring extends that idea.

### Out of scope

- **Specific cloud providers or deployment platforms.** The practices are meant to transfer across them.
- **Monitoring the forecasts that feed a model.** When demand or travel times come from a predictive model, tracking
  its accuracy is a machine-learning topic; this section monitors the optimization side.

## Planned chapters

| # | Working title | After it you can… |
|:---:|---|---|
| 01 | How a decision reaches its users | Choose the deployment shape (a scheduled batch run, an on-demand service, or an interactive planning tool) that fits the cadence of the decision |
| 02 | Package the model with its solver | Run the same model, solver version, and license setup on a laptop, a CI server, and production |
| 03 | Plan for runs that end badly | Set a time limit and a fallback, so a run that hits the limit or finds no feasible solution still leaves the business with a usable plan |
| 04 | Release a new model safely | Compare a new model against the current one on real data before switching, and roll back when it is worse |
| 05 | Measure the health of every run | Record for each run whether it finished, how the solver behaved, whether the input looked like what the model expects, and enough to reproduce it |
| 06 | Measure the quality of the decisions | Track whether the decisions stay good and stay used: objective value against a baseline, how often planners override the plan, and the business result |
| 07 | Conclusion | Recall in one page how a decision reaches production, and what tells you it is still a good one |

---

[← Book contents](../../README.md) · [Next section: 07 Working with legacy decision-support software →](../07-working-with-legacy-dss/README.md)
