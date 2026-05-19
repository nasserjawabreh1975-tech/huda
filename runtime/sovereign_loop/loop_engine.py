from autonomous_core.self_expand import autonomous_decision
from execution.firewall_executor import execute
from telemetry.event_bus import record_event
from cognitive_intake.file_observer import scan_workspace
from mission_core.mission_queue import next_mission

def run_cycle():

    mission = next_mission()

    if mission:
        print("\n[MISSION]", mission)

    observed = scan_workspace()

    print("\n[OBSERVED FILES]", len(observed))

    decision = autonomous_decision()

    print("\n[AUTONOMOUS]", decision)

    result = execute(decision["command"])

    print("\n[RESULT]", result)

    record_event({
        "type": "autonomous_execution",
        "decision": decision,
        "result": result,
        "observed_files": len(observed)
    })

    return {
        "mission": mission,
        "decision": decision,
        "result": result,
        "observed_files": observed[:5]
    }
