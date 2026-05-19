#!/bin/bash

while true
do

    if ! pgrep -f runtime_boot.py > /dev/null
    then
        echo "[WATCHDOG] RESTARTING HUDA..."
        nohup python3 ~/HUDA_SOVEREIGN_RUNTIME/runtime/runtime_boot.py > /dev/null 2>&1 &
    fi

    sleep 20

done
