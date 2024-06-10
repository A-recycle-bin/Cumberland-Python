import sys
import codecs


def affiche_infos(dico: dict, clé: str):
    if clé in dico.keys():
        print(f"La clé que vous avez inscrit est la suivante :, {clé} : {dico[clé]}")
    else:
        print(f"la clé [{clé}] n'existe pas")


FILE_NAME = "infos.txt"


# Ecriture dans le fichier
fic = None
try:
    fic = open(FILE_NAME, "w")
    for i in range(1, 101):
        ligne = f"Usager{i}:MDP{i - 1}:Chiffre_secret={i ** 2 - 24}"
        fic.write(f"{ligne}\n")
except IOError as erreur:
    print(f"Erreur d'exploitation du fichier {FILE_NAME} : {erreur}")
    sys.exit()
finally:
    if fic:
        fic.close()

# Lecture du fichier
fic = None
try:
    fic = open(FILE_NAME, "r")
    dico = {}
    ligne = fic.readline().strip()
    # tant que la ligne n'est pas vide
    while ligne != '':
        # on met la ligne dans un tableau
        infos = ligne.split(":")
        # on récupère le login
        login = infos[0]
        # on crée une entrée dans le dictionnaire
        dico[login] = infos
        # lecture ligne suivante
        ligne = fic.readline().strip()
except IOError as erreur:
    print(f"Erreur d'exploitation du fichier {FILE_NAME} : {erreur}")
    sys.exit()
finally:
    # on ferme le fichier s'il a été ouvert
    if fic:
        fic.close()


affiche_infos(dico, clé='Usager1')
affiche_infos(dico, clé='Usager10')

def create_utf8_file():
    file = codecs.open(filename=input('Veuillez entrer le nom du fichier à créer : '), mode='w', encoding='utf8')
    file.write(input('Entrez le message a inscrire dans le fichier : '))
    file.close()

def create_iso8859_file():
    file = codecs.open(filename=input('Veuillez entrer le nom du fichier à créer : '), mode='w', encoding='iso-8859-1')
    file.write(input('Entrez le message a inscrire dans le fichier : '))
    file.close()


create_utf8_file()
create_iso8859_file()