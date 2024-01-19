import pytest
from loguru import logger
from autotests.src.application import Application


@pytest.mark.smoke_test
def test_authorization_with_incorrect_email_correct_password(app: Application, browser):
    """ Smoke авто-тест для страницы авторизации пользователя 'User' """
    """" Ссылка на тест-кейс: <URL-адрес> """

    global error_description
    case_id = '34021'

    # Флаг. Используется в случае падения теста
    error_occurred = False
    # Список, который сохраняет шаги теста. В случае ошибки, отправляется в TestRail, как отчёт
    test_steps = []

    try:
        test_steps.append("Шаг 1: Перейти на тестовую площадку")
        browser.get(app.auth_page.start_page)

        test_steps.append("Шаг 2: Проверить отображение блока авторизации")
        app.auth_page.check_authorization_block_visibility()

        test_steps.append("Шаг 3: Заполнить поле Email")
        app.auth_page.enter_login(username='incorrect', url=None)

        test_steps.append("Шаг 4: Заполнить поле Password")
        app.auth_page.enter_password(username='admin', url=None)

        test_steps.append("Шаг 5: Авторизоваться")
        app.auth_page.perform_authorization()

    except Exception as e:
        logger.error("Тест упал!")
        error_description = str(e)
        error_occurred = True

    finally:
        if error_occurred:
            steps_description = "\n".join(test_steps)
            error_message = f"Тест упал на шаге:\n\n{steps_description}\n\nОшибка: {error_description}"
            app.report.report_test_result(case_id=case_id, status_id=5, test_steps=test_steps,
                                          error_occurred=error_occurred, error_description=error_description)
            pytest.fail(error_message)
        else:
            app.report.report_test_result(case_id=case_id, status_id=1, test_steps=test_steps,
                                          error_occurred=error_occurred, error_description="")
