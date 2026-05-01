import pytest
from selenium import webdriver

@pytest.fixture

def setup():
    options_webdriver = webdriver.ChromeOptions()
    options_webdriver.add_argument("--guest")

    driver = webdriver.Chrome(options = options_webdriver)
    driver.maximize_window()

    yield driver
    driver.quit()


