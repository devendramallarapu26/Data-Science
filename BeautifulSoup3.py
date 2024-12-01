import requests
from bs4 import BeautifulSoup
response = requests.get('https://quotes.toscrape.com/')
result = BeautifulSoup(response.text,'html.parser')
data1 = result.find_all('div',class_='quote')
for data2 in data1:
    print(data2.find('span',class_='text').text) # its give only text inside content of html tags
