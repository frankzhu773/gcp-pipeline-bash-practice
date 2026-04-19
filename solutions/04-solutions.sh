#!/bin/bash
# SOLUTIONS: Piping

DATA="data/sample.csv"
LOGS="data/pipeline_logs.txt"

echo "=== Exercise 1: Count error lines ==="
grep "ERROR" $LOGS | wc -l

echo "=== Exercise 2: Unique dates ==="
cut -d',' -f3 $DATA | sort | uniq

echo "=== Exercise 3: Top 3 amounts ==="
cut -d',' -f4 $DATA | sort -rn | head -3

echo "=== Exercise 4: Count failed records ==="
grep "failed" $DATA | wc -l

echo "=== Exercise 5: Most common log level ==="
grep -o "INFO\|WARNING\|ERROR" $LOGS | sort | uniq -c | sort -rn

echo "=== Exercise 6: Count duplicates in dirty.csv ==="
sort data/dirty.csv | uniq -d | wc -l
