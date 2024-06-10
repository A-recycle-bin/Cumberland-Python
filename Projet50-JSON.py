import codecs
import json
import sys

# lecture / écriture d'un fichier jSON
in_file=None
out_file=None
try:
    # ouverture du fichier jSON en lecture
    in_file = codecs.open("in.json", "r", "utf8")
    # transfert du contenu dans un dictionnaire
    data = json.load(in_file)
    # affichage des données lues
    print(f"Voici toutes les données dans le fichier : {data}, Le type de données dans le fichier est {type(data)}")
    salaire = data['salaire']
    print(f"Les salaires dans le fichier sont : {salaire}, Le type de données de salaire est : {type(salaire)}")
    print(f"Le deuxieme salaire dans la liste ={salaire[1]}, Le type de cette données est {type(salaire[1])}")
    # transfert du dictionnaire [data] dans un fichier json
    out_file = codecs.open("out.json", "w", "utf8")
    json.dump(data, out_file)
except BaseException as erreur:
    # on affiche l'erreur et on quitte
    print(f"L'erreur suivante s'est produite : {erreur}")
    sys.exit()
finally:
    # fermeture des fichiers s'ils sont ouverts
    if in_file:
        in_file.close()
    if out_file:
        out_file.close()

#*********************************************

data = {'marié': 'oui', 'impôt': 1340}
data2 = {'née': 'non', 'Pourquoi?': 111}

# écriture d'un fichier jSON
fichier1 = None
fichier2 = None
fichier3 = None
fichier4 = None
try:
    # transfert du dictionnaire [data] dans un fichier json
    fichier1 = codecs.open("fichier1", "w", "utf8")
    json.dump(data, fichier1, ensure_ascii=True)
    # transfert du dictionnaire [data] dans un fichier json
    fichier2 = codecs.open("fichier2", "w", "utf8")
    json.dump(data, fichier2, ensure_ascii=False)
    fichier3 = codecs.open("fichier3", "w", "utf8")
    json.dump(data2, fichier3, ensure_ascii=True)
    # transfert du dictionnaire [data] dans un fichier json
    fichier4 = codecs.open("fichier4", "w", "utf8")
    json.dump(data2, fichier4, ensure_ascii=False)
except BaseException as erreur:
    # on affiche l'erreur et on quitte
    print(f"L'erreur suivante s'est produite : {erreur}")
    sys.exit()
finally:
    # fermeture des fichiers s'ils sont ouverts
    if fichier1:
        fichier2.close()
    if fichier2:
        fichier2.close()


