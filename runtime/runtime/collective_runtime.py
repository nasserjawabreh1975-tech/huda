print("=" * 70)
print("COLLECTIVE INTELLIGENCE ACTIVE")
print("=" * 70)

AGENTS = {

    "engineering_agent": "proposing",
    "risk_agent": "evaluating",
    "planning_agent": "reordering",
    "optimization_agent": "comparing"
}

for k,v in AGENTS.items():
    print(k, "=>", v)
