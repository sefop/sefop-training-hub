# Section 03 — The lifecycle of decision-support software

> **Status:** in construction

## Introduction

The software development life cycle (SDLC) is a process that breaks down the process of creating software in phases.
There are 2 main models of applying SDCL: Waterfall and Agile.

### Ideas to develop

#### Why the lifecycle needs feedback

- **Software is not civil engineering.** A bridge is robust to small errors, and its requirements are known
  reasonably well before anything is built. Software is flexible and fragile at the same time: one wrong character
  changes what it does, and the team works with highly imperfect information throughout. The lifecycle a team
  chooses is a response to that asymmetry, not an administrative preference.
- **Building the system is how the requirements are discovered.** Users do not fully know what they want, they
  change their minds once they see a plan, and construction reveals constraints nobody stated. For decision-support
  software the effect is sharper: a planner cannot describe an objective function, and the business rules that
  matter often surface only when the first plan looks wrong to them. This is the material `### Elicitation` needs.
- **Two abilities decide how a team fares: learning quickly and adapting quickly.** Learning quickly needs short
  feedback loops and a disciplined way to draw conclusions from them. Adapting quickly needs low complexity:
  modularity to isolate a change, and safety mechanisms to make it without fear. Working hypothesis: every later
  section of this book is one of those two abilities applied to one lifecycle phase.
- **Why waterfall loses here.** It defers learning to the end — the team finds out what is wrong once everything is
  built — and treats development as a rigid linear process, so adapting costs a restart. Worth noting that Royce's
  1970 paper, the origin of the diagram, already argued for iteration; the caricature outlived the recommendation.
  Source: Royce (1970), "Managing the Development of Large Software Systems", *Proceedings, IEEE WESCON*.
- **Agile is a learning device, not a ceremony.** Its value is the short loop between a change and evidence about
  that change. Sources: Beck et al., the Agile Manifesto (2001); Forsgren, Humble & Kim, *Accelerate* (2018) for the
  measured link between fast feedback and delivery performance.
- **Iterative and incremental are two different moves.** Incremental: do not build it all at once. Iterative: do not
  try to get it right the first time. A decision-support team usually needs both — one region live before all
  regions (incremental), and a formulation revised after planners react to its first plans (iterative). Sources:
  Larman & Basili (2003), "Iterative and Incremental Development: A Brief History", *IEEE Computer*; Patton, *User
  Story Mapping* (2014). Candidate figure: the two moves side by side.

#### Learning: the scientific method as the engineering discipline

- **The reader already owns the method; only the object changes.** A scientist applies skepticism, evidence,
  reproducibility and causality to a claim about the world. The same principles apply to the claim "this code
  works". Working hypothesis: framed this way, engineering practice needs no separate justification for this
  audience — which is the same lever Section 08 uses to change a team's behavior.
- **Six principles, and what each one demands of code.** The table below is the chapter's core; the right-hand
  column collects violations heard in the field, to become a `### Check yourself`.

  | Principle | What it demands | A violation to use later |
  |---|---|---|
  | Skepticism | Do not trust, demand evidence | "No test needed — it is the same constraint as in another repository, which has worked for a long time." |
  | Evidence over authority | It does not matter who wrote the code, only what the evidence says | "It was written by [the boss / a principal engineer]." |
  | Relevance | Prove the experiment matters | "This will cut the model's run time from 10 seconds to 9.8 seconds." |
  | Testability | The hypothesis must be objective and measurable | "I will run 100 instances and see whether the results look OK." |
  | Reproducibility | Anyone should be able to run it again | "Follow the README, then call me — there are steps that are not written down." |
  | Causality | Control the variables so the result shows cause | "The tests pass either way; I was not asserting anything, only checking that it ran." |

- **Each practice serves a principle.** Static analysis catches errors before a run (skepticism); automated tests
  state the hypothesis and check it (testability, reproducibility); continuous integration gives evidence on every
  change (reproducibility); pinned environments make a run repeatable (reproducibility); branches and pull requests
  are isolated laboratories where one variable changes at a time (causality). The substance of testing is
  Section 05 — here the point is only which principle each practice serves.

#### Adapting: modularity and safety mechanisms

- **Adapting means changing code that already works.** Modularity isolates the change and keeps it small; automated
  tests are the safety mechanism that lets someone make it without fear. The techniques belong to Sections 04 and
  05. The lifecycle claim is narrower: a team without both cannot absorb change at the rate the business asks for
  it, whatever process it follows.

### Out of scope

- **Design principles and the parts of a system.** Coupling, cohesion, single responsibility, information hiding
  and where the boundaries of a system go are
  [Section 04 — Designing decision-support software](../04-design/README.md). This section claims only that a team
  needs modularity, never how to get it.
- **How to test any of it.** Every oracle, technique and test-design idea is
  [Section 05 — Testing decision-support software](../05-testing/README.md).
- **Tool tutorials.** Version control mechanics, continuous-integration configuration and environment management are
  in the [learning roadmap](../appendix/learning-roadmap.md).
- **What weak practice costs, and the failures that show it.** That case is made in
  [Section 01](../01-introduction/README.md#ch-what-goes-wrong).

## Context

Assume you are working in an ongoing project. The project is a decision-support software that runs an optimization
model to recommend a decision to your client. The project has a code repository hosted in GitHub and it has 3
environments: develop environment, stage environment and production environment.

## SDLC in decision-support software

On this section we will look at the main phases of the Agile SDLC and identify which phases require specialized
knowledge for a decision-support software. Each phase requiring specialized knowledge will be revisited later on its
own section of the book.

A typical development process starts from an idea that our client wants. Let's enumerate all the phases that this
idea has to go through to be usable by the client:

1. Elicitation
2. Planning
3. Design
4. Testing
5. Deployment
6. Monitoring

### Elicitation

This phase is related to gathering requirements, discovering and interpreting what the client actually wants. As an
OR scientist there are some nuances you should take in consideration when talking with your client, for example,
avoid talking in math terms:

- Avoid asking 'what is your objective function'
- Avoid asking 'what is your variable'

Because of these nuances, this will be assessed on a single section.

### Planning

This phase is related to estimation, backlog management and agile iterations. Working in decision-support software
does not have significant differences in planning than in traditional software, thus this will not be a specific
section.

### Design

Design is related to the structure of the code. There is structure at all levels of an application:

- Function-level
- Class-level
- Component-level
- Program-level
- Application-level
- Enterprise-level

For the purposes of DSS, we will focus from function-level to application-level. Usually at the program-level and
upward we tend to use the word 'architecture' instead, but that is just a detail. DSS have unique questions from the
class-level to the application-level, so we will dive into those in the design section. Some example questions to
answer:

- How should we design a DSS to be solver-agnostic?
- How should we design a DSS to support multiple solution algorithms?

Other design questions also come on this phase, which are related to situations where most of the big foundations
are already in place, and now I need to -for example- add a new constraint to the model. How should I design this
feature? Here we will dive into some principles for you to have in mind (ex: SOLID principles), with specific
examples for DSS.

### Testing

The testing phase is in charge of applying automated tests to the DSS features. This phase is deep in new questions
that arise from the mixture of DSS and software engineering, for example:

- How to automatically test the formulation of an optimization model?
- How to automatically test the output of an optimization model?
- How does integration test look like in DSS?
- How does end-to-end tests look like in DSS?

We will dive deep on this phase on the related section.

### Deployment

When deploying DSS there are no much differences from deploying traditional software. As of now this will not be a
new section.

### Monitoring

Monitoring a DSS may have some unique questions: what to monitor? how do I know if the model is behaving correctly
in production? We will explore these and other questions on this section.

---

<a id="ch-conclusion"></a>

## Conclusion

Decision-support software goes through the same lifecycle as any other software. The phases do not change; what
changes is how much specialized knowledge each one demands.

| Phase | Does it demand specialized knowledge? |
|---|---|
| Elicitation | Yes — the client does not think in objective functions and variables, so the requirements have to be drawn out in their own language |
| Planning | No — estimation, backlog management and iterations work here as they do anywhere |
| Design | Yes — staying solver-agnostic, supporting several solution algorithms, and deciding where a new constraint belongs |
| Testing | Yes — the expected answer is the very thing the model computes |
| Deployment | Yes — what ships is code together with a model, a solver and its license |
| Monitoring | Yes — a run that finishes is not the same as a run that produced a good decision |

That verdict is the map for the rest of the book: every phase in the Yes rows gets a section of its own, and each of
those sections opens by naming the difference it addresses.

---

[← Book contents](../../README.md) · [Next section: 04 Designing decision-support software →](../04-design/README.md)
