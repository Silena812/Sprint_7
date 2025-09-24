class Url:
    MAIN_SITE = 'https://qa-scooter.praktikum-services.ru/'
    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    DELETE_COURIER = '/api/v1/courier'
    CREATE_ORDER = '/api/v1/orders'
    GET_ORDERS_LIST = '/api/v1/orders'

class Order:
    order_data = {
    "firstName": "Елена",
    "lastName": "Силина",
    "address": "улица и дом 6",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 2,
    "deliveryDate": "2025-09-30",
    "comment": "комментарий к заказу",
    }
    color = [
        ['BLACK'],
        ['GREY'],
        ['BLACK','GREY'],
        []
    ]

class Response:
    COURIER_CREATION_SUCCESS = {'ok': True}
    COURIER_ALREADY_EXIST = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    COURIER_REGISTRATION_MISSED_DATA = {'code' : 400, 'message': 'Недостаточно данных для создания учетной записи'}
    COURIER_ACCOUNT_NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}
    COURIER_LOGIN_MISSED_LOGIN = {'code': 400, 'message':  'Недостаточно данных для входа'}
    COURIER_LOGIN_MISSED_PASSWORD = {'code': 504, 'message': 'Недостаточно данных для входа'}