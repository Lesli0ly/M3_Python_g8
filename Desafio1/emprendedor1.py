#Calcular utilidades del proyecto
import math

precio = float(input("Ingrese el precio de suscripción: "))
usuarios = float(input("Ingrese el número de usuarios: "))
gastos = float(input("Ingrese el gasto total: "))

utilidades = (precio * usuarios) - gastos
print ("Las utilidades de los usuarios normales corresponde a", int(utilidades), "pesos")