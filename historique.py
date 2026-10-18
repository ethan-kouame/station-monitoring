import sqlite3

connexion = sqlite3.connect ("station.db")
curseur = connexion.cursor()

curseur.execute("SELECT id, temperature, date FROM mesures")
lignes = curseur.fetchall()

print ("Historiquie :", len(lignes), "mesures enregistrées")

for ligne in lignes :
    print("n°", ligne[0], "|", ligne[2], "|", ligne[1], "°C")

connexion.close()