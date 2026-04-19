#!/bin/bash
# SOLUTIONS: Data Pipeline Debugging

DIRTY="data/dirty.csv"
CLEAN="data/sample.csv"

echo "=== Exercise 1: Check row counts ==="
echo "dirty.csv:"; wc -l $DIRTY
echo "sample.csv:"; wc -l $CLEAN

echo "=== Exercise 2: Find duplicate rows ==="
sort $DIRTY | uniq -d

echo "=== Exercise 3: Find rows with wrong delimiter ==="
grep "|" $DIRTY

echo "=== Exercise 4: Check column consistency ==="
awk -F',' '{print NF}' $DIRTY | sort | uniq -c

echo "=== Exercise 5: Find empty/null values ==="
grep ",," $DIRTY

echo "=== Exercise 6: Spot invalid dates ==="
grep "2024-01-3[2-9]" $DIRTY
