#Cálculo del factorial de un número
def factorial(numero):#5! = 5*4*3*2*1
    valor =1#variable acumuladora
    for n in range (1,numero+1):#1,2,3,4,5
        valor = valor * n
    return valor

#print("El factorial es:", factorial(5))

#Crear una función que calcule la poductoria

def productoria(lista):
    valor = 1 #
    for elemento in lista:
        valor *=elemento#forma abreviada de valor = valor * n
    return valor

print(productoria([4,6,7,4,3]))

#Paso 3: Una función que permita controlar los cálculos.
# Esta función se debe invocar de la siguiente manera:

def calcular(**parametros): #* tupla; ** diccionario **kwargv, es solo un nombre
    for clave in parametros.items():
        if "fact" in clave:#if "fact" not in clave (tambien se puede preguntar de esa forma)
            print(f"El factorial de {valor} es {factorial(valor)} ")
        else:
            print(f"La productoria de {valor} es {productoria(valor)} ")
            

#Paso 4: Invocación al método        
calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 =6 )
