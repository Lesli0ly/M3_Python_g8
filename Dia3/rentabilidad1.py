#Inputs de datos
precio = int(input("Ingrese el precio del servicio en clp: \n"))
cantidadUsuarios = int(input("Ingrese la cabtidad de usuarios: \n"))
gastosTotales = int(input("Ingrese los gastos totales en clp: \n"))

#Calculo --> utilidades = p * u - gt
utilidades = precio * cantidadUsuarios - gastosTotales

#Salida
print(f'Las utilidades son: ${utilidades} ')