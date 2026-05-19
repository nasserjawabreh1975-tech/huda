#!/bin/bash

BASE="$HOME/HUDA_CORE"

mkdir -p \
"$BASE/runtime/distributed"

cat > "$BASE/runtime/distributed/distributed_agents.py" << 'PY'
import threading
import time

def worker(name):

    for i in range(3):

        print(f"[{name}] cycle {i}")

        time.sleep(1)

threads = []

for n in [
    "builder",
    "planner",
    "recovery",
    "audit"
]:

    t = threading.Thread(
        target=worker,
        args=(n,)
    )

    threads.append(t)

    t.start()

for t in threads:
    t.join()

print("=" * 60)
print("DISTRIBUTED AGENTS COMPLETE")
print("=" * 60)
PY

echo "PHASE 14 READY"
