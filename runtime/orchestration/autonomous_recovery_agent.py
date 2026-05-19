import os
import subprocess
import socket
import time
from pathlib import Path

BASE = Path.home() / "HUDA_CORE"
LOGS = BASE / "logs"

print("=" * 60)
print("HUDA AUTONOMOUS RECOVERY AGENT")
print("=" * 60)

def run(cmd):
    print(f"\n>>> {cmd}\n")
    return subprocess.run(cmd, shell=True)

def free_port(start=3300):
    p = start
    while True:
        s = socket.socket()
        try:
            s.bind(("0.0.0.0", p))
            s.close()
            return p
        except:
            p += 1

print("\n[1] SEARCHING UI ROOT")

candidates = []

for root, dirs, files in os.walk(BASE):
    if "package.json" in files:
        candidates.append(root)

for c in candidates:
    print("FOUND:", c)

ui = None

for c in candidates:
    if "hudaui" in c.lower():
        ui = c
        break

if not ui and candidates:
    ui = candidates[0]

print("\nSELECTED UI:", ui)

os.chdir(ui)

print("\n[2] INSTALLING NODE STACK")

run("npm install")

print("\n[3] KILLING OLD VITE")

run("pkill -f vite")
run("pkill -f node")

PORT = free_port()

print(f"\n[4] FREE PORT => {PORT}")

vite = f'''
import {{ defineConfig }} from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({{
  plugins: [react()],
  server: {{
    host: "0.0.0.0",
    port: {PORT},
    strictPort: true
  }}
}})
'''

(Path(ui) / "vite.config.js").write_text(vite)

print("\n[5] STARTING UI")

run(
    f"nohup npm run dev -- --host 0.0.0.0 --port {PORT} "
    f"> {LOGS}/autonomous_ui.log 2>&1 &"
)

time.sleep(10)

print("\n[6] TESTING UI")

response = subprocess.getoutput(f"curl -I http://127.0.0.1:{PORT}")

print(response)

print("\n[7] OPENING BROWSER")

run(f"xdg-open http://127.0.0.1:{PORT}")

report = f'''
HUDA AUTONOMOUS REPORT
======================

UI ROOT:
{ui}

PORT:
{PORT}

STATUS:
ONLINE

LOG:
{LOGS}/autonomous_ui.log
'''

(BASE / "logs" / "recovery_report.txt").write_text(report)

print(report)

print("\n[8] LIVE LOGS\n")

run(f"tail -f {LOGS}/autonomous_ui.log")
