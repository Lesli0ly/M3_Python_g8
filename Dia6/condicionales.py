#condicional if


#Si se cumple la condición (true),
#entonces se ejecuta el código
#if condicion:
    #Codigo a ejecutar (tabulado a la derecha)
    
edad = input("¿Qué edad tienes?\n")#20 -> se almacena "20"
edad = int(edad)#edad = int("20")-> edad = 20

"""
Ejemplo1:

edad = int(input("¿Qué edad tienes?"))
if edad >= 18:
    print("Eres mayor de edad")

¿Qué edad tienes? 33
Eres mayor de edad
"""

#Si el usuario es mayor de edad o menor de edad
if edad > 18:
    print("Tú edad es mayor a 18, eres mayor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres menor de edad")   
    print("Programa terminado")
    
#ELSE se usa cuando se tiene mas de una condición como respuesta

#if condicion:
    #Codigo a ejecutar (tabulado a la derecha)
#else:
    #Ejecutar el siguiente código
    
"""Entonces:
if condición:
    #código que se ejecutará SOLO SI se cumple la condición
else:
    #código que se ejecutará si No se cumple la condición"""
    
"""Cuando tenemos mas de 1 condicion que evaluar existe ELIF, condicional que se encuentra entre if y ELSE
elif (otra condición:)
    #Si se cumple esta nueva condición se jeceuta el código

"""