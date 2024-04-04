#for each
"""
for variable in iterable:
iterable: algo que se puede recorrer
el valor que va tomando i, de acuerdo al rango que se asigna in range 
"""
#funcion range()
#valor de inicio es el cero por default [0-10[, donde el 10 no es considerado
for i in range(10):
    print(i)#1,2,3,4,5,6,7,8,9

print("----------(4,10)------------")
# [4-10[
for i in range (4,10):
    print(i)#4,5,6,7,8,9
    
print("--------(4,10,2)--------------")
# [4-10[ el tercer valor corresponde a la frecuencia (cada cuanto se va recorriendo) de ejecución partiendo del 4, va de 2 en 2 
for i in range (4,10,2):
    print(i)# 4,6,8
    
""" Imprimir los numeros pares que se encuentran entre el 1 y el 20"""
print("-------ejercicio (1,21,2)---------")
for i in range (1,21,2):
    print(i)

print("-------ejercicio (0,21,2)---------") 
for i in range (0,21,2):
    print(i)    
    
print("-------ejercicio (1,21)---------")
for num in range(1,21):
    if num % 2 == 0:
        print(num)

print("-------ejercicio while---------")
contador = 1
while contador <=20:
    if contador% 2 == 0:
        print (contador)
    contador+=1