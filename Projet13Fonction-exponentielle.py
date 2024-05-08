#Calculer lexponentielle

nbr = input('Entrez le nombre a calculer l exponentielle :')
def fonc_exponentielle():
    exp = 2.718282
    res = nbr ** exp
    print(res)

fonc_exponentielle()

# Avec le module math et la fonction .exp
import math

exponent = 3
print ("La valeur exponentielle est : ", math.exp(exponent))