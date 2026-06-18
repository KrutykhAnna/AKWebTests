import allure
from faker import Faker

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationPageHelper

BASE_URL = 'https://ok.ru/'

def test_reqistration_random_contry(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelper(browser)
    RegistrationPage.select_random_country()