#!/bin/bash
# SOLUTIONS: Text & Data Manipulation

DATA="data/sample.csv"

echo "=== Exercise 1: Extract columns ==="
cut -d',' -f2,4 $DATA

echo "=== Exercise 2: Sort by amount ==="
sort -t',' -k4 -n $DATA

echo "=== Exercise 3: Count records by status ==="
cut -d',' -f5 $DATA | sort | uniq -c

echo "=== Exercise 4: Print date column with awk ==="
awk -F',' '{print $3}' $DATA

echo "=== Exercise 5: Replace failed with FAILED ==="
sed 's/failed/FAILED/g' $DATA

echo "=== Exercise 6: Sum amounts ==="
awk -F',' 'NR > 1 {sum += $4} END {print "Total:", sum}' $DATA
