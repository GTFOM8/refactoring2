from src.methods.UI.filtering.filtering_table import Filtering
from src.methods.SQL.sql_methods import SqlMethods
from src.pages.Deposits.Deposits import Deposits
from src.authorization_page import AuthPage


class Application:

    """ Application(app) предоставляет доступ ко всем страницам и их функционалу. Также позволяет инкапсулировать
    общие методы и свойства, используемые в авто-тестах, для последующего быстрого вызова в любом участке кода """

    def __init__(self, browser):
        self.browser = browser

        self.sql = SqlMethods(self.browser)
        self.deposits = Deposits(self.browser)
        self.auth_page = AuthPage(self.browser)
        self.filtering = Filtering(self.browser)
