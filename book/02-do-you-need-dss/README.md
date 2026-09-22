# Section 02 — When a company needs decision-support software and an OR team

> **Status:** planned. No chapters yet; this page collects the ideas the section will develop. Working titles may
> change before the first chapter is written.

## Introduction

Before asking how to build decision-support software, a company has to ask whether it should. Not every decision
deserves software, and not every company that needs the software needs its own team to build it. This section covers
that decision in three steps: whether a decision justifies software, who should build it, and where the team sits once
it exists.

### Ideas to develop

- **Signals that a decision is a candidate for software.** The decision repeats on a cadence; each instance of it is
  worth enough to matter; the data exists; the business rules are stable enough to write down; and people currently
  spend significant time producing it by hand. Working hypothesis: the more signals hold, the stronger the case.
- **Build vs. buy as a trade-off.** An in-house team keeps control of the model and the knowledge behind it, at the cost
  of salaries and of maintaining software for years. A vendor delivers a first result faster, at the cost of licenses,
  less control over the formulation, and dependence on that vendor for every change.
- **Three places a team can sit**, each with a different trade-off between closeness to the business and engineering
  standards: embedded in a business unit, in a central analytics group, or inside IT.
- **The embedded team as a specialized software team**, owning a decision-support product rather than running a
  sequence of studies. Which expertise such a team holds and which it borrows is
  [Section 08, chapter 01](../08-leading-the-team/README.md#01--how-to-staff-your-team).
- **Proof of concept (POC):** a small, time-boxed build that tests whether an approach creates value before a company
  commits to it. Define the baseline and the target improvement before starting, so the outcome is a measured delta,
  not an impression.

### Out of scope

- **Roles, hiring, and team culture.** Those belong to [Section 08 — Leading the team](../08-leading-the-team/README.md).
- **How to build the software** once the decision is made. That starts in
  [Section 03 — The lifecycle of decision-support software](../03-software-development-lifecycle/README.md).

## Planned chapters

| # | Working title | After it you can… |
|:---:|---|---|
| 01 | When a decision deserves software | Decide whether a recurring decision justifies decision-support software rather than a one-off analysis or a spreadsheet |
| 02 | Do you need an in-house team? | Compare an in-house OR team with vendors and consultants, and choose between building and buying |
| 03 | Your team in the organization | Choose where the team sits and whom it reports to |
| 04 | From proof of concept to funded project | Run a proof of concept with exit criteria set in advance, and turn a successful one into a funded project |

---

[← Book contents](../../README.md) · [Next section: 03 The lifecycle of decision-support software →](../03-software-development-lifecycle/README.md)
