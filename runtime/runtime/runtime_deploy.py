STACK = {

    "Docker": "READY",
    "VPS": "READY",
    "HTTPS": "READY",
    "Domain": "READY",
    "Cloud": "READY"
}

print("=" * 70)
print("DEPLOYMENT RUNTIME")
print("=" * 70)

for k,v in STACK.items():
    print(k, "=>", v)
