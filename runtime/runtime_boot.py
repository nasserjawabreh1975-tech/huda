from cognitive_intake.intake_firewall import analyze_payload
from governance.governance_kernel import approve_action
from planner.master_planner import build_plan
from execution.firewall_executor import execute
from adaptive_learning.learning_engine import absorb_pattern
from immune_system.immune_engine import detect_anomaly
from recovery_oversight.recovery import recovery_action
from runtime_state.state_manager import get_state
from sovereign_memory.memory_core import get_memory
from telemetry.audit_spin import get_events
from autonomous_core.self_expand import autonomous_decision
from sovereign_loop.recursive_runtime import recursive_cycle

payload = "list files"

intake = analyze_payload(payload)
print("\nINTAKE:", intake)

approval = approve_action(payload, intake)
print("\nGOVERNANCE:", approval)

plan = build_plan(payload)
print("\nPLAN:", plan)

result = execute(plan["steps"][0]["command"])
print("\nEXECUTION:", result)

learning = absorb_pattern(result)
print("\nLEARNING:", learning)

immune = detect_anomaly(result)
print("\nIMMUNE:", immune)

recovery = recovery_action(immune)
print("\nRECOVERY:", recovery)

state = get_state()
print("\nSTATE:", state)

memory = get_memory()
print("\nMEMORY:", memory)

events = get_events()
print("\nEVENTS:", events)

decision = autonomous_decision()
print("\nAUTONOMOUS:", decision)

print("\n=== RECURSIVE LOOP ACTIVE ===")

recursive_cycle()
