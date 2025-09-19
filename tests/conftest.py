import pytest
import os
from pages.login_page import LoginPage
from lib.json_reader import load_json
from lib.driver_factory import create_driver

# Load credentials
credentials = load_json(os.path.join("testdata", "credentials.json"))

@pytest.fixture(scope="function")
def driver():
    """Base driver fixture"""
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """Provides a driver that is already logged in."""
    login_page = LoginPage(driver)
    login_page.login(credentials["valid"]["username"], credentials["valid"]["password"])
    return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        # Look for any fixture that is a WebDriver
        driver = None
        for fixture_value in item.funcargs.values():
            if hasattr(fixture_value, "save_screenshot"):
                driver = fixture_value
                break

        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = f"{rep.nodeid.replace('::', '_').replace('/', '_')}.png"
            path = os.path.join(screenshot_dir, file_name)
            driver.save_screenshot(path)
            print(f"\nScreenshot saved to {path}")

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android")
    parser.addoption("--cloud", action="store", default="local")

# conftest.py
# import pytest
# from pages.login_page import LoginPage
#
# @pytest.fixture(autouse=True)
# def ensure_dashboard(driver):
#     """
#     After each test, ensure the app is back on the main dashboard.
#     This runs automatically for every test because autouse=True.
#     """
#     yield  # Run the test
#     try:
#         # If user is logged in, perform logout to return to login/dashboard
#         login_page = LoginPage(driver)
#         login_page.logout()
#     except Exception:
#         # Already on login screen or dashboard, nothing to do
#         pass

