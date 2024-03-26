"""Velocidad de escape de un planeta se define como la minima velocidad necesaria para salir de un planeta
venciendo la gravedad. Calculemos el de la Tierra"""

import math
radio = input("Ingrese el radio en kilometros: ")
radio=int(radio) * 1000
constanteG = input ("Ingrese la constante g, en metros por segundo cuadrado: ")
constanteG = float(constanteG)
Ve = 2*(constanteG*radio)
escape = (math.sqrt(Ve))
print("La velocidad de escape es de",round (escape,1),"m/s")



