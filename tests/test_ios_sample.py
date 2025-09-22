import os
import pytest
from libs.driver_factory import create_driver

SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_ACCESS_KEY = os.getenv("SAUCE_ACCESS_KEY")

@pytest.fixture
def driver():
    driver = create_driver(
        platform="ios",
        cloud="sauce",
        username=SAUCE_USERNAME,
        access_key=SAUCE_ACCESS_KEY
    )
    yield driver
    driver.quit()

def test_launch_app(driver):
    el = driver.find_element("accessibility id", "test-Login")
    assert el.is_displayed()
