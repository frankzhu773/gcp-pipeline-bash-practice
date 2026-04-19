#!/bin/bash
# EXERCISES: Anomaly Detection in Financial Data
# HRT's core job: find bad data and trace it back to source
# Use data/market_data.csv and data/pipeline_errors.log

MARKET="data/market_data.csv"
LOGS="data/pipeline_errors.log"

echo "=============================="
echo " EXERCISE 1: Price spike detection"
echo "=============================="
# TODO: Find rows in market_data.csv where open price > 10000
# Hint: awk -F',' to check column 3



echo "=============================="
echo " EXERCISE 2: Negative price detection"
echo "=============================="
# TODO: Find rows where any price (open/high/low/close) is negative
# Hint: grep for a leading minus sign in numeric columns



echo "=============================="
echo " EXERCISE 3: Missing fields"
echo "=============================="
# TODO: Find rows with empty fields (consecutive commas)
# Hint: grep ",,"



echo "=============================="
echo " EXERCISE 4: Duplicate timestamps per symbol"
echo "=============================="
# TODO: Find duplicate (timestamp, symbol) combos
# Hint: cut columns 1 and 2, then sort | uniq -d



echo "=============================="
echo " EXERCISE 5: Row count reconciliation"
echo "=============================="
# TODO: Count total rows in market_data.csv (excl header)
#       Then grep the logs to find how many rows were expected vs loaded
#       Are they the same?



echo "=============================="
echo " EXERCISE 6: Trace an anomaly in the logs"
echo "=============================="
# TODO: Find all WARNING and ERROR lines in pipeline_errors.log
#       Then count how many of each type there are
# Hint: grep, then grep -c or wc -l
