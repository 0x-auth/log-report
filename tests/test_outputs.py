import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_exists():
    """The agent produced report.json."""
    assert REPORT.exists(), "report.json not found at /app/report.json"


def test_report_valid_json():
    """report.json is valid JSON."""
    text = REPORT.read_text()
    assert text.strip(), "report.json is empty"
    try:
        json.loads(text)
    except json.JSONDecodeError as e:
        raise AssertionError(f"report.json is not valid JSON: {e}")


def test_report_required_keys():
    """report.json contains total_requests, unique_ips, top_path."""
    data = json.loads(REPORT.read_text())
    for key in ("total_requests", "unique_ips", "top_path"):
        assert key in data, f"missing key: {key}"


def test_total_requests():
    """total_requests is correct (6 lines in access.log)."""
    data = json.loads(REPORT.read_text())
    assert data["total_requests"] == 6, f"expected 6, got {data['total_requests']}"


def test_unique_ips():
    """unique_ips is correct (3 distinct IPs)."""
    data = json.loads(REPORT.read_text())
    assert data["unique_ips"] == 3, f"expected 3, got {data['unique_ips']}"


def test_top_path():
    """top_path is /index.html (3 hits, most frequent)."""
    data = json.loads(REPORT.read_text())
    assert data["top_path"] == "/index.html", f"expected /index.html, got {data['top_path']}"
