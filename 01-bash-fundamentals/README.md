# 01 — Bash Fundamentals

Commands covered: `ls`, `cat`, `head`, `tail`, `wc`, `grep`

## Commands Cheatsheet

```bash
ls -lh data/              # list files with sizes
cat data/sample.csv       # print entire file
head -n 5 data/sample.csv # first 5 lines
tail -n 5 data/sample.csv # last 5 lines
wc -l data/sample.csv     # count lines
grep "failed" data/sample.csv          # search for pattern
grep -i "error" data/pipeline_logs.txt # case-insensitive
grep -n "error" data/pipeline_logs.txt # show line numbers
```

## Exercises
Open `exercises.sh` and complete each TODO.

## Interview Tips
- Always start with `head` and `wc -l` to understand the data shape
- `grep -c` counts matches without listing them — useful for quick checks
