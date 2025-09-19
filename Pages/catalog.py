from libs.json_reader import load_json
from libs.wait import wait_for_element, wait_and_click
from appium.webdriver.common.appiumby import AppiumBy
import os

locators = load_json(os.path.join("locators", "catalog_locator.json"))

def by_mapper(locator_type):
    mapping = {
        "id": AppiumBy.ID,
        "xpath": AppiumBy.XPATH,
        "accessibility_id": AppiumBy.ACCESSIBILITY_ID,
        "class_name": AppiumBy.CLASS_NAME
    }
    return mapping[locator_type]

class CatalogPageIOS:
    def __init__(self, driver):
        self.driver = driver

    def open_first_product(self):
        wait_and_click(self.driver, locators["catalog"]["value"], by_mapper(locators["catalog"]["by"]))

    def get_product_details(self):
        name = wait_for_element(self.driver, locators["product_name"]["value"], by_mapper(locators["product_name"]["by"])).text
        price = wait_for_element(self.driver, locators["product_price"]["value"], by_mapper(locators["product_price"]["by"])).text
        return name, price

    def add_to_cart(self):
        wait_and_click(self.driver, locators["add_to_cart_button"]["value"], by_mapper(locators["add_to_cart_button"]["by"]))

    def open_cart(self):
        wait_and_click(self.driver, locators["cart_icon"]["value"], by_mapper(locators["cart_icon"]["by"]))

    def get_cart_item_details(self):
        name = wait_for_element(self.driver, locators["cart_item_name"]["value"], by_mapper(locators["cart_item_name"]["by"])).text
        price = wait_for_element(self.driver, locators["cart_item_price"]["value"], by_mapper(locators["cart_item_price"]["by"])).text
        return name, price

    def sort_by_name_asc(self):
        wait_and_click(self.driver, locators["sort"]["value"], by_mapper(locators["sort"]["by"]))
        wait_and_click(self.driver, locators["sort_name_asc"]["value"], by_mapper(locators["sort_name_asc"]["by"]))

    def sort_by_name_desc(self):
        wait_and_click(self.driver, locators["sort"]["value"], by_mapper(locators["sort"]["by"]))
        wait_and_click(self.driver, locators["sort_name_desc"]["value"], by_mapper(locators["sort_name_desc"]["by"]))

    def sort_by_price_asc(self):
        wait_and_click(self.driver, locators["sort"]["value"], by_mapper(locators["sort"]["by"]))
        wait_and_click(self.driver, locators["sort_price_asc"]["value"], by_mapper(locators["sort_price_asc"]["by"]))

    def sort_by_price_desc(self):
        wait_and_click(self.driver, locators["sort"]["value"], by_mapper(locators["sort"]["by"]))
        wait_and_click(self.driver, locators["sort_price_descending"]["value"], by_mapper(locators["sort_price_descending"]["by"]))
