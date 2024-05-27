# script avec des exemples pour mieux comprendre les classes dans python
# A ECRIRE DIRECTMENT DANS L"INTERPRETER PYTHON

class identifiant:
    pass


titcoune = identifiant()
titcoune.id = 2
titcoune.nom = 'titcoune'
titcoune.prenom = 'poulet'

print('Holla {}'.format(titcoune.prenom))
print('On mange tu du {} ce soir, {} ?'.format(titcoune.prenom, titcoune.nom))
print("C'est vraiment un {} de pique ce {}. Il sent le {} en plus".format(titcoune.id, titcoune.nom, titcoune.prenom))


class chat:

    famille = 'felin'

    def __init__(self, nom):
        self.nom = nom

# ********** OUTPUT ***********

# a = chat('bobby')
# b = chat('allo')
# a.famille
# 'felin'
# b.famille
# 'felin'
# a.nom
# 'bobby'
# b.nom
# 'allo'

class chaton:

    def __init__(self, nom):
        self.nom = nom
        self.couleur = []

    def ajout_Couleur(self, couleur):
        self.couleur.append(couleur)

# ********** OUTPUT ***********
"""
a = chaton('bob')
b = chaton('boby')
a.ajout_Couleur('brun')
b.ajout_Couleur('roux')
b.couleur
['roux']
a.couleur
['brun']
"""