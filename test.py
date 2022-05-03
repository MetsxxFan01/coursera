import json

def write_json(data, filename="log.json"):
    with open(filename,"w") as file:
        json.dump(data, file, indent=4)
def load_json():     
    with open("log.json","r") as json_file:
        data = json.load(json_file)
    temp = data["names"]
    add_letters = {"A", "M", "A", "I", "C", "O", "N", "Z", "E"}
    temp.append(add_letters)

data = "A", "M", "A", "I", "C", "O", "N", "Z", "E"
write_json(data)