# Un autre test avec le module argparse


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("nombre", help='Specifiez un entier a calculer la factorielle', type=int)
args = parser.parse_args()

a = 1
b = args.nombre
for i in range(2, b + 1):
    a *= i
print('La factorielle du nombre entrée est :', a)