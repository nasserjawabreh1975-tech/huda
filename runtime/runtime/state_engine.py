import json
import os
from datetime import datetime

BASE = os.path.expanduser("~/HUDA_CORE/runtime/state")

os.makedirs(BASE, exist_ok=True)

STATE_FILE = os.path.join(BASE, "system_state.json")

default_state = {
    "runtime": "stable",
    "agents": 4,
    "memory_events": 0,
    "decisions": 0,
    "executions": 0,
    "last_update": str(datetime.now())
}

if not os.path.exists(STATE_FILE):

    with open(STATE_FILE, "w") as f:
        json.dump(default_state, f, indent=2)

def load_state():

    with open(STATE_FILE) as f:
        return json.load(f)

def save_state(state):

    state["last_update"] = str(datetime.now())

    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)
