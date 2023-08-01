from pytest_bdd import given, when, then, scenario
from common_strings import *
from pytest import mark


@scenario("../features/sort_products.feature", "Sort Products A to Z")
@mark.usefixtures("base_functions")
def test_sort_products_a_to_z(driver):
    pass


@scenario("../features/sort_products.feature", "Sort Products Z to A")
@mark.usefixtures("base_functions")
def test_sort_products_z_to_a(driver):
    pass


@scenario("../features/sort_products.feature", "Sort Products Low to High")
@mark.usefixtures("base_functions")
def test_sort_products_low_to_high(driver):
    pass


@scenario("../features/sort_products.feature", "Sort Products High to Low")
@mark.usefixtures("base_functions")
def test_sort_products_high_to_low(driver):
    pass


@given("the user is logged in")
def step_sign_in(base_functions):
    base_functions.sign_in(UserData.STANDARD_USER)


@when("the user sorts the items A to Z")
def step_sort_from_a_to_z(base_functions):
    base_functions.press_button(InventoryPage.SORT_CONTAINER)
    base_functions.press_button(InventoryPage.A_TO_Z_OPTION)


@then("the items should be displayed in alphabetical order")
def step_check_sort_from_a_to_z(base_functions):
    item_names = base_functions.assign_elements(InventoryPage.INVENTORY_ITEM_NAME)
    for i in range(0, len(item_names) - 1):
        assert item_names[i].text < item_names[i + 1].text


@when("the user sorts the items Z to A")
def step_sort_from_z_to_a(base_functions):
    base_functions.press_button(InventoryPage.SORT_CONTAINER)
    base_functions.press_button(InventoryPage.Z_TO_A_OPTION)


@then("the items should be displayed in reverse alphabetical order")
def step_check_sort_from_z_to_a(base_functions):
    item_names = base_functions.assign_elements(InventoryPage.INVENTORY_ITEM_NAME)
    for i in range(0, len(item_names) - 1):
        assert item_names[i].text > item_names[i + 1].text


@when("the user sorts the items low to high")
def step_sort_from_low_to_high(base_functions):
    base_functions.press_button(InventoryPage.SORT_CONTAINER)
    base_functions.press_button(InventoryPage.LOW_TO_HIGH_PRICE_OPTION)


@then("the items should be displayed in ascending order")
def step_check_sort_from_low_to_high(base_functions):
    item_prices = base_functions.assign_elements(InventoryPage.INVENTORY_ITEM_PRICE)
    for i in range(0, len(item_prices) - 1):
        assert float(item_prices[i].text[1:]) <= float(item_prices[i+1].text[1:])


@when("the user sorts the items high to low")
def step_sort_from_high_to_low(base_functions):
    base_functions.press_button(InventoryPage.SORT_CONTAINER)
    base_functions.press_button(InventoryPage.HIGH_TO_LOW_PRICE_OPTION)


@then("the items should be displayed in descending order")
def step_check_sort_from_high_to_low(base_functions):
    item_prices = base_functions.assign_elements(InventoryPage.INVENTORY_ITEM_PRICE)
    for i in range(0, len(item_prices) - 1):
        assert float(item_prices[i].text[1:]) >= float(item_prices[i+1].text[1:])