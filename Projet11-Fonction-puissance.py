# Une puissance d'un nombre est le résultat de la multiplication répétée de ce nombre avec lui-même
#Si le chiffre est 5, on effectue 5x5x5x5x5


# Fonction puissance avec if et else

a = input('Entrez le premier nombre : ')
b = input('Entrez le deuxieme nombre : ')

def fonc_puissance(a, b):
    if b == 0:
        return 1
    else:
        return a * fonc_puissance(a, b-1)

print('Le resultat, avec if/else, est :', fonc_puissance(a, b))


# Fonction puissance avec **
def fonc_puissance2():
    c = int(input('Entrez le premier nombre : '))
    e = int(input('Entrez le deuxieme nombre : '))
    r = c ** e
    print('Le resultat, avec **, est :', r)
fonc_puissance2()
print('\n')


# Fonction pow python
def fonc_puissancepow():
    a = int(input('Entrez le premier nombre : '))
    b = int(input('Entrez le deuxieme nombre :'))
    print('\n')
    print('Le resultat, avec pow, est :', pow(a, b))
fonc_puissancepow()

exit()

# Il est aussi possible de le faire avec le module math