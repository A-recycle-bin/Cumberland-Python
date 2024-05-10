# Creer une fonction qui calcule lexponentielle dun nombre
# x = nombre a calculer l exponentielle
# K = le nombre d iteration (simulation de l infini)

# Les fonctions puissance et factorielle sont reutilisés dans ce script
# La deuxieme fonction est calculé avec le module math de python

# x exposant k / factoriel k


def fonc_puissance(x,k):
    res_puissance = pow(x,k)
    return res_puissance


def fonc_factorielle(k):
    a = 1
    for i in range(2,k+1):
        a *= i
    return a


def fonc_exponentielle():
    x = int(input('\n[+] Veuillez entrer la valeur de x :'))
    k = int(input('\n[+] Veuillez entrer la valeur de k :'))
    k = 0
    res = 0
    while k <= x :
        res = res + fonc_puissance(x, k) / fonc_factorielle(k)
        k = k + 1
        print(res)


fonc_exponentielle()

# Avec le module math et la fonction .exp

#import math

#exponent = 3
#print ("La valeur exponentielle est : ", math.exp(exponent))