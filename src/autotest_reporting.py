from TestRail.testrail import APIClient
from TestRail.TestRail_API import TestRailAPI
from utilities.ReadProperties import ReadConfig
from environment_and_test_run import EnvAndRun as ER


host = ReadConfig.get_testrail_host()
login = ReadConfig.get_testrail_login()
password = ReadConfig.get_testrail_pass()


class AutotestReports:
    def __init__(self, browser):
        self.browser = browser
        self.host = host
        self.login = login
        self.password = password
        self.api = APIClient(self.host)
        self.api.user = self.login
        self.api.password = self.password

    run_id = ER.Run

    @staticmethod
    def check_page_errors(driver):
        try:
            console_logs = driver.get_log("browser")
            network_entries = driver.execute_script("return window.performance.getEntries()")

            console_errors = []
            network_errors = []

            for log in console_logs:
                if log["level"] == "SEVERE":
                    console_errors.append(log["message"])

            for entry in network_entries:
                if entry["response"]["status"] >= 400:
                    network_errors.append(entry["name"])

            if console_errors or network_errors:
                return console_errors + network_errors
            else:
                return "OK"

        except Exception as e:
            # Handle any exceptions that may occur
            print(f"An error occurred: {str(e)}")

    def report_test_result(self, case_id, status_id=None, error_description="", test_steps=None):
        """ Эта функция отвечает за отправку отчёта с результатом прохождения авто-теста в TestRail

        :param case_id: ID тест-кейса в TestRail
        :param status_id: Статус авто-теста. Если '1' - авто-тест отработал успешно. '5' - неудачно
        :param error_description: Описание ошибки, если авто-тест упал
        :param test_steps: Список шагов, выполненных в ходе авто-теста.

        """
        test_report = "\n".join(test_steps)

        if status_id == 1:
            comment = f'Test Passed\n\nШаги теста:\n{test_report}'
            TestRailAPI.APItestrail_massage2(status_id=status_id, case_id=case_id, run_id=AutotestReports.run_id,
                                             comment=comment)
        else:
            status_id = 5
            comment = f'Test Failed\n\nШаги теста:\n{test_report}\n\nОшибка: {error_description}'
            TestRailAPI.APItestrail_massage3(status_id=5, case_id=case_id, run_id=AutotestReports.run_id,
                                             comment=comment)
