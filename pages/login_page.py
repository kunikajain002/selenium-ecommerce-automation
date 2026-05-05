from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    username = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    login_btn = (By.XPATH, "//input[@id='login-button']")

    def enter_username(self, user):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)

    def enter_password(self, pw):
        self.driver.find_element(*self.password).send_keys(pw)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()

    def login(self, user, pw):
        self.enter_username(user)
        self.enter_password(pw)
        self.click_submit()