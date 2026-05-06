from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


VALIDATOR_NAME = "static_lab_fixture_validator"
VALIDATOR_VERSION = "v0.6.20-read-only-scaffold"

NON_AUTHORIZATION_STATEMENT = (
    "This read-only validator scaffold emits review-only results. It does not "
    "authorize execution, scanning, container-platform activity, credential injection, "
    "customer target operation, delivery, certification, legal approval, or audit opinion."
)

RUNTIME_BOUNDARY: dict[str, bool] = {
    "fixture_schema_complete": False,
    "fixture_validator_complete": False,
    "negative_tests_complete": False,
    "fixture_generated": False,
    "fixture_live_evidence": False,
    "validator_authorizes_execution": False,
    "validator_authorizes_scanning": False,
    "validator_authorizes_docker": False,
    "validator_authorizes_delivery": False,
    "docker_compose_file_created": False,
    "docker_compose_executed": False,
    "docker_image_pulled": False,
    "container_started": False,
    "port_bound": False,
    "docker_execution_authorized": False,
    "execution_authorized": False,
    "network_activity_allowed": False,
    "scan_execution_allowed": False,
    "credential_injection_permitted": False,
    "customer_target": False,
    "external_network_target": False,
    "delivery_authorized": False,
    "customer_deliverable": False,
}

PLANNED_FAILURE_CATEGORIES: tuple[str, ...] = (
    "missing_fixture_directory",
    "fixture_path_not_directory",
    "missing_manifest",
    "missing_required_node",
    "invalid_node_envelope",
    "invalid_reference",
    "invalid_trace_order",
    "missing_synthetic_data_statement",
    "missing_execution_boundary_statement",
    "secret_like_content_detected",
    "customer_like_content_detected",
    "runtime_marker_not_false",
    "runnable_configuration_detected",
    "delivery_implication_detected",
    "overclaiming_detected",
    "validator_uncertainty",
)


@dataclass(frozen=True)
class ValidationFailure:
    failure_category: str
    message: str
    blocking: bool = True
    fixture_ref: str | None = None


@dataclass(frozen=True)
class ValidationResult:
    validator_name: str
    validator_version: str
    validation_status: str
    fixture_dir: str
    failure_categories: list[str] = field(default_factory=list)
    blocking_failures: list[ValidationFailure] = field(default_factory=list)
    runtime_boundary: dict[str, bool] = field(default_factory=lambda: dict(RUNTIME_BOUNDARY))
    non_authorization_statement: str = NON_AUTHORIZATION_STATEMENT

    @property
    def blocking(self) -> bool:
        return bool(self.blocking_failures)


def _failure(category: str, message: str, fixture_ref: str | None = None) -> ValidationFailure:
    if category not in PLANNED_FAILURE_CATEGORIES:
        category = "validator_uncertainty"
    return ValidationFailure(
        failure_category=category,
        message=message,
        blocking=True,
        fixture_ref=fixture_ref,
    )


def validate_fixture_dir(fixture_dir: Path) -> ValidationResult:
    """Read-only scaffold validation for a static fixture directory.

    v0.6.20 intentionally implements only boundary-preserving behavior:
    missing/non-directory paths fail closed, and existing directories receive a
    review-only scaffold status. Full schema validation is intentionally deferred.
    """

    path = Path(fixture_dir)
    failures: list[ValidationFailure] = []

    if not path.exists():
        failures.append(
            _failure(
                "missing_fixture_directory",
                "Fixture directory does not exist. Validation fails closed.",
                str(path),
            )
        )
    elif not path.is_dir():
        failures.append(
            _failure(
                "fixture_path_not_directory",
                "Fixture path is not a directory. Validation fails closed.",
                str(path),
            )
        )

    status = "blocked" if failures else "scaffold_review_only"
    return ValidationResult(
        validator_name=VALIDATOR_NAME,
        validator_version=VALIDATOR_VERSION,
        validation_status=status,
        fixture_dir=str(path),
        failure_categories=[failure.failure_category for failure in failures],
        blocking_failures=failures,
    )


def result_to_dict(result: ValidationResult) -> dict[str, Any]:
    data = asdict(result)
    data["blocking"] = result.blocking
    return data


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Read-only static lab fixture validator scaffold. Emits review-only "
            "results and never authorizes execution."
        )
    )
    parser.add_argument(
        "--fixture-dir",
        required=True,
        help="Path to a local static fixture directory. The scaffold reads only metadata boundaries.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    result = validate_fixture_dir(Path(args.fixture_dir))
    print(json.dumps(result_to_dict(result), indent=2, sort_keys=True))
    return 1 if result.blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
