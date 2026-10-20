from flask import Flask, request, session, redirect
from werkzeug.security import check_password_hash
import sqlite3
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
def initialiser_base():
    connexion = sqlite3.connect("station.db")
    curseur = connexion.cursor()
    curseur.execute("CREATE TABLE IF NOT EXISTS audit_logs (id INTEGER PRIMARY KEY, date TEXT, identifiant TEXT, action TEXT, ip TEXT)")
    connexion.commit()
    connexion.close()

initialiser_base()
def journaliser (identifiant, action):
    connexion = sqlite3.connect("station.db")
    curseur = connexion.cursor()
    curseur.execute(
        "INSERT INTO audit_logs (date, identifiant, action, ip) VALUES (datetime('now', 'localtime'), ?, ?, ?)",
        [identifiant, action, request.remote_addr]
    )
    connexion.commit()
    connexion.close()


@app.route("/")
def acceuil():
    if "utilisateur" not in session:
        return redirect("/login")
    
    connexion = sqlite3.connect("station.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT id, temperature, date FROM mesures ORDER BY id DESC LIMIT 10 ")
    lignes = curseur.fetchall()
    connexion.close()

    page = "<style>"
    page += "body { font-family: Arial; background: #f4f6f8; padding: 20px; }"
    page += "h1 { color: #1a5276; }"
    page += "li { background: white; margin: 6px 0; padding: 10px; border-radius: 8px; list-style:none; }"
    page += ".alerte { background : #fadbd8; color: #922b21; font-weight: bold;  }"
    page += "</style>"


    page += "<h1>Station de monitoring</h1>"
    page += "<p><a href='/logout'>Se déconnecter</a></p>"
    page += "<p>Les 10 dernières mesures :</p>"
    page += "<ul>"
    for ligne in lignes:
        if ligne [1] > 30:
            page += "<li class='alerte'>⚠️ " + ligne[2] + " : " + str(ligne[1]) + " °C</li>"
        else:
            page += "<li>" + ligne[2] + " : " + str(ligne[1]) + " °C</li>"
    page += "</ul>"
    return page


@app.route("/login", methods=["GET", "POST"])
def login():
    message=""
    if request.method == "POST":
        identifiant = request.form["identifiant"]
        mot_de_passe = request.form["mot_de_passe"]
        if identifiant == config.IDENTIFIANT and check_password_hash(config.MOT_DE_PASSE_HASH, mot_de_passe):
            journaliser(identifiant, "LOGIN_SUCCESS")
            session["utilisateur"] = identifiant
            return redirect ("/")
        else:
            journaliser(identifiant, "LOGIN_FAIL")
            message = "Identifiant ou mot de passe incorrect"

    page = "<h1>Connexion</h1>"
    page += "<form method='post'>"
    page += "<p>Identifiant : <input name='identifiant'> </p>"
    page += "<p>Mot_de_passe : <input name='mot_de_passe'type='password'> </p>"
    page += "<button type='submit'>Se connecter</button>"
    page += "</form>"
    page += "<p>" + message + "</p>"
    return page

@app.route("/logout")
def logout():
    journaliser(session.get("utilisateur"), "LOGOUT")
    session.clear()
    return redirect("/login")

app.run(debug=True)