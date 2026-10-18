import secrets
from werkzeug.security import generate_password_hash

mot_de_passe = input("Choisis ton mot de passe : ")

print("Empreinte du mot de passe :")
print(generate_password_hash(mot_de_passe))

print("Clé secrète: ")
print(secrets.token_hex(32))
