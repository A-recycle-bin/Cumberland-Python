# Une puissance d'un nombre est le résultat de la multiplication répétée de ce nombre avec lui-même
#Si le chiffre est 5, on effectue 5x5x5x5x5


# Fonction puissance

a = input('Entrez le nombre a calculer la puissance : ')
b = input('Entrez son exposant : ')

def puissance(a, b):
    a = int(a)
    b = int(b)
    if b == 0:
        return 1
    else:
        return a * puissance(a, b-1)

print('Le resultat est :', puissance(a, b))

# Fonction puissance 2
def nombre_puissance():
    c = input('Entrez un nombre : ')
    c = int(c)
    e = input('Entrez son exposant : ')
    e = int(e)
    r = c ** e
    print('Le resultat est :', r)
nombre_puissance()
print('\n')


# Fonction pow python
def powpow():
    a = input('Entrez le nombre : ')
    b = input('Entrez son exposant :')
    a = int(a)
    b= int(b)
    print('\n')
    print('Le resultat est :', pow(a, b))
powpow()

exit()