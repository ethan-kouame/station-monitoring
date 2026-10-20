# 🌡️ Station de monitoring

Projet personnel d'apprentissage : une station qui mesure la température,
enregistre l'historique et l'affiche sur un site web protégé par mot de passe.

## Fonctionnalités

- **Capteur simulé** en Python, avec alerte au-delà de 30 °C
- **Base de données SQLite** : chaque mesure est horodatée et conservée
- **Site web Flask** : les 10 dernières mesures, alertes surlignées en rouge
- **Connexion sécurisée** : sessions, déconnexion, mot de passe haché

## Architecture

```
capteur.py  ──►  station.db (SQLite)  ──►  app.py (Flask)  ──►  navigateur
```

## Sécurité

- Mot de passe jamais stocké en clair : seule son **empreinte** (scrypt avec sel) est conservée
- **Secrets séparés du code** dans `config.py`, exclu de Git par `.gitignore`
- Message d'erreur de connexion volontairement vague, contre l'énumération des comptes
- Requêtes SQL **paramétrées** (`?`), contre l'injection SQL

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

## Feuille de route

- [x] Capteur simulé, base de données, site web, connexion sécurisée
- [ ] Vrai capteur (ESP32 + DHT22) connecté en Wi-Fi
- [ ] Journal des connexions et limitation des tentatives
- [ ] Détection d'anomalies par apprentissage automatique

## Auteur

**Ethan Kouamé**, étudiant ingénieur en systèmes d'information (ESME)