from appium.webdriver.common.appiumby import AppiumBy
from libs.json_reader import load_json
from libs.wait import wait_for_element, wait_and_click
import os

locators = load_json(os.path.join("locators", "login_locators.json"))

def by_mapper(locator_type):
    mapping = {
        "id": AppiumBy.ID,
        "xpath": AppiumBy.XPATH,
        "accessibility_id": AppiumBy.ACCESSIBILITY_ID,
        "class_name": AppiumBy.CLASS_NAME
    }
    return mapping[locator_type]

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        wait_and_click(self.driver, locators["hamburger_menu"]["value"], by_mapper(locators["hamburger_menu"]["by"]))
        wait_and_click(self.driver, locators["login_menu"]["value"], by_mapper(locators["login_menu"]["by"]))

        wait_for_element(self.driver, locators["user_field"]["value"], by_mapper(locators["user_field"]["by"])).send_keys(username)
        wait_for_element(self.driver, locators["password"]["value"], by_mapper(locators["password"]["by"])).send_keys(password)

        wait_and_click(self.driver, locators["login_button"]["value"], by_mapper(locators["login_button"]["by"]))

    def logout(self):
        wait_and_click(self.driver, locators["hamburger_menu"]["value"], by_mapper(locators["hamburger_menu"]["by"]))
        wait_and_click(self.driver, locators["logout_bar"]["value"], by_mapper(locators["logout_bar"]["by"]))
        wait_and_click(self.driver, locators["logout_alert"]["value"], by_mapper(locators["logout_alert"]["by"]))
        wait_and_click(self.driver, locators["click_logout"]["value"], by_mapper(locators["click_logout"]["by"]))

    def get_error_messages(self):
        error_message = wait_for_element(self.driver, locators["click_logout"]["value"], by_mapper(locators["click_logout"]["by"]))
        return error_message

