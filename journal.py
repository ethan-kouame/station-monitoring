import sqlite3

connexion = sqlite3.connect("station.db")
curseur = connexion.cursor()

curseur.execute("SELECT date, identifiant, action, ip FROM audit_logs ORDER BY id DESC")
lignes = curseur.fetchall()

print("Journal des connexions :", len(lignes), "évènements")
for ligne in lignes:
    print (ligne[0], "|", ligne[1], "|", ligne[2], "|", ligne[3])
connexion.close()