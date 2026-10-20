## Installation

```bash
git clone https://github.com/ethan-kouame/station-monitoring.git
cd station-monitoring
python -m pip install -r requirements.txt
python creer_secrets.py
```

Créer ensuite un fichier `config.py` à la racine du projet, avec les valeurs générées :

```python
IDENTIFIANT = "admin"
MOT_DE_PASSE_HASH = "empreinte-generee"
SECRET_KEY = "cle-generee"
```

Ce fichier contient des secrets : il est exclu de Git par `.gitignore` et ne doit jamais être publié.

Puis :

```bash
python capteur.py   # génère des mesures
python app.py       # lance le site sur http://127.0.0.1:5000
```