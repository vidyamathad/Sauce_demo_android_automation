import pytest
import os
from libs.driver_factory import create_driver

@pytest.fixture
def driver(request):
    platform = request.config.getoption("--platform")  # get CLI value
    cloud = request.config.getoption("--cloud")
    username = os.getenv("SAUCE_USERNAME")
    access_key = os.getenv("SAUCE_ACCESS_KEY")

    driver = create_driver(platform=platform, cloud=cloud, username=username, access_key=access_key)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    group = parser.getgroup("custom")  # optional group
    group.addoption(
        "--platform",
        action="store",
        default="ios",
        help="Platform to run tests on: ios or android"
    )
    group.addoption(
        "--cloud",
        action="store",
        default="sauce",
        help="Cloud to run tests on: sauce or local"
    )


