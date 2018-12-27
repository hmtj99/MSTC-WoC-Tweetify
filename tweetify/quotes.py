from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.lifewire.com/quotes-about-twitter-3289006').text

soup = BeautifulSoup(source,'lxml')

#print(soup.prettify)
quotes = soup.find_all('p')

with open('quotes.txt','w') as f:
    for quote in quotes:
        f.write(quote.text)
        f.write("\n")
print("Wrtiting of file done!")