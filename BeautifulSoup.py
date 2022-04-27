import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count_number = int(input('Enter count: '))
position_number = int(input('Enter position: ')) -1
count1 = 0
"""http://py4e-data.dr-chuck.net/known_by_Fikret.html"""

def parse_website(url, position_number):     
    url = tag[position_number ].get('href')
    i = 0
    for tag in tags:
        i += 1
        if i == position_number:
            return tag.get('href', None)

while count_number < count1:
    print('Retrieving: ', url)
    enter_website = parse_website(url, position_number)
    count1 = count_number + 1
    tags = soup('a')
    name = tags[position_number].contents[0]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')

print(name)
