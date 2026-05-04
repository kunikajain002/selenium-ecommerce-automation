from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    login_btn = (By.XPATH, "//input[@id='login-button']")

    def enter_username(self, user):
        self.driver.find_element(*self.username).send_keys(user)

    def enter_password(self, pw):
        self.driver.find_element(*self.password).send_keys(pw)

    def click_submit(self):
        self.driver.find_element(*self.login_btn).click()

    def login(self, user, pw):
        self.enter_username(user)
        self.enter_password(pw)
        self.click_submit()