import json

try:
    with (open("log.txt")) as file:
        data = json.load(file)
    
    print("data has been successfully retrieved")
except json.decoder.JSONDecodeError:
    print("There was a problem accessing the equipment data")
    
    #import json

#with open("equipment.json") as file:
	#data = json.load(file)

#print("Equipment data has been successfully retrieved.") #comment the code above and than uncomment it to have the code above work
