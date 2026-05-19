def approve_action(command, intake=None):

    dangerous = [
        "rm -rf",
        "shutdown",
        "reboot",
        "mkfs",
        "dd ",
        ":(){:|:&};:",
        "chmod 777",
        "wget",
        "curl"
    ]

    for item in dangerous:

        if item in command:

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
