import requests
from data import Url
import allure

class TestOrderList:
    @allure.title("Тест проверяет, что в тело ответа возвращается список заказов.")
    def test_get_order_list_returns_200(self):
        response = requests.get(f'{Url.MAIN_SITE}{Url.GET_ORDERS_LIST}')
        assert response.status_code == 200 and 'orders' in response.json()