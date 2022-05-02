import json

try:
    with (open("log.txt")) as file:
        data = json.load(file)
    
    print("data has been successfully retrieved")
except json.decoder.JSONDecodeError:
    print("There was a problem accessing the equipment data")