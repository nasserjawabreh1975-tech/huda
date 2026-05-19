DNA_REGISTRY = {
    "planner": {
        "allowed_interfaces": [
            "build_plan"
        ],
        "trust_level": 95,
        "genetic_signature": "DNA-PLANNER-001"
    },

    "governance": {
        "allowed_interfaces": [
            "approve_action"
        ],
        "trust_level": 100,
        "genetic_signature": "DNA-GOV-001"
    },

    "execution": {
        "allowed_interfaces": [
            "execute"
        ],
        "trust_level": 90,
        "genetic_signature": "DNA-EXEC-001"
    }
}

def validate_module(module_name):

    if module_name not in DNA_REGISTRY:

        return {
            "valid": False,
            "reason": "unknown genetic signature"
        }

    return {
        "valid": True,
        "dna": DNA_REGISTRY[module_name]
    }
