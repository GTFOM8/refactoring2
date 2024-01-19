from loguru import logger
from src.locators import NavigationTabs
from selenium.webdriver.support.wait import WebDriverWait
from src.locators import AuthorizationPage
from selenium.webdriver.support import expected_conditions as EC
from src.methods.UI.actions_on_elements import ActionsOnElements
from environment_and_test_run import EnvAndRun as ER


class AuthPage:
    """ Методы и функции, предназначенные для работы со страницей авторизации """
    def __init__(self, browser):
        self.browser = browser

    if ER.Env == '1':
        start_page = "URL-1"
    elif ER.Env == '2':
        start_page = "URL-2"
    elif ER.Env == '3':
        start_page = "URL-3"
    elif ER.Env == '4':
        start_page = "URL-4"

    global users
    # Словарь для хранения блокированных пользователей
    user_locks = {}

    def authorization(self, username):
        """ Функция авторизации пользователя """

        """ При использовании, указать в качестве аргумента, пользователя под
        которым нужно авторизоваться в виде: (username='имя_пользователя') """

        # Основные элементы, использующиеся в этой функции
        login_field = self.browser.find_element(*AuthorizationPage.LOGIN_FIELD)
        password_field = self.browser.find_element(*AuthorizationPage.PASSWORD_FIELD)
        login_button = self.browser.find_element(*AuthorizationPage.LOGIN_BUTTON)

        # Словарь, содержащий данные пользователей
        users_dict = {
            "url-1": {
                "user-1": {"login": ""},
                "user-2": {"login": ""},
                "user-3": {"login": ""},
            },
            "url-2": {
                "user-1": {"login": ""},
                "user-2": {"login": ""},
                "user-3": {"login": ""},
            },
            "url-3": {
                "user-1": {"login": ""},
                "user-2": {"login": ""},
                "user-3": {"login": ""},
            }
        }

        current_url = self.start_page

        if current_url in users_dict:
            users = users_dict[current_url]

            # Цикл, находящий данные указанного пользователя в словаре
            if username in users:
                login = users[username]["login"]
                password = users[username]["password"]
            else:
                print('Неизвестный пользователь')
                return False

            # Основные методы функции: Ввести логин и пароль, нажать кнопку 'Login'
            logger.info('Авторизоваться')
            login_field.send_keys(login)
            password_field.send_keys(password)
            login_button.click()

    def perform_authorization(self):
        """ Функция, выполняющая авторизацию """
        logger.info("Нажать на кнопку Login")
        ActionsOnElements.click_element(self.browser, selector=AuthorizationPage.LOGIN_BUTTON)

        incorrect_data_title = "These credentials do not match our records."
        pass_field_is_required = "The password field is required."
        email_field_is_required = "The email field is required."
        missing_symbol = 'Адрес электронной почты должен содержать символ "@"'
        page_source = self.browser.page_source

        if incorrect_data_title in page_source:
            assert incorrect_data_title in page_source, "Надпись об ошибке не появилась в разметке страницы"
            logger.error("Авторизация не произошла. Появился текст с ошибкой: " + incorrect_data_title)
        elif pass_field_is_required in page_source:
            assert pass_field_is_required in page_source, "Надпись о незаполненном поле пароля не появилась"
            logger.error("Авторизация не произошла. Появился текст с ошибкой: " + pass_field_is_required)
        elif email_field_is_required in page_source:
            assert email_field_is_required in page_source, "Надпись о незаполненном поле логина не появилась"
            logger.error("Авторизация не произошла. Появился текст с ошибкой: " + email_field_is_required)
        else:
            logger.info("Проверить, что выполнилась авторизация")
            ActionsOnElements.check_element_visibility(self.browser, selector=NavigationTabs.LOGOUT_BUTTON)

    def enter_login(self, username, url):
        """ Функция, вводящая логин """
        global users

        # Словарь, содержащий данные пользователей
        users_dict = {
            "url-1": {
                "user-1": {"login": ""},
                "user-2": {"login": ""},
                "user-3": {"login": ""},
            },
            "url-2": {
                "user-1": {"login": ""},
                "user-2": {"login": ""},
                "user-3": {"login": ""},
            },
            "url-3": {
                "user-1": {"login": ""},
                "user-2": {"login": ""},
                "user-3": {"login": ""},
            }
        }

        if url:
            current_url = url
        else:
            current_url = self.start_page

        if current_url in users_dict:
            users = users_dict[current_url]

        # Цикл, находящий данные указанного пользователя в словаре
        if username in users:
            login = users[username]["login"]
        else:
            print('Неизвестный пользователь')
            return False

        logger.info("Ввести email")
        element = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(AuthorizationPage.LOGIN_FIELD))
        element.send_keys(f'{login}')

        logger.info("Проверить, что поле Email заполнилось указанным логином")
        email = ActionsOnElements.get_element_text(self.browser, selector=AuthorizationPage.LOGIN_FIELD)
        assert email == f'{login}', 'В поле email было введено не то значение логина'

    def enter_password(self, username, url):
        """ Функция, вводящая пароль для Internal User """
        global users

        # Словарь, содержащий данные пользователей
        users_dict = {
            "URL-1": {
                "user-1": {"password": ""},
                "user-2": {"password": ""},
                "user-3": {"password": ""},
            },
            "URL-2": {
                "user-1": {"password": ""},
                "user-2": {"password": ""},
                "user-3": {"password": ""},
            },
            "URL-3": {
                "user-1": {"password": ""},
                "user-2": {"password": ""},
                "user-3": {"password": ""},
            }
        }

        if url:
            current_url = url
        else:
            current_url = self.start_page

        if current_url in users_dict:
            users = users_dict[current_url]

        # Цикл, находящий данные указанного пользователя в словаре
        if username in users:
            password = users[username]["password"]
        else:
            print('Неизвестный пользователь')
            return False

        logger.info("Ввести пароль")
        element = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(AuthorizationPage.PASSWORD_FIELD))
        print(f'Введен пароль: {password}')
        element.send_keys(f'{password}')

        logger.info("Проверить, что поле Password скрывает введённый пароль")
        password_field = self.browser.find_element(*AuthorizationPage.PASSWORD_FIELD)
        is_password_field = password_field.get_attribute('type') == 'password'
        assert is_password_field, "Поле ввода Password не скрывает пароль под звездочками"

    def check_authorization_block_visibility(self):
        """ Проверить видимость основных элементов на странице авторизации """
        logger.info("Проверить видимость поля Email")
        ActionsOnElements.check_element_visibility(self.browser, selector=AuthorizationPage.LOGIN_FIELD)
        ActionsOnElements.check_element_be_clickable(self.browser, selector=AuthorizationPage.LOGIN_FIELD)

        logger.info("Проверить видимость поля Password")
        ActionsOnElements.check_element_visibility(self.browser, selector=AuthorizationPage.PASSWORD_FIELD)
        ActionsOnElements.check_element_be_clickable(self.browser, selector=AuthorizationPage.PASSWORD_FIELD)

        logger.info("Проверить видимость чек-бокса Remember me")
        ActionsOnElements.check_element_visibility(self.browser, selector=AuthorizationPage.REMEMBER_ME_CHECKBOX)
        ActionsOnElements.check_element_be_clickable(self.browser, selector=AuthorizationPage.REMEMBER_ME_CHECKBOX)

        logger.info("Проверить видимость кнопки Submit")
        ActionsOnElements.check_element_visibility(self.browser, selector=AuthorizationPage.LOGIN_BUTTON)
        ActionsOnElements.check_element_be_clickable(self.browser, selector=AuthorizationPage.LOGIN_BUTTON)