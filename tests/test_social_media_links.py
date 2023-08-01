from pytest_bdd import given, when, then, scenario
from common_strings import *
from pytest import mark


@scenario("../features/social_media_links.feature", "Open Social Media Links")
def test_open_social_media_links(driver):
    pass


@given("the user is logged in")
def step_sign_in(base_functions):
    base_functions.sign_in(UserData.STANDARD_USER)


@when("the user opens the Twitter link")
def step_open_twitter_link(base_functions):
    base_functions.press_button(FooterPage.SOCIAL_TWITTER, wait=True)
    base_functions.check_window_handle(FooterPage.TWITTER_URL)


@then("the Twitter page should be opened")
def step_check_twitter_page(base_functions):
    assert base_functions.driver.current_url == FooterPage.TWITTER_URL


@when("the user opens the Facebook link")
def step_open_facebook_link(base_functions):
    base_functions.press_button(FooterPage.SOCIAL_FACEBOOK, wait=True)
    base_functions.check_window_handle(FooterPage.FACEBOOK_URL)


@then("the Facebook page should be opened")
def step_check_facebook_page(base_functions):
    assert base_functions.driver.current_url == FooterPage.FACEBOOK_URL


@when("the user opens the LinkedIn link")
def step_open_linkedin_link(base_functions):
    base_functions.press_button(FooterPage.SOCIAL_LINKEDIN, wait=True)
    base_functions.check_window_handle(FooterPage.LINKEDIN_URL)


@then("the LinkedIn page should be opened")
def step_check_linkedin_page(base_functions):
    assert FooterPage.LINKEDIN_URL in base_functions.driver.current_url
    assert FooterPage.SAUCE_LABS in base_functions.driver.current_url
