from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_btn = (By.CLASS_NAME, "btn_action")
    error_message = (
        By.XPATH,
        '//*[@id="login_button_container"]/div/form',
    )

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def set_password(self, password: str):
        self.driver.find_element(*self.password_input).send_keys(password)

    def set_username(self, username: str):
        self.driver.find_element(*self.username_input).send_keys(username)

    def get_error_message(self) -> str:
        if errors := self.driver.find_elements(*self.error_message):
            return errors[0].text
        return None

    def login(self, username: str, password: str):
        self.set_username(username)
        self.set_password(password)
        self.click_login()

    def is_displayed(self) -> bool:
        return (
            self.driver.find_element(*self.username_input).is_displayed()
            and self.driver.find_element(*self.password_input).is_displayed()
            and self.driver.find_element(*self.login_btn).is_displayed()
        )
