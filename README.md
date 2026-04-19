# GCP Data Pipeline — Bash Interview Practice

Practice repo for GCP Data Pipeline bash interview prep.

## Structure

```
.
├── data/
│   ├── sample.csv        # clean dataset
│   ├── dirty.csv         # dataset with intentional issues
│   └── pipeline_logs.txt # sample pipeline logs
├── 01-bash-fundamentals/ # ls, cat, head, tail, wc, grep
├── 02-data-debugging/    # finding issues in pipeline data
├── 03-text-manipulation/ # cut, sort, uniq, awk, sed
├── 04-piping/            # chaining commands with |
└── solutions/            # answers (try exercises first!)
```

## How to Use

```bash
# Clone the repo
git clone <repo-url>
cd gcp-pipeline-bash-practice

# Work through exercises in order
# Open the exercise file, read the TODOs, and run commands manually
# Check solutions only after attempting

bash solutions/01-solutions.sh  # see solutions for section 1
```

## Interview Strategy
1. **Start broad** — `wc -l`, `head -5` to understand the data
2. **Think out loud** — explain what you're checking and why
3. **Build pipes step by step** — test each command before chaining
4. **Don't panic** — `man <command>` or `command --help` is allowed
