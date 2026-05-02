from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import login

def test_cart(setup):
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

    badge = driver.find_element(By.XPATH, "//span[@class = 'shopping_cart_badge']").text

    assert badge == "2"