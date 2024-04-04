import getpass

password = getpass.getpass("Ingresa el password: ")
print(f"el password capturado {password}")
#hola
while password != "hola mundo":
    password = getpass.getpass("Error, Ingresa el password nuevamente: ")
    
print("Password correcto, puedes utilizar tu programa")