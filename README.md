# Data Production Engineer — Bash & Python Interview Practice

Practice repo tailored for **Data Production Engineer** interviews (e.g. HRT / Hudson River Trading).

## What to Expect in the Interview

Based on candidate reports:
- **Take-home test** + ~2 phone screens + full-day virtual/onsite
- **SSH debugging round** — you SSH into a cloud server and debug a broken pipeline live
- **Python** data manipulation (cleaning, validation, aggregation)
- **Bash** for log analysis, data inspection, pipeline debugging
- **OS/Linux fundamentals** — processes, memory, file descriptors, networking
- **Anomaly detection** — find bad data and trace it back to the source stage

## Repo Structure

```
.
├── data/
│   ├── sample.csv            # clean transaction dataset
│   ├── dirty.csv             # dataset with intentional issues
│   ├── market_data.csv       # financial tick data (with anomalies)
│   ├── pipeline_logs.txt     # basic pipeline logs
│   └── pipeline_errors.log   # detailed pipeline log with errors
│
├── 01-bash-fundamentals/     # ls, cat, head, tail, wc, grep
├── 02-data-debugging/        # find issues in CSVs
├── 03-text-manipulation/     # cut, sort, uniq, awk, sed
├── 04-piping/                # chaining commands with |
├── 05-python-data/           # Python CSV parsing, validation, aggregation
├── 06-ssh-debugging/         # SSH debugging workflow & scenarios
├── 07-anomaly-detection/     # find price spikes, nulls, duplicates in market data
├── 08-os-fundamentals/       # processes, memory, disk, networking Q&A
└── solutions/                # bash solutions (try first!)
```

## How to Use

```bash
git clone https://github.com/frankzhu773/gcp-pipeline-bash-practice.git
cd gcp-pipeline-bash-practice

# Work through each section in order
# Read the README in each folder first, then do exercises

# Bash exercises
bash 01-bash-fundamentals/exercises.sh

# Python exercises
python3 05-python-data/exercises.py

# Check solutions
bash solutions/01-solutions.sh
python3 05-python-data/solutions.py
```

## Interview Strategy

### Debugging Round (SSH into server)
1. Orient: `ps aux`, `df -h`, `free -h`, `uptime`
2. Check logs: `tail -f pipeline.log`, `grep "ERROR"`
3. Validate data: `wc -l`, `head -5`, `awk '{print NF}'`
4. Think out loud — they care about your process

### Data Validation Checklist
- [ ] Row count matches expected
- [ ] No missing/empty fields
- [ ] No duplicate records
- [ ] No price spikes or impossible values
- [ ] Correct delimiter throughout
- [ ] Valid dates and value ranges
- [ ] Consistent column count per row

### General Tips
- Start broad (`wc -l`, `head`) then narrow down
- Build pipes step by step — test each stage
- Say what you're checking and why before running the command
- `man <cmd>` and `--help` are allowed in interviews
