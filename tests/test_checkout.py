from pages.login_page import LoginPage
from pages.cart_page import AddProduct
from pages.checkout_page import CheckOut

def test_checkout(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    print(driver.title)

    lp = LoginPage(driver)
    lp.login("standard_user", "secret_sauce")

    cp = AddProduct(driver)
    cp.add_product()
    cp.get_cart()

    co = CheckOut(driver)
    co.checkout_cart()
    co.checkout_info("Kunika", "Jain", "122003")
    co.checkout_continue()
    co.checkout_overview()
    assert co.validation() == "Thank you for your order!"
    print("Checkout successful")
    co.back_and_logout()
    print("Log Out Successful")