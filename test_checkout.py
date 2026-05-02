from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import login

def test_checkout(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    login(driver)

    # Add product by searching the product name
    product_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text() = 'Sauce Labs Backpack']")))
    print("Product Name 1st: ", product_name.text)
    driver.find_element(By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-backpack']").click()

    # another product by searching the product name
    product_name_2 = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[text() = 'Sauce Labs Fleece Jacket']")))
    print("Product Name 2nd: ", product_name_2.text)
    driver.find_element(By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-fleece-jacket']").click()

    # Click on Cart
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class = 'shopping_cart_link']"))).click()

    # checkout
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()= 'Checkout']"))).click()

    # Checkout information
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id = 'first-name']"))).send_keys("Kunika")
    driver.find_element(By.XPATH, "//input[@id = 'last-name']").send_keys("Jain")
    driver.find_element(By.XPATH, "//input[@id = 'postal-code']").send_keys("122001")
    driver.find_element(By.XPATH, "//input[@id = 'continue']").click()

    # Checkout overview
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id = 'finish']"))).click()

    # Validate order completion
    message_shown = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text() = 'Thank you for your order!']"))).text

    assert message_shown == "Thank you for your order!"
    print("Checkout successful")

    # Checkout complete
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Back Home']"))).click()

    # logout
    driver.find_element(By.XPATH, "//button[text() = 'Open Menu']").click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text() = 'Logout']"))).click()
    print("Log Out Successful")