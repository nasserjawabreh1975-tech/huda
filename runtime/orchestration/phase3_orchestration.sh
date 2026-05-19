#!/bin/bash

BASE="$HOME/HUDA_CORE"

mkdir -p \
"$BASE/runtime/queues" \
"$BASE/runtime/pipelines" \
"$BASE/runtime/approval"

cat > "$BASE/runtime/queues/execution_queue.py" << 'PY'
QUEUE = []

def add(task):

    QUEUE.append(task)

    print("[ADD]", task)

def next_task():

    if not QUEUE:
        return None

    return QUEUE.pop(0)

if __name__ == "__main__":

    add("builder_task")

    print(next_task())
PY

cat > "$BASE/runtime/approval/approval_gate.py" << 'PY'
def approve(task):

    blocked = [
        "delete",
        "wipe",
        "format",
        "shutdown"
    ]

    for b in blocked:

        if b in task.lower():
            return False

    return True

print(approve("build ui"))
print(approve("delete runtime"))
PY

cat > "$BASE/runtime/pipelines/master_pipeline.py" << 'PY'
steps = [
    "analyze",
    "plan",
    "build",
    "validate",
    "test",
    "approve",
    "deploy"
]

print("=" * 60)

for s in steps:
    print("[STEP]", s)

print("=" * 60)
PY

echo "PHASE 3 READY"

