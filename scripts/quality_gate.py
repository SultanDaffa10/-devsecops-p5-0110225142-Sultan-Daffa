import json
import sys
from pathlib import Path


REPORT = Path("bandit-report.json")


def main():
    if not REPORT.exists():
        print("QUALITY GATE FAILED: Bandit report not found.")
        return 1

    try:
        report = json.loads(REPORT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"QUALITY GATE FAILED: Invalid report: {error}")
        return 1

    findings = [
        result
        for result in report.get("results", [])
        if result.get("issue_severity") == "HIGH"
        and result.get("issue_confidence") == "HIGH"
    ]

    if findings:
        print(f"QUALITY GATE FAILED: {len(findings)} critical finding(s).")
        for finding in findings:
            print(
                f"- {finding.get('filename')}:{finding.get('line_number')} "
                f"{finding.get('issue_text')}"
            )
        return 1

    print("QUALITY GATE PASSED: No HIGH/HIGH findings detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())