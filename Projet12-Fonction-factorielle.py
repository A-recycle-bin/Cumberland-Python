# la factorielle d'un entier naturel n est le produit des nombres entiers
# strictement positifs inférieurs ou égaux à n
# si la factorielle est 5, le calcul est 1x2x3x4x5

def fonct_factorielle():
    a = 1
    b = int(input('Entrez le nombre a calculer la factorielle : '))
    for i in range(2,b+1):
        a *= i
    print('La factorielle du nombre entrée est :', a)


fonct_factorielle()



