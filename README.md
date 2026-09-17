# training_assesment_Rajan_sahu

Three small Python scripts for pattern generation, telemetry logging, and ASCII digit reduction.

## 1. task_pattern.py — Pattern Generation

Generates a dynamic star pattern for any odd integer `n >= 5`.

**Run:**
```bash
python task_pattern.py
```
You'll be prompted to enter `n`. Example (`n=5`):
```
*     *
*     **
*********
*     **
*     *
```

## 2. task_logger.py — Scheduled Telemetry JSON Logger

Runs continuously and logs an entry (`time`, `date`, `counter`) to a JSON file every 10 minutes. If the file already exists, it resumes from the last saved counter instead of starting over.

**Run:**
```bash
python task_logger.py telemetry.json
```
Stop anytime with `Ctrl+C`. If no file path is given as an argument, the script will prompt for one.

## 3. task_ascii.py — ASCII Single-Digit Reduction

Converts a name to a single-digit number by summing the uppercase ASCII value of each letter, then repeatedly summing the digits until one digit remains. Prints each step of the calculation.

**Run:**
```bash
python task_ascii.py
```
Example (`RAHUL`) reduces `380 -> 11 -> 2`.

## Requirements

- Python 3
- No external libraries needed (uses only the standard library)
