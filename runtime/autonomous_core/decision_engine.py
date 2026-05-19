from sovereign_memory.memory_core import get_memory
from runtime_state.state_manager import get_state

def decide_next_action(current_goal):

    memory = get_memory()

    state = get_state()

    trusted_patterns = memory["successful_patterns"]

    if state["runtime_health"] != "stable":

        return {
            "decision": "halt",
            "reason": "runtime unstable"
        }

    if "ls" in trusted_patterns:

        return {
            "decision": "expand_scan",
            "command": "pwd"
        }

    return {
        "decision": "observe",
        "command": "ls"
    }
