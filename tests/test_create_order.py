import requests
import pytest
from data import Url, Order
import allure

class TestCreateOrder:
    @allure.title("Тест проверяет успешное создание заказа со всеми вариациями выбора цвета самоката")
    @pytest.mark.parametrize("color", [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        []
    ])
    def test_create_order_with_colors(self, color):
        order_data = Order.order_data.copy()
        order_data['color'] = color if color else None
        if order_data['color'] is None:
            order_data.pop('color')

        response = requests.post(f"{Url.MAIN_SITE}{Url.CREATE_ORDER}", json=order_data)

        assert response.status_code == 201
        assert 'track' in response.json()