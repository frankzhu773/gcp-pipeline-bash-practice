# 08 — OS & Linux Fundamentals

HRT interviews include OS/systems questions — they want to know you understand what's happening under the hood.

## Process Management

```bash
ps aux                        # list all running processes
ps aux | grep python          # find a specific process
kill -9 <pid>                 # force kill a process
top / htop                    # live process monitor
nice -n 10 python script.py   # run with lower CPU priority
nohup python script.py &      # run in background, survives logout
```

## File Descriptors & I/O

```bash
lsof -p <pid>                 # files opened by a process
lsof +D /path/                # what has this directory open?
/proc/<pid>/fd/               # file descriptors for a process
ulimit -n                     # max open files limit
```

## Memory

```bash
free -h                       # RAM usage
vmstat 1 5                    # memory/CPU stats every 1s, 5 times
cat /proc/meminfo             # detailed memory info
```

## Disk & I/O

```bash
df -h                         # disk space by filesystem
du -sh /path/                 # size of a directory
iostat -x 1                   # disk I/O stats
lsblk                         # block devices
```

## Networking

```bash
ping host                     # basic connectivity
curl -I https://url           # HTTP headers only
wget -q -O - https://url      # download to stdout
netstat -tuln                 # listening ports
ss -tuln                      # modern alternative
traceroute host               # network path
```

## Permissions

```bash
ls -la                        # show permissions
chmod 644 file                # rw-r--r--
chmod 755 script.sh           # rwxr-xr-x (executable)
chown user:group file         # change owner
```

## Key Interview Questions (practice these)

1. **What happens when you run `python script.py`?**
   - Shell forks a child process, exec replaces it with python, OS schedules it

2. **What is a file descriptor?**
   - Integer handle to an open file/socket. 0=stdin, 1=stdout, 2=stderr

3. **What does `kill -9` do vs `kill -15`?**
   - `-15` (SIGTERM): graceful shutdown, process can clean up
   - `-9` (SIGKILL): immediate termination, cannot be caught

4. **What does `2>&1` mean in bash?**
   - Redirect stderr (fd 2) to wherever stdout (fd 1) is going

5. **How do you check if a port is in use?**
   - `ss -tuln | grep :8080` or `lsof -i :8080`

6. **What is a zombie process?**
   - A process that finished but its parent hasn't called `wait()` to collect exit status

## Interview Tips
- If asked about a slow pipeline: check CPU (`top`), memory (`free`), disk (`df`, `iostat`)
- If asked about a hung process: `ps aux`, `lsof -p <pid>`, check if waiting on I/O or network
- Know the difference between process, thread, and goroutine conceptually
