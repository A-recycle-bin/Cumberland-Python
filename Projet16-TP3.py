# Exercice 3 Boucles
# Parcourt les nombres 1 à 10 et les affiche

# Boucle for
def boucle1():
    for i in range(1,11):
        print(i)
boucle1()
print('\n')


# Boucle while
# Calcul le carré des nombres 1 à 5
def boucle2():
    for n in range(1,6):
        k = n ** 2
        print('Le carré de', n, 'est égal a', k)
boucle2()