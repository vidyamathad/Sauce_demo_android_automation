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
import subprocess

def save_logcat(test_name):
    """Capture logcat logs for debugging"""
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    file_name = f"{test_name}.log"
    path = os.path.join(log_dir, file_name)

    with open(path, "w", encoding="utf-8") as f:
        subprocess.run(["adb", "logcat", "-d"], stdout=f, stderr=subprocess.STDOUT)

    # Clear logcat after saving, so next test starts fresh
    subprocess.run(["adb", "logcat", "-c"])
    print(f"\nLogcat saved to {path}")
    return path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = None
        for fixture_value in item.funcargs.values():
            if hasattr(fixture_value, "save_screenshot"):
                driver = fixture_value
                break

        test_name = rep.nodeid.replace("::", "_").replace("/", "_")

        # Save screenshot
        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved to {screenshot_path}")

        # Save logcat
        save_logcat(test_name)



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

