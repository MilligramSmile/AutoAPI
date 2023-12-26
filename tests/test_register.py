import json

import httpx
import allure
import pytest

BASE_URL = 'https://reqres.in/api/register'

json_file = open('./successful_register_creditional.json')
successful_register_creditional = json.load(json_file)
@pytest.mark.parametrize("successful_register_creditional",successful_register_creditional)
@allure.suite('Проверка запросов регистрации')
@allure.title('Метод, успешной регистрации')
def test_register(successful_register_creditional):
    headers = {'Content-Type': 'application/json'}
    with allure.step('Выполняем Post запрос'):
        response = httpx.post(BASE_URL, json=successful_register_creditional, headers=headers)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

json_file = open('./unsuccessful_register_creditional.json')
unsuccessful_register_creditional = json.load(json_file)
@pytest.mark.parametrize("unsuccessful_register_creditional",unsuccessful_register_creditional)
@allure.suite('Проверка запросов регистрации')
@allure.title('Метод, неуспешной регистрации')
def test_unsuccessful_register(unsuccessful_register_creditional):
    headers = {'Content-Type': 'application/json'}
    with allure.step('Выполняем Post запрос'):
        response = httpx.post(BASE_URL, json=unsuccessful_register_creditional, headers=headers)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 400