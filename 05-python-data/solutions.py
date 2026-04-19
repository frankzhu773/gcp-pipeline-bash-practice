#!/usr/bin/env python3
"""SOLUTIONS: Python Data Manipulation"""

import csv
from collections import defaultdict

DATA_FILE = "data/market_data.csv"
SAMPLE_FILE = "data/sample.csv"


def exercise1_read_csv():
    with open(SAMPLE_FILE) as f:
        for row in csv.DictReader(f):
            print(row)


def exercise2_filter_failed():
    with open(SAMPLE_FILE) as f:
        failed = [r for r in csv.DictReader(f) if r["status"] == "failed"]
    for row in failed:
        print(row)


def exercise3_find_missing():
    with open(DATA_FILE) as f:
        for i, row in enumerate(csv.DictReader(f), 2):
            if any(v.strip() == "" for v in row.values()):
                print(f"Row {i} has missing values: {row}")


def exercise4_price_anomalies():
    with open(DATA_FILE) as f:
        for i, row in enumerate(csv.DictReader(f), 2):
            open_price = row["open"].strip()
            if open_price == "":
                print(f"Row {i}: missing open price — {row['symbol']} @ {row['timestamp']}")
            else:
                price = float(open_price)
                if price > 10000:
                    print(f"Row {i}: spike detected — {row['symbol']} open={price}")
                elif price < 0:
                    print(f"Row {i}: negative price — {row['symbol']} open={price}")


def exercise5_find_duplicates():
    seen = {}
    with open(DATA_FILE) as f:
        for i, row in enumerate(csv.DictReader(f), 2):
            key = (row["timestamp"], row["symbol"])
            if key in seen:
                print(f"Duplicate at row {i}: {key} (first seen at row {seen[key]})")
            else:
                seen[key] = i


def exercise6_avg_close_by_symbol():
    totals = defaultdict(list)
    with open(DATA_FILE) as f:
        for row in csv.DictReader(f):
            if row["close"].strip():
                totals[row["symbol"]].append(float(row["close"]))
    for symbol, prices in sorted(totals.items()):
        print(f"{symbol}: avg close = {sum(prices)/len(prices):.2f}")


if __name__ == "__main__":
    print("=== Exercise 1 ==="); exercise1_read_csv()
    print("\n=== Exercise 2 ==="); exercise2_filter_failed()
    print("\n=== Exercise 3 ==="); exercise3_find_missing()
    print("\n=== Exercise 4 ==="); exercise4_price_anomalies()
    print("\n=== Exercise 5 ==="); exercise5_find_duplicates()
    print("\n=== Exercise 6 ==="); exercise6_avg_close_by_symbol()
