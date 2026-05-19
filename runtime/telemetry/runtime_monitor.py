
import os
import time
from datetime import datetime

while True:

    os.system("clear")

    print("="*50)
    print(" HUDA TELEMETRY ")
    print("="*50)

    print(f"[TIME] {datetime.now()}")

    os.system("free -h")
    os.system("df -h /")

    time.sleep(20)
