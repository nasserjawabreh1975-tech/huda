def recovery_action(anomaly):

    if not anomaly["anomaly"]:

        return {
            "recovered": False,
            "action": "system_clean"
        }

    threats = anomaly["threats"]

    actions = []

    for item in threats:

        if item == "traceback":
            actions.append("restart_runtime")

        elif item == "permission":
            actions.append("audit_permissions")

        elif item == "blocked":
            actions.append("increase_governance")

        elif item == "error":
            actions.append("inspect_execution")

        else:
            actions.append("monitor")

    return {
        "recovered": True,
        "actions": actions,
        "severity": anomaly["severity"]
    }
