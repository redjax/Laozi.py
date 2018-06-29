import json


def readjson(file):
    """Reads data from JSON file."""
    data = []  # Variable to store read JSON data.
    with open(file, encoding='utf-8') as jfile:
        data = json.loads(jfile.read())  # Write JSON data to variable.

    return data


def writejson(file, data):
    """Write new configuration to JSON."""
    with open(file, 'w') as wjfile:  # Open file for writing.
        json.dump(data, wjfile)  # Write 'data' to JSON file.


def getarg(file, arg):
    """Find an argument in JSON file."""
    data = readjson(file)  # Return the data in the JSON file to this function.
    return data.get(arg)  # Return argument if found in JSON file.
