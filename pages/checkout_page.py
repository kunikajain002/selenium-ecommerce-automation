import time
from selenium.webdriver.common.by import By

class CheckOut:
    def __init__(self, driver):
        self.driver = driver

    checkout = (By.XPATH, "//button[text()= 'Checkout']")
    first_name = (By.XPATH, "//input[@id = 'first-name']")
    last_name = (By.XPATH, "//input[@id = 'last-name']")
    postal_code = (By.XPATH, "//input[@id = 'postal-code']")
    continue_btn = (By.XPATH, "//input[@id = 'continue']")
    finish_btn = (By.XPATH, "//button[@id = 'finish']")
    thankyou = (By.XPATH, "//h2[text() = 'Thank you for your order!']")
    back_home = (By.XPATH, "//button[text() = 'Back Home']")
    menu = (By.XPATH, "//button[text() = 'Open Menu']")
    logout = (By.XPATH, "//a[text() = 'Logout']")

    def checkout_cart(self):
        self.driver.find_element(*self.checkout).click()

    def checkout_info(self, first, last, zip):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(zip)

    def checkout_continue(self):
        self.driver.find_element(*self.continue_btn).click()

    def checkout_overview(self):
        self.driver.find_element(*self.finish_btn).click()

    def validation(self):
        # Validate order completion
        return self.driver.find_element(*self.thankyou).text

    def back_and_logout(self):
        # Checkout complete
        self.driver.find_element(*self.back_home).click()
        # logout
        self.driver.find_element(*self.menu).click()
        time.sleep(2)
        self.driver.find_element(*self.logout).click()
