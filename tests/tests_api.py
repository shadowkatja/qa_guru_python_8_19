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

def test_get_list_of_resources_schema_successfully():
    url = "https://reqres.in/api/unknown"
    schema = load_schema("get_list_resource.json")

    result = requests.get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)


def test_get_list_of_resources_total_pages():
    url = "https://reqres.in/api/unknown"
    total_pages = 2

    result = requests.get(
        url,
        params={"total_pages": total_pages}
    )

    assert result.json()["total_pages"] == total_pages

def test_create_new_user_successfully():
    schema = load_schema("post_create_user.json")

    result = requests.post(
        'https://reqres.in/api/users',
        {
            "name": "Charles",
            "job": "Ferrari F1 driver"
        }
    )

    assert result.status_code == 201
    assert result.json()['name'] == 'Charles'
    assert result.json()['job'] == 'Ferrari F1 driver'
    jsonschema.validate(result.json(), schema)

def test_update_existent_user():
    schema = load_schema("put_update_user.json")

    result = requests.put(
        'https://reqres.in/api/users/2',
        {
            "name": "Charles Leclerc",
            "job": "Ferrari F1 driver"
        }
    )
    assert result.status_code == 200
    assert result.json()['name'] == 'Charles Leclerc'
    assert result.json()['job'] == 'Ferrari F1 driver'
    jsonschema.validate(result.json(), schema)

def test_delete_user():
    result = requests.delete(
        'https://reqres.in/api/users/2'
    )

    assert result.status_code == 204

def test_successful_registration():
    result = requests.post(
        'https://reqres.in/api/register',
        {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
    )

    assert result.status_code == 200
    assert result.json()['token'] is not None

def test_unsuccessful_registration():
    result = requests.post(
        'https://reqres.in/api/register',
        {
            "email": "eve.holt@reqres.in",
            "password": ""
        }
    )

    assert result.status_code == 400
    assert result.json()['error'] == 'Missing password'

def test_successful_login():
    result = requests.post(
        'https://reqres.in/api/login',
        {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    )

    assert result.status_code == 200
    assert result.json()['token'] == "QpwL5tke4Pnpja7X4"

def test_unsuccessful_login():
    result = requests.post(
        'https://reqres.in/api/login',
        {
            "email": "peter@klaven",
            "password": ""
        }
    )

    assert result.status_code == 400
    assert result.json()['error'] == 'Missing password'