import requests
from bs4 import BeautifulSoup

diccionario = {}
i = 0

# URL de la página web
url = "https://www.marca.com/futbol.html"

# Lista para almacenar los enlaces
enlaces = []

try:
    # Realizar la solicitud HTTP
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Analizar el HTML de la página
        soup = BeautifulSoup(response.text, "html.parser")

        # Encontrar todos los elementos <a> con la clase "ue-c-cover-content__link"
        links = soup.find_all("a", class_="ue-c-cover-content__link")

        # Obtener los enlaces (href) de los elementos encontrados
        enlaces = [link.get("href") for link in links]

    else:
        print("La solicitud no fue exitosa. Código de estado:", response.status_code)

except Exception as e:
    print("Ocurrió un error:", str(e))

# Lista para almacenar todos los párrafos de todas las noticias
todos_parrafos = []

# Recorrer los enlaces y obtener los párrafos de cada noticia
for enlace in enlaces:
    try:
        # Realizar la solicitud HTTP
        response = requests.get(enlace)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Analizar el HTML de la página
            soup = BeautifulSoup(response.text, "html.parser")

            # Encontrar todos los elementos <p>
            parrafos = soup.find_all("p")

            # Obtener el contenido de los párrafos
            parrafos = [parrafo.get_text() for parrafo in parrafos]

            todos_parrafos.extend(parrafos)

        else:
            print("La solicitud no fue exitosa. Código de estado:", response.status_code)

    except Exception as e:
        print("Ocurrió un error:", str(e))

palabra = input("Introduce una palabra: ")

contador = 0

for parrafo in todos_parrafos:
    if palabra in parrafo:
        contador += 1

print("La palabra", palabra, "aparece", contador, "veces en todas las noticias.")