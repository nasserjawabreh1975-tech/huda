def build_plan(goal):

    if "list" in goal and "files" in goal:

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

    if "show" in goal and "processes" in goal:

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
