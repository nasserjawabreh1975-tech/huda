from agents.decision_agent import (
    choose_priority,
    create_subtasks
)

from agents.execution_agent import execute_task

from agents.repair_agent import repair


def autonomous_master(goal):

    priority = choose_priority(goal)

    tasks = create_subtasks(goal)

    execution = execute_task(
        'print("MASTER AGENT EXECUTION")'
    )

    if not execution["success"]:

        repair_result = repair(
            execution["stderr"]
        )

    else:

        repair_result = None

    return {
        "goal": goal,
        "priority": priority,
        "tasks": tasks,
        "execution": execution,
        "repair": repair_result
    }


if __name__ == "__main__":

    result = autonomous_master(
        "Repair engineering dashboard"
    )

    print(result)
