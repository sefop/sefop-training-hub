# Part 01 — Testing optimization models

Software engineers test code by comparing its output with an answer they already know. An optimization model breaks
that habit: the answer you would compare against is the very thing the model exists to compute. This part explains
how to test a model anyway, in eight short chapters, each built around one idea.

## Who this part is for

- **Scientists who write optimization models** — PhD students and operations research practitioners. No software
  engineering background is assumed: every term is defined on first use and collected in the
  [glossary](../appendix/glossary.md).
- **Engineering managers** — chapters 01 and 02 explain why testing a model differs from testing other code, and
  what to ask your team for.

## Chapters

| # | Chapter | After it you can… | Status |
|:---:|---|---|---|
| 01 | [Why optimization models are hard to test](01-why-optimization-models-are-hard-to-test.md) | Name the oracle problem and explain why the usual way of testing fails for a MIP | Ready |
| 02 | [Test the contract, not the algorithm](02-test-the-contract-not-the-algorithm.md) | Write tests that keep passing when someone swaps the solver | Ready |
| 03 | [Oracles you write by hand](03-oracles-you-write-by-hand.md) | Choose a small, systematic set of instances whose answers you work out yourself | Ready |
| 04 | [Metamorphic relations](04-metamorphic-relations.md) | Test a model without knowing its optimal value | Ready |
| 05 | [Differential testing](05-differential-testing.md) | Use a second implementation to find mistakes in the formulation | Ready |
| 06 | [When optimality is not guaranteed](06-when-optimality-is-not-guaranteed.md) | Decide which tests survive when the solver is a heuristic | Ready |
| 07 | [Duality as an oracle](07-duality-as-an-oracle.md) | Check an LP's optimum with a certificate instead of re-solving | Coming soon |
| 08 | [Testing a Pareto front](08-testing-a-pareto-front.md) | Test a multi-objective model that has no single optimum | Coming soon |

The chapters build on each other. Chapters 01–02 set up the vocabulary. Chapters 03–05 present three kinds of
oracle, each covering a gap the previous one leaves open. Chapter 06 revisits all three under a weaker promise. Read
them in order the first time; after that, each chapter lists its prerequisites at the top.

## The running example: a knapsack

Every chapter uses the same problem, so that the testing ideas change while the model stays still.

A catalogue of items, each with a cost, a volume, and a calorie count. Each item can be taken more than once, up to a
maximum quantity. The task: choose how many units of each item to take so that total calories is maximized, subject
to a cost budget and a volume budget.

Let $I$ be the set of items. For each item $i \in I$, let $c_i$ be its cost, $v_i$ its volume, and $k_i$ its calorie
count, all fixed, **non-negative** parameters. Let $u_i$ be its maximum quantity, $C$ the cost budget, and $V$ the
volume budget. The decision variable $x_i$ is the quantity of item $i$ selected.

$$
\begin{aligned}
\max_{x} \quad & \sum_{i \in I} k_i x_i \\
\text{s.t.} \quad & \sum_{i \in I} c_i x_i \le C \\
& \sum_{i \in I} v_i x_i \le V \\
& 0 \le x_i \le u_i, \quad x_i \in \mathbb{Z}, \quad \forall i \in I
\end{aligned}
$$

The feasible region can be empty. If $C < 0$, no $x$ satisfies the cost constraint, not even $x = 0$ — this is where
the non-negativity of $c_i$ matters, since it puts every attainable total cost at zero or above. The instance then has
no solution at all, and a correct solver must report that rather than return some $x$ anyway.

### A two-item instance

| Item | Cost $c_i$ | Volume $v_i$ | Calories $k_i$ | Max quantity $u_i$ |
|:---:|:---:|:---:|:---:|:---:|
| A | 2 | 1 | 10 | 1 |
| B | 1 | 2 | 6 | 1 |

with cost budget $C = 2$ and volume budget $V = 2$:

$$
\begin{aligned}
\max_{x} \quad & 10 x_A + 6 x_B \\
\text{s.t.} \quad & 2 x_A + x_B \le 2 \\
& x_A + 2 x_B \le 2 \\
& x_A, x_B \in \{0, 1\}
\end{aligned}
$$

[Chapter 01](01-why-optimization-models-are-hard-to-test.md) solves it by hand.

## How to read the pseudocode

Chapters show tests as short, language-agnostic pseudocode, so the ideas transfer to any language. The conventions:

```
a = item(name="A", cost=2, volume=1, calories=10, max_quantity=1)

result = solve([a], cost_budget=2, volume_budget=2)

expect result.feasible == true
expect result.total_calories == 10
```

- `solve(items, cost_budget, volume_budget)` runs whichever solver is under test. When a chapter needs a specific
  one, it writes `enumeration_solver().solve(...)` or `mip_solver().solve(...)`.
- `result` has five fields: `feasible`, `quantities` (item name → units chosen), `total_calories`, `total_cost`, and
  `total_volume`. When `feasible` is false, the other fields carry no meaning.
- `expect` marks an assertion: the test fails if the condition is false. `==` on numbers means equal within a small
  numerical tolerance.

## Practice

Every chapter ends with a **Practice it** box linking to runnable exercises.

- **Python:** [training-testing-python — exercise 5](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md),
  which implements this knapsack with two solvers and ends with an untested shortest-path solver for you to test.
- **Java:** coming soon.

All practice repositories are listed in the [appendix](../appendix/practice-repositories.md).

## What this part does not cover

- **Performance and scale.** No chapter tests how fast a solver is or how large an instance it handles.
- **Input validation.** Items are never checked for nonsense values such as a negative cost. Every infeasible
  instance in this part comes from the budgets, never from a malformed item.
- **Continuous and multi-objective models**, until chapters 07 and 08.

---

[← Book contents](../../README.md) · [Next: 01 Why optimization models are hard to test →](01-why-optimization-models-are-hard-to-test.md)
