from bs4 import BeautifulSoup
import urllib
import urllib.parse
import urllib.request
from urllib.request import urlopen

url = input('enter - ')

html = urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')

for tag in tags:
    print (tag.get('href',None))

page = urlopen(url).read()
soup = BeautifulSoup(page)
print(soup.find_all('a'))

print(soup.find_all('a')[15])

