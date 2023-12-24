import httpx
import allure

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
