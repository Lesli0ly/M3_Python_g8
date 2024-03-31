#Solicitud de datos
precio_suscripcion = float(input("Ingrese precio de suscripción en clp: \n"))
usuarios = int(input("Ingrese número de usuarios: \n"))
gastos_totales = float(input("Ingrese gastos totales en clp: \n"))
utilidades_anio_anterior = float(input("Ingrese las utilidades del año anterior mayor a cero, en clp: \n"))
#año = anio
#utilidades = p * u -gt
utilidades_actuales = precio_suscripcion * usuarios - gastos_totales

#validación de variables (condicional)
if utilidades_anio_anterior > 0:
    #realizar lo que este tabulado
else:
    #realizar acción por default
    print("Las utilidades no pueden iguales a cero")
    
    """numero = 77
    #saber si es mayor a 40 o si es menor a 10 o es igual a 77
    
    if numero == 77: lo primero es validar la igualdad, anidar las consultas, 
                     para esto es necesario realizar las preguntas correctas"""
    
    #se divide la utilidad actual por la utilidad del año anterior para obtener la razón
    razon_utilidad_actual_y_anterior = utilidades_actuales / utilidades_anio_anterior

    #el resultado de la división se puede multiplicar por 100 para pasarlo a %
    #razon_utilidad_actual_y_anterior = razon_utilidad_actual_y_anterior * 100

    print(f"La razón entre la utilidad actual y del año anterior es: {round(razon_utilidad_actual_y_anterior,2)} de crecimiento")
    

