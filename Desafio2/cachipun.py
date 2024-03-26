"""1.- Se pide crear el programa cachipun.py, donde el usuario entregará como argumento: piedra,
papel o tijera. Para que el computador pueda jugar escogerá un valor al azar. Para eso se pide
investigar random.choices() de la librería random"""

import random
cachipunpersona = input("Ingrese su opcion del cachipun piedra,papel o tijera: ")

cachipunpc = "piedra", "papel", "tijera"
print("Computador jugó", random.choices(cachipunpc, weights = None, k = 1))

"""2.- Considerar las opciones de ganar, perder o empatar con la computadora"""

""" En caso que el argumento sea distinto a piedra, papel, o tijera, el programa debe mostrar las 
opciones que se pueden jugar"""

