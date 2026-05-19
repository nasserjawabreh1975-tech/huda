import os
import importlib.util
import traceback
import json

ROOT = os.path.expanduser("~/HUDA_CORE")

IGNORE = {
    "huda_env",
    "__pycache__",
    "node_modules",
    ".git",
    "quarantine"
}

results = {
    "healthy": [],
    "broken": []
}

for path, dirs, files in os.walk(ROOT):

    dirs[:] = [d for d in dirs if d not in IGNORE]

    for file in files:

        if not file.endswith(".py"):
            continue

        full = os.path.join(path, file)

        try:

            spec = importlib.util.spec_from_file_location(
                "module.name",
                full
            )

            module = importlib.util.module_from_spec(spec)

            spec.loader.exec_module(module)

            results["healthy"].append(full)

        except Exception as e:

            results["broken"].append({
                "file": full,
                "error": str(e),
                "trace": traceback.format_exc(limit=1)
            })

report_path = os.path.join(
    ROOT,
    "reports/runtime_diagnostics.json"
)

with open(report_path, "w") as f:
    json.dump(results, f, indent=2)

print("\n=== RUNTIME DIAGNOSTICS ===\n")

print(f"HEALTHY MODULES: {len(results['healthy'])}")
print(f"BROKEN MODULES: {len(results['broken'])}")

for b in results["broken"][:50]:

    print(f"\nFILE: {b['file']}")
    print(f"ERROR: {b['error']}")

print(f"\nREPORT:")
print(report_path)
