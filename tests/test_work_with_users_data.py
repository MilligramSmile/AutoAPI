import datetime
import json

import httpx
import allure
import pytest

BASE_URL = 'https://reqres.in/api/users'

@allure.suite('Проверка запросов с выполнением работ по юзерам')
@allure.title('Метод, удаляющий юзера')
def test_user_delete():
    with allure.step('Выполняем Delete запрос'):
        response = httpx.delete(BASE_URL + '/2')
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 204

@allure.suite('Проверка запросов с выполнением работ по юзерам')
@allure.title('Метод, создающий юзера')
def test_create_user():
    body = {"name": "morpheus", "job": "leader"}
    headers = {'Content-Type': 'application/json'}
    with allure.step('Выполняем Create запрос'):
        response = httpx.post(BASE_URL, json=body, headers=headers)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201
    user_name = body["name"]
    with allure.step('Проверяем соответствие имени'):
        assert user_name == response.json()['name']
    user_job = body["job"]
    with allure.step('Проверяем соответствие работы'):
        assert user_job == response.json()['job']

#тянем тело из json файла
json_file = open('./users_credentials.json')
users_credentials = json.load(json_file)
@pytest.mark.parametrize("users_credentials",users_credentials)
@allure.suite('Проверка запросов с выполнением работ по юзерам')
@allure.title('Метод, создающий юзера')
def test_create_user_from_json_file(users_credentials):
    headers = {'Content-Type': 'application/json'}
    with allure.step('Выполняем Create запрос'):
        response = httpx.post(BASE_URL, json=users_credentials, headers=headers)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201
    user_name = users_credentials["name"]
    with allure.step('Проверяем соответствие имени'):
        assert user_name == response.json()['name']
    user_job = users_credentials["job"]
    with allure.step('Проверяем соответствие работы'):
        assert user_job == response.json()['job']
    response_date = response.json()['createdAt'].replace('T', ' ')
    #альт допустимый вариант response_date = response_date.replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    with allure.step('Проверяем дату создания запроса c текущим временем'):
        assert response_date[0:19] == current_date[0:19]

