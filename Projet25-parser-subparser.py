# Un script qui va parser des switch mais avec des subparser.
# ce qui permet deffectuer plusieurs fonctions dans le meme script
# Afin de lutiliser on entre dans le commande line, par exemple :
# 'python Projet25-parser-subparser.py addition 10 10'
# 'python Projet25-parser-subparser.py soustraction 20 10'
# 'python Projet25-parser-subparser.py multiplication 10 10'
# 'python Projet25-parser-subparser.py division 100 10'

import argparse


parser = argparse.ArgumentParser

parser = argparse.ArgumentParser
subparsers = parser.add_subparsers(dest='operation', help='Operations disponible')

add_parser = subparsers.add_parser('addition', help='Addition')
add_parser.add_argument('nombres', nargs='+', type=int, help='Nombres a additionner')

subtract_parser = subparsers.add_parser('soustraction', help='Soustraction')
subtract_parser.add_argument('nombres', nargs='+', type=int, help='Nombres a soustraire')

subtract_parser = subparsers.add_parser('multiplication', help='Multiplication')
subtract_parser.add_argument('nombres', nargs='+', type=int, help='Nombres a multiplier')

subtract_parser = subparsers.add_parser('division', help='Division')
subtract_parser.add_argument('nombres', nargs='+', type=int, help='Nombres a diviser')

subtract_parser = subparsers.add_parser('modulo', help='Modulo')
subtract_parser.add_argument('nombres', nargs='+', type=int, help='Nombres a calculer le modulo')

args = parser.parse_args()


if args.operation == 'addition':
    print('La somme des nombres est : ', sum(args.nombres))
elif args.operation == 'soustraction':
    print('Le reste des nombres soustraits est : ', args.nombres[0] - sum(args.nombres[1:]))
elif args.operation == 'multiplication':
    print('Le produit des nombres multipliés est : ', args.nombres[0] * (args.nombres[1]))
elif args.operation == 'division':
    print('Le quotient des nombres divisés est : ', args.nombres[0] / (args.nombres[1]))
elif args.operation == 'modulo':
    print('Le modulo des deux nombres est : ', args.nombres[0] % (args.nombres[1]))


