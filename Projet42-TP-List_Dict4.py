# Exercice 4: Recherche dans une Liste de Dictionnaires

# Créez une liste de dictionnaires représentant des étudiants. Chaque
#dictionnaire devrait avoir les clés "nom" et "note".
nom = ('Alice', 'Bob', 'Cimon')
note = (9, 98, 97)
bulletin = dict(zip(nom,note))
#Affichez les noms des étudiants ayant obtenu une note supérieure ou égale à
#10.
reussite = dict((nom, note) for nom, note in bulletin.items() if note >= 10)
print(reussite)