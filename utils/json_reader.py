import json

def json_reader(path):
    # Your code goes here
    with open(path, "r") as f:
        return json.load(f)
