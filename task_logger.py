# File: task_logger.py
# Purpose: Log telemetry (time, date, counter) to a JSON file every 10 minutes.
# Run:     python task_logger.py [path_to_json_file]
# Stop:    Ctrl+C

import sys
import json
import time
import os
from datetime import datetime

INTERVAL = 10 * 60 
STEP = 10

path = sys.argv[1] if len(sys.argv) > 1 else input("Enter path to JSON file: ").strip()

entries = []
counter = STEP  

if os.path.exists(path):
    with open(path, "r") as f:
        content = f.read().strip()
    if content:
        entries = json.loads(content)
        if entries:
            counter = entries[-1]["counter"] + STEP

print(f"Logging to: {path}")
print(f"Starting counter: {counter}")
print("Press Ctrl+C to stop.\n")

try:
    while True:
        now = datetime.now()
        entry = {
            "time": now.strftime("%H:%M:%S"),
            "date": now.strftime("%Y-%m-%d"),
            "counter": counter,
        }
        entries.append(entry)

        with open(path, "w") as f:
            json.dump(entries, f, indent=2)

        print(f"Logged: {entry}")
        counter += STEP
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print(f"\nStopped by user. Final data saved to {path}")