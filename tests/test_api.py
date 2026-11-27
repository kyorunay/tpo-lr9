# Тесты REST API на Python (повторяют проверки из Postman)
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user():
    response = requests.get(BASE_URL + "/users/1")

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    user = response.json()
    for field in ["id", "name", "username", "email", "address", "company"]:
        assert field in user
    assert user["id"] == 1
    assert user["username"] == "Bret"
    assert "@" in user["email"]


def test_get_user_not_found():
    response = requests.get(BASE_URL + "/users/999")

    assert response.status_code == 404
    assert response.json() == {}


def test_create_user():
    new_user = {"name": "Анастасия Яковлева", "username": "nastya", "email": "nastya@mail.ru"}
    response = requests.post(BASE_URL + "/users", json=new_user)

    assert response.status_code == 201
    user = response.json()
    assert "id" in user
    assert isinstance(user["id"], int)
    assert user["name"] == new_user["name"]
    assert user["username"] == new_user["username"]
    assert user["email"] == new_user["email"]


def test_update_user():
    updated_user = {"id": 1, "name": "Анастасия Яковлева", "username": "nastya", "email": "new@mail.ru"}
    response = requests.put(BASE_URL + "/users/1", json=updated_user)

    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert user["name"] == "Анастасия Яковлева"
    assert user["email"] == "new@mail.ru"
