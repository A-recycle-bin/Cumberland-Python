from package.operations import addition
from package.operations import multiplication
from package.factorielle import factorielle
from package.puissance import puissance


a = int(input('[+] Veuillez entrer un nombre a additioner : '))
b = int(input('[+] Veuillez entrer un second nombre a additioner : \n'))
print('La somme est égale à : ', addition(a,b))


c = int(input('[+] Veuillez entrer un nombre a multiplier : '))
d = int(input('[+] Veuillez entrer un second nombre a multiplier : \n'))
print('Le produit est égale à : ', multiplication(c,d))


e = int(input('[+] Veuillez entrer le nombre à calculer la factorielle : \n'))
print('Le produit est égal à : ', factorielle(e))


g = int(input('[+] Veuillez entrer le nombre à calculer la puissance : '))
h = int(input('[+] Veuillez entrer sa puissance : \n'))
print('Le résultat est égal à : ', puissance(g,h))
