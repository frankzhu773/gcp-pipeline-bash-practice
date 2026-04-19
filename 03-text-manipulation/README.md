# 03 — Text & Data Manipulation

Commands covered: `cut`, `sort`, `uniq`, `awk`, `sed`

## Commands Cheatsheet

```bash
# cut — extract columns
cut -d',' -f1,3 data/sample.csv       # columns 1 and 3
cut -d',' -f2 data/sample.csv         # just column 2

# sort
sort data/sample.csv                          # alphabetical
sort -t',' -k4 -n data/sample.csv             # numeric sort on column 4
sort -t',' -k4 -nr data/sample.csv            # reverse numeric

# uniq — must sort first!
sort data/sample.csv | uniq                   # remove duplicates
sort data/sample.csv | uniq -c               # count occurrences
sort data/sample.csv | uniq -d               # show only duplicates

# awk — column manipulation
awk -F',' '{print $2}' data/sample.csv        # print column 2
awk -F',' '{sum += $4} END {print sum}'  data/sample.csv  # sum column 4
awk -F',' 'NR > 1 {print $0}' data/sample.csv  # skip header

# sed — find & replace
sed 's/failed/FAILED/g' data/sample.csv       # replace in output
sed -i 's/failed/FAILED/g' data/sample.csv    # replace in file (careful!)
```

## Interview Tips
- `awk` is your Swiss army knife — learn `NR`, `NF`, `$0`, `$1`
- Always use `NR > 1` in awk to skip the CSV header row
- `sort | uniq -c | sort -rn` ranks frequency — very useful pattern
