###### README.md >> markdown

<p align="center">

  <img src="https://img.shields.io/badge/ServalFR-Simulation_Logistique-4B5320?style=for-the-badge" />

  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" />

  <img src="https://img.shields.io/badge/Status-Actif-purple?style=for-the-badge" />

</p>

# ServalFR
ServalFR est un projet de simulation/logistique d'armement orienté défense française :
- Module d’armement : analyse, organisation, modélisation de scénarios et lancement.

### Objectifs
- Simuler des scénarios de déploiement ou d’appui logistique.
- Fournir des outils d’analyse pour des exercices ou études.
- Servir de base à un projet académique ou open‑source.

### Structure du projet
```text
ServalFR/
│
├── pyproject.toml
├── README.md
├── src/
│   ├── README.md 
│   └── servalfr/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── README.md 
│   └── test_main.py
└── .github/
    └── workflows/
        └── ci.yml
```

### Technologies
- Python 3.x
- pytest
- (optionnel) FastAPI pour une API
- (optionnel) Interface web (Vue/React)
