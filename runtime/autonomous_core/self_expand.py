STATE = {
    "last_command": None,
    "cycle": 0
}

def autonomous_decision():

    STATE["cycle"] += 1

    if STATE["last_command"] == "pwd":
        command = "ls"
        decision = "observe"

    elif STATE["last_command"] == "ls":
        command = "find . -name '*.py' | head"
        decision = "deep_scan"

    else:
        command = "pwd"
        decision = "expand_scan"

    STATE["last_command"] = command

    return {
        "decision": decision,
        "command": command,
        "cycle": STATE["cycle"]
    }
