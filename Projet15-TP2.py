
# Exercice 2 Tests conditionnels
# En se basant sur le nombre qui a été entré, printera si l<on est mineur ou majeur

def age():
    a = int(input('Veuillez entrer votre age : \n'))
    if a == 0:
        print('Petite jeunesse')
    elif a < 18:
        print('Vous etes donc mineur')
    else:
        print('Vous etes alors majeur')

age()
