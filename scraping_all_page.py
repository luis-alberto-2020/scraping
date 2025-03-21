import requests
from bs4 import BeautifulSoup
import csv

base_url = "http://books.toscrape.com/catalogue/page-{}.html" # Usaremos .format()
all_data = []

for page_num in range(1, 51):  # Books to Scrape tiene 50 páginas
    url = base_url.format(page_num)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text
        all_data.append([title, price])

with open('books_all_pages.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title','Price'])
    writer.writerows(all_data)

print("Datos de todas las páginas extraídos y guardados en books_all_pages.csv")