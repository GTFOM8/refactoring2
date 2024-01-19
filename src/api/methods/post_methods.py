import uuid
import random
import requests


class PostAPIMethods:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_post_request(self, amount, order_id, back_to_merchant_url, payment_method, currency, card_number,
                          callback_url, date, wallet_provider):
        """ Универсальная функция для выполнения POST-запросов """

        """ Генерация случайного числа в диапазоне от 9000 до 10000, с использованием функции 'randint' 
          из модуля 'random'. Полученное значение присваивается переменной random_amount """
        def get_random_between(min_val, max_val):
            return random.randint(min_val, max_val)

        random_amount = get_random_between(9000, 10000)

        """ Генерация случайного ID  с помощью UUID4 """
        random_id = f'test-{str(uuid.uuid4())}'

        body = {
            "amount": random_amount,
            "order_id": random_id,
            "back_to_merchant_url": '',
            "payment_method": 1,
            "card_number": "",
            "callback_url": '',
        }

        response = requests.post(url, json=data)
        return response

    def get_user(self, user_id):
        """
        Универсальная GET-функция получения данных о пользователе
        :param user_id: Идентификатор пользователя
        :return: Объект с сервера
        """

        endpoint = f'users/{user_id}'
        return self.get(endpoint)