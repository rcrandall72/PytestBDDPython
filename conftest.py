import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from distutils.util import strtobool

from base_functions import BaseFunctions
from common_strings import URLs


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Specify chrome, firefox or safari"
    )

    parser.addoption(
        "--headless", action="store", default=True, help="Specify True or False", type=lambda x: bool(strtobool(x))
    )


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    browser_option = request.param
    headless_mode = True

    # Set browser based on option
    if browser_option.lower() == "chrome":
        options = ChromeOptions()
        if headless_mode:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser_option.lower() == "firefox":
        options = FirefoxOptions()
        if headless_mode:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError("Invalid browser specified")

    # TODO: Go to URL based on environment
    driver.get(URLs.SAUCE_DEMO)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def base_functions(driver):
    return BaseFunctions(driver)
