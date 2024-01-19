import subprocess
import threading
import psycopg2
from loguru import logger


class SqlMethods:
    def __init__(self, browser):
        self.browser = browser

    result = None

    dev_connection_data = {
        'host': '',
        'port': '',
        'database': '',
        'user': '',
        'password': ''
    }
    release_connection_data = {
        'host': '',
        'port': '',
        'database': '',
        'user': '',
        'password': ''
    }

    @staticmethod
    def stop_openvpn(pas):
        """ Функция, разрывающая соединение с OpenVPN """
        try:
            password = pas
            args = ['taskkill', '/F', '/IM', 'openvpn.exe']
            subprocess.run(args, input=password, check=True, text=True)
            return "OpenVPN stopped successfully."

        except subprocess.CalledProcessError as e:
            return f"An error occurred while stopping OpenVPN: {e}"

    @staticmethod
    def execute_sql_request(config_path, connection_data, sql_query):
        """ Подключается к базе и выполняет SQL запрос, возвращает результат запроса или текст ошибки """
        logger.info('Подключиться к OpenVPN')
        vpn_thread = threading.Thread(target=lambda: subprocess.run(['openvpn', '--config', config_path]))
        vpn_thread.start()

        connection = None

        try:
            vpn_thread.join(timeout=30)

            connection = psycopg2.connect(
                host=connection_data['host'],
                user=connection_data['user'],
                password=connection_data['password'],
                database=connection_data['database']
            )

            logger.info('Отправить запрос к БД')
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                db_result = cursor.fetchall()

                SqlMethods.result = [row[0].lower() for row in db_result]

                print('[INFO]: Result: ', SqlMethods.result)

        except Exception as _ex:
            print('[INFO]: An error occurred while working with PostgreSQL', _ex)
        finally:
            if connection is not None:
                connection.close()

            logger.info('Остановить VPN-соединение')
            SqlMethods.stop_openvpn(pas='1927')

    @staticmethod
    def compare_values_dropdown_list(expected_values, db_values):
        """ Функция, проверяющая, что значения выпадающего списка с сайта и БД совпадают """
        filtered_expected_values = [val for val in expected_values if val not in ('all', 'none', '')]
        filtered_db_values = [val for val in db_values if val not in ('all', 'none', '')]

        # Преобразуем значения в плоский список
        print('Значения из дроп-дауна: ', sorted(expected_values))
        print('Значения из БД: ', sorted(db_values))

        assert sorted(filtered_expected_values) == sorted(filtered_db_values), 'Полученные значения не совпадают'


