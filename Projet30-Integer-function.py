def check_user_input(input):
    try:
        # Converti en integer
        val = int(input)
        print("L entrée est un integer et sa valeur est :", val)
    except ValueError:
        try:
            # Converti en float sinon
            val = float(input)
            print("L entrée est un float et sa valeur est :", val)
        except ValueError:
            print("Input est un string et ne peux PAS être converti")
            exit(print('\nLe programme va se terminer dû à votre arrogance..'))

input1 = input("Test 1 :")
check_user_input(input1)

input2 = input("Test 2 :")
check_user_input(input2)

input2 = input("Test 3 :")
check_user_input(input2)