# 05 — Python Data Manipulation

HRT uses a modern Python data stack for data production work. Expect to write Python to clean, validate, and summarize datasets.

## Key Patterns

```python
import csv
from collections import defaultdict

# Read CSV as dicts
with open("data/sample.csv") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["amount"])

# Filter rows
with open("data/sample.csv") as f:
    failed = [r for r in csv.DictReader(f) if r["status"] == "failed"]

# Find duplicates
seen = set()
with open("data/market_data.csv") as f:
    for row in csv.DictReader(f):
        key = (row["timestamp"], row["symbol"])
        if key in seen:
            print(f"Duplicate: {key}")
        seen.add(key)

# Detect missing values
with open("data/market_data.csv") as f:
    for i, row in enumerate(csv.DictReader(f), 2):
        if any(v.strip() == "" for v in row.values()):
            print(f"Row {i} missing data")

# Aggregate with defaultdict
from collections import defaultdict
totals = defaultdict(list)
with open("data/market_data.csv") as f:
    for row in csv.DictReader(f):
        totals[row["symbol"]].append(float(row["close"] or 0))
```

## Interview Tips
- HRT asks you to clean and validate data similar to financial feeds (price spikes, missing values, duplicates)
- Know `csv.DictReader` well — cleaner than index-based access
- `defaultdict(list)` is your go-to for grouping/aggregating
- Always handle empty strings before casting to `float()`
