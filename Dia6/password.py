contrasenia = input ("INgrese una contraseña (min 6 caracteres)")

#string.count("")
if contrasenia.count(" ")> 0:
    print("El password no puede contener espacios")

elif contrasenia == "12345":
    print("El password es incorrecto")
elif len(contrasenia) < 6:
    print("El password es demasiado corto")    
else:
    print ("El formato del password es correcto")