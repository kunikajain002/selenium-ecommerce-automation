from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def checkout(driver):
    wait = WebDriverWait(driver,10)
    # checkout
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()= 'Checkout']"))).click()

def checkout_info(driver):
    wait = WebDriverWait(driver, 10)
    # Checkout information
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id = 'first-name']"))).send_keys("Kunika")
    driver.find_element(By.XPATH, "//input[@id = 'last-name']").send_keys("Jain")
    driver.find_element(By.XPATH, "//input[@id = 'postal-code']").send_keys("122001")
    driver.find_element(By.XPATH, "//input[@id = 'continue']").click()

def checkout_overview(driver):
    wait = WebDriverWait(driver,10)
    # Checkout overview
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id = 'finish']"))).click()

def validation(driver):
    wait = WebDriverWait(driver, 10)
    # Validate order completion
    message_shown = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text() = 'Thank you for your order!']"))).text

    assert message_shown == "Thank you for your order!"
    print("Checkout successful")

    # Checkout complete
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Back Home']"))).click()

def logout(driver):
    wait = WebDriverWait(driver, 10)
    # logout
    driver.find_element(By.XPATH, "//button[text() = 'Open Menu']").click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text() = 'Logout']"))).click()
    print("Log Out Successful")