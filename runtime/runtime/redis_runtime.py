print("=" * 70)
print("REDIS DISTRIBUTED CACHE")
print("=" * 70)

CACHE = [
    "agent_runtime",
    "runtime_queue",
    "decision_cache",
    "memory_cache"
]

for c in CACHE:
    print("CACHE =>", c)
