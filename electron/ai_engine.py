import time
import random
from datetime import datetime

while True:

    reactor = random.choice(["STABLE","OPTIMAL","CONTROLLED"])
    cooling = random.choice(["ACTIVE","NORMAL","SECURE"])
    telemetry = random.choice(["ONLINE","CONNECTED","SYNCHRONIZED"])

    print("")
    print("===================================")
    print(" HUDA NUCLEAR AI ANALYSIS ENGINE ")
    print("===================================")
    print("")
    print("TIME:", datetime.now())
    print("")
    print("REACTOR STATUS:", reactor)
    print("COOLING SYSTEM:", cooling)
    print("TELEMETRY:", telemetry)
    print("")
    print("SYSTEM OPERATING NORMALLY")
    print("")

    time.sleep(5)
