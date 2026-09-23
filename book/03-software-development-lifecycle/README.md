# Section 03 — The lifecycle of decision-support software

> **Status:** in construction

## Introduction

The software development life cycle (SDLC) is a process that breaks down the process of creating software in phases.
There are 2 main models of applying SDCL: Waterfall and Agile.

## Waterfall v/s Agile

To develop this.

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
