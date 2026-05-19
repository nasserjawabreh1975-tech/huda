import json
import time
import requests
from pathlib import Path
from datetime import datetime

BASE = Path("~/HUDA_CORE").expanduser()

MISSIONS = BASE / "missions/runtime_queue.json"
STATE = BASE / "state/runtime_state.json"
LOGS = BASE / "logs/runtime.log"
GENERATED = BASE / "generated"
DIRECTIVE = BASE / "memory/system_directive.md"

GENERATED.mkdir(parents=True, exist_ok=True)

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3"

def ask_ollama(prompt):

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    r = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=300
    )

    return r.json().get("response", "")

def load_json(path, default):

    if not path.exists():
        path.write_text(json.dumps(default, indent=2))
        return default

    try:
        return json.loads(path.read_text())
    except:
        return default

def save_json(path, data):
    path.write_text(json.dumps(data, indent=2))

def log(text):

    with open(LOGS, "a") as f:
        f.write(f"\n[{datetime.utcnow()}]\n{text}\n")

runtime_state = {
    "status": "active",
    "missions_completed": 0
}

save_json(STATE, runtime_state)

if not MISSIONS.exists():
    MISSIONS.write_text("[]")

print("\nHUDA AUTONOMOUS RUNTIME ACTIVE\n")

while True:

    missions = load_json(MISSIONS, [])

    for mission in missions:

        if mission.get("status") == "done":
            continue

        title = mission["title"]
        objective = mission["objective"]

        system_directive = ""

        if DIRECTIVE.exists():
            system_directive = DIRECTIVE.read_text()

        prompt = f"""
{system_directive}

MISSION:
{objective}

Generate real production-grade Python implementation.

Requirements:
- executable
- modular
- documented
- engineering-grade
- no placeholders
- no pseudo code
- FastAPI compatible where needed
- runtime-safe

"""

        result = ask_ollama(prompt)

        filename = title.lower().replace(" ", "_") + ".py"

        output = GENERATED / filename

        output.write_text(result)

        mission["status"] = "done"
        mission["completed_at"] = str(datetime.utcnow())

        runtime_state["missions_completed"] += 1

        save_json(STATE, runtime_state)

        log(f"MISSION COMPLETED: {title}")

        print(f"\nGENERATED -> {output}")

    save_json(MISSIONS, missions)

    time.sleep(15)
