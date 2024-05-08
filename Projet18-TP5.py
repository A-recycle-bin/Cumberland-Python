# Ecrire une fonction qui va calculer la moyenne des nombres que l'on inscrit


def fonc_calcul_moyenne(a, b, c, d):
    somme = a + b + c + d
    moyenne = somme / 4
    print('La moyenne des nombres est :', moyenne)


fonc_calcul_moyenne(90, 60, 95, 70)


#Moyenne des nombres avec une boucle for
def fonc_calcul_moyenne2(nbr):
    somme = 0
    for i in nbr:
        somme += i
    moyenne =  somme / len(nbr)
    return moyenne


print('La moyenne des nombres est :', fonc_calcul_moyenne2([10,20,30,40,50]))