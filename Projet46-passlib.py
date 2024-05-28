from passlib.hash import sha256_crypt, sha512_crypt, md5_crypt, des_crypt


variable = input('Entrez le mot de passe a encrypter :')

sha256 = sha256_crypt.hash(variable)
print("Le mot de passe crypté avec l'algorithme sha256 est egal a", sha256)
print()

sha512 = sha512_crypt.hash(variable)
print("Le mot de passe crypté avec l'algorithme sha512 est egal a", sha512)
print()

md5 = md5_crypt.hash(variable)
print("Le mot de passe crypté avec l'algorithme md5 est egal a", md5)
print()

des = des_crypt.hash(variable)
print("Le mot de passe crypté avec l'algorithme des est egal a", des)
print()