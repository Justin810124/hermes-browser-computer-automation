#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from hermes_operator import decide  # noqa: E402


def main() -> int:
    cases = json.loads((ROOT / "tests/operator_cases.json").read_text(encoding="utf-8"))
    failures = []

    for case in cases:
        decision = decide(case["task"], "auto")
        actual = decision.control_surface
        expected = case["expected_surface"]
        status = "PASS" if actual == expected else "FAIL"
        print(f"{status} {expected} <- {case['task']}")
        if actual != expected:
            failures.append((case["task"], expected, actual))

    if failures:
        print("\nFailures:")
        for task, expected, actual in failures:
            print(f"- expected {expected}, got {actual}: {task}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
