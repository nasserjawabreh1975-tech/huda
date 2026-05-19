#!/bin/bash

BASE="$HOME/HUDA_CORE"

mkdir -p \
"$BASE/runtime/scheduler"

cat > "$BASE/runtime/scheduler/distributed_scheduler.py" << 'PY'
from queue import PriorityQueue
import time

QUEUE = PriorityQueue()

QUEUE.put((1, "critical_recovery"))
QUEUE.put((2, "mission_execution"))
QUEUE.put((3, "report_generation"))

print("=" * 70)
print("DISTRIBUTED TASK SCHEDULER")
print("=" * 70)

while not QUEUE.empty():

    p, task = QUEUE.get()

    print()
    print("TASK     :", task)
    print("PRIORITY :", p)

    time.sleep(0.5)
PY

echo "DISTRIBUTED SCHEDULER INSTALLED"

