from lib.json_reader import load_json
from lib.waits import wait_for_element, wait_and_click
from appium.webdriver.common.appiumby import AppiumBy
import os

locators = load_json(os.path.join("locators", "catalog_page.json"))

def by_mapper(locator_type):
    mapping = {
        "id": AppiumBy.ID,
        "xpath": AppiumBy.XPATH,
        "accessibility_id": AppiumBy.ACCESSIBILITY_ID,
        "class_name": AppiumBy.CLASS_NAME,
        "resource-id": AppiumBy.ID,
        "ui_automator": AppiumBy.ANDROID_UIAUTOMATOR
    }
    return mapping[locator_type]

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver

    def open_first_product(self):
        wait_and_click(self.driver, locators["catalog"]["value"], by_mapper(locators["catalog"]["by"]))

    def get_product_details(self):
        name = wait_for_element(self.driver, locators["product_name"]["value"], by_mapper(locators["product_name"]["by"])).text
        price = wait_for_element(self.driver, locators["product_price"]["value"], by_mapper(locators["product_price"]["by"])).text
        return name, price

    def add_to_cart(self):
        """
        Scroll until 'Add to Cart' button is visible and click it.
        Uses UiScrollable so it works even if button is not on screen.
        """
        resource_id = locators["add_to_cart_button"]["value"]
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().resourceId("{resource_id}"))'
        ).click()

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
        wait_and_click(self.driver, locators["sort_name_desc"]["value"],
                       by_mapper(locators["sort_name_desc"]["by"]))

    def sort_by_price_asc(self):
        wait_and_click(self.driver, locators["sort"]["value"], by_mapper(locators["sort"]["by"]))
        wait_and_click(self.driver, locators["sort_price_asc"]["value"],
                       by_mapper(locators["sort_price_asc"]["by"]))

    def sort_by_price_desc(self):
        wait_and_click(self.driver, locators["sort"]["value"], by_mapper(locators["sort"]["by"]))
        wait_and_click(self.driver, locators["sort_price_descending"]["value"],
                       by_mapper(locators["sort_price_descending"]["by"]))

    def get_all_names(self):
        name_elements = self.driver.find_elements(
            by_mapper(locators["cart_item_name"]["by"]),
            locators["cart_item_name"]["value"]
        )
        return [el.text.strip() for el in name_elements if el.text.strip()]

    def get_all_prices(self):
        price_elements = self.driver.find_elements(
            by_mapper(locators["product_list_prices"]["by"]),
            locators["product_list_prices"]["value"]
        )
        prices = []
        for el in price_elements:
            text = el.text.strip()
            if text:
                try:
                    prices.append(float(text.replace("$", "")))
                except ValueError:
                    continue
        return prices