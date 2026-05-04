from selenium.webdriver.common.by import By

class AddProduct:
    def __init__(self, driver):
        self.driver = driver

    product_name1 = (By.XPATH, "//div[text() = 'Sauce Labs Backpack']")
    add_to_cart1 = (By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-backpack']")
    product_name2 = (By.XPATH, "//div[text() = 'Sauce Labs Fleece Jacket']")
    add_to_cart2 = (By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-fleece-jacket']")
    cart = (By.XPATH, "//a[@class = 'shopping_cart_link']")
    cart_count = (By.XPATH, "//span[@class = 'shopping_cart_badge']")

    def add_product(self):
        # Add product by searching the product name
        product_name = self.driver.find_element(*self.product_name1)
        print("Product Name 1st: ", product_name.text)
        self.driver.find_element(*self.add_to_cart1).click()

        # another product by searching the product name
        product_name_2 = self.driver.find_element(*self.product_name2)
        print("Product Name 2nd: ", product_name_2.text)
        self.driver.find_element(*self.add_to_cart2).click()

    def get_cart(self):
        self.driver.find_element(*self.cart).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_count).text