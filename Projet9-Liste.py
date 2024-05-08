# Differents type de liste

# list
jour = ['lundi', 'mardi', 'mercredi', 'jeudi']
print(jour)
print(type(jour))
print('\n')


# Tuple
jour1 = ('lundi', 'mardi', 'mercredi', 'jeudi')
print(jour1)
print(type(jour1))
print('\n')


# Dictionnaire
jour2 = {'lundi': 'Premier',
         'mardi': 'Deuxieme',
         'mercredi': 'Troisieme',
         'jeudi': 'Quatrieme'}
print(jour2)
print(type(jour2))
print('\n')

# acceder a la valeur du dictionnaire
print(jour2['lundi'])
print('\n')

#modifier un item du dict
jour2['lundi'] = 'Week-end'
print(jour2['lundi'])
print('\n')

#supprimer un item du dict
jour2.pop('lundi')
jour2.pop('mardi')
print(jour2)
print('\n')

#Retourner les cles du dict
print(jour2.keys())
print('\n')

#Retourner les valeur du dict
print(jour2.values())
print('\n')

#Retourner les items du dict
print(jour2.values())
print('\n')

