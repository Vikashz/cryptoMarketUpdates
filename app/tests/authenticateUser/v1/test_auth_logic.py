import pytest
import requests
from app.constants import pre_url
import json
from bson import ObjectId
from app import mongo
from app.authenticateUser.v1.business import signup



@pytest.fixture(scope="function")
def delete_test_user(request):
    mongo.api_user.delete_one({"email": "vicky@mailinator.com"})
    def tear_down():
        mongo.api_user.delete_one({"email": "vicky@mailinator.com"})

    request.addfinalizer(tear_down)


@pytest.fixture(scope="function")
def populate_test_user(request):
    data = {"_id": ObjectId("63d643c25fe8b555a9da42b2"), "first_name": "Akash", "last_name": "Kumar",
            "email": "ak@mailinator.com",
            "password": "pbkdf2:sha256:260000$mzSxx8N5OdW4cprX$2d1c2acbf35193334a39f73fefe9c99f46fcd2273c9fb2ba91121b69a3d81ffd"}
    mongo.api_user.insert_one(data)

    def tear_down():
        mongo.api_user.delete_one({'_id': ObjectId("63d643c25fe8b555a9da42b2")})

    request.addfinalizer(tear_down)


def test_create_new_api_user(delete_test_user):
    """
    Test to check if new user can sign up
    """
    payload = {"email": "vicky@mailinator.com",
               "password": "lol123",
               "first_name": "vicky",
               "last_name": "K"}
    url = pre_url + "/signup"
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url, headers=headers, data=json.dumps(payload))
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == True


def test_create_existing_api_user(populate_test_user):
    """
    Test to check if existing user can sign up
    """
    payload = {"email": "ak@mailinator.com",
               "password": "lol123",
               "first_name": "Akash",
               "last_name": "Kumar"}
    url = pre_url + "/signup"
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url, headers=headers, data=json.dumps(payload))
    assert res.status_code == 500
    data = res.json()
    assert data["status"] == False


def test_valid_user_logs_in(populate_test_user):
    """
    Test valid user can log in
    """
    email = "ak@mailinator.com"
    password = "lol123"
    url = pre_url + f"/login/{email}?password={password}"
    headers = {'Content-Type': 'application/json'}
    res = requests.get(url, headers=headers)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == True
    assert data["message"] == "Valid User"


def test_invalid_user_logs_in():
    """
    Test invalid user can not log in
    """
    email = "test1234@mailinator.com"
    password = "lol123"
    url = pre_url + f"/login/{email}?password={password}"
    headers = {'Content-Type': 'application/json'}
    res = requests.get(url, headers=headers)
    assert res.status_code == 401
    data = res.json()
    assert data["status"] == False
    assert data["message"] == "User not found, Make sure that the credentials used are correct"


def test_create_new_api_user_business(delete_test_user):
    """
    Test business function to check if new user can sign up
    """
    payload = {"email": "vicky@mailinator.com",
               "password": "lol123",
               "first_name": "vicky",
               "last_name": "K"}
    res = signup(payload)
    assert isinstance(res, ObjectId) == True
