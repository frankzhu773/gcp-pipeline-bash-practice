#!/bin/bash
# EXERCISES: Data Pipeline Debugging
# Use data/dirty.csv — it has intentional issues. Find them all!

DIRTY="data/dirty.csv"
CLEAN="data/sample.csv"

echo "=============================="
echo " EXERCISE 1: Check row counts"
echo "=============================="
# TODO: Count rows in both dirty.csv and sample.csv and compare
# Expected: dirty.csv should have more rows due to duplicates



echo "=============================="
echo " EXERCISE 2: Find duplicate rows"
echo "=============================="
# TODO: Find duplicate lines in dirty.csv
# Hint: sort | uniq -d



echo "=============================="
echo " EXERCISE 3: Find rows with wrong delimiter"
echo "=============================="
# TODO: Find rows that use | instead of , as delimiter
# Hint: grep



echo "=============================="
echo " EXERCISE 4: Check column consistency"
echo "=============================="
# TODO: Count number of fields per row — inconsistent rows are data issues
# Hint: awk -F',' '{print NF}' data/dirty.csv | sort | uniq -c



echo "=============================="
echo " EXERCISE 5: Find empty/null values"
echo "=============================="
# TODO: Find rows where a field is empty (two commas in a row: ,,)
# Hint: grep ",," dirty.csv



echo "=============================="
echo " EXERCISE 6: Spot invalid dates"
echo "=============================="
# TODO: Find rows with day > 31 (e.g. 2024-01-32)
# Hint: grep with a pattern for -3[2-9] or just look for day 32+
