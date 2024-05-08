# Exercice 4 Types de donnees

# Creation dune liste avec les jours de la semaine.
# Afficher celle-ci avec une boucle for
semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
for i in semaine:
    print(i)

print()



# Creation dun tuple avec les mois de l annee
# Afficher les tuples avec une boucle while
mois = ('Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre')
m = 0
while m < len(mois):
  print(mois[m])
  m = m + 1

print()

# Creation dun dictionnaire avec la capitale des pays
# Afficher la liste, ajouter une entrée et afficher a nouveau
capitale = {
    'Canada': 'Ottawa',
    'USA': 'Washington',
    'République-tchèque': 'Prague',
    'Qatar':	'Doha',
    'Roumanie':	'Bucarest',
    'Royaume-Uni':	'Londres'
}
print('La liste des capitales est la suivante:\n',capitale)
print()
capitale.update({'Quebec': 'Quebec'})
print('La liste des capitales MISE A JOUR est la suivante:\n',capitale)

