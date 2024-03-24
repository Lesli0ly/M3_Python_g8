nombre = "Leslie"
apellido1 = "Galindo"
apellido2 = "Torres"
edad = "45"
#Python no permite sumar (concatenar) letras con números
print("*****Información*****")
#print("**      "+nombre+"       **")
print ("Tu nombre es  " + nombre)
print("**     "+apellido1+"       **")
print ("Tu apellido es  " + apellido1)
#print("**     "+apellido2+"     **")
print ("Tu segundo apellido es  " + apellido2)
#print ("****    "+edad+"      ****")
print ("Tu tienes   " + edad, "años")
print ("**************************")

# Interpolación de cadenas (otra forma de imprimir)(f)=> print(f"") forma básica de escribir la interpolación
mes = 3
dia = 6
año = 2024
print(f"Hola {nombre}, el año es {año} del mes {mes} y el día {dia}")
