import requests
from data import Url, Response
import allure


class TestLoginCourier:
    @allure.title("Тест проверяет успешный логин курьера со всеми обязательными полями")
    def test_courier_can_login(self, login_courier):
        create_courier_data, login_data = login_courier
        response = requests.post(f"{Url.MAIN_SITE}{Url.LOGIN_COURIER}", json=login_data)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Тест проверяет, что нельзя залогиниться без логина")
    def test_login_missing_login_returns_400(self, login_courier):
        create_courier_data, login_data = login_courier
        data = login_data.copy()
        data.pop("login")
        response = requests.post(f"{Url.MAIN_SITE}{Url.LOGIN_COURIER}", json=data)

        print(response.status_code, response.text)
        assert response.status_code == 400
        assert response.json()["message"] == Response.COURIER_LOGIN_MISSED_LOGIN["message"]

    @allure.title("Тест проверяет, что нельзя залогиниться без пароля")
    def test_login_missing_password(self, login_courier):
        create_courier_data, login_data = login_courier
        data = login_data.copy()
        data.pop("password")
        response = requests.post(f"{Url.MAIN_SITE}{Url.LOGIN_COURIER}", json=data)

        print(response.status_code, response.text)
        assert response.status_code in [400, 504]

    @allure.title("Тест проверяет, что нельзя залогиниться под несуществующим пользователем")
    def test_login_nonexistent_user_returns_404(self):
        import helper
        login_data = {"login": helper.generate_login(), "password": helper.generate_password()}
        response = requests.post(f"{Url.MAIN_SITE}{Url.LOGIN_COURIER}", json=login_data)
        assert response.status_code == 404
        assert response.json()["message"] == Response.COURIER_ACCOUNT_NOT_FOUND["message"]