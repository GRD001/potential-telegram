import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"  # замените ссылку на нужную

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # здесь можно использовать различные методы для поиска нужных элементов на странице с помощью библиотеки BeautifulSoup
    # например, можно найти все заголовки h1 на странице:
    headers = soup.find_all('h1')
    for header in headers:
        print(header.text)
else:
    print("Ошибка при запросе страницы")
