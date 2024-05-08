# la factorielle d'un entier naturel n est le produit des nombres entiers
# strictement positifs inférieurs ou égaux à n
# si la factorielle est 5, le calcul est 1x2x3x4x5
b = input('Entrez le nombre a calculer la factorielle : ')
def factoriel(b):
    b = int(b)
    a = 1
    for i in range(2,b+1):
        a = a * i
        print(a)

factoriel(b)