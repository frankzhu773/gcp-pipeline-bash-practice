#!/bin/bash
# EXERCISES: Piping — chaining commands together
# This is heavily tested in data pipeline interviews!

DATA="data/sample.csv"
LOGS="data/pipeline_logs.txt"

echo "=============================="
echo " EXERCISE 1: Count error lines in logs"
echo "=============================="
# TODO: Count how many ERROR lines are in pipeline_logs.txt
# Hint: grep "ERROR" | wc -l



echo "=============================="
echo " EXERCISE 2: Get unique dates from CSV"
echo "=============================="
# TODO: Extract the date column and list unique dates
# Hint: cut | sort | uniq



echo "=============================="
echo " EXERCISE 3: Top amounts"
echo "=============================="
# TODO: Show the top 3 highest amounts from sample.csv
# Hint: cut | sort -rn | head -3



echo "=============================="
echo " EXERCISE 4: Count failed records"
echo "=============================="
# TODO: Count rows where status is 'failed' (exclude header)
# Hint: grep "failed" | wc -l



echo "=============================="
echo " EXERCISE 5: Find most common log level"
echo "=============================="
# TODO: Count occurrences of INFO, WARNING, ERROR in pipeline_logs.txt
# Hint: grep -o "INFO\|WARNING\|ERROR" | sort | uniq -c | sort -rn



echo "=============================="
echo " EXERCISE 6: Pipeline chain"
echo "=============================="
# TODO: From dirty.csv, find duplicate rows and count how many there are
# Hint: sort | uniq -d | wc -l
