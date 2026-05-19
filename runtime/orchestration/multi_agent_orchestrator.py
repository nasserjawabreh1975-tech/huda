import time
import random
from datetime import datetime
BASE = "/home/nasser/HUDA_CORE"

agents = {
    "runtime_agent": [
        "monitor runtime",
        "scan cpu",
        "scan memory"
    ],
    "execution_agent": [
        "execute repair",
        "optimize runtime",
        "stabilize execution"
    ],
    "learning_agent": [
        "learn pattern",
        "store success",
        "analyze feedback"
    ],
    "governance_agent": [
        "validate action",
        "approve execution",
        "reject unstable action"
    ]
}

state = {
    "cycle": 0,
    "decisions": 0,
    "executions": 0,
    "learning_events": 0,
    "governance_checks": 0
}

print("")
print("=" * 60)
print("HUDA MULTI AGENT ORCHESTRATOR")
print("=" * 60)

for cycle in range(1, 11):

    print("")
    print(f"[CYCLE {cycle}]")
    print("-" * 40)

    runtime_action = random.choice(agents["runtime_agent"])
    execution_action = random.choice(agents["execution_agent"])
    learning_action = random.choice(agents["learning_agent"])
    governance_action = random.choice(agents["governance_agent"])

    print(f"RUNTIME AGENT      => {runtime_action}")
    print(f"EXECUTION AGENT    => {execution_action}")
    print(f"LEARNING AGENT     => {learning_action}")
    print(f"GOVERNANCE AGENT   => {governance_action}")

    state["cycle"] += 1
    state["decisions"] += 4
    state["executions"] += 1
    state["learning_events"] += 1
    state["governance_checks"] += 1

    time.sleep(1)

print("")
print("=" * 60)
print("ORCHESTRATOR SUMMARY")
print("=" * 60)

for k, v in state.items():
    print(f"{k.upper()} => {v}")

with open(f"{BASE}/logs/orchestrator_report.txt", "w") as f:
    f.write(str(state))

print("")
print("ORCHESTRATOR REPORT WRITTEN")
print("")
