import allure
from faker import Faker

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper

BASE_URL = 'https://ok.ru/'

@allure.suite("Проверка востановления пользователя")
@allure.title("Проверка перехода к востановлению после нескольких неудачных попыток авторизации")
def test_go_to_recovery_after_many_fails(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.send_login(Faker().email())
    for i in range(3):
        LoginPage.send_password(Faker().password())
        LoginPage.click_login()
        if i<2:
            LoginPage.get_error_login_or_password()

    LoginPage.click_recovery()
    RecoveryPageHelper(browser)