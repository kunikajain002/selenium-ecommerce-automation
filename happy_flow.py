from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Options_webdriver = webdriver.ChromeOptions()

# prefs = {
#     "credentials_enable_service": False,
#     "profile.password_manager_enabled": False
# }
#
# Options_webdriver.add_experimental_options("prefs", prefs)
# Options_webdriver.add_argument("--disable-save-password-bubble")
# Options_webdriver.add_argument("--disable-notifications")
# Options_webdriver.add_argument("--diable-popup-blocking")
Options_webdriver.add_argument("--guest")

driver = webdriver.Chrome(options = Options_webdriver)

driver.maximize_window()
driver.get("https://www.saucedemo.com/")
print(driver.title)

# Login
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@id='login-button']").click()

time.sleep(5)

# Add product by searching the product name
product_name = driver.find_element(By.XPATH, "//div[text() = 'Sauce Labs Backpack']")
print("Product Name 1st: ", product_name.text)
driver.find_element(By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-backpack']").click()
time.sleep(5)

# another product by searching the product name
product_name_2 = driver.find_element(By.XPATH, "//div[text() = 'Sauce Labs Fleece Jacket']")
print("Product Name 2nd: ", product_name_2.text)
driver.find_element(By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-fleece-jacket']").click()

# Click on Cart
driver.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']").click()

time.sleep(1)

# checkout
driver.find_element(By.XPATH, "//button[text()= 'Checkout']").click()

time.sleep(1)

# Checkout information
driver.find_element(By.XPATH, "//input[@id = 'first-name']").send_keys("Kunika")
driver.find_element(By.XPATH, "//input[@id = 'last-name']").send_keys("Jain")
driver.find_element(By.XPATH, "//input[@id = 'postal-code']").send_keys("122001")
driver.find_element(By.XPATH, "//input[@id = 'continue']").click()

time.sleep(1)

# Checkout overview
driver.find_element(By.XPATH, "//button[@id = 'finish']").click()

time.sleep(1)

# Checkout complete
driver.find_element(By.XPATH, "//button[text() = 'Back Home']").click()
