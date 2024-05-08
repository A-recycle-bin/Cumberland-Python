# Une puissance d'un nombre est le résultat de la multiplication répétée de ce nombre avec lui-même
#Si le chiffre est 5, on effectue 5x5x5x5x5

# Fonction puissance
def nombre_puissance():
    c = input('Entrez un nombre : ')
    c = int(c)
    c = c ** c
    print('Le resultat est :', c)

nombre_puissance()
print('\n')
# Fonction puissance 2
def nombre_puissance2():
    d = input('Essaie une deuxieme fois :')
    d = int(d)
    d = pow(d, d)
    print('Le resultat est :', d)
nombre_puissance2()
print('\n')
# Fonction pow python
def powpow():
    a = input('Entrez le nombre : ')
    a = int(a)
    print('\n')
    print('Le resultat est :', pow(a, a))
powpow()