from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def add_product(driver):
    wait = WebDriverWait(driver, 10)
    # Add product by searching the product name
    product_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text() = 'Sauce Labs Backpack']")))
    print("Product Name 1st: ", product_name.text)
    driver.find_element(By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-backpack']").click()

    # another product by searching the product name
    product_name_2 = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[text() = 'Sauce Labs Fleece Jacket']")))
    print("Product Name 2nd: ", product_name_2.text)
    driver.find_element(By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-fleece-jacket']").click()

def get_cart(driver):
    wait = WebDriverWait(driver, 10)
    # Click on Cart
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class = 'shopping_cart_link']"))).click()

def get_cart_count(driver):
    return driver.find_element(By.XPATH, "//span[@class = 'shopping_cart_badge']").text