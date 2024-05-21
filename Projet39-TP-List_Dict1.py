# TP sur les dictionnaires et les listes

#Exercice 1: Manipulation de Listes

#Créez une liste appelée nombres contenant les entiers de 1 à 5.
liste = [1,2,3,4,5]

#Ajoutez les entiers de 6 à 10 à la fin de la liste.
liste2 = [6,7,8,9,10]
newliste = liste + liste2

#Affichez la longueur de la liste.
print(len(newliste))

#Supprimez le nombre 3 de la liste.
newliste.pop(5)

#Triez la liste dans l'ordre décroissant.
decroissant = sorted(newliste, reverse=True)

#Affichez la liste résultante.
print(decroissant)