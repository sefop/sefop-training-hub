# Section 01 — Introduction

> **Status:** planned. No chapters yet; this page collects the ideas the section will develop. Working titles may
> change before the first chapter is written.

## Introduction

### Motivation

Operations research creates business value by helping organizations make better decisions. That value reaches the
business through **decision-support software**: software that runs repeatedly to turn data, mathematical models, and
business rules into recurring decisions. This section explains what that software is, why it often ends up hard to
maintain, and how the rest of the book is organized to address it.

### Ideas to develop

- **Four examples on four cadences**, one per level of decision: the **annual** extraction plan of a mine, the
  **monthly** shift schedules of a retail store, the **weekly** delivery plan of a transportation network, and the
  **daily** recovery of an airline's operation after a weather disruption.
- **The value is in the tool, not the analysis.** A one-off study ends at a deliverable. Decision-support software runs
  on a cadence, so it must be maintained, tested, deployed, and evolved.
- **Four symptoms** of weak engineering: the code works on one machine only; peers, and even the original authors,
  struggle to extend it; developers fear modifying it; and the application is eventually rewritten rather than evolved.
- **Two root causes**, following [Kanewala & Bieman (2014)](https://doi.org/10.1016/j.infsof.2014.05.006):
  1. **Cultural.** Operations research scientists are not trained in software engineering, and often do not see why they
     should be.
  2. **Technical.** Decision-support software has challenges that ordinary business software does not.
- **The literature thread**, in order: [Ackoff (1979)](https://doi.org/10.1057/jors.1979.22) on operations research
  becoming identified with models rather than with implementation and maintenance;
  [Vidoni (2021)](https://doi.org/10.1080/01605682.2020.1865848) on the need for an "Operations Research Engineering"
  practice; and [Vidoni & Cunico (2022)](https://doi.org/10.1007/s12532-022-00225-1), whose survey of 168 modellers found
  code and documentation debt widespread, and mostly introduced deliberately.
- **AI as an amplifier.** More than 70% of scientific programmers already write code with LLM-based tools
  ([O'Brien & Eisty, 2026](https://www.computer.org/csdl/magazine/cs/2026/01/11482007/2fJHVugY5UY)). The
  [2025 DORA report](https://dora.dev/research/2025/dora-report/) describes an AI assistant as an amplifier of the
  practices around it: strong teams move faster at good quality, weak teams ship more technical debt.
- **Where the book sits in SEFOP.** SEFOP has four dimensions: Train, Lead, Deliver, and Go Agentic. This book covers
  Train and Lead. Deliver lives in the reference-implementation repositories, and Go Agentic in `sefop-agentic`.

### Out of scope

- **How to apply any practice.** This section argues why the practices matter; Sections 03–09 explain how.

## Planned chapters

| # | Working title | After it you can… |
|:---:|---|---|
| 01 | What decision-support software is | Tell decision-support software apart from a one-off analysis, and place a system on the strategic, tactical, or operational level |
| 02 | What goes wrong, and why | Recognize the symptoms of weak engineering in decision-support software, and name its two root causes |
| 03 | AI coding assistants as amplifiers | Explain why AI assistants raise the value of engineering practices instead of replacing them |
| 04 | How to read this book | Pick a reading path for your role and find the sections that apply to your situation |

---

[← Book contents](../../README.md) · [Next section: 02 When a company needs decision-support software and an OR team →](../02-do-you-need-dss/README.md)
