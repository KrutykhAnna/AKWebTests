import allure
from faker import Faker

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Введите логин'
EMPTY_PASSWORD_ERROR = 'Введите пароль'
@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки при пустой форме авторизации")
def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_login_text() == EMPTY_LOGIN_ERROR, (f"Ожидаемый результат: error_message == {EMPTY_LOGIN_ERROR}, "
                                                                   f"Фактический результат: error_message == {LoginPage.get_error_login_text()} ")

@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки при передачи незаполненного поля пароль")
def test_without_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.send_login(Faker().email())
    LoginPage.click_login()
    assert LoginPage.get_error_password_text() == EMPTY_PASSWORD_ERROR,  (f"Ожидаемый результат: error_message == {EMPTY_PASSWORD_ERROR}, "
                                                                   f"Фактический результат: error_message == {LoginPage.get_error_password_text()} ")
