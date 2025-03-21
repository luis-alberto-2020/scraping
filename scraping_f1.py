import requests
from bs4 import BeautifulSoup
import csv

# URL del sitio web
url = "http://books.toscrape.com/"

# Obtener el HTML de la página
response = requests.get(url)
response.raise_for_status()  # Lanza un error si la petición falla

# Crear el objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todos los elementos que contienen información de los libros
books = soup.find_all('article', class_='product_pod')

# Crear una lista para almacenar los datos
data = []

# Iterar sobre cada libro
for book in books:
    # Extraer el título
    title = book.find('h3').find('a')['title']

    # Extraer el precio
    price = book.find('p', class_='price_color').text

    # Añadir los datos a la lista
    data.append([title, price])

# Guardar los datos en un archivo CSV
with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Price'])  # Escribir la cabecera
    writer.writerows(data)  # Escribir los datos

print("Datos extraídos y guardados en books.csv")