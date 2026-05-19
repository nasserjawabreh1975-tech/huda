def analyze_payload(payload):

    result = {
        "blocked": False,
        "trust_score": 100,
        "type": "unknown"
    }

    payload = str(payload).lower()

    if "python" in payload:
        result["type"] = "python_code"

    elif "bash" in payload:
        result["type"] = "bash_code"

    elif "javascript" in payload:
        result["type"] = "javascript_code"

    dangerous = [
        "os.system",
        "subprocess",
        "rm -rf",
        "eval(",
        "__import__",
        "exec("
    ]

    for item in dangerous:

        if item in payload:
            result["blocked"] = True
            result["trust_score"] -= 100

    return result
