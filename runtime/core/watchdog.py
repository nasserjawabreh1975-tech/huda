import os
import time

while True:
    if not os.path.exists(os.path.expanduser("~/HUDA_SOVEREIGN_RUNTIME")):
        os.makedirs(os.path.expanduser("~/HUDA_SOVEREIGN_RUNTIME"), exist_ok=True)

    time.sleep(20)
