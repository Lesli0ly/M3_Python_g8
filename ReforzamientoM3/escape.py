import math

radio = input("Ingrese el radio en kilometros:")
#print(type(radio))
radio = float(radio)
#print (type(radio))

radio = radio * 1000

constante_g = float(input("Ingrese la constante gravitacional:"))
                    

ve = math.sqrt(2 * constante_g * radio)

print(f"La velocidad de escape es {ve:.1f} [m/s]")# ve:.1 flotante