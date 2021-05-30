import json
import requests


def create_json_object():
    return {
        "users": [
            {
                "user": {
                    "id": 0,
                    "username": "Polia111",
                    "firstname": "Polia",
                    "lastName": "string",
                    "email": "string",
                    "password": "string",
                    "phone": "string",
                    "userStatus": 0,
                }
            }
        ]
    }


def test_send_json_with_unique_number_check_status_code():
    response = requests.post("https://petstore.swagger.io/v2/user/", json=create_json_object())
    print(response.request.body)
    assert response.status_code == 200


def test_put_json_with_unique_number_check_status_code():
    response = requests.put("https://petstore.swagger.io/v2/user/Polina8", data = json.dumps({'username':'Polina8'}))
    assert response.status_code == 200


def test_get_name_check_status_code_equals_200():
    response = requests.get("https://petstore.swagger.io/v2/user/Polia111")
    assert response.status_code == 200


def test_get_name_Polina8_check_status_code_equals_200():
    response = requests.get("https://petstore.swagger.io/v2/user/Polina8")
    response_body = response.json()
    assert response_body["username"] == "Polina8"


def delete_check_status_code_equals_200():
    response = requests.delete("https://petstore.swagger.io/v2/user/Polina8")
    assert response.status_code == 200


