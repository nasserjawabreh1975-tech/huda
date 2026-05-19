import subprocess

BLOCKED = [
    "rm",
    "shutdown",
    "reboot",
    "mkfs",
    "dd"
]

def execute(command):

    cmd = str(command).lower()

    for item in BLOCKED:

        if item in cmd:
            return {
                "status": "blocked",
                "reason": f"blocked command: {item}"
            }

    try:

        result = subprocess.check_output(
            command,
            shell=True,
            text=True
        )

        return {
            "status": "success",
            "command": command,
            "output": result
        }

    except Exception as e:

        return {
            "status": "error",
            "error": str(e)
        }
