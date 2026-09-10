from src.main import run_simulation

def test_run_simulation_basic():
    cfg = {"scenario": "test_serval", "units": 3}
    res = run_simulation(cfg)
    assert res["status"] == "ok"
    assert res["config"] == cfg
