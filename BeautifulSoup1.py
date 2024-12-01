import requests
from bs4 import BeautifulSoup
response = requests.get('https://quotes.toscrape.com/')
result = BeautifulSoup(response.text,'html.parser')
print(result.find_all('div')) # its give only div tags in html tags
