# The running example

A cargo airline flies freighters on scheduled departures. Shippers want to send pallets of goods — boxed chocolate,
bottled water, cartons of laptops — and a departure can rarely carry everything that was tendered. A load planner
decides how many pallets of each product go on the aircraft.

> [!NOTE]
> This is a simplified example on purpose. A real freighter operation also constrains how the load is balanced,
> which pallets may be stacked on which, and how dangerous goods are kept apart. The subject of this book is the
> engineering around a model rather than the model itself, and a model small enough to solve by hand is what keeps
> that engineering visible.

---

## The decision

Given a cargo flight, how many pallets of each tendered product to load, so that the revenue the aircraft carries is
as large as possible, without exceeding what it can lift or what fits in the hold.

What is *not* decided here: which aircraft flies, where it flies, what a shipper is charged, and the order in which
pallets are physically placed. All those are out of the scope.

## Who uses it

A load planner, once the booking list for a departure closes. They receive a load list and are accountable for the
departure, not for the system — so they can and do change the answer before it is acted on.

## Inputs

| Input             | Description                                                                    |
|-------------------|--------------------------------------------------------------------------------|
| Booking list      | How many pallets of each product were tendered, and how many of those must fly  |
| Product catalogue | Weight, volume and revenue for one pallet of each product                       |
| Aircraft capacity | The maximum weight this aircraft may carry, and the volume of its hold          |

The following picture may help to visualize this business problem:

<p align="center">
  <img src="assets/optimization_engine_cargo_flight_selection.png" width="640"
       alt="Cargo flight optimization">
</p>

## Business rules

The following:

- A pallet is loaded whole. There is no such thing as loading part of one.
- The system never loads more pallets of a product than were tendered.
- Revenue counts only for pallets actually loaded. A pallet left behind earns nothing on this departure.
- Some shipments are committed and must fly on this departure, whatever revenue they carry: priority freight, mail,
  and parts for an aircraft grounded elsewhere.

## The model formulation

Given a booking list, a catalogue and the two capacities, the system returns either a loadable selection of pallets
that maximizes revenue, or the statement that no selection is loadable. A selection is loadable when it respects both
capacities, loads no more of a product than was tendered, and loads at least the pallets that must fly.

Let $I$ be the set of products. For each product $i \in I$, let $r_i$ be the revenue of one pallet, $w_i$ its weight
and $v_i$ its volume, all fixed, **non-negative** parameters. Let $u_i$ be the number of pallets tendered and $l_i$
the number of those that must fly, with $0 \le l_i \le u_i$. Let $W$ be the maximum weight the aircraft may carry and
$V$ the capacity of its hold. The decision variable $x_i$ is the number of pallets of product $i$ loaded.

| Symbol | Name | Unit |
|:---:|---|---|
| $r_i$ | revenue of one pallet | thousands of USD |
| $w_i$ | weight of one pallet | tonnes |
| $v_i$ | volume of one pallet | m³ |
| $u_i$ | pallets tendered | count |
| $l_i$ | pallets that must fly | count |
| $W$ | max weight | tonnes |
| $V$ | hold capacity | m³ |
| $x_i$ | pallets loaded | integer |

$$
\begin{aligned}
\max_{x} \quad & \sum_{i \in I} r_i x_i \\
\text{s.t.} \quad & \sum_{i \in I} w_i x_i \le W \\
& \sum_{i \in I} v_i x_i \le V \\
& l_i \le x_i \le u_i, \quad x_i \in \mathbb{Z}, \quad \forall i \in I
\end{aligned}
$$

The feasible region can be empty. When nothing must fly, loading nothing is always loadable, so some selection always
exists. The pallets that must fly are what removes that guarantee: if $\sum_{i \in I} w_i l_i > W$, or the same for
volume, then even the smallest permitted load exceeds a capacity and no $x$ satisfies the constraints. The instance
then has no solution at all, and a correct solver must report that rather than return some $x$ anyway. For a load
planner this is a real morning: the committed freight does not fit, and somebody has to decide what gives.

<a id="ex-two-pallet"></a>

### A two-pallet instance

| Product | Weight $w_i$ | Volume $v_i$ | Revenue $r_i$ | Must fly $l_i$ | Tendered $u_i$ |
|---|:---:|:---:|:---:|:---:|:---:|
| A — boxed chocolate | 2 | 1 | 10 | 0 | 1 |
| B — bottled water | 1 | 2 | 6 | 0 | 1 |

with $W = 2$ tonnes and $V = 2$ m³, and nothing committed to fly:

$$
\begin{aligned}
\max_{x} \quad & 10 x_A + 6 x_B \\
\text{s.t.} \quad & 2 x_A + x_B \le 2 \\
& x_A + 2 x_B \le 2 \\
& x_A, x_B \in \{0, 1\}
\end{aligned}
$$

Small enough that a person can work out the answer without a solver, which is the whole reason it exists.

## The solver

The system reaches a solver through a single operation: hand it an instance, get back a result. Which solver stands
behind that operation is not part of the contract — brute-force enumeration, a MIP solver, and a heuristic all
satisfy it, and this book swaps between them deliberately. No solver product is named anywhere in the book: a system
welded to one vendor has made a decision it did not need to make.

## The output

A load list: for each product, how many pallets to load, together with the revenue that load carries and the payload
and hold it consumes. When no selection is loadable, the output says so and carries nothing else — the other numbers
have no meaning in that case.

## Cadence and delivery

Once per departure, after the booking list closes and before loading begins: several times a day at a busy station.
The planner has minutes rather than hours, because the aircraft has a slot. How the answer reaches them is a
deployment choice, and this book does not fix one.
