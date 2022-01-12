"""Inventory page / Homepage of the Sauce Demo webpage
This is displayed after a successful login"""

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class SauceDemoInventoryPage:
    # Locators
    PRODUCTS_SORT = (By.CLASS_NAME, "product_sort_container")
    PRODUCTS_ELEMENTS = (By.CLASS_NAME, "inventory_item")
    PRODUCTS_PRICES = (By.CLASS_NAME, "inventory_item_price")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    def sort_products(self, value):
        """Sort products selecting a dropdown option (lohi, hilo, az, za)"""
        Select(self.browser.find_element(*self.PRODUCTS_SORT)).select_by_value(value)

    def get_products(self):
        """Get all the products web element"""
        products = self.browser.find_elements(*self.PRODUCTS_ELEMENTS)
        return products

    def get_products_prices(self):
        """Returns a list of float prices from a list of product elements"""
        products = self.get_products()
        prices = []
        for element in products:
            prices.append(float(element.find_element(*self.PRODUCTS_PRICES).text[1:]))
        return prices
