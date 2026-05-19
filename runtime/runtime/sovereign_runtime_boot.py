import os
import time
import subprocess
from pathlib import Path

BASE = Path.home() / "HUDA_CORE"

UI_CANDIDATES = [
    BASE / "frontend",
    BASE / "hudaui",
    BASE / "hudaui",
    BASE / "ui",
]

ui_path = None

for p in UI_CANDIDATES:
    if (p / "package.json").exists():
        ui_path = p
        break

if ui_path is None:
    print("[HUDA] NO UI FOUND")
    exit()

print("\n==============================")
print("      HUDA SOVEREIGN CORE")
print("==============================\n")

os.system("pkill -f uvicorn")
os.system("pkill -f vite")
os.system("pkill -f node")

time.sleep(2)

print("[1] STARTING API")

api = subprocess.Popen(
    [
        "uvicorn",
        "backend.app:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000"
    ],
    cwd=BASE
)

time.sleep(3)

print("[2] STARTING UI")

ui = subprocess.Popen(
    [
        "npm",
        "run",
        "dev",
        "--",
        "--host",
        "0.0.0.0",
        "--port",
        "3000"
    ],
    cwd=ui_path
)

print("\n[3] SYSTEM ONLINE")
print("API  -> http://127.0.0.1:8000")
print("UI   -> http://127.0.0.1:3000\n")

api.wait()
ui.wait()
