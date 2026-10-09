# Section 07: Working with legacy decision-support software

<a id="ch-introduction"></a>

## 1. Introduction

An inherited decision-support system holds useful knowledge: business rules, modeling choices, and
behavior its users depend on. You need to extend or repair it while preserving that value. Yet a
small request can require reading a large function, rerunning the entire model, and asking the one
colleague who remembers why it works that way. A
[legacy system](../appendix/glossary.md#legacy-system) is software that is difficult to change safely.
Its difficulty has both technical and cultural causes.

Lasting improvement changes both the software and the way the team works. Technical protection
makes change possible; colleagues need a clear direction, confidence, and working conditions that
help them use that protection. This section addresses a team member with some support and limited
authority, building on the testing practices of [Section 05](../05-testing/README.md) and the
delivery practices of [Section 06](../06-deployment/README.md). The destination is a shared practice
of investing in the system while continuing to deliver useful decisions.

---

<a id="ch-brownfield"></a>

## 2. Understand the inherited system and its team

A system that already helps the business is worth preserving. Before improving it, you need to
understand which behavior people rely on and what makes changing it difficult. The source files
answer only some of those questions. The history of the project, its commitments, and the people
maintaining it explain the rest.

### The inherited cargo planner

The examples in this section follow a fictional team maintaining the
[cargo loading system](../appendix/cargo_model_example.md). The team began with a script for a
feasibility study. It now supports recurring planning, but reading the bookings, building the
optimization model, solving it, and writing the plan still happen in one large function. Most
checks involve running that function and inspecting its output.

The scientist who wrote the original formulation knows its assumptions well. A colleague manages
input changes and delivery commitments. You have joined the project with experience in automated
testing and some support to improve the software. All three want dependable plans; they have
different knowledge, responsibilities, and opportunities to work on the problem.

Start by following one planning run from its inputs to the delivered proposal. Ask the planner
which output they use, which conditions require attention, and what they do when a proposal cannot
be used. Ask colleagues where the system has surprised them and which changes they avoid. Keep
inputs, mathematical assumptions, and operational expectations together in your investigation:
a program can run successfully while answering the wrong planning question.

Then trace a recent change. Which functions had to be edited? How was the result checked? Who
needed to participate? This gives you a concrete account of the difficulty instead of a general
claim that the software needs improvement.

### How reasonable choices accumulate

[Tactical programming](../appendix/glossary.md#tactical-programming) prioritizes finishing the
current task while deferring improvements to the design. Repeatedly adding another condition to
the cargo script can satisfy each immediate request while making the next one harder. That is one
way a project accumulates [technical debt](../appendix/glossary.md#technical-debt): future effort
created by shortcuts taken today.

[Strategic programming](../appendix/glossary.md#strategic-programming) invests in the design while
delivering working behavior, so future changes remain manageable. John Ousterhout develops this
distinction in [_A Philosophy of Software Design_](https://web.stanford.edu/~ouster/cgi-bin/aposd.php).
[2. What design is for](../04-design/README.md#ch-design-purpose) in Section 04 applies it to the
cargo system.

The original script may have been appropriate for the study. Its responsibilities changed when
people began using it repeatedly and requesting extensions. Investigate when those expectations
changed, whether anyone had time to adapt the software, and whether the team knew how to begin.

Other paths lead to the same difficulty. Knowledge may leave with a colleague. A solver change may
make the old comparison process unreliable. A team may recognize a design problem but lack tests
that let it address the problem safely. Age alone tells you little about these conditions.

### What keeps the current practices in place

People who perform the same work can have different reasons for continuing it. Explore those
reasons with them. The following observations are starting points for a conversation, not labels
to attach to colleagues.

| Observation | Possible barrier | Question to explore |
| --- | --- | --- |
| A colleague agrees tests would help but has written none | No practical starting point | Can we write one relevant test together? |
| A colleague avoids restructuring the model-building function | Fear of changing behavior | What feedback would make that change safe enough to attempt? |
| Feature estimates include implementation and manual checking only | The plan leaves no time for automated checking | What work must an estimate include for the change to be complete? |
| A scientist sees model testing as someone else's job | A different understanding of professional responsibility | Who can establish that the formulation implements the intended rule? |
| The team follows one experienced colleague's view of acceptable work | Informal authority and an established norm | Whose participation would make a new practice credible? |

A request for another training session helps only if learning is the barrier. Someone who can
already write a test may need time to maintain it. Someone with time may need a demonstration that
the test can check their model. One colleague can face several barriers, and those barriers can
change as the project progresses.

You also need to understand your own room to act. Establish what improvement work your manager
supports, which changes you can make yourself, and who agrees on shared development practices.
You can model a practice in your own work and invite colleagues to try it. Allocating other
people's time or changing release responsibilities may require additional support.

Different priorities do not necessarily prevent collaboration. A colleague focused on delivering
a new input format may welcome a test that makes that delivery easier to verify. Begin with work
you can support together, and ask for specific backing when a necessary improvement exceeds your
authority. [Section 08](../08-leading-the-team/README.md) develops the broader leadership decisions.

### Check yourself

The team understands that a large model-building function is hard to change. A workshop on design
has produced no changes. What should you investigate before scheduling another workshop?

<details>
<summary>Answers</summary>

Check whether colleagues know how to begin, have protection for existing behavior, and have time
allocated to the work. Ask how delivery is estimated and whose agreement is needed. Awareness of a
problem does not establish the ability or opportunity to address it.

</details>

---

<a id="ch-safety"></a>

## 3. Establish safety for improvement

The team already has useful behavior to preserve. Yet it checks that behavior by running a few
familiar inputs and asking someone to inspect the result. Before changing the structure, you need
a way to notice unintended differences without relying on that person's memory.

An [automated test](../appendix/glossary.md#automated-test) runs the program with known inputs and
checks its output. Michael Feathers' [_Working Effectively with Legacy Code_](https://www.informit.com/store/working-effectively-with-legacy-code-9780132931779)
provides the technical foundation for bringing existing code under test.
A [characterization test](../appendix/glossary.md#characterization-test) records what the system
does today, then detects changes to that behavior. It supplies protection before you improve the
code's structure; it does not establish that the recorded behavior is correct.

### Capture behavior people depend on

Choose a small set of representative planning situations with the team. For the cargo planner,
include an ordinary departure, a capacity that cannot accommodate committed freight, and a case
near a capacity boundary. Include an input-reading failure if handling it matters to the users.

Retain the inputs and the settings needed to repeat each run. Identify the software version
being recorded. Prefer cases small enough to run frequently, and keep their outputs away from
operational planning while you investigate them.

Decide what a meaningful difference is before storing the result. A file timestamp is usually
irrelevant. A changed proposal status, missing committed freight, or changed objective value may
require attention. If several loads are equally acceptable, comparing their exact decision vectors
can reject a valid result. Specify the properties and tolerances that matter, using
[8. Testing an optimization model](../05-testing/README.md#ch-model-testing) in Section 05.

A saved result from the old system is evidence about the old system. Where the expected answer is
known independently, check that too. If a case exposes a defect, record it explicitly and develop a
correctness test for the intended behavior. Do not silently turn an observed error into an accepted
business rule, or erase the observation to make the new test pass.

### Create a path to controlled changes

Make the characterization checks runnable by another colleague. Connect them to
[continuous integration](../appendix/glossary.md#continuous-integration), which automatically builds
and checks changes. A check that runs only when its author remembers to run it offers weaker
protection during shared work.

If the code cannot be exercised without access to live planning data or a particular person's
machine, first create a repeatable way to supply saved inputs and capture output. Getting a broad
check around the existing behavior can require less restructuring than immediately isolating every
function. Feathers develops the detailed techniques for that work.

Once those checks work, make a small structural improvement and inspect any differences.
[Refactoring](../appendix/glossary.md#refactoring) changes the internal structure while preserving
behavior. For example, move input reading into a [module](../appendix/glossary.md#module), a function
or group of functions with a boundary, while leaving the formulation unchanged. Then add a focused
test of that module as the design makes it accessible.

Stabilization has a useful stopping point: colleagues can repeat important cases, see failures on
changes, and explain which behavior is protected and which remains uncertain. That gives the next
improvement a foundation. It does not require complete coverage or a finished redesign of the
entire system.

### Use agents to assist the work

A [coding agent](../appendix/glossary.md#coding-agent), an assistant that can inspect files and
propose changes, can help map the existing execution path, prepare saved-input cases, and draft
initial tests. Give it a bounded task and review the result against the behavior you intended to
capture.

Inspect what each assertion actually checks. An agent can produce a passing test that simply
copies the current output, or change an expected value when an implementation change makes a test
fail. Keep the behavioral record separate from the decision that a difference is acceptable.
Run the checks and review the changes before adopting them.

[Section 09](../09-ai-assisted-development/README.md) develops agent-assisted work in more depth.
Here, the useful outcome is a protection mechanism the team understands and can maintain.

### Further reading

- Michael Feathers, [_Working Effectively with Legacy Code_](https://www.informit.com/store/working-effectively-with-legacy-code-9780132931779),
  2004: technical methods for introducing tests and making controlled changes to inherited code.

---

<a id="ch-direction"></a>

## 4. Give change a clear direction

Colleagues can agree that a system is difficult to maintain and still have no common understanding
of what to do next. A request to improve quality leaves many decisions open: which problem to
address, what action to take, and how to tell whether it helped. Agreement becomes actionable when
those decisions are concrete.

Chip and Dan Heath offer a useful framework in
[_Switch: How to Change Things When Change Is Hard_](https://heathbrothers.com/books/switch/).
Their metaphor distinguishes the Rider, the planning side of change; the Elephant, the motivation
that sustains effort; and the Path, the circumstances in which people act. These are aspects to
consider together, not types of colleague. The applications here use selected strategies and
original decision-support examples.

This chapter applies the Rider idea: clarify a worthwhile destination, learn from work that already
succeeds, and make the next actions specific.

### Name a result the team needs

Begin with a difficulty colleagues recognize. In the cargo team, changing the booking format means
reading through the model-building function and running a complete solve to check that the input
was interpreted correctly. The colleague responsible for new formats already has a reason to want
that work to be easier.

A useful destination is: another scientist can change how bookings are read, check the result
without solving the optimization model, and show a reviewer what changed. That statement names an
ability the team needs. It gives design and testing a purpose beyond complying with a quality
target.

Agree on the evidence of completion before proposing a large program of improvement. For this
change, it includes examples of the old and new input formats, checks of the bookings each produces,
and passing checks of the system's existing planning behavior. The team can then estimate the work
that delivers that result, including its verification.

### Make the difficulty visible

Show the route the current change takes through the system. Use an example colleagues can inspect
together: the reading logic that sits beside model construction, the manual comparison required,
and the questions that comparison cannot answer confidently. Keep the discussion about the
system's current responsibilities.

A [static analysis](../appendix/glossary.md#static-analysis) tool inspects source files without
running the program and flags patterns that may need attention. Its findings can help identify
large functions or repeated logic. Explain what a finding means and connect it to an actual change;
a count alone gives little direction to someone unfamiliar with the tool.

Use shared examples and project-level evidence. A presentation centered on a named colleague's
mistake can make participation personally costly. A discussion of a function the team now needs
to change invites everyone to contribute what they know. A tool's finding is a prompt to examine
the code, and colleagues may have good reasons to disagree with it.

### Start from a working example

Look for a practice the team already uses successfully. Perhaps the catalogue reader has a small
[unit test](../appendix/glossary.md#unit-test), a test of one function or other bounded unit on its
own. Ask its author to show how the input, expected result, and failure message are arranged.

Adapt that example to the booking reader. The resemblance gives a colleague a starting point and
makes the practice visibly part of the team's work. If there is no useful local example, create one
on the current problem and work through it with someone who knows the input rules.

The example should be small enough to understand and complete enough to copy safely. Explain which
behavior it protects and what it leaves unchecked. A test that merely confirms the reader returned
something gives a learner the wrong pattern to repeat.

### Turn an intention into actions

Agree on a short sequence for the booking-format change:

1. Retain examples of the existing format and the new one.
2. State the booking records each example should produce.
3. Add a test that checks those records.
4. Change the reader and inspect the system-level checks for unintended differences.
5. Ask a colleague to review the behavior and the evidence together.

Those actions connect a broad goal to work someone can start. They also reveal missing support:
if nobody can state the expected records, the input rules need clarification; if the checks cannot
run, the team has more stabilization work to do.

Use training to address the gap that appears. Someone who understands the booking rules but has
never arranged a test benefits from writing this one with you. Someone who already has that skill
may need agreement that verification belongs in the delivery estimate. The shared destination
stays the same while the support differs.

### Check yourself

A team proposes raising test coverage as its first improvement goal. What additional agreement
would make that goal useful to the scientist changing an input format?

<details>
<summary>Answers</summary>

Agree which behavior needs protection, which examples establish it, and what the scientist will
be able to change or check afterward. A coverage number records execution of code; it does not
specify the behavior a test must verify.

</details>

---

<a id="ch-motivation"></a>

## 5. Build confidence and motivation

An improvement can be sensible and still feel difficult to begin. A colleague may understand the
benefit of tests yet worry about damaging a formulation, exposing a gap in their knowledge, or
missing a delivery commitment. Clear instructions address what to do; those concerns influence
whether someone feels able and willing to do it.

In the metaphor from Chip and Dan Heath's
[_Switch: How to Change Things When Change Is Hard_](https://heathbrothers.com/books/switch/),
the Elephant represents motivation. Here, its relevant applications are making the need for change
concrete and helping colleagues see themselves succeeding at the new practice.

### Connect the practice with scientific confidence

A scientist is responsible for the reasoning implemented in the model. Reviewing the equations is
valuable, but the software also selects records, creates indexed expressions, applies bounds, and
interprets the solver's result. Confidence in the mathematics includes checking those operations.

Consider a controlled demonstration using the cargo model. One departure has a two-tonne weight
capacity and three committed pallets, each weighing one tonne. Its hold has ample room.
No allowed load can meet the commitment. In a separate experimental copy of the model, omit the
minimum-load requirement for committed freight. The altered model can now return a feasible
proposal, although it answers a different problem.

A colleague can derive the expected infeasibility without needing to trust the solver. An
[automated test](../appendix/glossary.md#automated-test), a repeatable program that checks a result
against an expectation, makes the disagreement visible. The demonstration connects the test to
the scientist's own domain judgment.

The discovery can happen in a learning session before any operational use. Invite the colleague
to explain why the answer is wrong and help choose the case. The point is to establish a useful
way to examine their work. Keep the demonstration separate from live planning and from judgments
about who previously wrote the model.

### Make the first contribution achievable

Move from the demonstration to a contribution the colleague can complete. Let them choose another
small case and explain the expected behavior. Work together on expressing that expectation as a
test. Then let them make the next change while you review it.

A broad request to test every constraint can make the distance to competence look enormous. One
well-understood case creates a visible achievement and exposes the next learning need. Protect
time for that work with whatever support you have, and make its scope clear to the people waiting
for delivery.

Reduce the uncertainty of the first attempt. Show how to run the check, where its output appears,
and who can help interpret a failure. Ask about the test's reasoning during review. A colleague
who can explain the expectation and adjust the case is gaining something beyond the ability to
copy the example.

### Make learning safe

People need room to say that they do not understand a technique. In a review, ask how a test
establishes its expected result and discuss what the code makes difficult to check. Offer concrete
help with the difficulty. Admit your own uncertainty about business rules and let the domain
expert resolve it.

Respect expertise already present. The scientist knows which commitment matters, the input
specialist knows how booking records are interpreted, and you may know how to automate the check.
Combining that knowledge produces stronger evidence than expecting one role to supply everything.

This is a general condition for learning software practices. The decision-support setting gives it
a particular form: someone can be highly skilled in optimization and still need help with automated
testing, while someone skilled in testing needs help choosing a meaningful model expectation.

### Let colleagues own the achievement

As the booking checks and model examples become useful, ask colleagues to explain them to the team.
Credit the person who clarified the rule, designed the case, or improved the failure message.
A short demonstration by a colleague can make the practice recognizable as something the team
does for its own work.

Tie recognition to a concrete contribution. For example, the scientist explains how the
committed-freight case distinguishes the intended problem from the altered one. The achievement is
a more defensible model, not simply a larger test count.

A successful presentation is evidence of participation and advocacy. To assess independent skill,
look at subsequent work: can colleagues choose cases, justify expectations, and interpret failures
without needing you to make every decision? Keep support available while that ability develops.

### Check yourself

A scientist says testing is software engineering work and therefore outside their role. How can
the committed-freight demonstration help, and what support might still be needed?

<details>
<summary>Answers</summary>

It shows that the expected result depends on the scientist's knowledge of the planning problem.
Testing the implementation helps establish that it represents that problem. The colleague may
still need practical help writing the test, time to learn, and agreement about shared
responsibilities. A convincing demonstration does not remove all those barriers.

</details>

---

<a id="ch-team-practices"></a>

## 6. Make better practices easier to repeat

A team can understand a new practice, use it once, and still return to familiar work under pressure.
The effort of remembering, arranging, and checking the practice matters every time it is repeated.
For improvement to become normal work, the everyday workflow must support it.

The Path in Chip and Dan Heath's
[_Switch: How to Change Things When Change Is Hard_](https://heathbrothers.com/books/switch/)
represents those circumstances. The applications here focus on making the working environment
support the practice and attaching it to activities the team already performs.

### Put evidence where changes are reviewed

A [pull request](../appendix/glossary.md#pull-request) is a proposal to merge a change into the shared
code, with its differences available for review. If review is already part of the team's work,
use it as a point at which the changed behavior and its evidence are examined together.

Agree on a few questions the proposal should answer:

- What behavior or structure changes, and why?
- Which checks demonstrate the intended result?
- What observed differences need a reviewer or planner to assess?

For the booking reader, the proposal can point to the input examples and expected records developed
in [4. Give change a clear direction](#ch-direction). A reviewer has a concrete basis for asking
about an omitted check.

Model this practice in your own changes first. Work with colleagues to make the questions useful,
and agree who maintains the examples and review process. Introducing a form is easy; keeping its
questions relevant requires shared judgment. A completed form accompanies the evidence and does
not replace examining it.

### Keep feedback short and dependable

[Continuous integration](../appendix/glossary.md#continuous-integration) automatically builds and
checks changes. [Continuous delivery](../appendix/glossary.md#continuous-delivery) keeps checked
changes ready to release through an automated path. Together, continuous integration and
continuous delivery (CI/CD) make the repeated path from a proposed change to a running version
more predictable.

Connect the team's checks to that path. Put small input-reading and model cases early enough that
a colleague gets useful feedback while the change is fresh in mind. A failure should identify the
case, the expected behavior, and the observation that disagreed. Give someone responsibility for
investigating it rather than leaving a red status as everyone's background problem.

A [flaky test](../appendix/glossary.md#flaky-test) passes or fails without a relevant code change.
Repeated unexplained failures can teach the team to disregard its feedback. Investigate the cause:
an exact decision-vector comparison may reject equally valid optima, or a time-limited solve may
make an expectation unstable. Repair the check or its execution conditions and record any temporary
gap in protection.

Long-running experiments also need a deliberate place in the process. Keep them identifiable and
run them when the change warrants them. A quick check is useful only for the behavior it actually
covers. Model changes may require broader assessment before release, as developed in
[6. Release a new model safely](../06-deployment/README.md#ch-safe-release) in Section 06.

Humble and Farley's
[_Continuous Delivery_](https://www.informit.com/store/continuous-delivery-reliable-software-releases-through-9780321601919)
develops this repeatable delivery approach. Bug fixes use the same path as features. Improve
automation and feedback so the path supports urgent corrections as well as ordinary development.

### Remove a repeated obstacle

Find an adjacent task that makes improvement expensive. The cargo team may copy the same input
files, set the same options, and manually collect results whenever it compares two versions.
Automating that repeated work can make both delivery and testing easier.

Start with one repeatable comparison the team already needs. Keep its inputs identified and show
what was compared. Let a colleague run it, then use their experience to improve the instructions
and output. This provides practical value while building the ability to investigate changes.

Leave the means to repeat the work in the project. A command only you know, or a comparison that
depends on your private files, keeps responsibility concentrated. An understandable example with
shared inputs gives the next colleague something they can use and maintain.

### Support the people who carry the practice

Experienced colleagues influence what the team considers normal. Invite them to review a useful
example and contribute their domain judgment. A practice supported by respected peers can become
easier for others to adopt.

Observe that influence as the team changes. A colleague's departure can remove knowledge,
support, or a familiar review pattern; a new colleague may introduce a different one. Account for
these changes when interpreting progress. Do not assume every improvement resulted from your
intervention, or every setback means a colleague stopped caring.

Shared ownership becomes observable through ordinary work. Other people update the tests when
requirements change, investigate failures, and explain why a proposed shortcut creates risk.
Ask them to take turns in those activities with appropriate support.

### Look for sustained capability

[Strategic programming](../appendix/glossary.md#strategic-programming) makes investment in design
part of delivering working behavior. In this team, that means a booking-format change includes
protection for its interpretation and a model-rule change includes evidence about the rule.
The team learns to estimate, review, and maintain that work together.

Assess both the improvement and its cost in actual delivery. The following questions help keep
the discussion grounded.

| Question | Useful evidence |
| --- | --- |
| Can colleagues change a rule with more confidence? | They can explain which cases protect it and investigate an unexpected result |
| Is routine verification easier? | Record the time spent arranging checks, running them, and resolving failures |
| Is useful work still reaching planners? | Follow completed requests and their acceptance, including time spent verifying them |
| Is responsibility spreading? | Colleagues create, review, and maintain checks instead of routing every decision through one person |

[Code coverage](../appendix/glossary.md#code-coverage), the share of code executed by tests, can show
where checks reach. [Static analysis](../appendix/glossary.md#static-analysis), inspection of source
without running it, can reveal patterns worth examining. Both are partial indicators. Neither
establishes model correctness or the business value of a delivered feature. Likewise, counting
changes tells you little about their size or usefulness.

Distinguish three observations: people follow a practice with help; people apply it independently;
and the practice continues when the original advocate becomes less involved. These require
different evidence. Gradually share review and maintenance responsibilities, then examine what
continues to work and where support is still needed.

Under deadline pressure, a team may still take a shortcut. Record the unverified behavior, its
possible consequences, and who will return to it. If the same exception keeps recurring, examine
the estimates, available time, or tools supporting the work. The goal is an improved default with
visible decisions about exceptions.

### Further reading

- Chip and Dan Heath, [_Switch: How to Change Things When Change Is Hard_](https://heathbrothers.com/books/switch/),
  2010: the change framework behind the selected applications in this section.
- Jez Humble and David Farley, [_Continuous Delivery_](https://www.informit.com/store/continuous-delivery-reliable-software-releases-through-9780321601919),
  2010: automating the delivery path and making feedback part of everyday development.

---

<a id="ch-bug-protocol"></a>

## 7. Fix a bug together

A proposal that contradicts a planning rule gives the team an immediate problem to solve. People
need to know which results can be trusted, and the team needs evidence that its correction addresses
the cause. The original author, the domain expert, and the person investigating the failure each
hold information that can help.

Treat the defect as shared work. Establish its impact, assign responsibility for the investigation,
and coordinate the response. Ask what happened and what evidence would establish a repair.
Questions about who deserves blame make that collaboration harder without supplying the missing
evidence.

### Establish the impact and reproduce the problem

In the cargo team, a scientist checking a proposed load notices that its reported weight exceeds
the capacity supplied to the model. The team retains the input and result, then reduces the case
until the failure can be understood independently.

The reduced instance has one product, A. These are its inputs:

| Input | Value |
| --- | --- |
| Weight per pallet | 2 tonnes |
| Volume per pallet | 1 cubic meter |
| Revenue per pallet | 10 units |
| Committed pallets | 0 |
| Aircraft weight capacity | 3 tonnes |
| Hold volume capacity | 2 cubic meters |

All other rules are those of the
[cargo model](../appendix/cargo_model_example.md). The returned proposal contains two pallets.
Its solver status says the problem was solved to optimality. The scientist computes the load's
weight independently and finds four tonnes.

This example is discovered during development, before its proposal is used. If a comparable
failure occurs in operational planning, first identify which proposals and decisions may be
affected and coordinate the response with their users. The
[recovery practices](../06-deployment/README.md#ch-safe-release) of Section 06 apply. Restoring
software cannot undo a physical decision already executed.

### Investigate the calculation together

The investigator runs the saved case. The scientist explains the intended capacity rule. The
original author helps trace how the model-building function creates that rule. The team can divide
those activities while keeping a shared account of the evidence.

The mistake lies in the expression used to build the weight constraint. It adds a product's weight
once and omits multiplication by its pallet count.

| Expression in this instance | What it constrains |
| --- | --- |
| Faulty: $2 \le 3$ | A constant statement that places no limit on the pallet count |
| Intended: $2x_A \le 3$ | The loaded weight |

The volume constraint still limits the count to two. With positive revenue per pallet, the faulty
model therefore selects both pallets. Its optimality status is consistent with the model it was
given. The error is in translating the business rule into that model.

That explanation identifies a cause the team can change. It also gives the original author a
constructive role: explaining the surrounding implementation and checking the correction.
Knowing who changed an expression can help reconstruct events. It does not make personal blame
a useful repair technique.

### Preserve the evidence in a test

A [regression](../appendix/glossary.md#regression) is behavior that previously worked and later
fails. A [regression test](../appendix/glossary.md#regression-test) protects a corrected behavior
against that kind of future change. Write the test before correcting the expression so the team
can demonstrate that it detects this defect.

The following test uses the reduced instance already defined in this chapter. The result contains
a proposed load and the solver status. The weight calculation in the test uses the catalogue and
returned counts directly; it does not call the model-building expression being checked.
In the pseudocode, `expect` makes the test fail when its condition is false.

<a id="pseudo-weight-capacity-regression"></a>

**Pseudocode: weight-capacity regression**

```
// pseudocode: weight-capacity-regression
public test__cargo_model__heavy_pallets__respects_weight_capacity()
    instance = the reduced input defined in this chapter
    result = solve the cargo model for instance to proven optimality
    expect result.status == optimal
    loaded_weight = sum each catalogue weight multiplied by its returned pallet count
    expect loaded_weight <= instance.weight_capacity
```

With the faulty expression, the second assertion fails because it compares four tonnes with
three. A failure to start the solver would be a different failure and would not establish this
reproduction.

Correct the expression that creates the weight constraint. For this instance, the corrected model
loads one pallet, and the test's capacity assertion passes. Run the existing checks too. During
review, temporarily restoring the faulty expression should make this test fail again, confirming
that it detects the defect being repaired.

[Pseudocode: weight-capacity regression](#pseudo-weight-capacity-regression) checks the weight rule.
It does not establish every other rule or optimality against the intended formulation; the status
assertion reports what the solver claims. Broader model tests still matter, using the independent
expectations developed in [9. Test oracles](../05-testing/README.md#ch-oracles) in Section 05.

If a [characterization test](../appendix/glossary.md#characterization-test), which records previous
behavior, also changes its result, investigate the difference. Explain which prior result was
incorrect and why the correction is acceptable. Review any changed expectation explicitly.
Keep unrelated recorded behavior protected.

### Deliver through the normal path

The correction and its test enter a [pull request](../appendix/glossary.md#pull-request), a proposal
to merge the change into the shared code. Its description states the symptom, the faulty
expression, the intended rule, and the evidence that now detects the difference.

[Continuous integration](../appendix/glossary.md#continuous-integration) automatically builds and
checks the change. [Continuous delivery](../appendix/glossary.md#continuous-delivery) keeps checked
changes ready for release through an automated path. The bug fix uses that same continuous
integration and continuous delivery (CI/CD) path as any feature, including the applicable release
assessment.

Humble and Farley's
[_Continuous Delivery_](https://www.informit.com/store/continuous-delivery-reliable-software-releases-through-9780321601919)
develops the automation that makes this process repeatable. Urgency is a reason to keep its feedback
short and its steps dependable. A slow check or manual handoff that repeatedly delays corrections
is improvement work for the delivery process.

Follow the identified version through
[3. From a tested change to a running release](../06-deployment/README.md#ch-release-path) in
Section 06. Verify the installed version and retain the case and check results with the correction.
The same path that delivers features can then provide evidence for the repair.

### Improve what allowed the defect through

After the correction, ask how the team could have noticed the missing coefficient earlier.
Perhaps review concentrated on the written formulation while the implementation assembled an
expression too large to inspect confidently. Perhaps the tests exercised a single pallet, for
which multiplying by the count would make no difference.

Choose a bounded follow-up that addresses the observed gap. Add cases that vary pallet counts,
make the relevant expression easier to review, or add independent capacity checks to the returned
proposal. Assign someone to complete the action and someone to examine its evidence. A promise to
be more careful gives future colleagues less help than a repeatable check.

This learning approach applies to ordinary software too. The published chapter
[“Postmortem Culture: Learning from Failure”](https://sre.google/sre-book/postmortem-culture/) by
John Lunney and Sue Lueder emphasizes investigating contributing conditions and following through
on improvements without indicting individuals. Here, the decision-support setting determines the
specific evidence: the business rule, its mathematical expression, and an independently checked
proposal.

Scale the follow-up to the impact. A defect caught during development may need a short explanation
and a targeted test. A failure affecting operational decisions needs a fuller account of impact,
response, and preventive actions. In both cases, keep names associated with responsibilities and
use the investigation to improve the system and the team's work.

### Check yourself

1. The solver reported optimality for the faulty model. Why did that not establish a valid proposal?
2. A test checks only a load containing one pallet. Why might it miss this defect?
3. The correction's new test passes locally. What remains before delivering the repair?

<details>
<summary>Answers</summary>

1. The status concerns the formulation supplied to the solver. That formulation omitted the pallet
   count from its weight expression.
2. For a count of one, the faulty and intended weight expressions agree. A case with a larger count
   exposes the difference.
3. Review the correction and its evidence, run the shared checks, assess relevant result changes,
   and deliver the identified version through the normal automated path. Verify it where it runs.

</details>

### Further reading

- John Lunney and Sue Lueder,
  [“Postmortem Culture: Learning from Failure”](https://sre.google/sre-book/postmortem-culture/),
  in _Site Reliability Engineering_, 2016: collaborative investigation and accountable follow-up.

---

<a id="ch-conclusion"></a>

## 8. Conclusion

Lasting improvement makes safer changes and regular investment in design a shared way of working.

- [2. Understand the inherited system and its team](#ch-brownfield): investigate the difficulty
  and the conditions that keep it in place.
- [3. Establish safety for improvement](#ch-safety): protect existing behavior before changing
  the structure, and distinguish that protection from evidence of correctness.
- [4. Give change a clear direction](#ch-direction): connect a worthwhile destination with
  specific actions colleagues can begin.
- [5. Build confidence and motivation](#ch-motivation): connect the practice with scientific
  responsibility and make successful participation achievable.
- [6. Make better practices easier to repeat](#ch-team-practices): support improvement in the
  everyday workflow and examine how responsibility spreads.
- [7. Fix a bug together](#ch-bug-protocol): collaborate on the correction, preserve the learning,
  and deliver it through the normal delivery path.

[Section 08](../08-leading-the-team/README.md) develops how leaders provide the staffing, time,
and expectations that support this work within teams and across projects.

---

[← Book contents](../../README.md) ·
[Next section: 08 Leading the team →](../08-leading-the-team/README.md)
