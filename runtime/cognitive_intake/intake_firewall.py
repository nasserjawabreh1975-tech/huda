def analyze_payload(payload):

    dangerous = [
        "rm -rf",
        "shutdown",
        "reboot",
        "mkfs",
        ":(){ :|:& };:"
    ]

    for item in dangerous:

        if item in payload:

            return {
                "blocked": True,
                "trust_score": 0,
                "type": "dangerous"
            }

    return {
        "blocked": False,
        "trust_score": 100,
        "type": "unknown"
    }
