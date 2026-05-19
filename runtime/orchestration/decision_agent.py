import random

PRIORITIES = {
    "critical": 5,
    "high": 4,
    "medium": 3,
    "low": 2
}

def choose_priority(task):

    text = task.lower()

    if "crash" in text:
        return "critical"

    if "repair" in text:
        return "high"

    if "analyze" in text:
        return "medium"

    return "low"


def evaluate_result(result):

    if result.get("success"):
        return {
            "status": "SUCCESS",
            "next_action": "store_memory"
        }

    return {
        "status": "FAILED",
        "next_action": "repair_cycle"
    }


def create_subtasks(goal):

    return [
        f"Analyze goal: {goal}",
        f"Generate execution plan for: {goal}",
        f"Execute tasks for: {goal}",
        f"Validate outputs for: {goal}",
        f"Generate final report for: {goal}"
    ]


if __name__ == "__main__":

    task = "Repair frontend vite crash"

    print(
        choose_priority(task)
    )

    print(
        create_subtasks(
            "Build hospital BOQ analyzer"
        )
    )
