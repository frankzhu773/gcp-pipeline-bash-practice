#!/bin/bash
# EXERCISES: Text & Data Manipulation
# Commands: cut, sort, uniq, awk, sed

DATA="data/sample.csv"

echo "=============================="
echo " EXERCISE 1: Extract columns"
echo "=============================="
# TODO: Extract only the 'name' and 'amount' columns (columns 2 and 4)
# Hint: cut -d',' -f2,4 data/sample.csv



echo "=============================="
echo " EXERCISE 2: Sort by amount"
echo "=============================="
# TODO: Sort sample.csv by the amount column (column 4) numerically
# Hint: sort -t',' -k4 -n data/sample.csv



echo "=============================="
echo " EXERCISE 3: Count records by status"
echo "=============================="
# TODO: Count how many 'success' vs 'failed' records exist
# Hint: cut the status column, then sort | uniq -c



echo "=============================="
echo " EXERCISE 4: Print specific column with awk"
echo "=============================="
# TODO: Use awk to print only the 'date' column (column 3)
# Hint: awk -F',' '{print $3}' data/sample.csv



echo "=============================="
echo " EXERCISE 5: Find & replace with sed"
echo "=============================="
# TODO: Replace 'failed' with 'FAILED' in sample.csv output (don't modify file)
# Hint: sed 's/failed/FAILED/g' data/sample.csv



echo "=============================="
echo " EXERCISE 6: Sum amounts with awk"
echo "=============================="
# TODO: Calculate the total sum of the 'amount' column
# Hint: awk -F',' '{sum += $4} END {print sum}' data/sample.csv
