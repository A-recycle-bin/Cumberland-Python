#Exercice 2: Manipulation de Dictionnaires

#Créez un dictionnaire appelé personne avec les clés "nom", "âge" et "ville"
#contenant vos propres informations.
personne = {'nom': 'Cimon', 'age': '31', 'ville': 'Les éboulements'}
#Affichez la valeur associée à la clé "âge".
print(personne['age'])
#Modifiez la valeur associée à la clé "ville" pour "Paris".
personne['ville'] = 'Paris'
#Ajoutez une nouvelle paire clé-valeur au dictionnaire pour représenter le sexe
#de la personne.
personne['sexe'] = 'homme'
#Supprimez la clé "ville" du dictionnaire.
personne.pop('ville')
#Affichez le dictionnaire résultant.
print(personne)