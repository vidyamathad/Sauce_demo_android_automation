import os
import pytest
from datetime import datetime

def capture_screenshot(driver, name="screenshot"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join("screenshots", f"{name}_{timestamp}.png")
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(filepath)
    return filepath

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            capture_screenshot(driver, item.name)
