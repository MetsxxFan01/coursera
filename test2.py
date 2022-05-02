import json

try:
    with (open("log.txt", "r")) as f:
        pass
        data = json.load(f)
except json.decoder.JSONDecodeError:
    f = open("log.txt", "r")
    print(f.read())
    f.close()
    
#import json

#with open("log.txt") as file:
	#data = json.load(file)

#print("Equipment data has been successfully retrieved.") #comment the code above and than uncomment it to have the code above work
#this code below doesn't work 
