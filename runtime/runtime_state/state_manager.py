STATE = {
    "active_missions": 0,
    "anomaly_count": 0,
    "blocked_payloads": 0,
    "runtime_health": "stable",
    "trust_mode": "normal"
}

def get_state():

    return STATE

def update_state(key, value):

    STATE[key] = value

def increment(key):

    if key not in STATE:
        STATE[key] = 0

    STATE[key] += 1
