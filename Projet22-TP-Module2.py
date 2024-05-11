import math
import random
import os


#print(math.exp(10))
#print(math.factorial(10))

#print(random.randint(10, 18))


#cwd = os.getcwd()
#print("Current working directory : ", cwd)

def path_back():
    print("Current working directory before")
    print(os.getcwd())
    print()
    os.chdir('../')
    print('Current working directory after\n', os.getcwd())

#path_back()

#print(os.listdir())
#print(os.name)
