from time import sleep

from autonomous_core.self_expand import autonomous_decision
from execution.firewall_executor import execute
from telemetry.audit_spin import record_event

def recursive_cycle():

    while True:

        decision = autonomous_decision()

        print("\n[AUTONOMOUS]", decision)

        command = decision.get("command")

        if not command:

            sleep(2)
            continue

        result = execute(command)

        print("\n[RESULT]", result)

        record_event({
            "type": "autonomous_execution",
            "decision": decision,
            "result": result
        })

        sleep(3)
