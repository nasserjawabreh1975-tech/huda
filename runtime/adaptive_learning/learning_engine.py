MEMORY = []

def absorb_pattern(result):

    MEMORY.append(result.get("command", "unknown"))

    return {
        "learned": True,
        "type": "success_pattern"
    }

def get_patterns():

    return MEMORY
