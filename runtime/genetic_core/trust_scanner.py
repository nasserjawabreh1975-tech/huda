def scan_behavior(module_name, activity):

    suspicious = [
        "delete_system",
        "network_override",
        "disable_governance",
        "inject_payload"
    ]

    for item in suspicious:

        if item in activity:

            return {
                "trusted": False,
                "severity": "high",
                "reason": item
            }

    return {
        "trusted": True,
        "severity": "clean"
    }
