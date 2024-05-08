# Exercice 4 Types de donnees

# Creation dune liste avec les jours de la semaine.
# Afficher celle-ci avec une boucle for
semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
for i in semaine:
    print(i)
print('\n\n')

# Creation dun tuple avec les mois de l annee
mois = ('Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre')
m = 0
while m < len(mois):
  print(mois[m])
  i = i + 1

# Creation dun dictionnaire avec la capitale des pays
capitale = {
    'Canada': 'Ottawa',
    'USA': 'Washington',
    'République-tchèque': 'Prague',
    'Qatar':	'Doha',
    'Roumanie':	'Bucarest',
    'Royaume-Uni':	'Londres'
}
print(capitale)
capitale.update({'Quebec' = 'Quebec'})
print(capitale)
