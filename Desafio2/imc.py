"""Actividad 1 - IMC"""

"""1.- Al programa se debe ingresar el peso en Kg y la talla (altura) en centimetros"""
peso = float(input("Ingrese su peso en Kilogramos: "))
talla = float(input("Ingrese su talla (altura) en centímetros: "))

"""2.- Calcular el IMC ajustando los valores de entrada a las unidades requeridas por 
la fórmula. Se debe informar con 2 decimales"""
tallamodificada = talla/100
imc= round(peso/ tallamodificada**2,2)
print ("Su IMC es: " , imc)

"""3.-Entregar al usuario una salida acorde que permita conocer el valor de su IMC además 
de la clasificación dada por la OMS"""

if imc < 18.5:
    print("La Clasificación OMS es Bajo Peso")
elif imc >= 18.5 and imc <= 25.0 :
    print ("La Clasificación OMS es Adecuado")
elif imc >= 25.0 and imc <= 30.0 :
    print ("La Clasificación OMS es Sobrepeso")
elif imc >= 30.0 and imc <= 35.0 :
    print ("La Clasificación OMS es Obesidad Grado I")
elif imc >= 3.0 and imc <= 40.0 :
    print ("La Clasificación OMS es Obesidad Grado II")
elif imc > 40.0:
    print ("La Clasificación OMS es Obesidad Grado III")   
