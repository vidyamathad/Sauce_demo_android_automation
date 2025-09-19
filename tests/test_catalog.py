import pytest
from Pages.catalog import CatalogPageIOS
import os

@pytest.mark.usefixtures("driver")
class TestCatalogIOS:

    def test_open_product_details(self, driver):
        catalog = CatalogPageIOS(driver)
        catalog.open_first_product()
        name, price = catalog.get_product_details()
        assert name != "", "Product name should not be empty"
        assert "$" in price, "Product price should contain $ sign"

    def test_add_product_to_cart(self, driver):
        catalog = CatalogPageIOS(driver)
        catalog.open_first_product()
        product_name, product_price = catalog.get_product_details()
        catalog.add_to_cart()
        catalog.open_cart()
        cart_name, cart_price = catalog.get_cart_item_details()
        assert product_name == cart_name
        assert product_price == cart_price

    def test_sort_products_by_name_asc(self, driver):
        catalog = CatalogPageIOS(driver)
        catalog.sort_by_name_asc()
        names = [el.text for el in driver.find_elements("accessibility id", "CartItemTitle")]
        assert names == sorted(names)

    # Similarly add name_desc, price_asc, price_desc tests
