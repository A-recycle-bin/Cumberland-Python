"""
    4. Dans cet exercice, vous devez créer une fonction ip_checker qui acceptera un paramètre ip_address et qui retournera le booléen True si l'adresse IP est valide et False dans le cas contraire.
    Une adresse IP est valide quand elle est composée d'une suite de 4 nombres entre 0 et 255, par exemple :
	✅ 0.0.0.0
	✅ 192.168.0.1
	✅ 255.255.255.255
	⛔️ 928.394.201.293
	⛔️ -392.255.193.2
	⛔️ 192.4.3
"""

import re

regex = re.compile(
    r"\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b",
    re.IGNORECASE)


def ip_checker():
    print('Entrez exit pour quitter le programme')
    while True:
        ip = input('Veuillez entrer le ip a vérifier la validité : ')

        if (re.search(regex, ip)):
            print("Adresse ip VALIDE")
        elif ip == 'exit':
            break
        else:
            print("Adresse ip INVALIDE")


ip_checker()