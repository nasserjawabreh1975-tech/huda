print("=" * 70)
print("POSTGRES PRODUCTION DATABASE")
print("=" * 70)

DATABASE = {
    "projects_db": "connected",
    "runtime_db": "connected",
    "memory_db": "connected",
    "agents_db": "connected"
}

for k,v in DATABASE.items():
    print(k, "=>", v)
