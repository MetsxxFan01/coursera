import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

load_the_webpage_content = requests.get(url)

for tag in tags(range(count-1):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('a')
    url = tags[position - 1].a['href']
    
    while_loop = 5
while while_loop > 0:
    while_loop = while_loop -1
print('Retrieving: ', url)
