DNA_REGISTRY = {

    "planner": {
        "role": "strategic_planner",
        "trust_level": 95,
        "allowed_interfaces": [
            "event_bus",
            "governance",
            "execution"
        ],
        "execution_scope": [
            "build_plan"
        ],
        "lineage": "HUDA_CORE_V1",
        "signature": "DNA-PLANNER-001"
    },

    "executor": {
        "role": "runtime_executor",
        "trust_level": 90,
        "allowed_interfaces": [
            "planner",
            "immune_system"
        ],
        "execution_scope": [
            "execute_command"
        ],
        "lineage": "HUDA_CORE_V1",
        "signature": "DNA-EXECUTOR-001"
    },

    "immune_system": {
        "role": "runtime_protection",
        "trust_level": 99,
        "allowed_interfaces": [
            "execution",
            "recovery"
        ],
        "execution_scope": [
            "detect_anomaly"
        ],
        "lineage": "HUDA_CORE_V1",
        "signature": "DNA-IMMUNE-001"
    }
}
