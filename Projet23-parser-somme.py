# Ce script est un test afin de se familiariser avec le module argpaser
# Il est utile afin d'utiliser les switch dans le command line.
# *****************PROJET A TERMINER*****************


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("nbr1", type=int, )
parser.add_argument("nbr2", type=int, )
args = parser.parse_args()
somme = args.nbr1 + args.nbr2
print('La somme des deux nombres est : ', somme)
