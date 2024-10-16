# task2

import requests


def get_github_user_info(username):
    url = f'https://api.github.com/users/{username}'
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        name = data.get('name', 'Имя не указано')
        login = data.get('login', 'Логин не указан')
        public_repos = data.get('public_repos', 0)
        print(f'Имя пользователя: {name}')
        print(f'Логин пользователя: {login}')
        print(f'Количество репозиториев: {public_repos}')

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP ошибка: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Ошибка запроса: {err}')
    except requests.JSONDecodeError:
        print('Ошибка декодирования JSON ответа')
    except Exception as e:
        print(f'Произошла ошибка: {e}')


get_github_user_info(input("Введите имя пользователя:\n"))
