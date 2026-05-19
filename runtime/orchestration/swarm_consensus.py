import os
import json
from collections import Counter
from datetime import datetime, UTC

BASE = os.path.expanduser("~/HUDA_CORE")

STATE_DIR = os.path.join(BASE, "swarm_state")

nodes = []

for file in os.listdir(STATE_DIR):

    if not file.endswith(".json"):
        continue

    path = os.path.join(STATE_DIR, file)

    try:

        with open(path) as f:
            nodes.append(json.load(f))

    except:
        pass

scores = {
    "heartbeat": 0,
    "mutations": 0,
    "alerts": 0
}

for n in nodes:

    scores["heartbeat"] += n.get("heartbeat", 0)
    scores["mutations"] += n.get("mutations", 0)
    scores["alerts"] += n.get("alerts", 0)

modes = []

for n in nodes:

    if n.get("alerts", 0) > 10:
        modes.append("DEFENSIVE")

    elif n.get("mutations", 0) > 20:
        modes.append("EVOLVING")

    else:
        modes.append("STABLE")

consensus = Counter(modes).most_common(1)[0][0] if modes else "UNKNOWN"

timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")

report = {
    "timestamp": timestamp,
    "nodes": len(nodes),
    "scores": scores,
    "consensus": consensus
}

REPORT_DIR = os.path.join(BASE, "consensus_reports")
os.makedirs(REPORT_DIR, exist_ok=True)

path = os.path.join(
    REPORT_DIR,
    f"consensus_{timestamp}.json"
)

with open(path, "w") as f:
    json.dump(report, f, indent=2)

print("=" * 60)
print("HUDA SWARM CONSENSUS")
print("=" * 60)

print()

print("NODES =>", len(nodes))

print()

print("TOTAL HEARTBEATS =>", scores["heartbeat"])
print("TOTAL MUTATIONS =>", scores["mutations"])
print("TOTAL ALERTS =>", scores["alerts"])

print()

print("CONSENSUS =>", consensus)

print()

print("REPORT =>")
print(path)

print()
print("=" * 60)
print("SYSTEM MODE => COLLECTIVE COGNITION")
print("=" * 60)

