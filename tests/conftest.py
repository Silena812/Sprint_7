import requests
import helper
import pytest
from data import Url

@pytest.fixture
def courier_data():
    login = helper.generate_login()
    password = helper.generate_password()
    name = helper.generate_name()
    return {"login": login, "password": password, "firstName": name}

@pytest.fixture
def create_courier():
    login = helper.generate_login()
    password = helper.generate_password()
    name = helper.generate_name()
    courier_data = {'login' : login, 'password': password, 'firstName' : name}
    login_data  = {'login' : login, 'password': password}
    requests.post(f'{Url.MAIN_SITE}{Url.CREATE_COURIER}', json=courier_data)
    yield courier_data
    login_response = requests.post(f'{Url.MAIN_SITE}{Url.LOGIN_COURIER}', json=login_data)
    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        requests.delete(f"{Url.MAIN_SITE}{Url.DELETE_COURIER}/{courier_id}")

@pytest.fixture
def login_courier():
    login = helper.generate_login()
    password = helper.generate_password()
    name = helper.generate_name()
    courier_data = {'login': login, 'password': password, 'firstName': name}
    login_data = {'login': login, 'password': password}
    requests.post(f'{Url.MAIN_SITE}{Url.CREATE_COURIER}', json=courier_data)
    yield [courier_data, login_data]
    login_response = requests.post(f'{Url.MAIN_SITE}{Url.LOGIN_COURIER}', json=login_data)
    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        requests.delete(f"{Url.MAIN_SITE}{Url.DELETE_COURIER}/{courier_id}")