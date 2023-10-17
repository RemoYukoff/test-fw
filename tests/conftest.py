import pytest
from selenium import webdriver


@pytest.fixture
def driver() -> webdriver.Remote:
    # Selenium 4 allows us to not having to download the drivers
    # https://www.selenium.dev/blog/2022/introducing-selenium-manager/
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
