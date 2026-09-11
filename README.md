###### README.md >> markdown

---

<p align="center">

  <img src="https://img.shields.io/badge/ServalFR-Simulation_Logistique-4B5320?style=for-the-badge" />

  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" />

  <img src="https://img.shields.io/badge/Status-Actif-purple?style=for-the-badge" />

</p>

---

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

---

### ⚙️ Fonctionnalités
- Simulation logistique simple (scénarios, unités, paramètres).  
- Architecture Python moderne (src/servalfr/).  
- Tests automatiques via pytest.  
- CI GitHub Actions multi‑Python (3.10 → 3.12).  
- Packaging moderne via pyproject.toml.  

### Technologies
- Python 3.x
- pytest
- (optionnel) FastAPI pour une API
- (optionnel) Interface web (Vue/React)


### 📦 Installation
- Mode développement (recommandé)
```bash
pip install -e .
```

- Vérification
```bash
python -c "import servalfr; print(servalfr.run_simulation({'scenario':'test'}))"
```

---

### 🚀 Utilisation
- Exemple minimal
```python
from servalfr.main import run_simulation

config = {"scenario": "serval_exercice", "units": 12}
result = run_simulation(config)

print(result)
```

- Sortie typique
```json
{
  "status": "ok",
  "scenario": "serval_exercice",
  "units": 12,
  "config": {"scenario": "serval_exercice", "units": 12}
}
```

---

### 🧪 Tests
- Les tests se trouvent dans le dossier tests/.
Exécution :
```bash
pytest -q
```

---

### 🔓 Pour la section License
- The Unlicense
   - Ce projet est placé dans le domaine public via The Unlicense.
   - Vous êtes libre d’utiliser, modifier, distribuer ou vendre ce logiciel
   - sans aucune restriction.
   - Le code est fourni “tel quel”, sans garantie.

---

### 🐺 Auteur
- The MadDoG.tmdg / Major Hamblin  
- Ingénierie Python
   - Architecture militaire
   - Simulation logistique
