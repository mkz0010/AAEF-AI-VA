from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

SCHEMA_MAP = {
    "tool-action-request": Path("schemas/tool-action-request.schema.json"),
    "authorization-decision": Path("schemas/authorization-decision.schema.json"),
    "tool-execution-result": Path("schemas/tool-execution-result.schema.json"),
    "evidence-record": Path("schemas/evidence-record.schema.json"),
}

EXAMPLE_DIR = Path("prototypes/tool-gateway/examples")

FORBIDDEN_SECRET_FIELD_NAMES = {
    "username",
    "password",
    "api_key",
    "apikey",
    "secret",
    "secret_key",
    "session_cookie",
    "cookie",
    "authorization",
    "bearer_token",
    "vpn_password",
    "mfa_seed",
    "totp_seed",
}

def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def matches_type(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    return True

def validate_value(value: Any, schema: dict[str, Any], path: str, errors: list[str]) -> None:
    expected_type = schema.get("type")
    if expected_type is not None:
        allowed_types = expected_type if isinstance(expected_type, list) else [expected_type]
        if not any(matches_type(value, t) for t in allowed_types):
            errors.append(f"{path}: expected type {allowed_types}, got {type(value).__name__}")
            return

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected const {schema['const']!r}, got {value!r}")

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value {value!r} is not in enum {schema['enum']!r}")

    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(f"{path}: string shorter than minLength {schema['minLength']}")
        if "pattern" in schema and not re.match(schema["pattern"], value):
            errors.append(f"{path}: string does not match pattern {schema['pattern']}")

    if isinstance(value, int) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: integer below minimum {schema['minimum']}")

    if isinstance(value, dict):
        validate_object(value, schema, path, errors)

    if isinstance(value, list):
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                validate_value(item, item_schema, f"{path}[{index}]", errors)

def validate_object(obj: dict[str, Any], schema: dict[str, Any], path: str, errors: list[str]) -> None:
    required = schema.get("required", [])
    for key in required:
        if key not in obj:
            errors.append(f"{path}: missing required key {key}")

    properties = schema.get("properties", {})
    additional = schema.get("additionalProperties", True)

    for key, value in obj.items():
        if key in properties:
            validate_value(value, properties[key], f"{path}.{key}", errors)
        else:
            if additional is False:
                errors.append(f"{path}: additional property not allowed: {key}")
            elif isinstance(additional, dict):
                validate_value(value, additional, f"{path}.{key}", errors)

def validate_against_schema(instance_path: Path, schema_path: Path) -> list[str]:
    instance = load_json(instance_path)
    schema = load_json(schema_path)
    errors: list[str] = []
    validate_value(instance, schema, str(instance_path), errors)
    return errors

def detect_forbidden_secret_fields(value: Any, path: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            normalized = key.lower().replace("-", "_")
            if normalized in FORBIDDEN_SECRET_FIELD_NAMES:
                errors.append(f"{path}: forbidden secret-like field name: {key}")
            detect_forbidden_secret_fields(nested, f"{path}.{key}", errors)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            detect_forbidden_secret_fields(item, f"{path}[{index}]", errors)

def schema_for_example(path: Path) -> Path:
    name = path.name
    for token, schema_path in SCHEMA_MAP.items():
        if name.endswith(f".{token}.json"):
            return schema_path
    raise ValueError(f"Cannot determine schema for {path}")

def main() -> int:
    errors: list[str] = []
    example_files = sorted(EXAMPLE_DIR.glob("*.json"))

    if not example_files:
        errors.append(f"No example JSON files found under {EXAMPLE_DIR}")

    for example in example_files:
        try:
            schema_path = schema_for_example(example)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        if not schema_path.exists():
            errors.append(f"Missing schema file: {schema_path}")
            continue

        errors.extend(validate_against_schema(example, schema_path))

        data = load_json(example)
        detect_forbidden_secret_fields(data, str(example), errors)

        if isinstance(data, dict) and data.get("secret_exposed_to_ai") is not None:
            if data.get("secret_exposed_to_ai") is not False:
                errors.append(f"{example}: secret_exposed_to_ai must be false")

    if errors:
        print("MVP example validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"MVP example validation passed for {len(example_files)} files.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
