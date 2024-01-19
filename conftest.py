import os
import pytest
from sys import platform
from selenium import webdriver
from src.application import Application
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def app(browser):
    return Application(browser)


@pytest.fixture
def browser(config_browser='chrome'):
    if platform == "linux" or platform == "linux2":
        # linux
        razd = '/'
    elif platform == "darwin":
        # OS X
        razd = '/'
    elif platform == "win32":
        # Windows...
        razd = "\\"
    print(platform)

    os_name = os.name
    this_folder = os.path.dirname(os.path.abspath(__file__))
    full_folder = this_folder + razd + "Drivers" + razd
    directory = os.path.abspath(os.curdir) + razd + 'download'

    # Initialize WebDriver

    """ 
    :param no-sandbox: Отключает песочницу в браузере. В общем, отвечает за безопасность: снижает риск подцепить вирусы
    :param headless: Запуск авто-тестов без графического отображения. Если закоммитить, то браузер будет отображаться
    :param disable-gpu: Работает в паре с headless. Решает проблемы, связанные с отрисовкой графики в Chrome
    :param ignore-certificate-errors: Указывает браузеру игнорировать SSL-сертификаты
    :param allow-insecure-localhost: Разрешает доступ к сайтам на локальном хосте
    :param window-size: Противоположность '--start-maximized'. Устанавливает указанный размер окна. Если включить
        отображение браузера при запуске авто-тестов, то нужно закоммитить '--window-size' и раскоммитить 
        '--start-maximized'. Если при запуске в --headless режиме оставить '--start-maximized', то АТ упадут
    :param '--start-maximized': Запускает браузер на максимальный размер окна
    :param driver: Скачивает webdriver-manager, позволяя запустить АТ на любой машине. Для работы необходимо установить
        webdriver-manager в разделе 'Settings -> Project -> Python Interpreter' 
    """

    if config_browser == 'chrome':
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": directory, }
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-insecure-localhost')
        options.add_argument('--window-size=1920,1080')
        # options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # options.add_argument('<указать_путь_до_файла_веб_драйвера>')
        # options.add_argument(this_folder)

        # driver = webdriver.Chrome(options=options)
        # Wait implicitly for elements to be ready before attempting interactions
        driver.implicitly_wait(20)
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()
