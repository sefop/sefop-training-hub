# Section 07: Working with legacy decision-support software

<a id="ch-introduction"></a>

## 1. Introduction

An inherited decision-support system already holds useful knowledge: business rules, modeling
choices, and behavior its users depend on. You need to extend or repair it while preserving that
value. Yet a change can be difficult to understand, difficult to test, and difficult to agree on
with the colleagues who maintain it. A [legacy system](../appendix/glossary.md#legacy-system) is one
that is difficult to change safely.

Those difficulties have both technical and cultural causes. Improving the software requires
understanding the decisions and working conditions that shaped it, and what keeps those practices
in place today. Lasting improvement changes both the software and the way the team works.

### Ideas to develop

- **Destination: shared [strategic programming](../appendix/glossary.md#strategic-programming).**
  The team invests in design while delivering working behavior, so that future changes remain
  manageable. Build on
  [2. What design is for](../04-design/README.md#ch-design-purpose) in Section 04. Success means safer
  changes become a shared, repeatable practice, with responsibility spreading beyond the original
  advocate. Adoption under guidance and independent expertise are different achievements.
- **Several paths lead to legacy.** Investigate knowledge gaps, delivery pressure, changing
  expectations, professional identity, and informal norms. Repeated
  [tactical programming](../appendix/glossary.md#tactical-programming), prioritizing the current task
  while deferring design improvements, is one route. People on the same team may face different
  barriers; explore those barriers with them before choosing an intervention.
- **A practitioner with some support and limited authority.** The reader can demonstrate better
  practices and help colleagues adopt them, while recognizing when more support is needed.
  [Section 08](../08-leading-the-team/README.md) develops leadership at different levels of
  authority, staffing, incentives, training strategy, and adoption across projects.
- **A brief technical foundation.** Draw on Michael Feathers,
  [_Working Effectively with Legacy Code_](https://www.informit.com/store/working-effectively-with-legacy-code-9780132931779),
  for stabilization before improvement: representative protection for existing behavior and
  reliable feedback on changes. Keep the detailed technical methods in that book and Section 05.
- **Change management supplies the central framework.** Use selected strategies from Chip and Dan
  Heath's [_Switch: How to Change Things When Change Is Hard_](https://heathbrothers.com/books/switch/).
  Organize them around giving clear direction (Rider), building motivation (Elephant), and improving
  the working environment (Path). Develop original applications to this setting.
- **Examples from decision-support software.** Use plausible fictional situations involving model
  rules, uncertain results, changes to inputs, and delivery commitments. Show how technical safety
  can reduce fear, working examples can make a practice approachable, and shared workflows can help
  colleagues repeat it. Identify general software practices as such.
- **Bug fixing as a shared learning opportunity.** Focus the team on repairing the defect and
  improving its safeguards. Investigate decisions constructively, without personal blame, and keep
  responsibility for the response clear. Preserve what the team learns in a test and deliver the
  correction through the same checks and automated release path as a feature. Automation and short
  feedback loops make that response faster.
- **Agents assist stabilization.** Mention their potential to help investigate code and draft tests,
  while retaining review and verification. Link to Section 09 for practical depth.
- **Assess progress realistically.** Look for shared use and maintenance of safer practices.
  Examine whether they persist as the original advocate's involvement decreases. Expect occasional
  shortcuts under pressure and make their consequences explicit.

### Chapters

| # | Chapter | After it you can… | Status |
| :-: | --- | --- | --- |
| 1 | [Introduction](#ch-introduction) | State the section's purpose and the reader's room to act | Draft |
| 2 | [Understand the inherited system and its team](#ch-brownfield) | Investigate what makes change difficult and what keeps existing practices in place | Draft |
| 3 | [Establish safety for improvement](#ch-safety) | Define a bounded stabilization effort that enables further changes | Draft |
| 4 | [Give change a clear direction](#ch-direction) | Help colleagues understand the improvement and the actions it requires | Draft |
| 5 | [Build confidence and motivation](#ch-motivation) | Connect better practices with colleagues' concerns and professional responsibilities | Draft |
| 6 | [Make better practices easier to repeat](#ch-team-practices) | Establish workflows that support shared strategic programming | Draft |
| 7 | [Fix a bug together](#ch-bug-protocol) | Combine collaborative investigation, a verified correction, and the normal delivery pipeline | Draft |
| 8 | [Conclusion](#ch-conclusion) | Connect technical safety with a shared way of improving the system | Draft |

This section assumes the testing foundations of [Section 05](../05-testing/README.md) and the
delivery practices of [Section 06](../06-deployment/README.md). The chapter bodies below record the
agreed scope; their detailed explanations and examples remain to be developed.

---

<a id="ch-brownfield"></a>

## 2. Understand the inherited system and its team

Define a [legacy system](../appendix/glossary.md#legacy-system) by the difficulty of changing it
safely, then develop how to investigate its history, current purpose, and barriers to improvement.
Connect [tactical programming](../appendix/glossary.md#tactical-programming), prioritizing the
current task while deferring design improvements, with accumulated difficulty, while considering
other causes. Examine colleagues' knowledge, working conditions, priorities, and professional
responsibilities to understand why existing practices continue.

---

<a id="ch-safety"></a>

## 3. Establish safety for improvement

Develop a brief stabilization approach grounded in Feathers. Introduce
[characterization tests](../appendix/glossary.md#characterization-test): tests that record existing
behavior and reveal unintended changes to it. Distinguish preserving behavior from establishing
its correctness, and define enough protection to begin controlled improvements. Mention agent
assistance here, with a link to [Section 09](../09-ai-assisted-development/README.md).

---

<a id="ch-direction"></a>

## 4. Give change a clear direction

Develop selected Rider strategies from Switch around the planning and understanding needed for
change. Help colleagues see a concrete problem, a worthwhile destination, and specific actions they
can take. Use decision-support examples to show how a working demonstration gives someone a starting
point.

---

<a id="ch-motivation"></a>

## 5. Build confidence and motivation

Develop selected Elephant strategies from Switch around motivation and confidence. Address fear
of breaking the system, uncertainty about learning a new practice, and whether engineering belongs
in a scientist's work. Connect improvements with confidence in model behavior and shared
accomplishment, using examples that can motivate change before an operational failure.

---

<a id="ch-team-practices"></a>

## 6. Make better practices easier to repeat

Develop selected Path strategies from Switch around the conditions in which people work.
Explore working examples, constructive review, shared expectations, and automation that reduce the
effort of repeating safer practices. Connect these changes with the release path in
[3. From a tested change to a running release](../06-deployment/README.md#ch-release-path) in Section
06, and assess how responsibility becomes shared.

---

<a id="ch-bug-protocol"></a>

## 7. Fix a bug together

Develop a fictional cargo-planning defect as a worked example of the section's approach. Show a
team investigating and repairing the problem together, capturing its learning in a test, and
delivering the correction through its normal pipeline. Draw on Humble and Farley's
[_Continuous Delivery_](https://www.informit.com/store/continuous-delivery-reliable-software-releases-through-9780321601919)
for the repeatable, automated delivery process. Connect the example with the technical and cultural
strategies developed earlier.

---

<a id="ch-conclusion"></a>

## 8. Conclusion

Lasting improvement connects technical safety with a shared way of working.

- [2. Understand the inherited system and its team](#ch-brownfield): investigate both the current
  difficulties and the conditions that keep them in place.
- [3. Establish safety for improvement](#ch-safety): protect existing behavior so controlled changes
  can begin.
- [4. Give change a clear direction](#ch-direction): make the problem, destination, and next actions
  concrete.
- [5. Build confidence and motivation](#ch-motivation): help colleagues connect the improvement with
  work they value.
- [6. Make better practices easier to repeat](#ch-team-practices): support shared
  [strategic programming](../appendix/glossary.md#strategic-programming), investing in design as the
  system evolves, through the everyday workflow.
- [7. Fix a bug together](#ch-bug-protocol): collaborate on the correction, preserve the learning,
  and use the normal delivery pipeline.

[Section 08](../08-leading-the-team/README.md) develops how leaders support and extend these
practices within teams and across projects.

---

[← Book contents](../../README.md) ·
[Next section: 08 Leading the team →](../08-leading-the-team/README.md)
