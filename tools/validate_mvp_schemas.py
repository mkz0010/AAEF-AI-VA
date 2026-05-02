from __future__ import annotations

import json
from pathlib import Path

REQUIRED_SCHEMA_FILES = [
    Path("schemas/tool-action-request.schema.json"),
    Path("schemas/authorization-decision.schema.json"),
    Path("schemas/tool-execution-result.schema.json"),
    Path("schemas/evidence-record.schema.json"),
]

REQUIRED_TOP_LEVEL_KEYS = {"$schema", "title", "type", "properties", "required"}

def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_SCHEMA_FILES:
        if not path.exists():
            errors.append(f"Missing schema file: {path}")
            continue

        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid JSON in {path}: {exc}")
            continue

        missing = REQUIRED_TOP_LEVEL_KEYS - set(data.keys())
        if missing:
            errors.append(f"{path} is missing top-level keys: {sorted(missing)}")

        if data.get("type") != "object":
            errors.append(f"{path} must define an object schema")

        if data.get("additionalProperties") is not False:
            errors.append(f"{path} must set additionalProperties to false")

    if errors:
        print("MVP schema validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("MVP schema validation passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
