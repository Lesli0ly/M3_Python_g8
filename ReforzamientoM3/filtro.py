
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
    }

#print(precios['Monitor'])

umbral = int(input("Ingrese el valor del umbral: "))#50000

#if precios['Notebook'] > umbral:
    #print("Es mayor que el umbral")
#else:
    #print("Es menor que el umbral")

mayores = {}#Crear diccionario vacío
menores = {}

for clave, valor in precios.items():
    if valor > umbral:
        #print(f"{clave, valor} es mayor que el umbral") 
        mayores[clave] = valor 
    else:
        #print(f"{clave, valor} es menor que el umbral")  
        menores[clave] = valor
        
#print(f"Grupo de mayores que el umbral", mayores)
#print("**********")
#print(f"Grupo de menores que el umbral", menores)

def funcion_filtrar(umbral, dicionario):
    for clave, valor in precios.items():
        
        if valor > umbral:
        #print(f"{clave, valor} es mayor que el umbral") 
            mayores[clave] = valor 
        
        else:
        #print(f"{clave, valor} es menor que el umbral")  
            menores[clave] = valor

funcion_filtrar(umbral, precios)#llamar a la función

print(f"Grupo de mayores que el umbral", mayores)
print("**********")
print(f"Grupo de menores que el umbral", menores)
