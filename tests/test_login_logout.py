from pytest_bdd import given, when, then, scenario
from common_strings import *
from pytest import mark
from log_functions import log_test, log_step


@scenario("../features/login_logout.feature", "Login and Logout")
@mark.usefixtures("base_functions")
def test_login_logout(driver):
    pass


@scenario("../features/login_logout.feature", "User cannot login with a locked account")
@mark.usefixtures("base_functions")
def test_cannot_login_with_locked_user(driver):
    pass


@scenario("../features/login_logout.feature", "User cannot login with invalid credentials")
@mark.usefixtures("base_functions")
def test_user_signing_credential_errors(driver):
    pass


@given("the user is on the login page")
def step_start_on_login_page():
    pass


@when("the user enters valid credentials and clicks the login button")
def step_valid_login(base_functions):
    base_functions.sign_in(UserData.STANDARD_USER)


@then("the user should be on the main homepage")
def step_check_logged_in(base_functions):
    assert base_functions.driver.current_url == URLs.SAUCE_DEMO_INVENTORY


@when("the user logs out")
def step_logout(base_functions):
    base_functions.press_button(InventoryPage.MENU_BUTTON, wait=True)
    base_functions.press_button(InventoryPage.LOGOUT_BUTTON)


@then("the user should be on the login page")
def step_check_logged_out(base_functions):
    assert base_functions.check_for_element(LoginPage.LOGIN_BUTTON)
    assert base_functions.driver.current_url == URLs.SAUCE_DEMO


@when("the user enters valid credentials for a locked account and clicks the login button")
def step_enter_locked_credentials(base_functions):
    base_functions.sign_in(UserData.LOCKED_OUT_USER)


@then("the user should see an error message indicating the account is locked")
def step_check_locked_out_message_appears(base_functions):
    assert base_functions.check_for_element(LoginPage.ERROR_MESSAGE)
    assert base_functions.assign_element(LoginPage.ERROR_MESSAGE).text == LoginPage.LOCKED_OUT_ERROR_MESSAGE


@when("the user leaves both username and password fields empty and clicks the login button")
def step_login_without_credentials(base_functions):
    base_functions.press_button(LoginPage.LOGIN_BUTTON)


@then("the user should see an error message indicating the username is required")
def step_check_username_required_appears(base_functions):
    assert base_functions.check_for_element(LoginPage.ERROR_MESSAGE)
    assert base_functions.assign_element(LoginPage.ERROR_MESSAGE).text == LoginPage.USERNAME_REQUIRED_MESSAGE


@when("the user enters only a username, and clicks the login button")
def step_login_enter_only_username(base_functions):
    base_functions.send_keys(LoginPage.USERNAME_FIELD, base_functions.get_random_string())
    base_functions.press_button(LoginPage.LOGIN_BUTTON)


@then("the user should see an error message indicating the password is required")
def step_check_password_required_appears(base_functions):
    assert base_functions.check_for_element(LoginPage.ERROR_MESSAGE)
    assert base_functions.assign_element(LoginPage.ERROR_MESSAGE).text == LoginPage.PASSWORD_REQUIRED_MESSAGE


@when("the user enters an invalid username and an incorrect password, and clicks the login button")
def step_login_with_invalid_credentials(base_functions):
    base_functions.send_keys(LoginPage.PASSWORD_FIELD, base_functions.get_random_string())
    base_functions.press_button(LoginPage.LOGIN_BUTTON)


@then("the user should see an error message indicating the password is incorrect")
def step_check_password_mismatch_appears(base_functions):
    assert base_functions.check_for_element(LoginPage.ERROR_MESSAGE)
    assert base_functions.assign_element(LoginPage.ERROR_MESSAGE).text == LoginPage.USERNAME_PASSWORD_MISMATCH_MESSAGE


#

#
#     @log_test
#     def test_sort_products(self):
#         """
#         Verifies products can be sorted in a certain order
#         """
#         # Login as user
#         self.sign_in(UserData.STANDARD_USER)
#
#         # Sort products by A to Z
#         self.press_button(InventoryPage.SORT_CONTAINER)
#         self.press_button(InventoryPage.A_TO_Z_OPTION)
#         item_names = self.assign_elements(InventoryPage.INVENTORY_ITEM_NAME)
#         for i in range(0, len(item_names)-1):
#             assert item_names[i].text < item_names[i+1].text
#
#         # Sort products by A to Z
#         self.press_button(InventoryPage.SORT_CONTAINER)
#         self.press_button(InventoryPage.Z_TO_A_OPTION)
#         item_names = self.assign_elements(InventoryPage.INVENTORY_ITEM_NAME)
#         for i in range(0, len(item_names)-1):
#             assert item_names[i].text > item_names[i+1].text
#
#         # Sort products by low to high
#         self.press_button(InventoryPage.SORT_CONTAINER)
#         self.press_button(InventoryPage.LOW_TO_HIGH_PRICE_OPTION)
#         item_prices = self.assign_elements(InventoryPage.INVENTORY_ITEM_PRICE)
#         for i in range(0, len(item_prices)-1):
#             assert float(item_prices[i].text[1:]) <= float(item_prices[i+1].text[1:])
#
#         # Sort products by high to low
#         self.press_button(InventoryPage.SORT_CONTAINER)
#         self.press_button(InventoryPage.HIGH_TO_LOW_PRICE_OPTION)
#         item_prices = self.assign_elements(InventoryPage.INVENTORY_ITEM_PRICE)
#         for i in range(0, len(item_prices)-1):
#             assert float(item_prices[i].text[1:]) >= float(item_prices[i+1].text[1:])
