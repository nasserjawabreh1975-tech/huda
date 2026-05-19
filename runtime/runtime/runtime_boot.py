import os
import time
import json
from datetime import datetime

class HUDA_RUNTIME:

    def __init__(self):

        self.state = {
            "runtime": "ACTIVE",
            "memory": "CONNECTED",
            "execution": "ONLINE",
            "governance": "ACTIVE",
            "reasoning": "ACTIVE",
            "timestamp": str(datetime.now())
        }

    def cycle(self):

        while True:

            os.system("clear")

            print("="*50)
            print(" HUDA SOVEREIGN RUNTIME ")
            print("="*50)

            for k,v in self.state.items():
                print(f"[{k.upper()}] {v}")

            with open(
                os.path.expanduser(
                    "~/HUDA_SOVEREIGN_RUNTIME/runtime/runtime_state.json"
                ),
                "w"
            ) as f:

                json.dump(self.state,f,indent=4)

            time.sleep(15)

HUDA_RUNTIME().cycle()
