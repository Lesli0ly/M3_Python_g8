#El input siempre captura un string, por lo que si es necesario, 
# se debe transformar int o float

#forma abreviada de transformar string capturado por el input
peso = float(input("Ingrese el peso en Kilogramos: "))

altura = float(input("Ingrese la altura en centimetros: "))

altura_mts = altura/100

imc = peso /(altura_mts * altura_mts)
#imc = peso / (altura_mts**2)

print(f"Tu IMC es {imc:.2f}") #Truncar y aproximar los decimales


#Estructura condicional (pregunta de validacion)

if imc < 18.5:
    print("Tu clasificación según la OMS es Bajo Peso")
    
elif imc >= 18.5 and imc < 25: #[18.5, 25[ tiene que cumplir las dos condiciones
    print("Tu clasificación según la OMS es Adecuado")

elif imc >= 25 and imc < 30: #[18.5, 25[ tiene que cumplir las dos condiciones
    print("Tu clasificación según la OMS es Sobrepeso")
    
elif imc >= 30 and imc < 35: #[18.5, 25[ tiene que cumplir las dos condiciones
    print("Tu clasificación según la OMS es Obesidad I")
    
elif imc >= 35 and imc < 40: #[18.5, 25[ tiene que cumplir las dos condiciones
    print("Tu clasificación según la OMS es Obesidad II")

elif imc >= 40:    
#else:
    print("Tu clasificación según la OMS es Obesidad III")
