#!/bin/bash

BASE="$HOME/HUDA_CORE"

mkdir -p "$BASE/runtime/state"

cat > "$BASE/runtime/state/runtime_graph.py" << 'PY'
from pathlib import Path
import json

BASE = Path.home() / "HUDA_CORE"

graph = {
    "runtime_kernel": [
        "pipeline",
        "watchdog",
        "metrics"
    ],
    "pipeline": [
        "approval",
        "validator",
        "deploy"
    ],
    "builders": [
        "queue",
        "contracts"
    ]
}

p = BASE / "runtime/state/runtime_graph.json"

p.write_text(json.dumps(graph, indent=2))

print("=" * 60)
print("RUNTIME GRAPH GENERATED")
print("=" * 60)
print(p)
PY

echo "PHASE 3 READY"
