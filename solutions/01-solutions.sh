#!/bin/bash
# SOLUTIONS: Bash Fundamentals

DATA="data/sample.csv"

echo "=== Exercise 1: List files ==="
ls -lh data/

echo "=== Exercise 2: Preview the file ==="
head -n 5 $DATA

echo "=== Exercise 3: Count rows ==="
wc -l $DATA

echo "=== Exercise 4: Search for failed records ==="
grep "failed" $DATA

echo "=== Exercise 5: Search logs for errors ==="
grep "ERROR" data/pipeline_logs.txt
