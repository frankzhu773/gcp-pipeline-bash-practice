#!/bin/bash
# EXERCISES: Bash Fundamentals
# Run from repo root: bash 01-bash-fundamentals/exercises.sh
# Or practice each command manually in your terminal.

DATA="data/sample.csv"

echo "=============================="
echo " EXERCISE 1: List files"
echo "=============================="
# TODO: List all files in the data/ folder with details and human-readable sizes
# Hint: ls -lh data/



echo "=============================="
echo " EXERCISE 2: Preview the file"
echo "=============================="
# TODO: Show the first 5 lines of sample.csv
# Hint: head



echo "=============================="
echo " EXERCISE 3: Count rows"
echo "=============================="
# TODO: Count how many rows are in sample.csv (including header)
# Hint: wc -l



echo "=============================="
echo " EXERCISE 4: Search for failed records"
echo "=============================="
# TODO: Find all rows in sample.csv where status is 'failed'
# Hint: grep



echo "=============================="
echo " EXERCISE 5: Search logs for errors"
echo "=============================="
# TODO: Find all ERROR lines in pipeline_logs.txt
# Hint: grep data/pipeline_logs.txt
