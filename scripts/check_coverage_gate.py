#!/usr/bin/env python3
"""Coverage gate with minimum, ideal target, and optional previous-baseline check."""

from __future__ import annotations

import pathlib
import sys
import xml.etree.ElementTree as ET

MINIMUM_COVERAGE = 80.0
IDEAL_COVERAGE = 95.0


def read_coverage_percentage(xml_file: pathlib.Path) -> float:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    line_rate = root.get("line-rate")
    if line_rate is None:
        raise ValueError("coverage.xml missing line-rate attribute")
    return float(line_rate) * 100.0


def read_previous_baseline(baseline_file: pathlib.Path) -> float | None:
    if not baseline_file.exists():
        return None
    raw = baseline_file.read_text(encoding="utf-8").strip()
    if not raw:
        return None
    return float(raw)


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: check_coverage_gate.py <coverage.xml> <baseline-file>")
        return 2

    coverage_file = pathlib.Path(sys.argv[1])
    baseline_file = pathlib.Path(sys.argv[2])

    current = read_coverage_percentage(coverage_file)
    previous = read_previous_baseline(baseline_file)

    print(f"Current coverage: {current:.2f}%")

    if current < MINIMUM_COVERAGE:
        print(f"ERROR: coverage below minimum threshold ({MINIMUM_COVERAGE:.2f}%).")
        return 1

    if previous is not None and current < previous:
        print(
            f"ERROR: coverage regressed: previous={previous:.2f}% current={current:.2f}%"
        )
        return 1

    if current < IDEAL_COVERAGE:
        print(f"WARNING: coverage is below ideal target ({IDEAL_COVERAGE:.2f}%).")
    else:
        print("Coverage reached ideal target.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
