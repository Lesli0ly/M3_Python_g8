import requests
input ("ingrese nº de post: {}")  
url = "https://jsonplaceholder.typicode.com/posts/{}"

response = requests.get(url)

print(response)

if response.status_code == 200:
    print("Obtención correcta")
    print(response.json())
    print("")
    post = response.json()
    print(response.json()["title"])
else:
    print("Error en la solicitud")