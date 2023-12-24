import httpx
from jsonschema import validate
from core.contracts import RESOURSES_SCHEMA
import allure

BASE_URL = 'https://reqres.in/api/unknown'


@allure.suite('Проверка запросов с данными ресурсов')
@allure.title('Метод, проверяющий список ресурсов')
def test_list_resources():
    with allure.step('Выполняем Get запрос'):
        response = httpx.get(BASE_URL + '?page=2')
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    resource_data = response.json()['data']
    for item in resource_data:
        with allure.step('Сверяем ответ с контрактом'):
            validate(item, RESOURSES_SCHEMA)


@allure.suite('Проверка запросов с данными ресурсов')
@allure.title('Метод, проверяющий одного ресурса')
def test_one_resource():
    with allure.step('Выполняем Get запрос'):
        response = httpx.get(BASE_URL + '/2')
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    resource_data = response.json()['data']
    with allure.step('Сверяем ответ с контрактом'):
        validate(resource_data, RESOURSES_SCHEMA)
    with allure.step('Проверяем айди'):
        assert resource_data['id'] == 2
    with allure.step('Проверяем имя цвета'):
        assert resource_data['name'] == 'fuchsia rose'
    with allure.step('Проверяем год цвета'):
        assert resource_data['year'] == 2001
    with allure.step('Проверяем цвет'):
        assert resource_data['color'] == '#C74375'
    with allure.step('Проверяем значение Pantone'):
        assert resource_data['pantone_value'] == '17-2031'


@allure.suite('Проверка запросов с данными ресурсов')
@allure.title('Метод, проверяющий ненайденного ресурса')
def test_resource_not_found():
    with allure.step('Выполняем Get запрос'):
        response = httpx.get(BASE_URL + '/23')
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 404

