import time
import random
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select
from src.methods.UI.actions_on_elements import ActionsOnElements


class Filtering:
    """ Функции, используемые для тестирования фильтрации списков/таблиц """
    def __init__(self, browser):
        self.browser = browser

    def cleat_field(self, field_name):
        ActionsOnElements.clear_input_field(self.browser, selector=field_name)

    def filtering_random_value(self, line, search_field, column):
        """ Функция, выполняющая ввод случайных значений в поле 'Search' """
        logger.info('Собираем значения из колонки')
        lines_value = []
        for i in range(35):
            locator = (By.XPATH, f'{line}'.replace('0', f'{i}'))
            try:
                element = self.browser.find_element(*locator)
                lines_value.append(element.text)
            except NoSuchElementException:
                break

        logger.info('Выбираем два случайных значения')
        random_value = random.sample(lines_value, 2)

        logger.info('Осуществляем поиск значений в колонке')
        for value in random_value:
            ActionsOnElements.clear_input_field(self.browser, selector=search_field)
            time.sleep(1)
            ActionsOnElements.input_text(self.browser, selector=search_field, text=value)
            time.sleep(1)

            line_value = self.browser.find_element(By.XPATH, f'{line}')

            assert value in line_value.text, f'Значение {value} не обнаружено в колонке {column}'

    def filtering_truncated_random_value(self, line, search_field, column):
        """ Функция, выполняющая ввод половину(первые пять символов) случайных значений в поле 'Search' """
        logger.info('Собираем значения из колонки')
        lines_value = []
        for i in range(35):
            locator = (By.XPATH, f'{line}'.replace('0', f'{i}'))
            try:
                element = self.browser.find_element(*locator)
                lines_value.append(element.text)
            except NoSuchElementException:
                break

        logger.info('Выбираем два случайных значения')
        random_value = random.sample(lines_value, 2)

        logger.info('Осуществляем поиск значений в колонке')
        for value in random_value:
            truncated_value = value[:5]
            ActionsOnElements.clear_input_field(self.browser, selector=search_field)
            time.sleep(1)
            ActionsOnElements.input_text(self.browser, selector=search_field, text=truncated_value)
            time.sleep(1)

            line_value = self.browser.find_element(By.XPATH, f'{line}')

            assert value in line_value.text, f'Значение {value} не обнаружено в колонке {column}'

    def filtering_invalid_value(self, line, search_field):
        """ Функция, выполняющая ввод несуществующего значения в поле 'Search' """
        logger.info('Вводим в поле "Search" несуществующее значение колонки "Internal ID"')
        invalid_values = ['3830701', '6699123']

        for value in invalid_values:
            ActionsOnElements.clear_input_field(self.browser, selector=search_field)
            time.sleep(1)
            ActionsOnElements.input_text(self.browser, selector=search_field, text=value)
            time.sleep(1)

            no_data_in_table = self.browser.find_element(By.XPATH, f'{line}')

            assert no_data_in_table.text == "No data available in table", \
                f'Не отобразилась надпись "No data available in table"; Найдено несуществующее значение {value}'

    def filtering_iterable_value(self, dropdown_name, line):
        dropdown_values = []
        dropdown_text_values = []
        dropdown_element = self.browser.find_element(*dropdown_name)
        dropdown_options = dropdown_element.find_elements(By.TAG_NAME, 'option')
        for option in dropdown_options:
            value = option.get_attribute('value')
            if value.strip() != 'All' and value.strip() != '':
                text_value = option.text.strip()
                dropdown_text_values.append(text_value)
                dropdown_values.append(value)
                option.click()
                time.sleep(1)

        selected_column = dropdown_name
        is_column_selected = False

        for value in dropdown_values:
            option_line = dropdown_element.find_element(By.XPATH, f'//option[@value="{value}"]')
            option_line.click()
            time.sleep(1)

            if selected_column == dropdown_name:
                line_value = []
                for i in range(35):
                    locator = (By.XPATH, f'{line}'.replace('0', f'{i}'))
                    try:
                        element = self.browser.find_element(*locator)
                        line_value.append(element.text)
                    except NoSuchElementException:
                        break

                current_value = dropdown_text_values[dropdown_values.index(value)]
                assert all(item == current_value for item in line_value), \
                    f'Колонка {current_value} не отфильтрована. В таблице значения {dropdown_text_values}'
                is_column_selected = True

            if is_column_selected:
                break

    def check_dropdown_include_expected_values(self, dropdown_name, expected_values):
        """ Функция, проверяющая, что выпадающий список содержит ожидаемые значения """
        dropdown = Select(self.browser.find_element(*dropdown_name))

        actual_values = [option.text for option in dropdown.options]

        logger.info('Проверить, что выпадающий список содержит указанные пользователем значения')
        for value in expected_values:
            assert value in actual_values, f"Значение {value} отсутствует в выпадающем списке"

    def select_dropdown_value(self, dropdown_name, value_to_select):
        """ Функция, выбирающее указанное значение из выпадающего списка """
        logger.info('Выбрать указанное значение из выпадающего списка')
        dropdown = Select(self.browser.find_element(*dropdown_name))
        dropdown.select_by_visible_text(value_to_select)
