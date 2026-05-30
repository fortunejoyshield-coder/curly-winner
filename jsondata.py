import json

data = {"name": "SS", "prime_candidate": True}

with open("output.json", "w") as f:
    json.dump(data, f, indent=4)
import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)

