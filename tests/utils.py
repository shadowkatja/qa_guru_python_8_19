import json
import os

resources_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../schema'))

def load_schema(file):
    with open(os.path.join(resources_path, file)) as file:
        schema = json.load(file)
        return schema
