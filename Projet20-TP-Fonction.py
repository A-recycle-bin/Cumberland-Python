# TP sur les fonctions python

# Exercice 1 Créer une fonction qui calculera la somme de deux nombres
def fonc_somme():
    print('Cette fonction nécessite deux nombres en entrée et calculera la somme de ceux-ci\n')
    nbr1 = int(input('[+] Veuillez entrer le premier nombre : '))
    nbr2 = int(input('[+] Veuillez entrer le deuxième nombre : '))
    somme = nbr1 + nbr2
    print('\nLa somme des deux nombres est égal à : ',somme)
#fonc_somme()


# Exercice 2 Créer une fonction qui calculera le produit de deux nombres
def fonc_produit():
    print('\nCette fonction nécessite deux nombres en entrée et calculera le produit de ceux-ci\n')
    nbr3 = int(input('[+] Veuillez entrer le premier nombre : '))
    nbr4 = int(input('[+] Veuillez entrer le deuxième nombre : '))
    produit = nbr3 * nbr4
    print('\nLe produit des deux nombres est égal à :',produit)
#fonc_produit()


# Exercice 3 Converti une entrée de température Fahrenheit en celsius

def fonc_celsius():
    print('\nCette fonction converti une température Fahrenheit en Celsius\n')
    f = int(input('[+] Veuillez entrer la température Fahrenheit a convertir : '))
    c = (f-32) * 5 / 9
    print('\nLa donnée entrée en Fahrenheit équivaut à',c, 'en degré Celsius')
#fonc_celsius()


# Exercice 4 Créer une fonction qui calculera le plus grand commun diviseur de deux nombres
def fonc_pgcd(nbr5,nbr6):
    if nbr6 == 0:
        return nbr5
    else:
        r = nbr5 % nbr6
        print('Le PGCD des deux nombres est de :', fonc_pgcd(nbr6, r))
        return fonc_pgcd(nbr6,r)
#fonc_pgcd(11, 99)


# Exercice 5 Créer une fonction qui vérifie si l'entrée est pair ou non

def fonc_pair():
    nbr7 = int(input('\n[+] Veuillez entrer le nombre à vérifier la parité : '))
    if nbr7 % 2 == 0:
        print('\nLe nombre entré est PAIR')
    else:
        print('\nLe nombre entré n est PAS PAIR')
#fonc_pair()


# Exercice 6 Creer une fonction qui prend en entrée des nombres et en sortie leur moyenne

def fonc_calcul_moyenne2(nbr):
    somme = 0
    for i in nbr:
        somme += i
    moyenne = somme / len(nbr)
    return moyenne


#a = int(input('Entrez le premier nombre : '))
#b = int(input('Entrez le deuxieme nombre :'))
#c = int(input('Entrez le troisieme nombre : '))
#d = int(input('Entrez le quatrieme nombre :'))
#e = int(input('Entrez le cinquieme nombre :'))
#print('La moyenne des nombres est :', fonc_calcul_moyenne2([a,b,c,d,e]))


# Exercice 7 Créer une fonction qui a une liste et qui renvoie true si la valeur speocifié est présente


def fonc_presence():
    liste = [10,23,44,86,99]
    ent = int(input('[+] Veuillez entrer un entier pour valider s il est contenu dans la liste : '))
    if ent in liste:
        print('Le nombre est bien présent dans la liste')
    else:
        print('Le nombre n est PAS présent dans la liste')

#fonc_presence()

# Exercice 8 Calcul de la factorielle d'un nombre x si x = 5 factorielle = 5x4x3x2x1

def fonc_factorielle(k):
    a = 1
    for i in range(2,k+1):
        a *= i
    return a

#print(fonc_factorielle(4))


# Exercice 9 Créer une fonction qui prend ds nombres en entrées et les renvoie en ordre croissant

def fonc_croissance():
    a = int(input('Entrez le premier nombre : '))
    b = int(input('Entrez le deuxieme nombre :'))
    c = int(input('Entrez le troisieme nombre : '))
    d = int(input('Entrez le quatrieme nombre :'))
    e = int(input('Entrez le cinquieme nombre :'))
    liste = [a,b,c,d,e]
    liste.sort()
    print('Les nombres en ordre croissant sont :', liste)

#fonc_croissance()

# Exercice 10 Créer une fonction qui vérifier la primalité d'un nombre (s'il est premier ou non)

def fonc_primaire():
    nbr = int(input('[+] Veuillez entrer un nombre pour vérifier s il est premier ou non : '))
    x = 2
    if nbr % x == 0:
        print('Le nombre nest pas premier')
    else:
        print('Le nombre est premier')

#fonc_primaire()