import os
import time

while True:
    runtime = os.path.expanduser("~/HUDA_SOVEREIGN_RUNTIME")
    if not os.path.exists(runtime):
        os.makedirs(runtime, exist_ok=True)
    time.sleep(30)
