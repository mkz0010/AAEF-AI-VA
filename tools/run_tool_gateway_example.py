from __future__ import annotations

import runpy
import sys
from pathlib import Path

RUNNER = Path("prototypes/tool-gateway/runner.py")

if not RUNNER.exists():
    raise SystemExit(f"Missing runner: {RUNNER}")

sys.argv = [str(RUNNER), *sys.argv[1:]]
runpy.run_path(str(RUNNER), run_name="__main__")
