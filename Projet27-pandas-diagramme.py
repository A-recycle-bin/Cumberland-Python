# Utilise le module pandas pour lire le fichier de données,
# Utilise ensuite le module matplotlib pour en créer un diagramme avec les données

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('evenement.csv')

# df.plot()
# df.plot(x = 'Nom de l evenement', y = 'Places restantes')
# df.plot(x = 'Nom de l evenement', y = 'Prix du billet')
# df.plot(kind = 'scatter',x = 'Nom de l evenement', y = 'Places restantes')

plt.show()