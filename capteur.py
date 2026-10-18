import random
import time
import sqlite3


connexion = sqlite3.connect("station.db")
curseur = connexion.cursor()
curseur.execute("CREATE TABLE IF NOT EXISTS mesures (id INTEGER PRIMARY KEY, temperature REAL, date TEXT)")

print("station de monitoring : démarrage")

mesures = []

for i in range(5):
    temperature = random.uniform(18, 35)
    temperature = round (temperature, 1)
    mesures.append(temperature)

    curseur.execute("INSERT INTO mesures (temperature, date) VALUES (?, datetime('now', 'localtime'))", [temperature])
    connexion.commit()
    
    print("Mesure", i + 1, ":", temperature,"°C")
    if temperature > 30:
        print(" ⚠️ ALERTE : trop chaud !")
    time.sleep(1)

print("fin des mesures")
print("Toutes les mesures :",mesures)
print("Moyenne:", round(sum(mesures) / len(mesures),1), "°C")
print("Maximum:", max(mesures), "°C")
print("Minimum:",min(mesures), "°C")

connexion.close()