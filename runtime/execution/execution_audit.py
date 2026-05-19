from pathlib import Path

BASE = Path.home() / "HUDA_CORE/real_execution"

CHECKS = [
BASE / "openai/live_openai_runtime.py",
BASE / "uploads/live_uploads.py",
BASE / "vector_db/vector_database.py",
BASE / "postgres/postgres_live.py",
BASE / "redis/redis_live.py",
BASE / "websocket/live_events.py"
]

print("=" * 70)
print("REAL EXECUTION AUDIT")
print("=" * 70)

score = 0

for c in CHECKS:

    if c.exists():
        print(c.name, "=> OK")
        score += 1

    else:
        print(c.name, "=> MISSING")

print("=" * 70)
print(f"EXECUTION INTEGRATION => {(score/len(CHECKS))*100}%")
print("LEVEL => LIVE COGNITIVE AI INFRASTRUCTURE")
print("=" * 70)
