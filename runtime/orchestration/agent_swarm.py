import threading
import time

agents = [
    "ENGINEERING_AGENT",
    "PLANNING_AGENT",
    "REPAIR_AGENT",
    "MEMORY_AGENT",
    "SUPERVISOR_AGENT"
]

def run_agent(name):

    while True:

        print(f"[{name}] ACTIVE")

        time.sleep(3)

threads = []

for agent in agents:

    t = threading.Thread(
        target=run_agent,
        args=(agent,),
        daemon=True
    )

    t.start()

    threads.append(t)

while True:
    time.sleep(1)
