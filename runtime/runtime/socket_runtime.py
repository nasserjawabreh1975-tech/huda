print("=" * 70)
print("LIVE WEBSOCKET RUNTIME")
print("=" * 70)

CHANNELS = [
    "runtime_events",
    "agent_events",
    "engineering_events",
    "decision_events"
]

for c in CHANNELS:
    print("CHANNEL =>", c)
