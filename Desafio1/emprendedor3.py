import math

precio = int(input("Ingrese el precio de suscripción: "))
usuarios = int(input("Ingrese el número de usuarios: "))
gastos = int(input("Ingrese el gasto total: "))
utilidadesActuales = (precio * usuarios) - gastos
utilidadesAnterior = int(input("Ingrese utilidades del año anterior: "))
razonUtilidades = round (int(utilidadesActuales)/int(utilidadesAnterior),2)

if utilidadesAnterior >= 0:
    print ("La razón entre las utilidades actuales y las del año anterior: ", razonUtilidades)
else:
    print ("Las utilidades no pueden ser menores que 0!")


