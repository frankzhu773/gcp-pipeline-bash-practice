#!/usr/bin/env python3
"""
EXERCISE 2: Aggregation
File: orders.csv (clean data)
1. Calculate total revenue per category
2. Calculate total revenue per region
3. Find the top 3 best selling products by quantity
4. Find the customer who spent the most
5. Calculate average order value per region

Revenue = quantity * unit_price

Run: python3 09-python-deep/exercises/02_aggregation.py
"""

import csv
from collections import defaultdict

FILE = "09-python-deep/data/orders.csv"


def revenue_by_category(file):
    """Total revenue per category"""
    # TODO: implement
    pass


def revenue_by_region(file):
    """Total revenue per region"""
    # TODO: implement
    pass


def top_products_by_quantity(file, n=3):
    """Top N products by total quantity sold"""
    # TODO: implement
    pass


def top_spending_customer(file):
    """Customer who spent the most total"""
    # TODO: implement
    pass


def avg_order_value_by_region(file):
    """Average order value (quantity * price) per region"""
    # TODO: implement
    pass


if __name__ == "__main__":
    print("=== Revenue by Category ===")
    revenue_by_category(FILE)

    print("\n=== Revenue by Region ===")
    revenue_by_region(FILE)

    print("\n=== Top 3 Products by Quantity ===")
    top_products_by_quantity(FILE)

    print("\n=== Top Spending Customer ===")
    top_spending_customer(FILE)

    print("\n=== Avg Order Value by Region ===")
    avg_order_value_by_region(FILE)
