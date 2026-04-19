#!/usr/bin/env python3
"""
EXERCISES: Python Data Manipulation
HRT uses Python heavily for data production work.
Run: python3 05-python-data/exercises.py
"""

import csv
from collections import defaultdict
from datetime import datetime

DATA_FILE = "data/market_data.csv"
SAMPLE_FILE = "data/sample.csv"


# ==============================
# EXERCISE 1: Read and print CSV
# ==============================
# TODO: Read sample.csv using the csv module and print each row
# Hint: use csv.DictReader so columns are named

def exercise1_read_csv():
    pass  # replace with your solution


# ==============================
# EXERCISE 2: Filter rows
# ==============================
# TODO: Read sample.csv and return only rows where status == 'failed'

def exercise2_filter_failed():
    pass


# ==============================
# EXERCISE 3: Detect missing values
# ==============================
# TODO: Read market_data.csv and print rows where any field is empty

def exercise3_find_missing():
    pass


# ==============================
# EXERCISE 4: Detect price anomalies
# ==============================
# TODO: Read market_data.csv and flag rows where:
#   - open price > 10000 (clearly wrong spike)
#   - open price < 0 (negative price)
#   - open price is missing

def exercise4_price_anomalies():
    pass


# ==============================
# EXERCISE 5: Find duplicates
# ==============================
# TODO: Read market_data.csv and detect rows with duplicate (timestamp, symbol)

def exercise5_find_duplicates():
    pass


# ==============================
# EXERCISE 6: Summarize by symbol
# ==============================
# TODO: Read market_data.csv and compute average close price per symbol

def exercise6_avg_close_by_symbol():
    pass


if __name__ == "__main__":
    print("=== Exercise 1: Read CSV ===")
    exercise1_read_csv()

    print("\n=== Exercise 2: Filter failed rows ===")
    exercise2_filter_failed()

    print("\n=== Exercise 3: Find missing values ===")
    exercise3_find_missing()

    print("\n=== Exercise 4: Price anomalies ===")
    exercise4_price_anomalies()

    print("\n=== Exercise 5: Duplicates ===")
    exercise5_find_duplicates()

    print("\n=== Exercise 6: Avg close by symbol ===")
    exercise6_avg_close_by_symbol()
