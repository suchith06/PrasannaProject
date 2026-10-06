import subprocess
import sys


def run_step(name, command):
    print(f"\n{'=' * 50}")
    print(f"Running: {name}")
    print("=" * 50)

    result = subprocess.run(command)

    if result.returncode != 0:
        print(f"\nFAILED: {name}")
        sys.exit(1)

    print(f"\nSUCCESS: {name}")


print("\nSTARTING E-COMMERCE DATA PIPELINE")

run_step("EXTRACT", [sys.executable, "src/extract.py"])

run_step("TRANSFORM", [sys.executable, "src/transform.py"])

run_step(
    "DATA QUALITY TESTS",
    [sys.executable, "-m", "pytest", "tests/test_data.py", "-v"]
)

run_step("LOAD TO POSTGRESQL", [sys.executable, "src/load.py"])

print("\nPIPELINE COMPLETED SUCCESSFULLY!")