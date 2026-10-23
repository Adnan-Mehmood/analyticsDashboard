from pathlib import Path


def test_dashboard_exposes_core_data_helpers():
    code = Path("Analytics_Dashboard.py").read_text()
    assert "def generate_sample_data" in code
    assert "def filter_data" in code
    assert "def compute_kpis" in code
