# 07 — Anomaly Detection

This is the core of the HRT Data Production Engineer role: finding bad data in pipelines and tracing it to its source.

## Types of Anomalies to Know

| Type | Example | How to Detect |
|------|---------|--------------|
| Price spike | open=999999 | `awk` threshold check |
| Negative price | close=-50 | `grep` for `-` prefix |
| Missing field | `,,` in CSV | `grep ",,"` |
| Duplicate records | same timestamp+symbol | `sort \| uniq -d` |
| Row count mismatch | expected 1000, got 996 | `wc -l` vs log |
| Wrong delimiter | pipe instead of comma | `grep "\|"` |
| Invalid date | 2024-01-32 | `grep` date pattern |
| Schema drift | wrong column count | `awk '{print NF}'` |

## Key Commands

```bash
# Price spike: open > 10000
awk -F',' 'NR>1 && $3 != "" && $3+0 > 10000 {print NR, $0}' data/market_data.csv

# Negative prices
grep -E ',-[0-9]' data/market_data.csv

# Missing fields
grep ",," data/market_data.csv

# Duplicate (timestamp, symbol) pairs
cut -d',' -f1,2 data/market_data.csv | sort | uniq -d

# Row count vs log reconciliation
wc -l data/market_data.csv
grep "Expected\|loaded" data/pipeline_errors.log

# Count warnings vs errors
grep -c "WARNING" data/pipeline_errors.log
grep -c "ERROR" data/pipeline_errors.log
```

## Interview Tips
- HRT wants you to **trace anomalies back to the source** — don't just find the bad row, explain which stage introduced it
- Always reconcile row counts: source → transform → load
- "The log says 4 rows were dropped — let me find which validation step dropped them" is exactly the right thought process
