print("=" * 70)
print("REAL AI EXECUTION ENGINE")
print("=" * 70)

MODELS = {
    "planner_model": "online",
    "engineering_model": "online",
    "reasoning_model": "online",
    "execution_model": "online"
}

for k,v in MODELS.items():
    print(k, "=>", v)
