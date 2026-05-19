permissions = {
    "execution": False,
    "internet": False,
    "filesystem": False,
    "autonomous_mode": False
}

print("")
print("HUDA CONTROL PANEL")
print("")

for k,v in permissions.items():
    print(f"{k} => {v}")

while True:

    cmd = input("ENABLE PERMISSION > ")

    if cmd in permissions:

        permissions[cmd] = True

        print(f"[ENABLED] {cmd}")
