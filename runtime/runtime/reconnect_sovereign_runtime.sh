#!/bin/bash

BASE="$HOME/HUDA_CORE"

echo "======================================"
echo "HUDA SOVEREIGN RUNTIME RECONNECT"
echo "======================================"

cd "$BASE" || exit 1

echo "[1] STOPPING FALLBACK LOOPS..."
pkill -f sovereign_runtime_boot.py 2>/dev/null
pkill -f "while true" 2>/dev/null

sleep 2

echo "[2] SEARCHING FOR REAL PRODUCTION RUNTIME..."

ORCH=$(find "$BASE" -type f \( \
-name "engine.py" -o \
-name "main.py" -o \
-name "runtime.py" -o \
-name "executor.py" -o \
-name "supervisor.py" \
\) | head -n 1)

if [ -z "$ORCH" ]; then
    echo "NO ORCHESTRATOR FOUND"
    exit 1
fi

echo "FOUND:"
echo "$ORCH"

echo "[3] BUILDING NEW SOVEREIGN ENTRYPOINT..."

cat > "$BASE/sovereign_runtime_boot.py" << PY
import subprocess
import time

TARGET = "$ORCH"

print("HUDA PRODUCTION RUNTIME CONNECTED")
print("TARGET:", TARGET)

while True:
    try:
        process = subprocess.Popen(
            ["python3", TARGET]
        )

        process.wait()

        print("RUNTIME STOPPED -> RESTARTING")
        time.sleep(5)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(5)
PY

echo "[4] STARTING REAL RUNTIME..."

python3 "$BASE/sovereign_runtime_boot.py"

