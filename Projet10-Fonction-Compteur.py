def compteur():
    i = 0
    while i < 3:
        print(i)
        i = i + 1

print('bonjour')
compteur()
compteur()
print('fin du premier compteur\n')
def compteur1(stop):
    i = 0
    while i < stop:
        print(i)
        i = i + 1

compteur1(4)
compteur1(2)
a = 5
compteur1(a)
print('fin du deuxieme compteur\n')
def compteur_complet(start, stop, step):
    i = start
    while i < stop:
        print(i)
        i = i + step

compteur_complet(1, 9, 2)

print('fin du troisieme compteur\n')