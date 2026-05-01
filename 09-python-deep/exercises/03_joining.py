#!/usr/bin/env python3
"""
EXERCISE 3: Joining Datasets
Join orders.csv with customers.csv on customer_id
1. Print each order with the customer's name and tier
2. Calculate total revenue per customer tier (GOLD/SILVER/BRONZE)
3. Find all orders made by GOLD tier customers
4. Write the enriched orders to a new CSV file: output/enriched_orders.csv

Run: python3 09-python-deep/exercises/03_joining.py
"""

import csv
import os

ORDERS_FILE = "09-python-deep/data/orders.csv"
CUSTOMERS_FILE = "09-python-deep/data/customers.csv"
OUTPUT_FILE = "09-python-deep/data/enriched_orders.csv"


def load_customers(file):
    """Load customers into a dict keyed by customer_id"""
    # TODO: implement
    # Hint: return {row["customer_id"]: row for row in csv.DictReader(f)}
    pass


def enrich_orders(orders_file, customers):
    """Join orders with customer data"""
    # TODO: implement
    pass


def revenue_by_tier(orders_file, customers):
    """Total revenue per customer tier"""
    # TODO: implement
    pass


def gold_customer_orders(orders_file, customers):
    """All orders from GOLD tier customers"""
    # TODO: implement
    pass


def write_enriched_csv(orders_file, customers, output_file):
    """Write enriched orders to a new CSV"""
    # TODO: implement
    # Hint: use csv.DictWriter
    pass


if __name__ == "__main__":
    customers = load_customers(CUSTOMERS_FILE)

    print("=== Enriched Orders ===")
    enrich_orders(ORDERS_FILE, customers)

    print("\n=== Revenue by Tier ===")
    revenue_by_tier(ORDERS_FILE, customers)

    print("\n=== GOLD Customer Orders ===")
    gold_customer_orders(ORDERS_FILE, customers)

    print("\n=== Writing Enriched CSV ===")
    write_enriched_csv(ORDERS_FILE, customers, OUTPUT_FILE)
    print(f"Written to {OUTPUT_FILE}")
