import os

IGNORED = [
    "__pycache__",
    ".git",
    ".venv"
]

def scan_workspace(base="."):

    observed = []

    for root, dirs, files in os.walk(base):

        dirs[:] = [d for d in dirs if d not in IGNORED]

        for f in files:

            path = os.path.join(root, f)

            observed.append({
                "file": path,
                "size": os.path.getsize(path)
            })

    return observed
