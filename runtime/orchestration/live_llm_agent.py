import requests
import json
import time

MODEL = "llama3"

PROMPTS = [
    "Analyze runtime stability",
    "Optimize agent coordination",
    "Evaluate governance integrity",
    "Improve planning strategy",
    "Simulate recursive reasoning"
]

print("=" * 60)
print("LIVE LLM EXECUTION")
print("=" * 60)

for prompt in PROMPTS:

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        data = response.json()

        output = data.get("response", "")

        print("\nPROMPT =>", prompt)
        print("STATUS => SUCCESS")
        print("OUTPUT =>", output[:300])

    except Exception as e:

        print("\nPROMPT =>", prompt)
        print("STATUS => FAILED")
        print("ERROR =>", str(e))

    time.sleep(1)

print("\n" + "=" * 60)
print("LIVE LLM LOOP COMPLETE")
print("=" * 60)
