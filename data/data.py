import json
import os


current_dir = os.getcwd()
json_file_path = os.path.join(current_dir, 'data', 'genres.json')

with open(json_file_path) as file:
    data = json.load(file)

def readJson():
    return data