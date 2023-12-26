import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEMA
import allure

BASE_URL = 'https://reqres.in/api/users'
EMAIL_ENDS = '@reqres.in'


@allure.suite('Проверка запросов с данными пользователей')
@allure.title('Метод, проверяющий список пользователей')
def test_list_users():
    with allure.step('Выполняем Get запрос'):
        response = httpx.get(BASE_URL + '?page=2')
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    users_data = response.json()['data']
    for item in users_data:
        with allure.step('Сверяем ответ с контрактом'):
            validate(item, USER_DATA_SCHEMA)
        with allure.step(f'Проверяем, что еmail оканчивается на {EMAIL_ENDS}'):
            assert item['email'].endswith(EMAIL_ENDS)


@allure.suite('Проверка запросов с данными пользователей')
@allure.title('Метод, проверяющий одного пользователя')
def test_one_user():
    with allure.step('Выполняем Get запрос'):
        response = httpx.get(BASE_URL + '/2')
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    users_data = response.json()['data']
    with allure.step('Сверяем ответ с контрактом'):
        validate(users_data, USER_DATA_SCHEMA)
    with allure.step(f'Проверяем, что еmail оканчивается на {EMAIL_ENDS}'):
        assert users_data['email'].endswith(EMAIL_ENDS)


@allure.suite('Проверка запросов с данными пользователей')
@allure.title('Метод, проверяющий ненайденного пользователя')
def test_user_not_found():
    with allure.step('Выполняем Get запрос'):
        response = httpx.get(BASE_URL + '/23')
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 404

