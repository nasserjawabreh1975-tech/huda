def approve_action(goal, intake=None):

    dangerous = [
        "rm -rf",
        "shutdown",
        "reboot",
        "mkfs",
        "dd if="
    ]

    for item in dangerous:

        if item in goal:

            return {
                "approved": False,
                "reason": f"blocked keyword: {item}"
            }

    if intake:

        if intake.get("blocked"):

            return {
                "approved": False,
                "reason": "intake firewall blocked payload"
            }

    return {
        "approved": True,
        "reason": "governance approved"
    }
