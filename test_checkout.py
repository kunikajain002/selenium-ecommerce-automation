from login_page import login
from cart_page import *
from checkout_page import *

def test_checkout(setup):
    driver = setup

    login(driver)

    add_product(driver)

    get_cart(driver)

    checkout(driver)

    checkout_info(driver)

    checkout_overview(driver)

    validation(driver)

    logout(driver)