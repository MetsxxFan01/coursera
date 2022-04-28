
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
for i in range(count):
    i += 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    newtag = tags[position-1]
    url = newtag.get('href', None)
    print(url)
