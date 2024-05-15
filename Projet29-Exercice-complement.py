""""
    1. Écrire une fonction appelée est_present qui prend en entrée une liste, recherche une valeur
    et renvoie True si la valeur est présente dans la liste, sinon renvoie False.
"""

def est_present():
    a = int(input('Veuillez entrer le nombre d éléments à insérer à la liste : '))
    list = []
    for i in range(a):
        x = int(input("Entrez le nombre a insérer : "))
        list.append(x)
    #print('List:', list)
    b = int(input('Veuillez entrer le nombre a verifier la presence dans la liste :'))
    if b in list:
        print('Le nombre est present')
    else:
        print('Le nombre n est PAS present')

#est_present()

"""
    2. Ecrire une fonction permettant de remplir une liste dont l'utilisateur va choisir le nombre 
    d'élément de la liste. 
    NB : Controle de saisi obligatoire
"""

def int_input(input):
    try:
        val = int(input)
    except ValueError:
        try:
            val = float(input)
        except ValueError:
            print('La valeur ne peux pas etre transformé en integer')


def liste():
    a = int(input('Veuillez entrer le nombre d éléments à insérer à la liste : '))
    int_input(a)
    list = []
    for i in range(a):
        x = int(input("Entrez le nombre a insérer : "))
        list.append(x)
    print('La liste contient les nombres :', list)

#liste()

"""
    3. Ecrire une fomction qui permet de crypter une phrase saisie par l'utilisateur.
    Lescaratères saisis doivent être changé par substitution.
    par exemple ''Bonjour'' va devenir une nouvelle chane en subtituant chaque caractère par un code(un autre caractère ou une chaine).
    Faire une autre fonction qui permet de décrypter la chaine cryptée obtenue.
"""

substitution = {
    'a': 'z',
    'b': 'y',
    'c': 'x',
    'd': 'w',
    'e': 'v',
    'f': 'u',
    'g': 't',
    'h': 's',
    'i': 'r',
    'j': 'q',
    'k': 'p',
    'l': 'o',
    'm': 'n',
    'n': 'm',
    'o': 'l',
    'p': 'k',
    'q': 'j',
    'r': 'i',
    's': 'h',
    't': 'g',
    'u': 'f',
    'v': 'e',
    'w': 'd',
    'x': 'c',
    'y': 'b',
    'z': 'a',
}

def cryptage():
    msg = input('Entrez le message a chiffrer : ')
    msg_crypte = ""
    for lettre in msg.lower():
        if lettre in substitution:
            msg_crypte += substitution[lettre]
        else:
            msg_crypte += lettre
    print('Le message une fois chiffré est :', msg_crypte)

cryptage()

def decryptage():
    msg = input('Entrez le me message a déchiffrer : ')
    msg_decrypte = ""
    for lettre in msg.lower():
        if lettre in substitution.values():
            for key in substitution:
                if substitution[key] == lettre:
                    msg_decrypte += key
        else:
            msg_decrypte += lettre
    print('Le message une fois déchiffré est :', msg_decrypte)

decryptage()