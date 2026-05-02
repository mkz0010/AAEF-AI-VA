from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from sanitizer import SanitizerError, sanitize_raw_artifact, sanitize_text, validate_sanitized_artifact


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_sanitizer_error(fn, message: str) -> None:
    try:
        fn()
    except SanitizerError:
        return
    raise AssertionError(message)


def main() -> int:
    sample = (
        "Authorization: Bearer abcdefghijklmnopqrstuvwxyz\n"
        "Cookie: sessionid=abc123456789\n"
        "Set-Cookie: sessionid=def987654321\n"
        "password=hunter2 csrf_token=tok_1234567890abcdef api_key=abcdef1234567890\n"
        "internal 192.168.10.5 and 10.0.0.1"
    )

    sanitized, redactions = sanitize_text(sample)

    assert_true("Authorization: Bearer" not in sanitized, "authorization header should be redacted")
    assert_true("Cookie:" not in sanitized, "cookie header should be redacted")
    assert_true("Set-Cookie:" not in sanitized, "set-cookie header should be redacted")
    assert_true("hunter2" not in sanitized, "password value should be redacted")
    assert_true("192.168.10.5" not in sanitized, "private IP should be redacted")
    assert_true(len(redactions) >= 5, "expected multiple redactions")

    raw = {
        "request": sample,
        "nested": {
            "response": "csrf_token=tok_1234567890abcdef\nSet-Cookie: sessionid=secretsecret\n",
        },
        "list": ["Authorization: Bearer zyxwvutsrqponmlkjihgfedcba"],
    }

    artifact = sanitize_raw_artifact(
        raw,
        raw_artifact_ref="private-not-in-git/raw-artifacts/zap/demo.json",
        sanitized_artifact_ref="private-not-in-git/sanitized-artifacts/zap/demo.json",
    )

    assert_true(artifact["sanitizer_status"] == "completed", "sanitizer should complete")
    assert_true(artifact["secret_exposed_to_ai"] is False, "secret exposure flag should be false")
    assert_true(artifact["ai_visible_allowed"] is True, "AI-visible should be allowed after sanitizer")
    assert_true(artifact["redaction_count"] >= 5, "redaction count should be populated")
    validate_sanitized_artifact(artifact)

    expect_sanitizer_error(
        lambda: sanitize_raw_artifact(
            raw,
            raw_artifact_ref="tracked/raw.json",
            sanitized_artifact_ref="private-not-in-git/sanitized.json",
        ),
        "tracked raw path should fail closed",
    )

    expect_sanitizer_error(
        lambda: validate_sanitized_artifact(
            {
                "sanitizer_status": "completed",
                "secret_exposed_to_ai": False,
                "ai_visible_allowed": True,
                "sanitized_content": {"leak": "Authorization: Bearer abcdefghijklmnopqrstuvwxyz"},
            }
        ),
        "forbidden literal should fail sanitized validation",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_sanitized_artifact_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "sanitized-artifacts" / "demo" / "sanitized-artifact.generated.json"
    assert_true(generated.exists(), "generated sanitized artifact missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["sanitizer_status"] == "completed", "generated artifact should be completed")
    assert_true(data["secret_exposed_to_ai"] is False, "generated artifact should not expose secret")
    assert_true(data["redaction_count"] >= 1, "generated artifact should include redactions")

    print("Sanitizer redaction policy tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
