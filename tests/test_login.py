
import pytest
from pages.login_page import LoginPage
from lib.json_reader import load_json
import os
from time import sleep

credentials = load_json(os.path.join("testdata", "credentials.json"))

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login(credentials["valid"]["username"], credentials["valid"]["password"])
        sleep(5)
        assert "Products" in driver.page_source


    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login(credentials["invalid"]["username"], credentials["invalid"]["password"])
        error_messages = login_page.get_error_messages()
        assert "Login" not in error_messages


    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.login(credentials["valid"]["username"], credentials["valid"]["password"])
        assert "Products" in driver.page_source
        login_page.logout()
        assert "Login" in driver.page_source


