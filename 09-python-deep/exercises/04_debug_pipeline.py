#!/usr/bin/env python3
"""
EXERCISE 4: Debug This Pipeline
This pipeline reads dirty_orders.csv, validates it, and produces a summary.
It has 6 bugs. Find and fix them all.

Run: python3 09-python-deep/exercises/04_debug_pipeline.py
Expected output when fixed:
  Valid rows: 9
  Invalid rows: 6
  Total revenue (valid orders): 14249.67
  Top region: EAST
"""

import csv
from collections import defaultdict

FILE = "09-python-deep/data/dirty_orders.csv"
VALID_REGIONS = {"EAST", "WEST", "NORTH", "SOUTH"}


def load_orders(file):
    orders = []
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            orders.append(row)
    return orders


def validate_orders(orders):
    valid = []
    invalid = []

    seen_ids = {}

    for i, row in enumerate(orders, 2):

        # Bug 1: this check never catches empty customer_id
        if row["customer_id"] == None:
            invalid.append((i, row, "missing customer_id"))
            continue

        # Bug 2: this will crash on non-integer quantity instead of flagging it
        quantity = int(row["quantity"])
        if quantity <= 0:
            invalid.append((i, row, "invalid quantity"))
            continue

        # Bug 3: price check is wrong — it flags valid prices, not invalid ones
        price = float(row["unit_price"])
        if price > 0 and price < 100000:
            invalid.append((i, row, "invalid price"))
            continue

        # Bug 4: region check is incorrect
        if row["region"] in VALID_REGIONS:
            invalid.append((i, row, "invalid region"))
            continue

        # Bug 5: duplicate check never works
        order_id = row["order_id"]
        if order_id not in seen_ids:
            invalid.append((i, row, "duplicate order_id"))
            continue
        seen_ids[order_id] = i

        valid.append(row)

    return valid, invalid


def summarize(valid, invalid):
    print(f"Valid rows: {len(valid)}")
    print(f"Invalid rows: {len(invalid)}")

    total_revenue = 0
    region_revenue = defaultdict(float)

    for row in valid:
        revenue = float(row["quantity"]) * float(row["unit_price"])
        total_revenue += revenue
        region_revenue[row["region"]] += revenue

    # Bug 6: this will crash — wrong way to find max in a dict
    top_region = max(region_revenue)

    print(f"Total revenue (valid orders): {total_revenue:.2f}")
    print(f"Top region: {top_region}")


if __name__ == "__main__":
    orders = load_orders(FILE)
    valid, invalid = validate_orders(orders)
    summarize(valid, invalid)
