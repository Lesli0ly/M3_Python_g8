ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,#para concepto de diccionario el mes corresponde a la clave
}

#umbral o valor a comparar
#25000
#umbral_str = input ("Ingrese el umbral: ")#Enviamos un mensaje al usuario, se espera recibir un dato, 
#y la informacion capturada es siempre un string
#umbral_int = int(umbral_str)

#for venta_mensual in ventas:#como recorremos un diccionario
#   print(venta_mensual)#por default nos entrega la clave a traves de la cual vamos a obtener el valor
    
#for clave, valor in ventas.items():#al agregar el.item, nos entrega la clave y el valor
    #print(clave, valor)

#print (ventas["Septiembre"])

#para agregar datos a un diccionario el diccionario debe existir
diccionario = {}#diccionario vacío

umbral = int(input ("Ingrese el umbral: "))
for clave, valor in ventas.items():
    if valor > umbral:
        
        diccionario[clave] = valor
        #print(clave, valor)
        print (diccionario)