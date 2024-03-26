from os import system


"""def nombre_de_la_funcion(variable):
    #codigo a ejecutar

print("Inicio")

"""
"""Funciones
   
parametro, variable a utilizar en la función
argumento, valor que tomará el parámetro para ser utilizado dentro de la función """

"""#llamado a la función (invocación)
imprimir_menu()
imprimir_menu()
imprimir_menu()
print("Fin")

system("clear")

def suma (valor1, valor2): #valor1=3 ; valor2=5
    suma = valor1 + valor2 # suma=3+5; suma = 8
    return suma# return 8

def suma2(valo1, valor2):
    return valor1 + valor2
    print("querty123456")#Nunca se ejecutará, si se queire imprimir debe ir antes del return

suma(3,5)

suma(3,5)
print(suma(1,9))#Se imprime el valor de retorno

resultado = suma(6,7)#Capturando el valor de retorno
print("valor respuesta carpturado", resultado)#imprimiendo el valor de retorno

system("clear")
#Retorno múltiple
def cuadrado_cubo(base):
cuadrado = base**2
cubo = base**3
return cuadrado, cubo

print(cuadrado_cubo(2))# Retorno de una tupla (4, 8)

valor_cuadrado, valor_cubo = cuadrado_cubo(3)
print (valor_cuadrado, valor_cubo)"""

#system("clear")

#VARIABLES LOCALES Y VARIABLES GLOBALES
pais = "Chile"#variable global
#constantes
G = 9.8
PI = 3.14
IVA = 19

def ciudades():
    #scope de la variable "capital" es solo en el método ciudades()
    capital = "Santiago"
    print(pais, capital)
    #pais= "Peru"#No se debe sobreescribir el valor de la variable global
    return capital

print(pais)
ciudades()
#print(capital)#variable no definida
print(pais)