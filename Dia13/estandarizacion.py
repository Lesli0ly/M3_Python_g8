def media(lista):
    return sum(lista)/len(lista)

import math
def sdd(lista, media):
    diff = [(elemento-media)**2 for elemento in lista]
    return math.sqrt(sum(diff)/(len(lista)-1))

def resultado(lista):
    m = media(lista)
    sd =sdd(lista, m)
    l_e = [(valor-m)/sd for valor in lista]
    return m, sd, l_e #podemos llamar a otros métodos en una list comprehension, llamar a otros métodos dentro de un método

lista = [1,2,3,4,5,6]

m, desv_st, l_e = resultado(lista)
print('La media es: ', m)
print('La Desviación estandar es: ', desv_st)
print('La lista estandarizada es: ', l_e)