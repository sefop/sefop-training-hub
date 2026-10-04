# Section 04: Designing decision-support software

## Introduction

Decision-support software must preserve the meaning of a decision while its data sources,
mathematical formulation, solution methods, and delivery channels evolve. Replacing an optimizer can
change which guarantees are available; changing an input format can alter the mathematical instance
without changing a single constraint. Design must make these changes visible and controllable, so
that the system can continue to deliver recommendations its users can interpret correctly.

The central question is where each responsibility belongs and what its owner promises to the rest of
the program. Clear boundaries limit unnecessary dependencies. Explicit promises let a caller
distinguish an acceptable change in implementation from a change in behavior that requires a new
decision. Together they make the consequences of a change easier to understand and check.

### Out of scope

- **Writing and organizing automated tests:** the testing section develops the evidence for the
  contracts designed here; this section explains how to make the relevant inputs and outcomes
  accessible.
- **Choosing the mathematical formulation:** the cargo problem is specified in the running example;
  this section keeps its mathematics fixed while reorganizing the software around it.
- **Deployment and infrastructure:** packaging, environments, and operating the software belong in
  the deployment section; selecting dependencies and assigning deadline responsibility are design
  decisions covered here.
- **User-interface design and enterprise architecture:** screen layout and coordination across an
  entire organization require a broader treatment than this single-system example.
- **A catalogue of design patterns:** only patterns that solve a concrete problem in the example are
  introduced.

Read the chapters in order. The tangled script exposes the cost of change, and coupling and cohesion
help choose its boundaries. Contracts then establish what may cross those boundaries. Replaceable
implementations and adapters make the design executable, the cargo workflow joins the parts, and
architecture makes their dependency direction explicit. The revised
[testing section](../05-testing/README_codex.md) builds experiments around these same promises.

## Chapters

| #   | Chapter                                                             | After it you can…                                                                  |
| --- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 1   | [What design is for](#ch-design-purpose)                            | Explain why a working script can still be expensive to change.                     |
| 2   | [Choosing boundaries](#ch-forces)                                   | Group responsibilities by the knowledge they own and the changes they absorb.      |
| 3   | [Interfaces and behavioral contracts](#ch-contracts)                | Specify accepted inputs, meaningful outcomes, and guarantees.                      |
| 4   | [Replacing implementations safely](#ch-replaceable-implementations) | Supply and select implementations without silently weakening their promises.       |
| 5   | [Translating across boundaries](#ch-adapters)                       | Preserve units, identities, and result meanings through external representations.  |
| 6   | [Composing the cargo workflow](#ch-cargo-architecture)              | Assign each step a responsibility and assemble a complete recommendation path.     |
| 7   | [From components to architecture](#ch-architecture)                 | Distinguish execution flow from dependencies and choose a proportionate structure. |
| 8   | [Conclusion](#ch-conclusion)                                        | Relate controlled change, preserved meaning, and checkable responsibilities.       |

## The running example

The [cargo loading system](../appendix/running-example.md) recommends pallet quantities for one
flight. Its inputs are a booking list, a product catalogue, and aircraft capacity. Its fixed model
maximizes revenue while respecting weight and volume limits, tendered quantities, committed
quantities, and whole-pallet decisions. The load planner remains responsible for the operational
loading decision.

This section retains the base model, including the tender limit. The revised testing section
explicitly uses the
[unlimited-tender evolution](../appendix/running-example.md#ev-unlimited-tender). That evolution
changes the instance requirements and feasibility rules; it does not erase the need for the
boundaries developed here. Providers must agree on the chosen model variant before they can be
substituted for one another.

### How to read the pseudocode

Pseudocode is structured English. `class` groups state and operations; `record` groups named values;
`interface` declares operations supplied by an implementation. `implements` states which interface a
class provides. [Public and private](../appendix/glossary.md#public-and-private) mark access:
callers may use public operations, while private helpers and state remain inside their component. A
constructor creates an object and receives its initial dependencies. `absent` means that an optional
value is unavailable, not that its numerical value is zero.

Descriptions inside pseudocode, such as "check the selected load," name work owned by that
component. They do not stand for a particular solver or language library. Each example includes only
the detail needed for its argument.

### Editorial and exercise notes

This is an alternate draft with numbered chapters. Its links to the revised testing section
deliberately target `README_codex.md`. Before promotion, update the book navigation and those draft
links together. The former `ch-principles` and `ch-patterns` anchors remain as entry points into the
redistributed material, while the original section remains unchanged.

Align the shared glossary's testability and implementation-detail entries with this draft:
controllable inputs and observable outcomes support checking, but do not guarantee a cheap optimum
or make a promised runtime incidental. Add entries for signature and module when promoting the
draft; both are defined locally below. The other technical terms use existing glossary entries and
are explained where introduced.

Figure placeholders specify asset names and drawing briefs. Use a light background and the
established colors: interfaces blue, implementations orange, and clients and records green. Class
diagrams use simplified
[Unified Modeling Language](../appendix/glossary.md#unified-modeling-language): `+` means public,
`-` means private, and a hollow arrowhead points from an implementing class to its interface.

Exercise maintenance notes identify follow-up work for the separate Python and Java repositories.
They describe proposed changes, not exercises implemented by this draft. Keep the same behavior in
both languages and use topic names rather than chapter numbers for exercise packages.

---

<a id="ch-design-purpose"></a>

## 1. What design is for

A program that answers today's question has value. If the question recurs, the team must also be
able to change how the answer is obtained without losing what already works. The difficulty is that
a small request can require understanding much more code than the behavior being changed.

### A working calculation becomes a recurring service

An operations research scientist can reasonably begin with one script: read the data, construct a
model, solve it, and inspect the answer. The arrangement keeps an exploratory calculation close at
hand. As colleagues start relying on repeated runs, new obligations appear: input errors need a
response, a stopped search needs an honest outcome, and the delivered result must identify the
decision it concerns.

Software design is the set of choices about how this work is divided and connected. Those choices
exist even when everything stays in one function. They determine how much a person must understand
to make the next change.

### The tangled script

[Pseudocode: tangled script](#pseudo-tangled-script) gathers the recurring cargo workflow into one
function. It acknowledges that a stopped solve may have different outcomes, but gives one place
responsibility for interpreting all of them as well as reading and writing external records.

<a id="pseudo-tangled-script"></a>

**Pseudocode: tangled script**

```
// pseudocode: tangled-script
public plan_flight_load(source_files, requested_flight, output_file)
    read booking, product, and aircraft rows from source_files
    select the records for requested_flight
    reject missing fields, duplicate identifiers, and invalid quantities
    convert the declared source units to the model's units
    if the committed load exceeds a capacity:
        write a proven-infeasible outcome to output_file
        return
    create a model using the solver library
    add the specified variables, constraints, and objective
    solve with a 60-second search limit
    inspect termination status and solution availability
    if a usable candidate exists:
        extract and check whole-pallet quantities and totals
        write the load and its quality label to output_file
    otherwise:
        write the appropriate no-plan or failure outcome to output_file
```

A solver library is software used to construct and solve optimization problems. Its records and
operations need interpretation before they can become information a planner should act on. The
pseudocode names that interpretation without teaching its numerical details yet.

### Five changes that reveal the design

Consider requests that leave the mathematical model unchanged:

1. Bookings arrive from a web service instead of a local file.
2. Catalogue weights arrive in kilograms rather than tonnes.
3. The output needs a different file format, including for unsuccessful runs.
4. The team needs to replace its solver library while preserving the promised outcomes.
5. A scientist needs to exercise the committed-load check without reading files or running a solve.

All five lead back to the same function. A change in the output format affects several branches. A
unit conversion sits beside formulation construction, so a reviewer must distinguish mathematical
edits from representational ones. The committed-load calculation is entangled with external reading
and writing even though the arithmetic needs neither of them.

The problem is not the function's length alone. It is the mixture of knowledge a change requires:
external formats, cargo rules, solver operations, and delivered wording. Splitting the same function
into arbitrary shorter pieces would not necessarily reduce that mixture.

### The payoff and its limits

[Modularity](../appendix/glossary.md#modularity) means organizing the program around clear
boundaries so that parts can be understood and changed with limited knowledge of the others.
[Testability](../appendix/glossary.md#testability) concerns how readily their behavior can be
checked. Explicit inputs and observable outcomes help; a hard optimization problem can remain
expensive even behind an excellent boundary.

The design goal is to limit unnecessary consequences and make necessary consequences explicit. A new
source format should not force a change in the objective. A genuine change to the decision rules may
rightly affect input requirements, optimization, and acceptance of the delivered load. A good design
reveals that scope rather than promising to confine every change to one file.

---

<a id="ch-forces"></a>

## 2. Choosing boundaries

When a change requires understanding unrelated decisions, those decisions are too closely entangled.
The useful question is which knowledge should stay together and which dependencies can be removed.
Two established concepts, coupling and cohesion, give that question a precise vocabulary.

### Coupling: what a change can disturb

[Coupling](../appendix/glossary.md#coupling) describes dependence between parts. If report
generation asks the solver's model object for each variable value, the report depends on the
solver's representation. Replacing the solver can then require changes in report generation even
though the report's meaning has not changed.

The goal is appropriate dependence, not zero dependence. A report must depend on what a load means.
It does not need to depend on which numerical library produced that load. Reducing coupling means
retaining the first relationship while removing the second.

### Cohesion: what belongs together

[Cohesion](../appendix/glossary.md#cohesion) describes how closely the work inside a part belongs
together. All paths that write the external output format share knowledge of that format. Grouping
them under one writer means a format change has an identifiable owner, whether the run produced a
candidate, established infeasibility, or failed.

Grouping by a vague label such as `utilities` does not provide that ownership. A unit conversion,
solver selector, and file writer can all be useful without belonging in the same component. Their
shared usefulness says nothing about why they would change together.

### Reasons for change

The [single responsibility principle](../appendix/glossary.md#single-responsibility-principle) asks
a component to serve one coherent responsibility, often described as one reason to change. Here
"reason" means a related source of requirements, not one executable action. A reader can open a
file, parse records, and report malformed syntax while still owning one external representation.

For the cargo script, a first responsibility map is:

| Knowledge                                      | Owner          | A change it should absorb                        |
| ---------------------------------------------- | -------------- | ------------------------------------------------ |
| External input layout                          | Reader         | A field is renamed in the source format          |
| Input meaning and normalization                | Preprocessing  | A supported weight unit changes                  |
| Mathematical instance and optimization outcome | Optimization   | A compatible solution method is replaced         |
| Acceptable delivered recommendation            | Postprocessing | A quality label must become more explicit        |
| External output layout                         | Writer         | The plan is delivered in a different file format |

This map is a proposal to evaluate, not a command to create exactly five classes. Some
responsibilities may start as functions in one module. What matters is whether their inputs and
outputs let their owners change independently.

<a id="fig-forces-responsibility-boundaries"></a>

**Figure: responsibility boundaries**

> **Figure placeholder:** `assets/forces-responsibility-boundaries.svg`. Show the tangled script as
> actions colored by responsibility, then regroup those same actions into the five owners in the
> table. Highlight all output-format actions together. Do not add testing layers or architecture
> rings; the figure teaches grouping and dependence.

### Owning knowledge without scattering it

[Don't repeat yourself](../appendix/glossary.md#dont-repeat-yourself) means giving each piece of
authoritative knowledge one maintained definition. If kilograms are converted to tonnes in several
unrelated production paths, one path may be updated while another keeps the old assumption. A named
normalization operation gives that decision a home.

The rule does not require every expression that looks alike to share one function. Nor should an
independent scientific check blindly call the calculation it is meant to scrutinize. Production
ownership and independent evidence serve different purposes. Sharing data definitions can preserve
meaning while separately deriving a check from the written requirement.

### Public behavior and private helpers

An operation that another component needs should be public at the chosen boundary. Its internal
steps can remain private. [Pseudocode: preprocessing boundary](#pseudo-preprocessing-boundary)
exposes preparation as a complete responsibility, while keeping its detailed decomposition inside
the component.

<a id="pseudo-preprocessing-boundary"></a>

**Pseudocode: preprocessing boundary**

```
// pseudocode: preprocessing-boundary
class Preprocess
    public run(source_data) returns PreparedRequest
        reject_invalid_records(source_data)
        instance = normalize(source_data)
        return the instance with its request identity and committed-load assessment

    private reject_invalid_records(source_data)
    private normalize(source_data) returns Instance
```

A caller can supply ordinary records and observe the prepared result without using a file or solver.
It need not call a private committed-load helper. Changing how the preparation is divided internally
should not force callers to change.

### When splitting stops helping

Each boundary has a cost: another concept to name, a representation to agree on, and a connection to
maintain. Extract a part when it owns meaningful knowledge, provides an independently useful
operation, or separates a likely source of change. One-line helpers can improve readability, but
they do not automatically deserve public interfaces.

### Further reading

- David L. Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules," _Communications
  of the ACM_, 1972: choosing boundaries around information that other modules should not need to
  know.
- John Ousterhout, _A Philosophy of Software Design_, Yaknyam Press, 2018: reducing complexity
  through useful modules whose interfaces conceal substantial internal work.

**Exercise maintenance notes:** Use a transformation of the tangled script that preserves its
observable outcomes. Ask learners to identify the knowledge owned by each extracted part. Expose
`Preprocess.run` for the committed-load exercise rather than requiring direct calls to a private
helper. Keep the mathematics and model variant unchanged.

---

<a id="ch-principles"></a> <a id="ch-contracts"></a>

## 3. Interfaces and behavioral contracts

Separating two parts creates an obligation to say how they cooperate. A caller needs more than the
name of an operation and the shape of its return value: it needs to know what a successful result
means and what other outcomes are possible. Without that agreement, separation merely moves the
uncertainty to a boundary.

### The operation and the promise

An [interface](../appendix/glossary.md#interface) lists the operations a component offers. A
signature describes one operation's name, parameters, and return type. A
[contract](../appendix/glossary.md#contract) adds accepted inputs, promised behavior, and error
meanings. `run(instance, policy) returns SolveResult` is a signature; it does not by itself promise
feasibility, truthful revenue, or optimality.

[Information hiding](../appendix/glossary.md#information-hiding) keeps implementation decisions
behind that agreement. A caller can rely on the guarantee without knowing how the component keeps
it. The algorithm and solver-specific objects can stay hidden. Whether a returned candidate is
proven optimal cannot stay hidden if the caller needs that fact to decide whether to publish it.

### The instance is a mathematical input

For the bounded-tender cargo model, an `Instance` contains a finite collection of uniquely
identified products and the aircraft's capacities. Each product has weight, volume, revenue,
tendered quantity, and committed quantity. Weights, volumes, revenues, and capacities are finite and
nonnegative; quantities are integers with $0\le l_i\le u_i$. Required fields and identifiers must be
present. Units are tonnes, cubic meters, and thousands of US dollars, as defined in the running
example.

These assumptions make the problem well defined. A negative tender quantity is malformed input.
Commitments that exceed aircraft capacity describe a valid but infeasible instance. Rejecting the
first and establishing the second are different operations with different meanings for a caller.

The request's flight and source-snapshot identifiers travel with the instance in a
`PreparedRequest`. A snapshot means the fixed set of source records used for this request, so
records changing during the run cannot silently change which question the answer concerns. The
mathematical calculation need not interpret flight identifiers; the surrounding workflow must
preserve their association with its input and result.

### A candidate is not the whole outcome

Returning either a load or nothing erases information. A stopped computation might have proved
infeasibility, found no candidate yet, or failed to execute normally. A returned load might be
optimal or merely feasible. Use outcomes that express these distinctions in the application's
vocabulary:

| Status       | Candidate | Meaning                                                                                 |
| ------------ | --------- | --------------------------------------------------------------------------------------- |
| `optimal`    | Required  | Candidate is feasible and optimality is established under the declared numerical policy |
| `feasible`   | Required  | Candidate is feasible; optimality has not been established                              |
| `infeasible` | Absent    | No feasible solution exists for the supplied instance                                   |
| `unresolved` | Absent    | Search stopped without a candidate or a proof of infeasibility                          |
| `failed`     | Absent    | Execution did not complete normally                                                     |

These are application outcomes, not a copy of every status offered by a numerical library. The
implementation translates the library's information into this vocabulary. Malformed input raises
`InvalidInput` separately.

<a id="pseudo-solve-result"></a>

**Pseudocode: optimization outcome**

```
// pseudocode: solve-result
record Solution
    picked                         // product identifier -> whole-pallet quantity, including zero
    objective_value                // thousands of US dollars
    total_weight                   // tonnes
    total_volume                   // cubic meters

record SolveResult
    status                         // optimal, feasible, infeasible, unresolved, failed
    solution                       // present only for optimal or feasible
    upper_bound                    // optional valid upper bound on maximum revenue
    termination_reason             // explanation in application vocabulary

interface SolutionProvider
    public solve(instance, policy) returns SolveResult
        // reject malformed input with InvalidInput
        // return quantities keyed by every input product identifier
        // report outcomes and numerical guarantees truthfully
```

[Pseudocode: optimization outcome](#pseudo-solve-result) separates the candidate from information
about the solve. The optional bound and explanation are meaningful to clients that assess quality;
an absent bound is not zero. An `infeasible` outcome is a claim requiring justification, not a
default label for an empty result.

### Numerical and quality promises

Every candidate must respect the supplied instance and report its objective and resource totals
truthfully. An `optimal` result additionally satisfies the declared optimality criterion. State
numerical conventions explicitly: how nearly integral solver values are converted, which
discrepancies are accepted, and how optimality is assessed. Those conventions form part of the
contract because changing them can change which load or quality label is accepted.

An upper bound can communicate how much improvement remains possible without exposing search nodes
or internal data structures. A solver log, in contrast, is usually diagnostic material. Whether
information belongs in the interface depends on what callers need, not on whether it originated
inside a solver.

Several loads may tie. Unless the contract defines a tie-breaking rule, a replacement may return a
different valid load with the same optimal value. Preserving behavior means preserving the stated
promises, not reproducing an incidental choice by the previous implementation.

### The optimization result and the delivered plan

`SolveResult` describes the answer to a mathematical instance. `LoadPlan` describes an accepted
recommendation for a particular flight and snapshot, with quantities, units, totals, and an honest
quality label. A no-plan outcome has no `LoadPlan`; it carries a reason the user can act on. These
records serve different callers and should not be collapsed into a boolean named `feasible`.

An [abstraction](../appendix/glossary.md#abstraction) is useful when it hides work while preserving
the distinctions its clients need. Hiding the solver's model object achieves that. Hiding the
difference between " none exists" and "none was found" defeats it.

### Check yourself

1. A provider stops at its time limit with a valid load and no proof of optimality. What may it
   report?
2. A different provider returns a different tied optimum. Has substitution necessarily changed the
   contract?
3. The aircraft cannot carry its committed freight. Is the instance malformed?

<details>
<summary>Answers</summary>

1. `feasible`, with the candidate and an accurate termination explanation; not `optimal` without the
   required evidence.
2. No. The contract allows either optimum unless it promises a particular tie-breaking rule.
3. Not merely for that reason. With valid fields and quantities, it is an infeasible instance and
   should be reported as such.

</details>

**Exercise maintenance notes:** Use the same `Solution` and `SolveResult` field names as the revised
testing exercises. Keep the bounded-tender input contract here and name the unlimited-tender variant
explicitly when moving to Section

5.  Add examples of malformed input, proven infeasibility, and unresolved search so the records
    carry useful meaning before learners write their implementations.

---

<a id="ch-patterns"></a> <a id="ch-replaceable-implementations"></a>

## 4. Replacing implementations safely

Once callers agree on a promise, several implementations may be able to keep it. That flexibility is
valuable only when replacing one implementation preserves the behavior its callers require. An
identical operation name cannot compensate for an incompatible guarantee.

### Compatibility includes behavior

The [Liskov substitution principle](../appendix/glossary.md#solid) says that an implementation must
be usable wherever its [interface](../appendix/glossary.md#interface) is expected, without violating
the interface's [contract](../appendix/glossary.md#contract). In practical terms, it must accept the
promised inputs and keep the promised guarantees. Requiring positive weights would violate a
contract that accepts the base model's zero-weight products, even if that implementation works
perfectly on its preferred inputs.

The same reasoning applies to quality. A [heuristic](../appendix/glossary.md#heuristic) seeks useful
solutions without a general optimality guarantee. It cannot replace an implementation whose promised
behavior is always to produce a proven optimum for every supported feasible case. It can implement a
broader outcome contract that permits a feasible candidate, provided it respects every constraint
and reports its evidence honestly.

Separate two decisions: which outcomes a provider can truthfully return, and which outcomes the
application will accept for delivery. If a request requires a proven optimum, receiving `feasible`
is an unsuccessful attempt to meet that request, not permission to lower the quality requirement. An
algorithm-selection rule must respect that policy.

### Make application policy depend on its own interface

A [dependency](../appendix/glossary.md#dependency) is something a component relies on to do its
work. If application policy directly creates a vendor model and reads vendor status codes, the
policy depends on that vendor's vocabulary. Moving those operations behind `SolutionProvider` lets
the policy request an outcome in its own terms.

This is [dependency inversion](../appendix/glossary.md#dependency-inversion-principle): the
application defines the interface it needs, and the concrete implementation depends on that
definition. The application need not import the implementation's library or its model objects.

For example, Gurobi is a commercial optimization solver. A `MipProviderGurobi` constructs the cargo
[mixed-integer program](../appendix/glossary.md#mixed-integer-program), abbreviated MIP, through
that library and translates its result. [Pseudocode: solver provider](#pseudo-solver-provider) shows
the boundary without teaching the library's operations.

<a id="pseudo-solver-provider"></a>

**Pseudocode: solver provider**

```
// pseudocode: solver-provider
class MipProviderGurobi implements SolutionProvider
    public solve(instance, policy) returns SolveResult
        build the bounded-tender cargo formulation with the solver library
        apply the supported stopping and numerical policy
        execute the solve
        translate status, candidate availability, and valid bound information
        convert and check any candidate before constructing Solution
        return the corresponding SolveResult
```

The provider owns exception translation as well: an execution error produces `failed` with an
explanation. Malformed input remains `InvalidInput`. Neither is evidence of mathematical
infeasibility. It may keep logs for diagnosis without making every caller understand the log format.

<a id="fig-replaceable-implementations-provider"></a>

**Figure: the provider dependency**

> **Figure placeholder:** `assets/replaceable-implementations-provider.svg`. Draw `Optimization`
> calling `SolutionProvider`, with `+ solve(instance, policy)` on the interface. Put
> `MipProviderGurobi` below it with a hollow implementation arrow pointing upward. Show its separate
> dependency on the solver library. Distinguish the caller's use of the interface from the
> implementation's use of the vendor library.

### Supply dependencies from outside

Depending on an interface is only part of the separation. If `Optimization` still constructs
`MipProviderGurobi` inside `run`, that operation still knows the concrete choice. Instead, give it
the configured providers from outside. This is
[dependency injection](../appendix/glossary.md#dependency-injection).

[Pseudocode: supplied providers](#pseudo-supplied-providers) shows `Optimization` receiving those
objects. A program with one configured provider simply supplies a one-element collection; it does
not need automatic selection.

<a id="pseudo-supplied-providers"></a>

**Pseudocode: supplied providers**

```
// pseudocode: supplied-providers
class Optimization
    private providers

    public constructor(providers)
        keep providers

    public run(instance, policy) returns SolveResult
        provider = choose(instance, policy)
        return provider.solve(instance, policy)

    private choose(instance, policy) returns SolutionProvider
        select a configured provider compatible with the instance and requested policy
```

`choose` does not build a provider or alter the request's quality requirements. Unsupported
configuration should be rejected explicitly, ideally before a live request begins. The configured
implementations must support the chosen model variant and the required input domain.

The [composition root](../appendix/glossary.md#composition-root) is the place where the program
constructs concrete objects and connects them. A simple entry function can do this; a
dependency-injection framework is unnecessary. Supplying dependencies also makes controlled
experiments possible: the caller can receive a prepared implementation without changing the
production operation it exercises.

### Select an algorithm only when selection is needed

The [strategy pattern](../appendix/glossary.md#strategy-pattern) puts interchangeable algorithms
behind a shared interface. It is one [design pattern](../appendix/glossary.md#design-pattern), a
named solution to a recurring design problem. The relevant problem here is choosing among compatible
ways to produce an optimization outcome.

Enumeration can be practical for a bounded collection of small cases. A mathematical solver may
handle a wider range. A heuristic may be useful when acceptable candidates matter more than a proof
within the available budget. Those are possible roles, not a universal progression from small to
medium to large. Instance structure, input domain, available implementations, quality requirements,
and empirical runtime all affect the choice.

A simple selection policy might use enumeration for explicitly bounded cases it is known to handle,
a configured solver for other exact-search requests, and a heuristic only when the request permits
its guarantees. Stopping an exact method early does not turn the resulting candidate into a proven
optimum. The result must retain the outcome actually established.

<a id="fig-replaceable-implementations-strategies"></a>

**Figure: compatible optimization strategies**

> **Figure placeholder:** `assets/replaceable-implementations-strategies.svg`. Extend the provider
> class diagram with `EnumerationProvider`, `MipProviderGurobi`, and `GreedyProvider` implementing
> `SolutionProvider`. Show `Optimization` receiving providers and policy. Annotate selection with
> "compatible inputs and guarantees" rather than universal size thresholds. Show `- providers`,
> `- choose`, `+ constructor(providers)`, and `+ run`. Draw the constructor receiving existing
> provider objects to make dependency injection explicit.

### Extend a design without promising that nothing changes

The [open-closed principle](../appendix/glossary.md#solid) encourages adding implementations without
rewriting stable clients. With this boundary, a new compatible provider can leave postprocessing and
output formatting untouched. Configuration and selection policy may still require changes. Adding a
class does not by itself establish that the new provider meets the contract.

[Interface segregation](../appendix/glossary.md#solid) asks callers to depend only on the operations
they need. A writer should receive a delivered outcome, not a solver controller with operations for
changing algorithms. A publication policy may legitimately need a quality bound even when a simple
file writer does not. Small interfaces should follow these actual needs; they should not erase
information that a decision requires.

### Further reading

- Robert C. Martin, _Agile Software Development: Principles, Patterns, and Practices_, Prentice
  Hall, 2002: substitution, dependency inversion, and the other principles used to assess designs
  with replaceable objects.
- Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, _Design Patterns: Elements of
  Reusable Object-Oriented Software_, Addison-Wesley, 1994: strategy and other recurring
  arrangements of cooperating objects.
- Mark Seemann and Steven van Deursen, _Dependency Injection Principles, Practices, and Patterns_,
  Manning, 2019: constructing dependencies and keeping their configuration outside application
  behavior.

**Exercise maintenance notes:** Use `Optimization.run(instance, policy)` as the outer component
boundary and `SolutionProvider.solve(instance, policy)` for its implementation dependency. Supply a
one-element provider collection before adding a selection exercise. Include a provider that returns
a feasible candidate honestly and one that incorrectly labels it optimal, so learners distinguish
sharing a signature from satisfying a contract. Treat provider selection thresholds as
exercise-specific assumptions, not optimization theory.

---

<a id="ch-adapters"></a>

## 5. Translating across boundaries

Two representations can refer to the same cargo and still disagree about its meaning. A value of
2,000 might denote kilograms in a catalogue and tonnes in a model. A row position might change while
its product identity must remain fixed. Designing a translation means deciding which meaning has to
survive, not merely moving values between fields.

### Reading a format and interpreting its values

An [adapter](../appendix/glossary.md#adapter-pattern) translates between an external representation
and the [interface](../appendix/glossary.md#interface) expected by the application. A reader for
comma-separated values (CSV) knows column names, separators, and the source's record structure. A
reader for JavaScript Object Notation (JSON) knows field names and document structure. Both produce
the same application-owned source records.

Keep the distinction between syntax and meaning explicit. The reader checks that it can obtain the
required fields and represents a weight together with its declared unit. Preprocessing checks
supported units and normalizes the values into the mathematical instance. If a particular external
source has a fixed undocumented convention, its adapter must make that convention explicit rather
than leave downstream code to guess.

<a id="pseudo-source-readers"></a>

**Pseudocode: source readers**

```
// pseudocode: source-readers
interface SourceReader
    public read(request) returns SourceData

class CsvSourceReader implements SourceReader
    private source_locations

    public read(request) returns SourceData
        read the requested snapshot from source_locations
        select the requested flight's booking and capacity records
        attach the relevant catalogue records with their declared units
        return SourceData preserving flight, snapshot, and product identifiers

class JsonSourceReader implements SourceReader
    private source_address

    public read(request) returns SourceData
        obtain the requested snapshot from source_address
        interpret the document's fields under the documented source format
        return the same SourceData structure for the requested flight
```

Both operations in [Pseudocode: source readers](#pseudo-source-readers) reject a missing or
ambiguous requested record rather than substituting a different flight. `SourceData` belongs to the
application and contains no file handle, web response object, or vendor-specific row type. Access
errors remain distinguishable from invalid records.

<a id="fig-adapters-source-readers"></a>

**Figure: two source formats, one input meaning**

> **Figure placeholder:** `assets/adapters-source-readers.svg`. Draw the `SourceReader` interface
> and its two implementations using simplified class notation. Each implementation receives its own
> external format; both return `SourceData`. Label identifiers and declared units on that record.
> Keep normalization outside the readers in this diagram, matching the responsibilities chosen in
> the text.

### Normalize units without changing the decision

A catalogue entry for A can contain weight 2,000 kilograms, volume 1,000 liters, and revenue 10,000
dollars. The model entry contains 2 tonnes, 1 cubic meter, and 10 thousand dollars for the same
pallet. These are changes in representation, not changes in the load's properties or economic value.

Normalize the capacities under the same unit policy and preserve the original source values where
they are needed to explain or check a delivered result. An unsupported or missing unit is an input
error. Treating it as the expected unit would manufacture a mathematical instance whose relationship
to the source is unknown.

The conversion belongs in a named operation whose [contract](../appendix/glossary.md#contract)
states both sides of the translation. It can live in a small function; the important design choice
is explicit ownership, not a separate class for each arithmetic step.

### Keep identifiers attached to quantities

Suppose optimization returns one pallet of A and zero of B. If presentation sorts products by
revenue or name, it must move each quantity with its product identifier. Associating the first
quantity with the first displayed row after sorting creates a different recommendation.

Represent selected quantities as a map from stable product identifier to quantity. Do not rely on
array position across independently transformed collections. Keep flight and source-snapshot
identity with the request as it passes through the workflow. The numerical solver can use private
indices internally, but its provider must restore the declared identifiers when it constructs the
result.

### Translate numerical results before exposing candidates

A numerical solver may represent a whole-pallet decision by a value very close to an integer. The
provider owns conversion from that representation into the integer quantities promised by
`Solution`. Define the conversion tolerance, reject materially fractional or nonfinite values, and
recompute feasibility and totals after conversion. The production component performing this work is
`CandidateTranslator`.

For example, a raw quantity of `1.9999998` might be converted to 2 under a declared integrality
rule. Whether 2 pallets fit is a separate question requiring the instance's constraints, including
tender and commitments. Conversion does not authorize exceeding a capacity. If the candidate cannot
satisfy the promised acceptance rules, the provider reports a computation failure with that
explanation rather than claiming the problem is infeasible.

Postprocessing owns the next translation: from an accepted mathematical result to the delivered
recommendation. It preserves quantities and quality information, chooses the required labels and
presentation units, and checks the delivered form against its acceptance rules. If no quantities
change, it need not perform a second rounding step.

### Translate meanings, not just status names

Mapping vendor status codes is more than renaming strings. A stop at the search limit may accompany
a valid candidate or no candidate. Those cases produce `feasible` and `unresolved`, respectively,
unless stronger evidence establishes another outcome. A numerical or execution failure must not
become a message that no feasible load exists.

The output adapter has a different responsibility: serialize the application's delivery outcome into
a file or response. It should not infer optimality from a nonempty load list or decide whether a
result is acceptable. Those decisions must already be expressed in the record it receives.

### Where the translation stops

Changing kilograms to tonnes preserves the mathematical problem. Adding a new constraint on a
selected combination of cargo changes the problem. Such a change cannot generally be implemented as
input cleanup: it must be represented in the optimization rules and respected by every compatible
provider and delivered-load check.

This is why the distinction between representation and decision rules matters to design. A
well-separated adapter can absorb a source-format change. It cannot make a substantive model change
disappear.

**Exercise maintenance notes:** Add parallel source examples using the same records in two formats.
Preserve units and identifiers explicitly, then normalize in preprocessing. Include a row-reordering
example and a numerical candidate-conversion example. The design exercise establishes ownership; the
Section 05 exercises check those behaviors through the corresponding public boundaries. Do not make
the expected test result call the production conversion helper it is intended to scrutinize.

---

<a id="ch-cargo-architecture"></a>

## 6. Composing the cargo workflow

Individually understandable parts still need an agreement about the whole request. Someone must
decide which source records belong to the flight, what to do with an unproven candidate, and whether
a result arrived in time to be useful. Those responsibilities cannot be left to whichever component
happens to encounter the situation first.

### One request, one identifiable decision

A request contains a flight identifier, a source-snapshot identifier, and a delivery deadline. Its
source data contains the selected bookings, catalogue entries, and aircraft capacities. The
request's quality policy states whether a feasible unproven load is acceptable and which numerical
rules apply.

The workflow preserves this association through every step. A `SolveResult` belongs to the
particular instance passed to the provider. In a synchronous workflow, keeping that association in
one request is straightforward; do not substitute global variables such as "the current flight" that
another request could change.

`PlanFlightLoad` owns the application decision: prepare the instance, obtain an optimization result,
and turn it into an accepted delivery outcome. It receives ordinary records rather than opening
files. The input reader and output writer own the external communication around it.

### Assign the promises before connecting the parts

An [interface](../appendix/glossary.md#interface) becomes useful when its
[contract](../appendix/glossary.md#contract) makes responsibility clear. The following table defines
the important boundaries of the assembled design:

| Part               | Receives                                                    | Promises                                                                                             |
| ------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `SourceReader`     | Request identifying flight and source snapshot              | Selected source records with declared units and identities, or a defined read/input error            |
| `Preprocess`       | Source records                                              | Valid normalized instance and source association, with any established commitment infeasibility      |
| `Optimization`     | Instance and supported search policy                        | A truthful `SolveResult` for that instance through a compatible provider                             |
| `SolutionProvider` | Instance and policy                                         | Construction/search/result translation consistent with the mathematical and numerical contract       |
| `Postprocess`      | Request, prepared data, solve result, and acceptance policy | A delivery outcome with an accepted plan or an accurate no-plan reason                               |
| `PlanWriter`       | Delivery outcome and publication deadline                   | A complete correctly represented artifact, or an explicit delivery failure; no late plan publication |
| `PlanFlightLoad`   | Request, source data, and policy                            | Correct coordination of preparation, optimization, and result acceptance                             |

The reader rejects malformed syntax and missing requested records; preprocessing rejects invalid
field meanings and inconsistent quantities. `PreparedRequest` retains the normalized instance,
flight and snapshot identifiers, the relevant source values, and an optional `infeasible_reason`. No
data source is reread during postprocessing.

The committed-load assessment follows directly from the fixed model. If $x=l$ exceeds weight or
volume capacity, every permitted load does too. Otherwise $x=l$ is feasible because valid inputs
already satisfy $l_i\le u_i$. This precheck can establish infeasibility without a solver; it is
specific to these rules and assumptions.

For clarity, preprocessing retains all participating product identifiers. An optimization
implementation may remove products it can prove will have zero quantity, but it must restore those
zero entries when returning a candidate. That reduction is optional, and it cannot discard committed
cargo or change the problem's meaning.

### Make outcome handling part of the application

A `DeliveryOutcome` contains the request identity, a status, an optional `LoadPlan`, and an
explanation. Its plan is present only when postprocessing accepts a candidate under the request's
policy. It preserves the optimization quality status rather than inferring quality from the
existence of a load.

If unproven feasible loads are accepted, a `feasible` candidate can become a plan with that label.
If the request requires proven optimality, the same candidate produces a no-plan outcome explaining
the unmet requirement. Proven infeasibility, unresolved search, and execution failure retain their
distinct meanings. Invalid source input is reported as `invalid_input` at the delivery boundary, not
inserted into the solver's mathematical outcomes.

Postprocessing also rejects an inconsistent provider result, such as an unknown product identifier
or a candidate that fails the delivered-load rules. That is a failed computation or translation, not
proof of infeasibility. The policy for this example does not publish a candidate recovered from an
execution failure.

### Give the deadline an owner

A solver's search limit covers only part of the request. Reading, normalization, checking, and
writing also take time. `PlanFlightLoad` receives a clock, an ordinary component whose public
`now()` operation returns the current time. It can compute how much time remains and reserve a
budget for postprocessing and delivery.

If no search time remains, it returns a deadline outcome without starting a solve. Restricting the
search budget does not weaken a required quality guarantee. If a valid baseline is part of the
supported policy, it may be used under that policy; otherwise an unmet search or quality requirement
remains an honest no-plan outcome.

`PlanWriter` owns the final publication check because completing the computation does not itself
deliver a plan. It prepares the entire artifact before making it visible as the completed result and
refuses to release a plan after the deadline. A computation-side time check alone would leave a gap
in which writing could finish late. Actual timing guarantees require appropriate runtime support and
measurement; assigning ownership makes that requirement explicit rather than proving it will always
be met.

### Assemble the application behavior

[Pseudocode: plan flight load](#pseudo-plan-flight-load) puts these responsibilities together.
Record constructors such as `deadline_outcome(request)` mean creation of a delivery record with no
plan and the given request identity. They are not external output operations.

<a id="pseudo-plan-flight-load"></a>

**Pseudocode: plan flight load**

```
// pseudocode: plan-flight-load
class PlanFlightLoad
    private preprocess, optimization, postprocess, clock

    public constructor(preprocess, optimization, postprocess, clock)
        keep preprocess, optimization, postprocess, and clock

    public run(request, source_data, policy) returns DeliveryOutcome
        if clock.now() >= request.deadline:
            return deadline_outcome(request)
        require source_data flight and snapshot identifiers to match request
        prepared = preprocess.run(source_data)

        if prepared.infeasible_reason is present:
            result = SolveResult(status=infeasible, solution=absent, upper_bound=absent,
                                 termination_reason=prepared.infeasible_reason)
        otherwise:
            search_budget = remaining time after reserving the policy's delivery budget
            if search_budget <= 0:
                return deadline_outcome(request)
            search_policy = policy with its search budget restricted to search_budget
            result = optimization.run(prepared.instance, search_policy)

        if clock.now() >= request.deadline:
            return deadline_outcome(request)
        return postprocess.run(request, prepared, result, policy)
```

The identity requirement raises `InvalidInput` on a mismatch. Invalid input and invalid-candidate
errors are translated by the application entry point into delivery outcomes; the former becomes
`invalid_input`, the latter `failed` with the failing stage recorded. Read or write failures remain
communication failures with that stage identified. These paths do not claim that a mathematical
problem is infeasible.

The [composition root](../appendix/glossary.md#composition-root) supplies the concrete dependencies.
It uses the same [dependency injection](../appendix/glossary.md#dependency-injection) arrangement
introduced earlier. [Pseudocode: assembled cargo application](#pseudo-assembled-cargo-application)
shows the normal request path; its entry-point error handler applies the translations just
described.

<a id="pseudo-assembled-cargo-application"></a>

**Pseudocode: assembled cargo application**

```
// pseudocode: assembled-cargo-application
public start_program(settings, request)
    clock = SystemClock()
    reader = CsvSourceReader(settings.source_locations)
    provider = MipProviderGurobi()
    optimization = Optimization(providers=[provider])
    application = PlanFlightLoad(Preprocess(), optimization, Postprocess(), clock)
    writer = CsvPlanWriter(settings.output_location, clock)

    source_data = reader.read(request)
    outcome = application.run(request, source_data, settings.policy)
    receipt = writer.publish(outcome, deadline=request.deadline)
    report the actual delivery result from receipt
```

`SystemClock` reads the execution environment's time; `CsvPlanWriter` implements the `PlanWriter`
interface from the responsibility table. A delivery receipt distinguishes completed publication, a
refused late plan, and a write failure. If delivery fails, a separate reporting path informs the
caller; success must not be inferred merely from the existence of a candidate in memory. An old
artifact keeps its own request identity and is never relabeled as the new result. Informational
no-plan or failure notices can be reported after the deadline, but they are not late plans.

### Follow one recommendation through the boundaries

Use the [two-product example](../appendix/running-example.md#ex-two-pallet): flight `F-101` has room
for 2 tonnes and 2 cubic meters. One pallet of each product is tendered and none is committed. A
earns more than B, and the capacities prevent taking both. The unique optimum is one A and zero B.

| Boundary           | Representation of this request                                                                     |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| Source records     | `F-101`, snapshot `S-1`; A weighs 2,000 kilograms, occupies 1,000 liters, and earns 10,000 dollars |
| Prepared instance  | A has weight 2, volume 1, revenue 10, tender 1, and commitment 0 in the declared model units       |
| Provider result    | `optimal`, quantities `{A: 1, B: 0}`, revenue 10, weight 2, and volume 1                           |
| Accepted plan      | Same quantities and quality, associated with `F-101` and `S-1`, expressed in delivery units        |
| Published artifact | Complete load list and totals, delivered under that request identity before its deadline           |

Product B and the capacities undergo the same defined unit conversion. Each transformation has a
stated owner, and each resulting record can be inspected without exposing the solver's internal
model. A wrong recommendation can therefore be investigated at the boundary where its meaning first
changed.

<a id="fig-cargo-architecture"></a>

**Figure: the cargo request and its records**

> **Figure placeholder:** `assets/cargo-architecture-request-records.svg`. Draw the reader,
> `PlanFlightLoad`, and writer in execution order. Expand `PlanFlightLoad` into preprocessing,
> optimization, and postprocessing, and show `SolutionProvider` behind optimization. Label the
> crossing records `SourceData`, `Instance`, `SolveResult`, and `DeliveryOutcome`. Carry a visible
> flight/snapshot tag around the mathematical calculation to the output. Show no-plan outcomes
> reaching the writer without inventing an empty load as a replacement.

### Where the original changes now land

| Requested change                           | Main owner                                                | Agreement that must remain intact                             |
| ------------------------------------------ | --------------------------------------------------------- | ------------------------------------------------------------- |
| Read from a web service                    | A new `SourceReader` implementation and configuration     | Same source identities and declared meanings                  |
| Accept a different source weight unit      | Normalization in preprocessing                            | Same physical quantities in the mathematical instance         |
| Write a different output format            | A new `PlanWriter` implementation and configuration       | Same delivered decision and outcome wording                   |
| Replace the solver library                 | A new `SolutionProvider` implementation and configuration | Same model, input domain, and reported guarantees             |
| Exercise the committed-load check directly | Public `Preprocess.run` boundary                          | Same preparation behavior without file or solver dependencies |

The boundaries make the scope of each change inspectable. They do not remove the need to check the
new adapter or provider. Compatible signatures and well-drawn diagrams remain design intentions
until implementations keep their promises.

**Exercise maintenance notes:** Mirror this component vocabulary in Section 05: `Optimization` is
the component under test, `SolutionProvider` is its algorithm dependency, and `CandidateTranslator`
handles numerical extraction inside a numerical provider. Expand the old `BookingReader` role into
`SourceReader` to cover catalogue and capacity records explicitly. Add a supplied clock and a writer
receipt to workflow exercises. Keep a bounded-tender worked request here and identify the deliberate
variant change in the testing exercises.

---

<a id="ch-architecture"></a>

## 7. From components to architecture

The assembled workflow explains what happens during a request. It does not yet explain which parts
must know about which other parts in order to be written and maintained. Confusing those two
relationships can preserve a working pipeline while leaving the application tightly dependent on its
external tools.

### Execution flow and dependency direction

[Software architecture](../appendix/glossary.md#software-architecture) concerns the large structural
decisions about a system's parts and their relationships, especially decisions that are costly to
reverse. One such decision is the direction of dependencies: which definitions a part imports or
otherwise relies on.

At runtime, `Optimization` calls a provider and the provider calls a numerical library. In the
source structure, `Optimization` needs only the application-owned `SolutionProvider` definition. The
concrete provider depends on both that definition and the numerical library. Calling a concrete
object during execution does not require the caller to name its concrete class.

This distinction is [dependency inversion](../appendix/glossary.md#dependency-inversion-principle)
at system scale. It allows the workflow to use an external capability while keeping the external
vocabulary out of the workflow's own rules. The composition code knows the concrete classes because
selecting and assembling them is its job.

### Place policy and mechanisms deliberately

[Clean architecture](../appendix/glossary.md#clean-architecture) is one way to organize this
separation. It groups domain records and rules at the center, application workflows around them,
adapters farther out, and external tools at the boundary. Its dependency rule is that inner code
must not depend on outer implementation definitions.

For this cargo application, the groups can be described concretely:

| Group                            | Contains                                                                                        | Must not require                                    |
| -------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Domain records and rules         | Product and quantity meanings, instance rules, solution and plan meanings                       | File formats, solver objects, or web response types |
| Application behavior             | `PlanFlightLoad`, preprocessing, postprocessing, optimization coordination, required interfaces | Concrete readers, writers, and solver libraries     |
| Implementations at the boundary  | Source readers, plan writers, solver-dependent providers, system clock                          | Knowledge leaking back into application callers     |
| External facilities and assembly | File system, web client, numerical library, program entry and configuration                     | Ownership of the application's decision policy      |

Ordinary internal functions may be implemented directly without an interface for every operation.
Interfaces are particularly valuable where the application needs an external capability or genuinely
replaceable behavior. The groups describe dependency constraints; they do not require separate
services or independently deployed programs.

<a id="fig-architecture-dependency-direction"></a>

**Figure: execution and dependency direction**

> **Figure placeholder:** `assets/architecture-execution-dependencies.svg`. Use two panels with the
> same three elements: application caller, provider interface, and concrete solver provider. One
> panel shows the runtime call reaching the concrete provider; the other shows source dependencies
> pointing toward the application-owned interface, with a separate arrow from the concrete provider
> to the numerical library. Use distinct arrow styles and a legend. Add the reader and writer only
> if doing so keeps the direction readable.

### The formulation and the solver-dependent provider

The mathematical rules are central to the system's meaning. Their implementation through a
particular numerical library can still belong in an outer provider. Architectural placement
describes dependence on mechanisms, not the business importance of the work.

`MipProviderGurobi` therefore belongs at the implementation boundary when it directly uses that
library. Its [interface](../appendix/glossary.md#interface), input record definitions, and result
meanings remain owned by the application. The mathematical specification remains explicit and
independently reviewable rather than being defined only by the calls made to the library.

Keeping formulation construction and solver calls together can be a reasonable local choice.
Splitting them would require a useful representation to pass between them; building a general
modeling layer solely to satisfy a diagram may cost more than it saves. A solver replacement may
then require reimplementing formulation construction inside the new provider. That is a real
tradeoff, not a one-line migration, even though the workflow and output adapter can remain
unchanged.

If several implementations repeatedly need the same independently useful construction operation, an
additional boundary may earn its cost. The criterion is whether it simplifies actual
responsibilities and changes, not whether every box can be made smaller. A provider may also have
focused internal construction checks alongside checks of its external result; information hiding
does not forbid scrutinizing its implementation.

### Keep source dependencies visible

A useful review asks whether `PlanFlightLoad` names a vendor model class, whether a domain record
contains a file handle, or whether postprocessing inspects a numerical library's status code. Each
would cross a boundary the design intends to protect. Moving such an object through a generic
container does not remove the dependence if callers still need to understand it.

Conversely, a plain `SolveResult` containing a valid bound is not automatically a leak. The bound
expresses useful mathematical information in the application's vocabulary. The distinction is
whether the caller depends on a meaningful promise or on the particular machinery used to obtain it.

### Use the smallest structure that carries the responsibilities

A small program can implement this design as a few modules in one process. A module is simply a
named grouping of code with a boundary; it need not be a service or a class hierarchy. The rules
concern what those groups know and what they promise, not how many folders the repository contains.

Begin with the readers, transformations, optimization boundary, and writer the actual workflow
needs. Add runtime strategy selection when there are multiple useful implementations. Add a new
abstraction when it gives a caller a stable, meaningful operation or isolates a real source of
change. Extra interfaces without such a purpose add agreements to maintain without necessarily
reducing complexity.

### Further reading

- Robert C. Martin, _Clean Architecture: A Craftsman's Guide to Software Structure and Design_,
  Prentice Hall, 2017: dependency direction, application policy, and separation from external
  mechanisms.
- David L. Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules," _Communications
  of the ACM_, 1972: an alternative starting point for evaluating boundaries by the knowledge they
  conceal.

**Exercise maintenance notes:** Ask learners to draw both execution flow and source dependencies for
the same assembled program. Keep the solver-dependent provider outside application policy, and make
all vendor-specific imports belong to that implementation. Compare the cost of replacing that
provider with the cost of changing the delivered format; do not promise that implementing a new
solver is a one-line task.

---

<a id="ch-conclusion"></a>

## 8. Conclusion

A changeable decision-support system preserves the meaning of a recommendation while allowing the
machinery that produces it to evolve. That requires boundaries and promises together. A boundary
without a clear promise merely moves ambiguity between components; a promise without a boundary
leaves its callers exposed to the implementation's unrelated decisions.

The design developed here makes responsibility follow meaning. Source representations have owners,
the mathematical instance has explicit assumptions, the optimization outcome records what was
actually established, and publication has its own acceptance rules. This division allows a change to
be assessed by the agreements it preserves or alters. Changing a representation can stay local when
its meaning is preserved. Changing a guarantee must be visible to the parts whose decisions rely on
it.

This is also the connection between modularity and confidence. Isolating a solver library makes
replacement possible; preserving the provider's contract makes replacement acceptable. Supplying a
dependency from outside makes a behavior controllable; exposing a meaningful outcome makes it
observable. Neither property establishes correctness by itself, but together they make precise
evidence possible without forcing every question through the entire application.

The result is a way to reason about change rather than a prescribed number of classes or rings. The
team can ask which responsibility changed, which agreement crosses its boundary, and which
surrounding decisions depend on that agreement. A small design that answers those questions clearly
is more useful than an elaborate structure that leaves them implicit. The next section turns these
agreements into experiments that check whether the software keeps them.

---

[← Book contents](../../README.md) ·
[Next section: Testing decision-support software →](../05-testing/README_codex.md)
