print("=" * 70)
print("EMBEDDING ENGINE ACTIVE")
print("=" * 70)

EMBEDDINGS = [
    "project_documents",
    "engineering_memory",
    "claims_memory",
    "runtime_context"
]

for e in EMBEDDINGS:
    print("EMBED =>", e)
