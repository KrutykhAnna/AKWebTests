import allure
import random
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    PHONE_FIELD = (By.XPATH, '//*[@name="phone"]')
    COUNTRY_FIELD = (By.XPATH, '//button[@aria-label="Страна или код"]')
    COUNTRY_ITEM = (By.CSS_SELECTOR, 'button[class*="phoneInput_numberIconInput"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@type="submit"]')

class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_elements(RegistrationPageLocators.PHONE_FIELD)
        self.find_elements(RegistrationPageLocators.COUNTRY_FIELD)
        self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        self.find_elements(RegistrationPageLocators.SUBMIT_BUTTON)

    def select_random_country(self):
        random_num = random.randint(0,212)
        self.find_element(RegistrationPageLocators.COUNTRY_FIELD).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
