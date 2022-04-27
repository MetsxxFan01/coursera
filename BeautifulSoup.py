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
load_the_webpage_content = requests.get("http://py4e-data.dr-chuck.net/known_by_Fikret.html")
soup = BeautifulSoup(html, 'html.parser')
for tag in soup.find_all('a'):
    tags = soup('a')
while_loop = 5
while while_loop > 0:
    while_loop = while_loop -1
print('Retrieving: ', tag)
