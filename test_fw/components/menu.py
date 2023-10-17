from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Menu:
    menu_btn = (By.ID, "react-burger-menu-btn")
    logout_btn = (By.ID, "logout_sidebar_link")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def logout(self) -> bool:
        self.driver.find_element(*self.menu_btn).click()
        self.driver.find_element(*self.logout_btn).click()
