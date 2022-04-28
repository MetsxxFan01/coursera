import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
num = int(input('Enter count: '))
pos = int(input('Enter position: '))
html = urllib.request.urlopen(url, context=ctx).read()
load_the_webpage_content = requests.get(url)
soup = BeautifulSoup(html, 'html.parser')
tags = soup.find_all('li')
for tag in soup.find_all('li'):
    print('%-10s : %s' % (tag.string, tag.a['href']))
    while_loop = 5
while while_loop > 0:
    while_loop = while_loop -1
    print('Retrieving: ', tag)
