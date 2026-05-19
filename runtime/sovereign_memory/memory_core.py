import json
import os

MEMORY_FILE = "sovereign_memory/memory.json"

def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return {
            "successful_patterns": [],
            "blocked_patterns": [],
            "missions": []
        }

    with open(MEMORY_FILE, "r") as f:

        return json.load(f)

def save_memory(memory):

    with open(MEMORY_FILE, "w") as f:

        json.dump(memory, f, indent=2)

def remember_success(command):

    memory = load_memory()

    if command not in memory["successful_patterns"]:

        memory["successful_patterns"].append(command)

    save_memory(memory)

def remember_blocked(command):

    memory = load_memory()

    if command not in memory["blocked_patterns"]:

        memory["blocked_patterns"].append(command)

    save_memory(memory)

def get_memory():

    return load_memory()
