#!/usr/bin/env python3
"""
EXERCISE 1: Data Validation Pipeline
File: dirty_orders.csv has several issues. Your job:
1. Find all rows with missing fields
2. Find rows where quantity is not a valid integer
3. Find rows with negative prices
4. Find rows with price spikes (> 100000)
5. Find rows with invalid region (only EAST/WEST/NORTH/SOUTH allowed)
6. Find duplicate order_ids

Run: python3 09-python-deep/exercises/01_validation.py
"""

import csv

FILE = "09-python-deep/data/dirty_orders.csv"
VALID_REGIONS = {"EAST", "WEST", "NORTH", "SOUTH"}


def find_missing_fields(file):
    """Find rows where any field is empty"""
    # TODO: implement
    pass


def find_invalid_quantity(file):
    """Find rows where quantity is not a valid integer"""
    # TODO: implement
    # Hint: try int(row["quantity"]) inside a try/except
    pass


def find_invalid_prices(file):
    """Find rows with negative price or price > 100000"""
    # TODO: implement
    pass


def find_invalid_regions(file):
    """Find rows where region is not in VALID_REGIONS"""
    # TODO: implement
    pass


def find_duplicate_orders(file):
    """Find duplicate order_ids"""
    # TODO: implement
    pass


if __name__ == "__main__":
    print("=== Missing Fields ===")
    find_missing_fields(FILE)

    print("\n=== Invalid Quantity ===")
    find_invalid_quantity(FILE)

    print("\n=== Invalid Prices ===")
    find_invalid_prices(FILE)

    print("\n=== Invalid Regions ===")
    find_invalid_regions(FILE)

    print("\n=== Duplicate Orders ===")
    find_duplicate_orders(FILE)
