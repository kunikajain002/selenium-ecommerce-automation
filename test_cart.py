from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cart(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")
    print(driver.title)

    # Login
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))).send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    assert "inventory" in driver.current_url  # Validates the login success

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