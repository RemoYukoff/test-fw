from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    title = (By.CSS_SELECTOR, "title")
    item = (By.CSS_SELECTOR, ".inventory_item")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def is_displayed(self) -> bool:
        self.driver.find_element(*self.title).is_displayed()
        return len(self.driver.find_elements(*self.item)) > 0
