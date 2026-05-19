def approve_action(payload, intake):

    if intake.get("blocked"):

        return {
            "approved": False,
            "reason": "blocked by intake firewall"
        }

    return {
        "approved": True,
        "reason": "governance approved"
    }
