def detect_anomaly(result):

    text = str(result).lower()

    threats = [
        "error",
        "traceback",
        "denied",
        "blocked",
        "permission"
    ]

    detected = []

    for item in threats:

        if item in text:
            detected.append(item)

    if detected:

        return {
            "anomaly": True,
            "threats": detected,
            "severity": "high"
        }

    return {
        "anomaly": False,
        "threats": [],
        "severity": "clean"
    }
