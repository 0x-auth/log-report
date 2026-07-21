import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_exists():
    # criterion 1: /app/report.json exists and contains valid JSON
    assert REPORT.exists(), "report.json not found at /app/report.json"


def test_report_valid_json():
    # criterion 1: /app/report.json exists and contains valid JSON
    text = REPORT.read_text()
    assert text.strip(), "report.json is empty"
    try:
        json.loads(text)
    except json.JSONDecodeError as e:
        raise AssertionError(f"report.json is not valid JSON: {e}")


def test_report_required_keys():
    # criteria 2, 3, 4: total_requests, unique_ips, top_path must all be present
    data = json.loads(REPORT.read_text())
    for key in ("total_requests", "unique_ips", "top_path"):
        assert key in data, f"missing key: {key}"


def test_total_requests():
    # criterion 2: total_requests is an integer count of all log lines
    data = json.loads(REPORT.read_text())
    assert data["total_requests"] == 6, f"expected 6, got {data['total_requests']}"


def test_unique_ips():
    # criterion 3: unique_ips is an integer count of distinct client IP addresses
    data = json.loads(REPORT.read_text())
    assert data["unique_ips"] == 3, f"expected 3, got {data['unique_ips']}"


def test_top_path():
    # criterion 4: top_path is the URL path with the most requests
    data = json.loads(REPORT.read_text())
    assert data["top_path"] == "/index.html", f"expected /index.html, got {data['top_path']}"
