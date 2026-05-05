import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckOut:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

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
        self.wait.until(EC.element_to_be_clickable(self.checkout)).click()

    def checkout_info(self, first, last, zip):
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(zip)

    def checkout_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_btn)).click()

    def checkout_overview(self):
        self.wait.until(EC.element_to_be_clickable(self.finish_btn)).click()

    def validation(self):
        # Validate order completion
        return self.driver.find_element(*self.thankyou).text

    def back_and_logout(self):
        # Checkout complete
        self.driver.find_element(*self.back_home).click()
        # logout
        self.driver.find_element(*self.menu).click()
        self.wait.until(EC.element_to_be_clickable(self.logout)).click()
