from loguru import logger
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class ActionsOnElements:
    """ Класс, содержащий основные рабочие методы """

    @staticmethod
    def click_element(browser, selector):
        """ Функция, нажимающая один раз на выбранный элемент """
        logger.info(f'Нажать на указанный элемент {selector}')
        button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable(selector))
        button.click()

    @staticmethod
    def double_click_element(browser, selector):
        """ Функция, нажимающая дважды на выбранный элемент """
        element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(selector))
        actions = ActionChains(browser)
        actions.double_click(element).perform()

    @staticmethod
    def chose_value_in_dropdown(browser, desired_value, selector):
        """ Функция, нажимающая один раз на выбранный элемент """
        logger.info(f'Выбрать значение {desired_value} из выпадающего списка')
        dropdown = browser.find_element(*selector)
        dropdown_options = dropdown.find_elements(By.TAG_NAME, 'option')

        for option in dropdown_options:
            option_text = option.text
            if option_text == desired_value:
                option.click()
                break

    @staticmethod
    def check_element_visibility(browser, selector):
        """ Функция с помощью которой проверяем видимость элемента на странице """
        element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(selector)), \
                  f'Не обнаружен ожидаемый элемент: {selector}'

    @staticmethod
    def check_elements_visibility(browser, selector):
        """ Функция с помощью которой проверяем видимость элементов на странице """
        element = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(selector)), \
                  f'Не обнаружен ожидаемый элемент: {selector}'

    @staticmethod
    def check_element_contains_text(browser, selector, expected_text):
        """ Функция, проверяющая, что указанный элемент содержит указанный текст """
        element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(selector))

        actual_text = element.text.strip()
        assert actual_text == expected_text, f'Текст элемента {actual_text} не совпадает с ожидаемым {expected_text}'

    @staticmethod
    def check_element_be_clickable(browser, selector):
        """ Функция, проверяющая доступен ли элемент для нажатия """
        try:
            return WebDriverWait(browser, 10).until(EC.element_to_be_clickable(selector))
        except TimeoutException:
            raise Exception(f'Элемент {selector} недоступен для нажатий!')

    @staticmethod
    def check_element_invisibility(browser, selector):
        """ Функция, проверяющая, что указанный элемент отсутствует на странице """
        return WebDriverWait(browser, 20).until(EC.invisibility_of_element_located(selector))

    @staticmethod
    def clear_input_field(browser, selector):
        """ Функция, выполняющая очистку поля ввода """
        element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(selector))
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACKSPACE)

    @staticmethod
    def input_text(browser, selector, text):
        """ Функция, вводящая текст в указанный элемент на странице """
        element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable(selector))
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    @staticmethod
    def scroll_to_element_and_click_him(browser, element):
        actions = ActionChains(browser)
        actions.move_to_element(element)  # Прокручиваем страницу к элементу
        actions.click(element)  # Кликаем на элементе
        actions.perform()  # Выполняем действия

    @staticmethod
    def scroll_to_element(browser, element_locator, max_attempts=10):
        """Прокрутка до указанного веб-элемента"""
        attempts = 0
        while attempts < max_attempts:
            try:
                element = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located(element_locator)
                )

                if element.is_enabled():
                    return True  # Элемент кликабелен, успешно прокрутили до элемента

                browser.execute_script("arguments[0].scrollIntoView(true);", element)

            except Exception as e:
                attempts += 1
                print(f"Попытка {attempts} не удалась. Ошибка: {e}")

            # Прокручиваем вниз на весь экран
            browser.execute_script("window.scrollBy(0, window.innerHeight);")

        print(f"Не удалось прокрутить до кликабельного элемента {element_locator} за {max_attempts} попыток.")
        return False  # Не удалось прокрутить до элемента

    @staticmethod
    def get_element_text(browser, selector):
        """ Функция, получающая текст выбранного элемента """
        element = browser.find_element(*selector)
        return element.get_attribute('value')

    @staticmethod
    def wait_for_element_with_text(browser, selector, text):
        element = WebDriverWait(browser, 20).until(EC.visibility_of_element_located(selector))
        assert element.text == text, f'Текст веб-элемента {selector} не схож с требуемым {text}'

    @staticmethod
    def wait_for_element_clickable(browser, selector):
        return WebDriverWait(browser, 20).until(EC.element_to_be_clickable(selector))

    @staticmethod
    def radio_button_is_selected(browser, selector):
        radio_button = WebDriverWait(browser, 20).until(EC.visibility_of_element_located(selector))
        is_selected = radio_button.is_selected()

        if is_selected:
            return True
        else:
            print(f'Radio Button {selector} не была нажата')
            return False
