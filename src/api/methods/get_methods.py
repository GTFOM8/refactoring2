import requests


class GetAPIMethods:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        """
        Универсальная функция для выполнения GET-запросов
        :param endpoint: Конечная точка API
        :param params: Параметры запроса(необязательно)
        :return: Объект ответа от сервера.
        """

        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url, params=params)
        return response

    def get_user(self, user_id):
        """
        Универсальная GET-функция получения данных о пользователе
        :param user_id: Идентификатор пользователя
        :return: Объект с сервера
        """

        endpoint = f'users/{user_id}'
        return self.get(endpoint)