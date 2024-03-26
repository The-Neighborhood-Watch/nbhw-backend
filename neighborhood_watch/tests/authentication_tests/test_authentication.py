import pytest
import requests
from unittest.mock import patch

# Function to make HTTP requests
def make_request(url, method, headers=None, data=None):
    if method == 'GET':
        return requests.get(url, headers=headers)
    elif method == 'POST':
        return requests.post(url, headers=headers, json=data)

# Function to simulate login
def login(url, data):
    return make_request(url, 'POST', data=data)

# Function to simulate signup
def signup(url, data):
    return make_request(url, 'POST', data=data)

# Function to simulate getting test token
def get_test_token(url, token):
    headers = {'Authorization': f'Token {token}'}
    return make_request(url, 'GET', headers=headers)

# Test cases
def test_login_successful(mocker):
    # Mock the post method of requests module
    mocker.patch('requests.post')
    # Simulate successful login
    requests.post.return_value.status_code = 200
    url = 'http://127.0.0.1:8000/login'
    data = {
        "username": "caseycalkins008",
        "password": "password",
        "email": "cc008@gmail.com"
    }
    response = login(url, data)
    assert response.status_code == 200

def test_signup_successful(mocker):
    # Mock the post method of requests module
    mocker.patch('requests.post')
    # Simulate successful signup
    requests.post.return_value.status_code = 200
    url = 'http://127.0.0.1:8000/signup'
    data = {
        "username": "caseycalkins008",
        "password": "password",
        "email": "cc008@gmail.com"
    }
    response = signup(url, data)
    assert response.status_code == 200

def test_get_test_token_successful(mocker):
    # Mock the get method of requests module
    mocker.patch('requests.get')
    # Simulate successful token retrieval
    requests.get.return_value.status_code = 200
    url = 'http://127.0.0.1:8000/test_token'
    token = 'd6d3e1c956fc7ab4938f460b5de6ce81926d8382'
    response = get_test_token(url, token)
    assert response.status_code == 200

if __name__ == "__main__":
    pytest.main()
