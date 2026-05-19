#!/bin/bash

BASE="$HOME/HUDA_CORE"

mkdir -p \
"$BASE/runtime/broker"

cat > "$BASE/runtime/broker/message_broker.py" << 'PY'
MESSAGES = []

def publish(channel, payload):

    MESSAGES.append({

        "channel": channel,
        "payload": payload
    })

publish("missions", "mission_started")
publish("planner", "plan_generated")
publish("agents", "task_assigned")

print("=" * 70)
print("MESSAGE BROKER ACTIVE")
print("=" * 70)

for m in MESSAGES:

    print()
    print(m)
PY

echo "MESSAGE BROKER INSTALLED"

