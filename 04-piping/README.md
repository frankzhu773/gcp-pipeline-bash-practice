# 04 — Piping

Piping (`|`) passes the output of one command as input to the next. This is the most common pattern in data pipeline interviews.

## Key Patterns

```bash
# Count matches
grep "ERROR" data/pipeline_logs.txt | wc -l

# Unique values from a column
cut -d',' -f3 data/sample.csv | sort | uniq

# Top N values
cut -d',' -f4 data/sample.csv | sort -rn | head -5

# Frequency ranking (very powerful)
grep -o "INFO\|WARNING\|ERROR" data/pipeline_logs.txt | sort | uniq -c | sort -rn

# Multi-step pipeline example
cat data/dirty.csv | grep -v "^id" | cut -d',' -f5 | sort | uniq -c
```

## Think Out Loud Template (for interviews)
1. "First, I'll look at the data shape with `head` and `wc -l`"
2. "Then I'll extract the column I care about with `cut` or `awk`"
3. "Then I'll filter/sort/count with `grep`, `sort`, `uniq`"

## Interview Tips
- Build pipes step by step — don't write the whole thing at once
- Test each step before adding the next `|`
- `grep -o` extracts only the matching part, not the whole line
