import requests
import pytest
import helper
import allure

from data import Url, Response

class TestCreateCourier:
    @allure.title("Тест проверяет успешное создание курьера со всеми обязательными полями")
    def test_create_courier_positive_result(self, courier_data):
        response = requests.post(f"{Url.MAIN_SITE}{Url.CREATE_COURIER}", json=courier_data)
        assert response.status_code == 201
        assert response.json() == Response.COURIER_CREATION_SUCCESS

        login_response = requests.post(
            f"{Url.MAIN_SITE}{Url.LOGIN_COURIER}",
            json={"login": courier_data["login"], "password": courier_data["password"]}
        )
        assert login_response.status_code == 200
        courier_id = login_response.json()["id"]

        delete_response = requests.delete(f"{Url.MAIN_SITE}{Url.DELETE_COURIER}/{courier_id}")
        assert delete_response.status_code == 200

    @allure.title("Тест проверяет, что нельзя создать двух одинаковых курьеров")
    def test_create_existing_courier_returns_409(self, create_courier):
        response = requests.post(f"{Url.MAIN_SITE}{Url.CREATE_COURIER}", json=create_courier)

        assert response.status_code == 409
        assert response.json() == Response.COURIER_ALREADY_EXIST

    @allure.title("Тест проверяет, что нельзя создать курьера без логина или без пароля")
    @pytest.mark.parametrize("courier_data", [
        lambda: {"password": helper.generate_password(), "firstName": helper.generate_name()},
        lambda: {"login": helper.generate_login(), "firstName": helper.generate_name()},
        ])
    def test_create_courier_missing_data_returns_400(self, courier_data):
        data = courier_data()
        response = requests.post(f"{Url.MAIN_SITE}{Url.CREATE_COURIER}", json=data)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"