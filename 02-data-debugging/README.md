# 02 — Data Pipeline Debugging

The `dirty.csv` file has these intentional issues — your job is to find them all:
- Duplicate rows
- Wrong delimiter (pipe `|` instead of comma)
- Missing/empty values
- Invalid date
- Unknown status value

## Debugging Workflow (use this in interviews!)

```bash
# 1. Check row count first
wc -l data/dirty.csv

# 2. Preview the data
head -5 data/dirty.csv

# 3. Check column consistency
awk -F',' '{print NF}' data/dirty.csv | sort | uniq -c

# 4. Find duplicates
sort data/dirty.csv | uniq -d

# 5. Find empty fields
grep ",," data/dirty.csv

# 6. Find unexpected values
grep -v "success\|failed\|status" data/dirty.csv
```

## Interview Tips
- Say "I'd first check the row count and column count" — shows structured thinking
- Always verify delimiter consistency with `awk -F`
- `sort | uniq -d` is your best friend for finding duplicates
