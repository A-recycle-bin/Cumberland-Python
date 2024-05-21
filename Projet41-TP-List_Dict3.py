#Exercice 3: Fusion de Listes et Dictionnaires

#Créez deux listes noms et ages contenant des noms et des âges
#respectivement.
noms = ('Alice', 'Bob', 'Cimon')
age = ('8', '55', '101')

#Créez un dictionnaire appelé personnes en associant chaque nom à son âge
#correspondant.
personnes = dict(zip(noms,age))

#Affichez le dictionnaire personnes.
print(personnes)

#Ajoutez une nouvelle personne au dictionnaire en utilisant une saisie
#utilisateur pour le nom et l'âge.
add_nom = input('Entrez votre nom :')
add_age = input('Entrez votre age :')
personnes[add_nom] = add_age
#Affichez à nouveau le dictionnaire personnes après l'ajout.
print(personnes)