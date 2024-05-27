# Projet pour tester le module bcrypt, qui va hash les passwords
import bcrypt

password = input('Veuillez entrer le mot de passe a crypter :').encode('utf-8')
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
hashed_password = print('Le mot de passe une fois crypté donnera donc comme resultat :', hashed)


verify = input('Veuillez entrer a nouveau le mot de passe pour valider sil est egal au HASH: ').encode('utf-8')
if bcrypt.checkpw(verify, hashed):
    print('Mot de passe CORRESPONDANT')
else:
    print('Mot de passe INCORRECT, ne correspond PAS')
