import json

data = {"name": "SS", "prime_candidate": True}
def write(data)
    with open("output.json", "w") as f:
        json.dump(data, f, indent=4)

def read():
    with open("data.json", "r") as f:
        data = json.load(f)
        return data

print(data)

