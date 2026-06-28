# code_smell.py — "Long Method" / "God Function" Example
#
# CODE SMELL: A "long method" (also called a "god function") is a function
# that does far too many unrelated things. It's the software equivalent of
# writing a paper where the introduction, model formulation, computational
# experiments, and conclusions are all one giant unbroken paragraph.
#
# You'll recognize this smell because:
#   - You need to scroll just to read a single function
#   - You can't test one part without running everything else
#   - Changing one step (e.g., the file format) forces you to edit
#     code that's tangled with unrelated steps (e.g., the optimizer)
#
# The function below is intentionally bad — study it, then we'll refactor it.

import csv
import json
import math


def optimize():
    # -------------------------------------------------------------------------
    # STEP 1: Load demand data from a CSV file
    # -------------------------------------------------------------------------
    # Already we're doing I/O (input/output) inside the optimizer. If you ever
    # want to test the optimizer logic itself, you're forced to have a file on
    # disk first. This creates an invisible dependency.

    demands = []
    with open("demand.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            demands.append({
                "node": row["node"],
                "demand": float(row["demand"]),
                "priority": int(row["priority"]),
            })

    # -------------------------------------------------------------------------
    # STEP 2: Load network configuration from a JSON file
    # -------------------------------------------------------------------------
    # Now we're loading a second file, in a completely different format.
    # The function is already doing two different I/O jobs. Notice how far
    # we are from the "optimization" part — we haven't even started yet.

    with open("network_config.json", "r") as f:
        config = json.load(f)

    capacity = config["capacity"]
    fixed_cost = config["fixed_cost"]
    variable_cost = config["variable_cost"]
    num_facilities = config["num_facilities"]

    # -------------------------------------------------------------------------
    # STEP 3: Preprocess — clean, validate, and transform raw data
    # -------------------------------------------------------------------------
    # Data wrangling is a completely separate responsibility from optimization.
    # If the CSV format changes (e.g., "demand_kg" instead of "demand"),
    # you have to hunt for that logic buried inside the optimizer function.

    # Remove nodes with zero or negative demand
    demands = [d for d in demands if d["demand"] > 0]

    # Normalize demands so they sum to 1 (useful for some formulations)
    total_demand = sum(d["demand"] for d in demands)
    for d in demands:
        d["demand_normalized"] = d["demand"] / total_demand

    # Sort by priority so high-priority nodes are served first
    demands.sort(key=lambda d: d["priority"], reverse=True)

    # Build a simple distance proxy using node index (placeholder logic)
    for i, d in enumerate(demands):
        d["distance_proxy"] = math.sqrt(i + 1)

    # -------------------------------------------------------------------------
    # STEP 4: Set up the optimizer (greedy heuristic)
    # -------------------------------------------------------------------------
    # The "optimizer" here is a greedy heuristic — it assigns each demand node
    # to a facility one at a time, always picking the cheapest available slot.
    # A real version might call scipy, PuLP, or Gurobi here.
    #
    # Notice: we're now four conceptual steps in, all inside one function.
    # A reader who just wants to understand the algorithm has to wade through
    # CSV parsing and JSON loading to get here.

    facilities = [
        {"id": i, "remaining_capacity": capacity, "assigned": []}
        for i in range(num_facilities)
    ]

    total_cost = 0.0
    unserved = []

    # -------------------------------------------------------------------------
    # STEP 5: Run the optimizer — the core logic
    # -------------------------------------------------------------------------
    # This is the part that actually matters scientifically, but it's tangled
    # with everything else. If you want to swap this for a different algorithm,
    # you have to copy-paste or rewrite the entire 100+ line function.

    for demand_node in demands:
        best_facility = None
        best_cost = float("inf")

        for facility in facilities:
            if facility["remaining_capacity"] >= demand_node["demand"]:
                # Cost = fixed cost (amortized) + variable cost * distance proxy
                cost = (fixed_cost / num_facilities) + \
                       variable_cost * demand_node["distance_proxy"] * demand_node["demand"]

                if cost < best_cost:
                    best_cost = cost
                    best_facility = facility

        if best_facility is not None:
            best_facility["assigned"].append(demand_node["node"])
            best_facility["remaining_capacity"] -= demand_node["demand"]
            total_cost += best_cost
        else:
            # Demand could not be served — capacity exhausted
            unserved.append(demand_node["node"])

    # -------------------------------------------------------------------------
    # STEP 6: Postprocess — compute summary statistics
    # -------------------------------------------------------------------------
    # Back to data wrangling, but now at the end. This is a third distinct
    # responsibility mixed into the same function. Changing the reporting
    # format means editing the same function as the algorithm.

    num_served = sum(len(f["assigned"]) for f in facilities)
    utilization = [
        1 - (f["remaining_capacity"] / capacity) for f in facilities
    ]
    avg_utilization = sum(utilization) / len(utilization) if utilization else 0
    service_rate = num_served / len(demands) if demands else 0

    # -------------------------------------------------------------------------
    # STEP 7: Write results to a TXT file
    # -------------------------------------------------------------------------
    # And now we're back to I/O — a fourth distinct responsibility.
    # The function started by reading files and ends by writing files,
    # with an algorithm sandwiched in between. None of these pieces
    # can be reused, tested, or replaced independently.

    with open("results.txt", "w") as f:
        f.write("=== Optimization Results ===\n\n")
        f.write(f"Total cost:          {total_cost:.2f}\n")
        f.write(f"Nodes served:        {num_served} / {len(demands)}\n")
        f.write(f"Service rate:        {service_rate:.1%}\n")
        f.write(f"Avg utilization:     {avg_utilization:.1%}\n")

        if unserved:
            f.write(f"\nUnserved nodes ({len(unserved)}):\n")
            for node in unserved:
                f.write(f"  - {node}\n")

        f.write("\nFacility assignments:\n")
        for facility in facilities:
            assigned_str = ", ".join(facility["assigned"]) or "(none)"
            f.write(f"  Facility {facility['id']}: {assigned_str}\n")

    # -------------------------------------------------------------------------
    # END OF FUNCTION
    # -------------------------------------------------------------------------
    # You just read ~130 lines of a single function.
    # It does 7 different jobs. It is impossible to:
    #   - Unit-test the optimizer without creating real files
    #   - Reuse the preprocessing logic elsewhere
    #   - Swap the output format without touching the algorithm
    #   - Read the algorithm without first reading the I/O boilerplate
    #
    # This is the long method smell. Next, we'll refactor it.

    print("Done. Results written to results.txt.")


if __name__ == "__main__":
    optimize()
