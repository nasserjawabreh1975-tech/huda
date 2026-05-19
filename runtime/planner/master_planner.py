def build_plan(goal):

    goal = str(goal).lower()

    if "list files" in goal:
        return {
            "goal": goal,
            "steps": [
                {
                    "id": 1,
                    "action": "list_directory",
                    "command": "ls"
                }
            ]
        }

    if "show processes" in goal:
        return {
            "goal": goal,
            "steps": [
                {
                    "id": 1,
                    "action": "list_processes",
                    "command": "ps aux"
                }
            ]
        }

    return {
        "goal": goal,
        "steps": []
    }
