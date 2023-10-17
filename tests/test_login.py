from pytest_bdd import scenarios, when, then, parsers
from test_fw.pages.inventory import InventoryPage
from test_fw.pages.login import LoginPage
from test_fw.components.menu import Menu


scenarios("features/login.feature")


@when(parsers.re(r'I login with "(?P<user>\w*)" and "(?P<password>\w*)"'))
def login(driver, user: str, password: str):
    LoginPage(driver).login(user, password)


@when("I logout")
def logout(driver):
    Menu(driver).logout()


@when("I go to the Inventory page")
def open_inventory(driver):
    InventoryPage(driver).open()


@then(parsers.parse('I should see the error "{error}"'))
def login_error_is_displayed(driver, error: str):
    assert error == LoginPage(driver).get_error_message()


@then("I should see the inventory page")
def inventory_is_displayed(driver):
    assert InventoryPage(driver).is_displayed()


@then("I should see the login page")
def login_is_displayed(driver):
    assert LoginPage(driver).is_displayed()
