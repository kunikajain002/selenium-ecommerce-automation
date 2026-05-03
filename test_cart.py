from login_page import login
from cart_page import *

def test_cart(setup):
    driver = setup

    login(driver)

    add_product(driver)

    assert get_cart_count(driver) == "2"