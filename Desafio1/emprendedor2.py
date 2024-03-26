#
import math

precio = float(input("Ingrese el precio de suscripción: "))
usuarios=int(input("Ingrese el número de usuarios: "))
gastos = int(input("Ingrese el gasto total: "))
precioPremiun = precio * 1.5
print (precioPremiun)
utilidadesPremiun = (precioPremiun * usuarios - gastos)
print ("Las utilidades de los usuarios premiun corresponde a", (utilidadesPremiun), "pesos")