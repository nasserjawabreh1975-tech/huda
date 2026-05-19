USERS = {

    "admin": "AUTHORIZED",
    "engineer": "AUTHORIZED",
    "planner": "AUTHORIZED"
}

print("=" * 70)
print("AUTH ENGINE ACTIVE")
print("=" * 70)

for k,v in USERS.items():
    print(k, "=>", v)
