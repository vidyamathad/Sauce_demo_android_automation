import os
import pytest
from libs.driver_factory import create_driver
from dotenv import load_dotenv

# Load global environment variables
load_dotenv()
SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_ACCESS_KEY = os.getenv("SAUCE_ACCESS_KEY")

@pytest.fixture(scope="session")
def driver(request):
    platform = request.config.getoption("--platform")
    cloud = request.config.getoption("--cloud")
    return create_driver(platform, cloud, SAUCE_USERNAME, SAUCE_ACCESS_KEY)

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android")
    parser.addoption("--cloud", action="store", default="sauce")
