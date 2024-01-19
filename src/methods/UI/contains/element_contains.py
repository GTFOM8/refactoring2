from selenium.webdriver.support.select import Select


class ElementContains:
    def __init__(self, browser):
        self.browser = browser

    values = None

    def check_element_contains_certain_number_of_values(self, selector, length):
        """ Функция, проверяющая, что элемент содержит определенное количество символов """
        element_length = self.browser.find_element(*selector)
        element_length = element_length.text.replace('...', '')
        print('Вот что: ', element_length)
        assert len(element_length) == int(length), f'Длина текста в {selector} не равна {length}'

    def get_dropdown_values(self, selector):
        """ Функция, получающая значения выпадающего списка """
        try:
            dropdown = Select(self.browser.find_element(*selector))

            # Получаем все значения выпадающего списка
            all_options = dropdown.options

            # Извлекаем текст каждого значения
            ElementContains.values = [option.text.lower() for option in all_options if option.text.lower() != 'select']

            if 'all' not in ElementContains.values and 'none' not in ElementContains.values:
                raise AssertionError(f'В выпадающем списке {selector} отсутствует значение "all"/"none"')

            return ElementContains.values
        except Exception as e:
            print(f'Произошла ошибка при получении значений из выпадающего списка: {e}')
            return []
