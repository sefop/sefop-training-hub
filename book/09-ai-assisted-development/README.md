# Section 09 — AI-assisted development of decision-support software

> **Status:** planned. No chapters yet; this page collects the ideas the section will develop. Working titles may
> change before the first chapter is written.

## Introduction

### Motivation

More than 70% of scientific programmers already write code with LLM-based tools
([O'Brien & Eisty, 2026](https://www.computer.org/csdl/magazine/cs/2026/01/11482007/2fJHVugY5UY)), and the
[2025 DORA report](https://dora.dev/research/2025/dora-report/) describes an AI coding assistant as an amplifier of the
practices already around it. **The difference this section addresses:** an assistant writes plausible model code, and
a wrong formulation looks just as plausible as a right one. Because the correct output of a model is expensive to know
(Section 05, chapter 02), AI-written decision-support code is harder to verify than AI-written business code. This
section covers how to capture the speed of AI assistants without accepting that risk blindly.

### Ideas to develop

- **A failure mode to name explicitly:** asked to make a failing test pass, an assistant may change the expected value
  instead of the code. Contract tests written by a person, and reviewed changes to them, are the defense.
- **Formulation review.** A checklist for reviewing an AI-written formulation: every constraint traced to a business
  rule, every index set checked for silently dropped elements, and a differential test against enumeration on small
  instances (Section 05, chapter 06).
- **Context files** that tell an assistant the project's conventions, contract, and glossary — the same information a new
  team member needs.
- **Evaluations** (a fixed set of tasks with known good outcomes, used to measure an AI workflow) before adopting a
  workflow team-wide. See "Don't Ship Skills Without Evals" in the
  [Learning Roadmap](../appendix/learning-roadmap.md#ai-assisted-coding).
- **Tools and guides** in the [`sefop-agentic`](https://github.com/sefop/sefop-agentic) repository, currently under
  construction.

### Out of scope

- **A comparison of specific AI tools.** They change faster than a book can; the section focuses on practices that
  outlast any one tool.

## Who this section is for

Scientists who use AI coding assistants on models, and managers deciding how their team should adopt them.

## Planned chapters

| # | Working title | After it you can… |
|:---:|---|---|
| 01 | Why fundamentals matter more with AI | Explain why tests, modularity, and clear contracts make an AI assistant more useful, not less |
| 02 | Tests as the guardrail for AI-written models | Use the oracles of Section 05 to check code an assistant wrote |
| 03 | Giving an assistant the context of your model | Write the project context an assistant needs: the contract, the formulation, and the vocabulary |
| 04 | Evaluating AI workflows | Measure whether an AI workflow actually improves your results before relying on it |

---

[← Book contents](../../README.md)
