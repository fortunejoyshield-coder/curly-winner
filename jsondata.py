import json

data = {"name": "SS", "prime_candidate": True}

def write(data):
    with open("output.json", "w") as f:
        json.dump(data, f, indent=4)

def read():
    with open("data.json", "r") as f:
        return json.load(f)

def stringify(kind):
    if kind == 1:
        return "TF="
    elif kind == 2:
        return "P+1F="
    else:
        return "PollardP-1 ="

def format(assignment):
    data1 = stringify(assignment.type)
    return data1 + "," + str(assignment.p) + "," + str(assignment.limit)

def formatcores(cpu_num, work):
    data = ""
    for x in range(1, cpu_num + 1):
        data += f"Worker {x} doing assignment {work[x]}\n"
    return data
