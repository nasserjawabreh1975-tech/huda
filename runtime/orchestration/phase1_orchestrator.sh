#!/bin/bash

BASE="$HOME/HUDA_CORE"

mkdir -p \
"$BASE/runtime/orchestrator" \
"$BASE/runtime/state"

cat > "$BASE/runtime/orchestrator/runtime_orchestrator.py" << 'PY'
from pathlib import Path
import json
import time

BASE = Path.home() / "HUDA_CORE"

STATE = {
    "boot_time": time.time(),
    "layers": [],
    "agents": [],
    "missions": [],
    "health": "ACTIVE"
}

def register_layer(name):
    STATE["layers"].append(name)

def register_agent(name):
    STATE["agents"].append(name)

def snapshot():
    out = BASE / "runtime/state/orchestrator_state.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(STATE, indent=2))
    return out

if __name__ == "__main__":

    register_layer("kernel")
    register_layer("memory")
    register_layer("recovery")
    register_layer("planner")

    register_agent("builder_agent")
    register_agent("analysis_agent")

    p = snapshot()

    print("=" * 60)
    print("RUNTIME ORCHESTRATOR ACTIVE")
    print("=" * 60)
    print(p)
PY

chmod +x "$BASE/runtime/orchestrator/runtime_orchestrator.py"

echo "PHASE 1 READY"
