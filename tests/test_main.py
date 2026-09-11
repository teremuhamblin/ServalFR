import pytest
from servalfr.main import run_simulation

def test_run_simulation_basic():
    config = {"scenario": "serval_exercice", "units": 12}
    result = run_simulation(config)

    assert isinstance(result, dict)
    assert result["status"] == "ok"
    assert result["scenario"] == "serval_exercice"
    assert result["units"] == 12
    assert result["config"] == config


def test_run_simulation_missing_fields():
    config = {}
    result = run_simulation(config)

    assert result["scenario"] == "unknown"
    assert result["units"] == 0
