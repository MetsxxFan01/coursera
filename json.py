import urllib.request	#importing urllib
import json		#importing json

#requesting a json file url
url = input("Enter the URL:")		
#load json file as list -info
info = json.loads(urllib.request.urlopen(url).read())

x = 0 
#loop through each item in list comments
for items in info['comments']:
#loop through the value of the key count in the list and add 
	x = x + int(items['count'])
print('count: ',(x))