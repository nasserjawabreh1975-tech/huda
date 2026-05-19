import os
import json
import hashlib
from collections import defaultdict
from datetime import datetime, UTC

BASE = os.path.expanduser("~/HUDA_CORE")

PATCH_EXTENSIONS = [".sh", ".py"]

HIGH_RISK_KEYWORDS = [
    "rm -rf",
    "sudo",
    "kill -9",
    "pkill",
    "systemctl stop",
    "chmod -R 777",
    "runtime_core",
    "self_modify",
    "overwrite",
    "daemonize",
    "forkbomb",
    "RECURSIVE_SPAWN_DISABLED"
]

CORE_IDENTITY = [
    "runtime",
    "governance",
    "kernel",
    "cognitive",
    "memory",
    "orchestrator",
    "supervisor"
]

def sha256(path):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return "unknown"

def risk_score(content):
    score = 0

    for kw in HIGH_RISK_KEYWORDS:
        if kw.lower() in content.lower():
            score += 25

    if "while true" in content.lower():
        score += 20

    if content.count("subprocess") > 3:
        score += 20

    if content.count("thread") > 5:
        score += 15

    return min(score, 100)

def lineage_tags(name):
    tags = []

    for token in CORE_IDENTITY:
        if token in name.lower():
            tags.append(token)

    if "governance" in name:
        tags.append("governance")

    if "runtime" in name:
        tags.append("runtime")

    if "memory" in name:
        tags.append("memory")

    if "agent" in name:
        tags.append("agents")

    return list(set(tags))

patches = []

for root, dirs, files in os.walk(BASE):

    if "venv" in root:
        continue

    if "__pycache__" in root:
        continue

    for file in files:

        if not any(file.endswith(x) for x in PATCH_EXTENSIONS):
            continue

        path = os.path.join(root, file)

        try:
            with open(path, "r", errors="ignore") as f:
                content = f.read()
        except:
            continue

        genome = {
            "file": path,
            "hash": sha256(path),
            "risk": risk_score(content),
            "size": len(content),
            "tags": lineage_tags(file),
            "timestamp": datetime.now(UTC).isoformat()
        }

        patches.append(genome)

hash_map = defaultdict(list)

for p in patches:
    hash_map[p["hash"]].append(p["file"])

duplicates = {
    k: v for k, v in hash_map.items()
    if len(v) > 1
}

governed = []
quarantine = []

for p in patches:

    if p["risk"] >= 70:
        p["status"] = "BLOCKED"
        quarantine.append(p)

    elif p["risk"] >= 35:
        p["status"] = "REVIEW"

    else:
        p["status"] = "SAFE"

    governed.append(p)

safe_count = len([x for x in governed if x["status"] == "SAFE"])
review_count = len([x for x in governed if x["status"] == "REVIEW"])
blocked_count = len([x for x in governed if x["status"] == "BLOCKED"])

REPORT_DIR = os.path.join(BASE, "genome_reports")
os.makedirs(REPORT_DIR, exist_ok=True)

timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")

report_path = os.path.join(
    REPORT_DIR,
    f"genome_governance_{timestamp}.json"
)

with open(report_path, "w") as f:
    json.dump({
        "safe": safe_count,
        "review": review_count,
        "blocked": blocked_count,
        "duplicates": duplicates,
        "patches": governed
    }, f, indent=2)

print("=" * 60)
print("HUDA GENOME GOVERNOR")
print("=" * 60)

print()
print("TOTAL PATCHES =>", len(governed))
print("SAFE           =>", safe_count)
print("REVIEW         =>", review_count)
print("BLOCKED        =>", blocked_count)

print()
print("TOP BLOCKED PATCHES")
print("-" * 60)

blocked_sorted = sorted(
    quarantine,
    key=lambda x: x["risk"],
    reverse=True
)

for p in blocked_sorted[:20]:

    print()
    print("PATCH  =>", p["file"])
    print("RISK   =>", p["risk"])
    print("TAGS   =>", ",".join(p["tags"]))

print()
print("DUPLICATE CLUSTERS =>", len(duplicates))

print()
print("REPORT =>")
print(report_path)

print()
print("=" * 60)
print("SYSTEM MODE => EVOLUTION GOVERNANCE")
print("=" * 60)

