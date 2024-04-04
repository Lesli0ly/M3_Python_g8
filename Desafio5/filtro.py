#filter(lambda item: item[precios] expression, iterable)

def multiple(precios):    # Primero declaramos una función condicional
    if precios == 30000:

        precios = {
            'Notebook': 700000,
            'Teclado': 25000,
        'Mouse': 12000,
        'Monitor': 250000,
        'Escritorio': 135000,
        'Tarjeta de Video': 1500000
        }

#print(list(filter(lambda x: x[0].lower() in 'aeiou', precios)))
#print(list( filter(lambda precio: precio == 30000, precios) ))

menores = filter(lambda precio: precio < 30000, precios)

for precio in precios:
    print(menor)