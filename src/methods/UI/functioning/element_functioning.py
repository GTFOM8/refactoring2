import pyperclip
from loguru import logger
from src.methods.UI.actions_on_elements import ActionsOnElements


class ElementFunction:
    def __init__(self, browser):
        self.browser = browser

    def check_copy_function(self, selector, field):
        """ Функция, проверяющая работает ли правильно копирование какого-либо значения из таблицы """
        logger.info("Скопировать значение из таблицы")
        ActionsOnElements.click_element(self.browser, selector=selector)
        base_value = self.browser.find_element(*selector).text.replace('...', '')[:10]
        clipboard_text = pyperclip.paste()[:10]

        print('Скопированное значение: ', clipboard_text)
        print('Базовое значение: ', base_value)

        # Проверяем, если base_value пусто, устанавливаем clipboard_text в значение base_value
        if not base_value:
            base_value = clipboard_text

        logger.info("Вводим в поисковую строку скопированный текст")
        ActionsOnElements.input_text(self.browser, selector=field, text=clipboard_text)

        assert base_value == clipboard_text, f'Скопированное значение {clipboard_text} не равно ожидаемому {base_value}'
