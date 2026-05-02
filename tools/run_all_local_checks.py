from __future__ import annotations

import subprocess
import sys


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> int:
    run([sys.executable, "-m", "compileall", "-q", "prototypes", "tools"])
    run([sys.executable, "tools/validate_mvp_schemas.py"])
    run([sys.executable, "tools/validate_mvp_examples.py"])
    run([sys.executable, "tools/run_tool_gateway_example.py", "all"])
    run([sys.executable, "tools/test_tool_gateway_runner.py"])
    run([sys.executable, "tools/test_tool_gateway_adapters.py"])
    print("All local checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
