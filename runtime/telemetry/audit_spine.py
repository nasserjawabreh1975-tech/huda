import json
from datetime import datetime

AUDIT_FILE = "telemetry/audit_log.jsonl"

def record_event(event):

    payload = {
        "timestamp": str(datetime.utcnow()),
        "event": event
    }

    with open(AUDIT_FILE, "a") as f:
        f.write(json.dumps(payload) + "\n")
