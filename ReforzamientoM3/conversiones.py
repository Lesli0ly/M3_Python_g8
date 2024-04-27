import sys

#python conversiones.py 0.0046 0.093 0.0013 10000
#trabajar con argumentos es trabajar con una lista
#sys.argv[posicion] -> siempre capturamos un string
print(sys.argv)#['conversiones.py', '0.0046', '0.093', '0.0013', '10000']

archivo = sys.argv[0]#todo lo relacionado al archivo...conversiones.py

print(sys.argv)['conversiones.py', '0.0046', '0.093', '0.0013', '10000']

archivo = sys.argv[0]

sol_peruano_str = sys.argv[1]
sol_peruano_float = float(sol_peruano_str)

peso_argentino_float = float(sys.argv[2])

dolar_americano_float = float(sys.argv[3])

peso_chileno_int = int(sys.argv[4])#

dicc_tasa_conversion = {#diccionario, permite almacenar gran cantidad de datos
    'sol': sol_peruano_float,
    'dolar': dolar_americano_float,
    #'dolar': float
    'argentino': peso_argentino_float
   }

print ("Conversión de divisas")
print (f"Los {peso_chileno_int} pesos, transformados a soles {peso_chileno_int * dicc_tasa_conversion ['sol'] }")