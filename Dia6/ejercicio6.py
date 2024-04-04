"""Determinar si un número ingresado por el usuario es par o impar,
utilizaremos el módulo o resto de la división"""

#valor = int(input("Ingresa el avlor a probar"))
#Paso1
numero = input("Ingresa número a evaluar\n")

#Paso2: transformar string a dato numérico
numero = int(numero)

#Paso3: evaluar con las condicionales es par o es impar
if numero%2 == 0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")