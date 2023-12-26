import json

import httpx
import allure
import pytest

BASE_URL = 'https://reqres.in/api/register'


@allure.suite('Проверка запросов регистрации')
@allure.title('Метод, успешной регистрации')
def test_register():
    body = {"email": "eve.holt@reqres.in", "password": "pistol"}
    headers = {'Content-Type': 'application/json'}
    with allure.step('Выполняем Post запрос'):
        response = httpx.post(BASE_URL, json=body, headers=headers)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

json_file = open('./register_creditional.json')
register_creditional = json.load(json_file)
@pytest.mark.parametrize("register_creditional",register_creditional)
@allure.suite('Проверка запросов с выполнением работ по юзерам')
@allure.title('Метод, создающий юзера')
def test_unsuccessful_register(register_creditional):
    headers = {'Content-Type': 'application/json'}
    with allure.step('Выполняем Post запрос'):
        response = httpx.post(BASE_URL, json=register_creditional, headers=headers)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 400