import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-test-id="enter-action"]')
    LOGIN_BY_QR_BUTTON = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    FORGOT_LOGIN_BUTTON = (By.XPATH, '//*[@aria-label="Не получается войти?"]')
    REGISTER_BUTTON = (By.XPATH, '//button[.//span[text()="Зарегистрироваться"]]')
    VK_LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAIL_LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')

    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')

    ERROR_LOGIN_TEXT = (By.XPATH, '//span[text()="Введите логин"]')
    ERROR_PASSWORD_TEXT = (By.XPATH, '//span[text()="Введите пароль"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BY_QR_BUTTON)
        self.find_element(LoginPageLocators.FORGOT_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.VK_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.MAIL_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_LOGIN_BUTTON)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_login_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_LOGIN_TEXT).text

    @allure.step('Получаем текст ошибки')
    def get_error_password_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_PASSWORD_TEXT).text

    @allure.step('Заполняем логин')
    def send_login(self, login: str):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)

