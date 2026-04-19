# 06 — SSH Debugging Round

HRT has a dedicated debugging round where you SSH into a cloud server and diagnose a broken pipeline. This section simulates that experience.

## What to Expect
- You'll be dropped into a Linux server with a broken or misbehaving pipeline
- You need to find the root cause and explain your reasoning out loud
- No googling — but `man` and `--help` are allowed

## SSH Debugging Workflow

### Step 1: Orient yourself
```bash
whoami && hostname          # who am I, where am I
pwd && ls -la               # where are files
ps aux | grep python        # what processes are running
df -h                       # disk space
free -h                     # memory
uptime                      # load average
```

### Step 2: Check logs first
```bash
tail -f /var/log/pipeline.log          # watch live logs
grep "ERROR\|WARNING" pipeline.log     # find issues
grep "ERROR" pipeline.log | wc -l     # count errors
```

### Step 3: Check pipeline processes
```bash
ps aux | grep pipeline      # is the process running?
top -b -n 1                 # CPU/memory usage snapshot
lsof -p <pid>               # what files is the process using?
```

### Step 4: Check file integrity
```bash
wc -l input.csv             # expected row count?
head -5 input.csv           # correct format?
awk -F',' '{print NF}' input.csv | sort | uniq -c  # consistent columns?
```

### Step 5: Check network/connectivity
```bash
ping google.com             # basic connectivity
curl -I https://api.example.com   # API reachable?
netstat -tuln               # open ports
ss -tuln                    # modern alternative to netstat
```

### Step 6: Check disk/permissions
```bash
df -h                       # disk full?
ls -la /path/to/output/     # write permissions?
chmod 644 file.csv          # fix permissions
```

## Common Pipeline Failure Scenarios

| Symptom | Likely Cause | How to Check |
|---------|-------------|--------------|
| Pipeline hung | Disk full | `df -h` |
| No output file | Permission denied | `ls -la`, check stderr |
| Row count mismatch | Parsing error | `wc -l`, check ERROR logs |
| Slow pipeline | High CPU/memory | `top`, `htop` |
| Connection error | Network/firewall | `ping`, `curl`, `netstat` |
| Duplicate rows | Retry without dedup | `sort \| uniq -d` |
| Wrong values | Bad source data | `head`, `grep` anomalies |

## Practice Exercise

Simulate a debugging session on your own machine:

```bash
# 1. Create a "broken" pipeline scenario
echo "id,value" > broken_input.csv
echo "1,100" >> broken_input.csv
echo "2," >> broken_input.csv        # missing value
echo "2,200" >> broken_input.csv     # duplicate
echo "3,99999" >> broken_input.csv   # spike

# 2. Now debug it as if you SSHed in:
wc -l broken_input.csv
head broken_input.csv
awk -F',' '{print NF}' broken_input.csv | sort | uniq -c
grep ",," broken_input.csv
sort broken_input.csv | uniq -d
```

## Interview Tips
- **Think out loud** — they want to hear your process, not just the answer
- Start with `ps aux`, `df -h`, `tail -f logs` every time — shows structured thinking
- "Let me check the logs first" is always the right instinct
- If you don't know a command flag, say so and use `--help`
