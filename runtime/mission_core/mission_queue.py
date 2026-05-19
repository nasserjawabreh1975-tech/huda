MISSIONS = [
    {
        "id": 1,
        "goal": "scan files",
        "status": "pending"
    }
]

def next_mission():

    for mission in MISSIONS:

        if mission["status"] == "pending":

            mission["status"] = "active"

            return mission

    return None
