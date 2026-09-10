def run_simulation(config):
    """
    Simulation logistique générique ServalFR.
    Aucun calcul d’armement, uniquement organisation/scénarios.
    """
    return {"status": "ok", "config": config}


if __name__ == "__main__":
    example_config = {"scenario": "serval_exercice", "units": 12}
    result = run_simulation(example_config)
    print(result)
