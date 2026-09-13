# 01 — Why optimization models are hard to test

> **Audience:** Scientists & Engineering Managers · **Prerequisites:** the [running example](README.md#the-running-example-a-knapsack) · **~7 min read**

After this chapter you can explain why the usual way of testing code does not transfer to an optimization model, and
name the problem that makes it hard.

## The problem

An [automated test](../appendix/glossary.md#automated-test) is a small program that runs your code on a known input
and checks the output against an expected answer. The textbook example is a calculator: `add(2, 3)` should return 5,
and you know that without reading a single line of `add`. The test is cheap to write because the expected answer is
cheap to compute.

Now try the same with a MIP. To write `expect result.total_calories == ???`, you need the optimal value. For any
instance large enough to be interesting, computing that value independently means solving the very problem the model
exists to solve. The test needs the answer before the code can provide it.

## The idea

Whatever decides whether an output is correct is called a [test oracle](../appendix/glossary.md#test-oracle). For the
calculator, the oracle is arithmetic you already know. The difficulty of building an oracle when the correct output is
expensive, or impossible, to compute independently has a name in the software testing literature: the
[oracle problem](../appendix/glossary.md#oracle-problem).

You already know this asymmetry from optimization. Checking that a solution is *feasible* is cheap: substitute $x$
into each constraint. Proving that it is *optimal* is expensive: you need a matching bound, which is exactly what
branch-and-bound spends most of its time building. An oracle for feasibility is easy to write. An oracle for
optimality runs into the same wall your solver does.

The oracle problem is a reason to choose a testing technique deliberately, not a reason to skip testing. A model is
software: it gets refactored, its data changes, and eventually someone swaps its solver. Chapters 03–05 present three
kinds of oracle that work around the problem, each at a different cost.

## Worked example

The simplest oracle is a person. Take the [two-item instance](README.md#a-two-item-instance): each $x_i \in \{0, 1\}$,
so there are $2 \times 2 = 4$ candidate selections, few enough to list.

| $x_A$ | $x_B$ | Cost (≤ 2) | Volume (≤ 2) | Calories | Feasible? |
|:---:|:---:|:---:|:---:|:---:|---|
| 0 | 0 | 0 | 0 | 0 | yes |
| 1 | 0 | 2 | 1 | 10 | yes |
| 0 | 1 | 1 | 2 | 6 | yes |
| 1 | 1 | 3 | 3 | 16 | no — both budgets exceeded |

The best feasible selection is $x_A = 1$, $x_B = 0$, worth 10 calories. Nobody needed a solver to produce that answer,
so it can serve as the expected value of a test:

```
a = item(name="A", cost=2, volume=1, calories=10, max_quantity=1)
b = item(name="B", cost=1, volume=2, calories=6,  max_quantity=1)

result = solve([a, b], cost_budget=2, volume_budget=2)

expect result.feasible == true
expect result.total_calories == 10
```

The price of a human oracle grows fast. The number of candidate selections is $\prod_{i \in I} (u_i + 1)$: 4 for this
instance, but $4^{30} \approx 1.2 \times 10^{18}$ for 30 items that can each be taken up to 3 times. A person can
only be the oracle at teaching scale, which is exactly how [chapter 03](03-oracles-you-write-by-hand.md) uses one.

## Check yourself

1. For the calculator, what plays the role of the test oracle?
2. In the two-item instance, the cost budget rises from 2 to 3 and the volume budget stays at 2. What is the optimal
   calorie total?
3. How many candidate selections does an instance with three items and maximum quantities 1, 2, and 4 have?

<details>
<summary>Answers</summary>

1. Arithmetic you already know: you compute 2 + 3 in your head, independently of the code.
2. Still 10. Taking both items now fits the cost budget (3 ≤ 3) but uses volume 3 > 2, so item A alone remains best.
3. $2 \times 3 \times 5 = 30$.

</details>

## Where this stops working

The knapsack does not fully honour the claim of this chapter. It is only *weakly* NP-hard: a pseudo-polynomial dynamic
program solves it exactly, so a cheap independent oracle does exist for this particular problem. The oracle problem
bites hardest on general MIPs, where no such shortcut is available. The knapsack is used here because it is small
enough to reason about by hand, not because it is the hardest case.

> **Practice it**
> - Python: [training-testing-python — exercise 5, Setup](https://github.com/sefop/training-testing-python/blob/main/exercises/5-testing-mip-single-objective/instructions.md#setup)
> - Java: coming soon

## Further reading

- Barr et al., ["The Oracle Problem in Software Testing: A Survey"](https://ieeexplore.ieee.org/document/6963470),
  IEEE Transactions on Software Engineering, 2015 — the survey that names and organizes the problem.
- [Test oracle](https://en.wikipedia.org/wiki/Test_oracle), Wikipedia — a short overview.

---

[← Part 01 overview](README.md) · [Next: 02 Test the contract, not the algorithm →](02-test-the-contract-not-the-algorithm.md)
