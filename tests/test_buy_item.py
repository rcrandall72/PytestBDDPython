from pytest_bdd import given, when, then, scenario
from common_strings import *
from pytest import mark


@scenario("../features/buy_item.feature", "Buy Item")
@mark.usefixtures("base_functions")
def test_buy_item(driver):
    pass


@given("the user is logged in")
def step_sign_in(base_functions):
    base_functions.sign_in(UserData.STANDARD_USER)


@when("the user adds an item to the cart")
def step_add_item_to_cart(base_functions):
    base_functions.press_button(InventoryPage.ADD_BACKPACK_TO_CART)


@then("the cart total should increase by 1")
def step_check_item_added_to_cart(base_functions):
    assert base_functions.assign_element(InventoryPage.SHOPPING_CART_CONTAINER).text == "1"


@when("the user opens the cart")
def step_open_cart(base_functions):
    base_functions.press_button(InventoryPage.SHOPPING_CART_CONTAINER)


@then("the item name added should appear")
def step_check_item_name_added_to_cart(base_functions):
    assert base_functions.assign_element(CartPage.INVENTORY_ITEM_NAME).text == InventoryPage.SAUCE_LABS_BACKPACK


@when("the user enters their information")
def step_enter_user_information(base_functions):
    base_functions.press_button(CartPage.CHECKOUT_BUTTON)
    base_functions.send_keys(CartPage.FIRST_NAME_FIELD, base_functions.get_random_string())
    base_functions.send_keys(CartPage.LAST_NAME_FIELD, base_functions.get_random_string())
    base_functions.send_keys(CartPage.ZIP_FIELD, base_functions.get_random_string())


@when("the user finalizes their order")
def step_finalize_order(base_functions):
    base_functions.press_button(CartPage.CONTINUE_BUTTON)
    base_functions.press_button(CartPage.FINISH_BUTTON)


@then("the confirmation prompt should appear")
def step_check_confirmation(base_functions):
    assert base_functions.check_for_element(CartPage.CONFIRMATION_CONTAINER)
