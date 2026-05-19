from communication.message_bus import send, receive
import time

AGENTS = [
    "planner_agent",
    "engineering_agent",
    "repair_agent",
    "memory_agent",
    "supervisor_agent"
]

def activate():

    print("=" * 60)
    print("HUDA INTELLIGENT SWARM ACTIVE")
    print("=" * 60)

    send(
        "supervisor_agent",
        "planner_agent",
        "Analyze mega hospital BOQ"
    )

    while True:

        planner_msg = receive("planner_agent")

        if planner_msg:

            print("[PLANNER]", planner_msg)

            send(
                "planner_agent",
                "engineering_agent",
                "Generate engineering execution plan"
            )

        eng_msg = receive("engineering_agent")

        if eng_msg:

            print("[ENGINEERING]", eng_msg)

            send(
                "engineering_agent",
                "repair_agent",
                "Validate execution quality"
            )

        repair_msg = receive("repair_agent")

        if repair_msg:

            print("[REPAIR]", repair_msg)

            send(
                "repair_agent",
                "memory_agent",
                "Store engineering mission"
            )

        memory_msg = receive("memory_agent")

        if memory_msg:

            print("[MEMORY]", memory_msg)

            print("=" * 60)
            print("MISSION COMPLETED")
            print("=" * 60)

            break

        time.sleep(1)

if __name__ == "__main__":
    activate()
