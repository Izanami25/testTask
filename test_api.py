import pytest
import requests
import allure

API_BASE_URL = "https://demoqa.com"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IjEyMyIsInBhc3N3b3JkIjoiWmh1a3VzaDEyMyEiLCJpYXQiOjE3MTI1NzA2NTd9.mUvvwh750uOZxfLo28tObseR6pOAkgc1q_D9G2fz6cQ"

@pytest.mark.parametrize("username,password", [("Ulan", "Zhukush")])
@allure.feature("API Account")
@allure.story("Login with not registered user")
def test_invalid_login(username, password):
    url = f"{API_BASE_URL}/Account/v1/Authorized"
    payload = {"userName": username, "password": password}
    response = requests.post(url, json=payload)
    assert response.status_code == 404
    
@pytest.mark.parametrize("username,password", [("Ulan1", "Zhukush123563222!")])
@allure.feature("API Account")
@allure.story("Register")
def test_register(username, password):
    url = f"{API_BASE_URL}/Account/v1/User"
    payload = {"userName": username, "password": password}
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert username in response.json()["username"]
    
@pytest.mark.parametrize("username,password", [("Ulan1", "Zhukush123!")])
@allure.feature("API Account")
@allure.story("Login with registered user")
def test_valid_login(username, password):
    url = f"{API_BASE_URL}/Account/v1/Authorized"
    payload = {"userName": username, "password": password}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    
@pytest.mark.parametrize("username,password", [("123", "Zhukush")])
@allure.feature("API Account")
@allure.story("Register with invalid password")
def test_invalid_password_register(username, password):
    url = f"{API_BASE_URL}/Account/v1/User"
    payload = {"userName": username, "password": password}
    response = requests.post(url, json=payload)
    assert response.status_code == 400
    
@pytest.mark.parametrize("username,password", [("123", "Zhukush123!")])
@allure.feature("API Account")
@allure.story("Register with registered account")
def test_already_registered(username, password):
    url = f"{API_BASE_URL}/Account/v1/User"
    payload = {"userName": username, "password": password}
    response = requests.post(url, json=payload)
    assert "User exists!" in response.json()["message"]
    
@pytest.mark.parametrize("username,password", [("123", "Zhukush123!")])
@allure.feature("API Account")
@allure.story("Generate Token")
def test_token(username, password):
    url = f"{API_BASE_URL}/Account/v1/GenerateToken"
    payload = {"userName": username, "password": password}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    
    
@allure.feature("API Account")
@allure.story("Info User")
def test_info_user():
    url = f"{API_BASE_URL}/Account/v1/User"
    headers = {"Authorization": f"{TOKEN}"}
    params = {"UserId": TOKEN}
    response = requests.get(url, params=params, headers=headers)
    assert response.status_code == 200
    
@allure.feature("API Account")
@allure.story("Delete User")
def test_delete_user():
    url = f"{API_BASE_URL}/Account/v1/User"
    params = {"UserId": TOKEN}
    response = requests.delete(url, params=params)
    assert response.status_code == 200

