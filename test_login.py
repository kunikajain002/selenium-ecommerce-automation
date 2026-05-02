from login_page import login

def test_login(setup):
    driver = setup

    login(driver)

    assert "inventory" in driver.current_url  # Validates the login success