from __future__ import annotations

import subprocess
import sys


COMMANDS = [
    [sys.executable, "-m", "compileall", "-q", "prototypes", "tools"],
    [sys.executable, "tools/validate_mvp_schemas.py"],
    [sys.executable, "tools/validate_mvp_examples.py"],
    [sys.executable, "tools/run_tool_gateway_example.py", "all"],
    [sys.executable, "tools/test_tool_gateway_runner.py"],
]


def main() -> int:
    for command in COMMANDS:
        print("+", " ".join(command))
        subprocess.run(command, check=True)

    print("All local checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
