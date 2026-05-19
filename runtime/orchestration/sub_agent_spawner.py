def spawn(goal):

    print("=" * 60)
    print("[SUB AGENT SPAWNER]")
    print("=" * 60)

    agents = [
        "analysis_agent",
        "planning_agent",
        "execution_agent",
        "verification_agent"
    ]

    print("GOAL:", goal)

    print()

    for a in agents:

        print("[SPAWNED]", a)

    return agents


if __name__ == "__main__":

    spawn("complex autonomous mission")
