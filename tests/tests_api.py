import jsonschema
import requests

from tests.utils import load_schema


def test_get_single_resource_successfully():
    url = "https://reqres.in/api/unknown/2"
    schema = load_schema("get_single_resource.json")

    result = requests.get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)

def test_get_single_resource_not_found():
    url = "https://reqres.in/api/unknown/23"

    result = requests.get(url)

    assert result.status_code == 404
