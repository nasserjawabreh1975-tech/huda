print("=" * 70)
print("CELERY DISTRIBUTED WORKERS")
print("=" * 70)

WORKERS = [
    "engineering_worker",
    "claims_worker",
    "planning_worker",
    "analysis_worker"
]

for w in WORKERS:
    print("WORKER =>", w)
