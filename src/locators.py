from selenium.webdriver.common.by import By


class NavigationTabs:
    """  Локаторы навигационных вкладок (Operations Log, Export/Import, Finance, etc)"""
    # Локаторы для вкладки 'TAB-1'
    ELEMENT_ONE = (By.XPATH, '//a[@data-pytest=""]')
    ELEMENT_TWO = (By.XPATH, '//a[@data-pytest=""]')
    ELEMENT_THREE = (By.XPATH, '//a[@data-pytest=""]')
    ELEMENT_FOUR = (By.XPATH, '//a[@data-pytest=""]')

    # Локатор вкладки 'TAB-2'
    BUTTON_ONE = (By.XPATH, '//a[@data-pytest=""]')

    # Локаторы для вкладки 'TAB-3'
    DROPDOWN_ONE = (By.XPATH, '//a[@data-pytest=""]')
    DROPDOWN_TWO = (By.XPATH, '//a[@data-pytest=""]')
    DROPDOWN_THREE = (By.XPATH, '(//a[@class="")])[1]')
    DROPDOWN_FOUR = (By.XPATH, '(//a[@class="")])[1]')
    DROPDOWN_FIVE = (By.XPATH, '(//a[@class="")])[1]')

    # Локаторы для вкладки 'TAB-4'
    CHECKBOX_ONE = (By.XPATH, '//a[@data-pytest=""]')
    CHECKBOX_TWO = (By.XPATH, '(//a[@class="")])[2]')
    CHECKBOX_THREE = (By.XPATH, '(//a[@class="")])[2]')
    CHECKBOX_FOUR = (By.XPATH, '(//a[@class="")])[2]')
