from pages.login_page import LoginPage
from pages.cart_page import AddProduct

def test_cart(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    print(driver.title)

    lp = LoginPage(driver)
    lp.login("standard_user", "secret_sauce")

    cp = AddProduct(driver)
    cp.add_product()

    assert cp.get_cart_count() == "2"