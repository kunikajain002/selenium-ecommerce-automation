from pages.login_page import LoginPage

def test_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    print(driver.title)

    lp = LoginPage(driver)
    lp.login("standard_user","secret_sauce")

    assert "inventory" in driver.current_url  # Validates the login success