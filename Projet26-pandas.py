# Script de test avec pandas, le module qui sert a traiter une grande quantité de données
# Je teste differente fonctions dans ce script afin de ma familiariser avec pandas


import pandas as pd

# Creation d'un set, qu'on assigne ensuite un index et on le print

monSet = {
    'cars': ["BMW", "Volvo", "Ford"],
    'En inventaire': [3, 7, 2]
}
#df = pd.DataFrame(monSet, index=['Salle 1', 'Salle 2', 'Salle 3'])
#print(df)
#print(df.loc[0])

"""
# on peut créer notre propre table également de cette facon.
data = {
  "Duration": {
    "0": 60,
    "1": 60,

  },
  "Pulse": {
    "0": 110,
    "1": 117,
  },
  "Maxpulse": {
    "0": 130,
    "1": 145,
  },
  "Calories": {
    "0": 409,
    "1": 479,
  }
}
"""
# df = pd.DataFrame(data)
# print(df)

# on prend un fichier csv et on le lit avec le module


df = pd.read_csv('evenement.csv')
#print(df.to_string())

#print(df.head(4))
#print(df.tail(2))

# with this you can remove the row with an empty cell
# cleaned_df = df.dropna()
# print(cleaned_df.to_string())

# with this you can replace the empty cell with something
# df = df.fillna(999)
# print(df.to_string())

# Retourne s'il y a des duplicatas
# print(df.duplicated())

# Permet de retirer les duplicatas ( en garde 1 quand meme)
# print(df.drop_duplicates())

# Permet de definir s'il y a des correlations dans les colonnes
# print(df.corr(2))