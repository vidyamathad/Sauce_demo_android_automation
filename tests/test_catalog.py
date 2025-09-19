import pytest
from pages.catalog_page import CatalogPage

@pytest.mark.usefixtures("logged_in_driver")
class TestCatalog:

    def test_open_product_details(self, logged_in_driver):
        catalog = CatalogPage(logged_in_driver)
        catalog.open_first_product()
        name, price = catalog.get_product_details()
        assert name != "", "Product name should not be empty"
        assert "$" in price, "Product price should contain $ sign"

    def test_add_product_to_cart(self, logged_in_driver):
        catalog = CatalogPage(logged_in_driver)
        catalog.open_first_product()
        product_name, product_price = catalog.get_product_details()
        catalog.add_to_cart()
        catalog.open_cart()
        cart_name, cart_price = catalog.get_cart_item_details()
        assert product_name == cart_name, "Product name in cart should match"
        assert product_price == cart_price, "Product price in cart should match"

    def test_sort_products_by_name_asc(self, logged_in_driver):
        catalog = CatalogPage(logged_in_driver)
        catalog.sort_by_name_asc()
        names = catalog.get_all_names()
        assert names == sorted(names), "Products should be sorted by name ascending"

    def test_sort_products_by_name_desc(self, logged_in_driver):
        catalog = CatalogPage(logged_in_driver)
        catalog.sort_by_name_desc()
        names = catalog.get_all_names()
        assert names == sorted(names, reverse=True), "Products should be sorted by name descending"

    def test_sort_products_by_price_asc(self, logged_in_driver):
        catalog = CatalogPage(logged_in_driver)
        catalog.sort_by_price_asc()
        prices = catalog.get_all_prices()
        assert prices == sorted(prices), "Products should be sorted by price ascending"

    def test_sort_products_by_price_desc(self, logged_in_driver):
        catalog = CatalogPage(logged_in_driver)
        catalog.sort_by_price_desc()
        prices = catalog.get_all_prices()
        assert prices == sorted(prices, reverse=True), "Products should be sorted by price descending"
