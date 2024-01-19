from loguru import logger
from datetime import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.methods.UI.actions_on_elements import ActionsOnElements


class SortedMethods:
    """ В файле хранятся функции сортировки """

    def __init__(self, browser):
        self.browser = browser

    def sort_column_by_ascending(self, column_locator):
        """ Функция, выполняющая сортировку колонки по возрастанию """
        logger.info('Находим колонку')
        column = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(column_locator))

        logger.info('Проверяем, что колонка не была нажата, с помощью проверки её атрибута "Class".')
        WebDriverWait(self.browser, 20).until(
            EC.text_to_be_present_in_element_attribute(column_locator, 'class', 'small sorting'),
            f'Колонка {column_locator} - ошибка с атрибутом Class')

        logger.info('Кликаем по колонке для сортировки')
        column.click()

        logger.info('Проверяем, что колонка перешла в режим сортировки через изменившийся атрибут "Class".')
        # Он должен содержать "asc"(по возрастанию) или "desc"(по убыванию)
        WebDriverWait(self.browser, 20).until(
            EC.text_to_be_present_in_element_attribute(column_locator, 'class', 'small sorting sorting_asc'),
            f'Колонка {column_locator} - атрибут Class не содержит указатель "asc"')

    def sort_column_by_descending(self, column_locator, base_check):
        """ Функция, выполняющая сортировку колонки по убыванию """
        logger.info('Находим колонку')
        column = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(column_locator))

        if base_check == 'yes':
            logger.info('Проверяем, что колонка не была нажата, с помощью проверки её атрибута "Class".')
            WebDriverWait(self.browser, 20).until(
                EC.text_to_be_present_in_element_attribute(column_locator, 'class', 'small sorting'),
                f'Колонка {column_locator} - ошибка с атрибутом Class')

        # logger.info('Кликаем по колонке для сортировки по убыванию')
        # ActionsOnElements.click_element(self.browser, selector=column)

        logger.info('Проверяем, что колонка перешла в режим сортировки через изменившийся атрибут "Class".')
        # Он должен содержать "asc"(по возрастанию) или "desc"(по убыванию)
        sorting_class = 'small sorting sorting_desc'
        WebDriverWait(self.browser, 20).until(
            EC.text_to_be_present_in_element_attribute(column_locator, 'class', 'small sorting sorting_desc'),
            f'Колонка {column_locator} - атрибут Class не содержит указатель "desc"')

        if sorting_class in column.get_attribute('class'):
            return

        logger.info('Кликаем по колонке для сортировки по убыванию')
        ActionsOnElements.click_element(self.browser, selector=column)

        WebDriverWait(self.browser, 20).until(
            EC.text_to_be_present_in_element_attribute(column_locator, 'class', 'small sorting sorting_desc'),
            f'Колонка {column_locator} - атрибут Class не содержит указатель "desc"')

    def check_date_column_is_sorted_by_ascending(self, line_locator):
        """ Функция, проверяющая, что колонка, связанная с датой, отсортирована по возрастанию """
        logger.info('Извлекаем текстовые значения из строк')
        text_elements = []
        i = 0

        while True:
            locator = (By.XPATH, f'//td[@data-pytest="{line_locator}{i}"]')

            try:
                element = self.browser.find_element(*locator)
                date_str = element.text
                date_obj = datetime.strptime(date_str, "%d.%m.%Y")
                text_elements.append(date_obj)
                i += 1
            except NoSuchElementException:
                break

        print('Неотсортированный текст: ', text_elements)
        print('Отсортированный текст: ', sorted(text_elements))

        logger.info('Проверяем сортировку по возрастанию')
        assert text_elements == sorted(text_elements), f'Колонка {line_locator} не отсортирована по возрастанию'

    def check_date_column_is_sorted_by_descending(self, line_locator):
        """ Функция, проверяющая, что колонка, связанная с датой, отсортирована по убыванию """
        logger.info('Извлекаем текстовые значения из строк')
        text_elements = []
        i = 0

        while True:
            locator = (By.XPATH, f'//td[@data-pytest="{line_locator}{i}"]')

            try:
                element = self.browser.find_element(*locator)
                date_str = element.text
                date_obj = datetime.strptime(date_str, "%d.%m.%Y")
                text_elements.append(date_obj)
                i += 1
            except NoSuchElementException:
                break

        print('Неотсортированный текст: ', text_elements)
        print('Отсортированный текст: ', sorted(text_elements, reverse=True))

        logger.info('Проверяем сортировку по убыванию')
        assert text_elements == sorted(text_elements, reverse=True), \
            f'Колонка {line_locator} не отсортирована по убыванию'
