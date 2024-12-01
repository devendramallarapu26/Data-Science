import requests
from bs4 import BeautifulSoup
response = requests.get('https://quotes.toscrape.com/')
result = BeautifulSoup(response.text,'html.parser')
dict = {}
for data2 in data1:
    key = data2.find('small',class_='author').text
    value = data2.find('span',class_='text').text
    dict[key]=value
print(dict) # it store the data in dict
