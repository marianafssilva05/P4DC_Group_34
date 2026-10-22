import json

def json_reader(path):
    with open(path, "r") as f:
        return json.load(f)
