"""Inventory page / Homepage of the Sauce Demo webpage
This is displayed after a successful login"""

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class SauceDemoInventoryPage:
    # Locators
    PRODUCT_SORT = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_ELEMENTS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    CART_BADGE_COUNTER = (By.CLASS_NAME, "shopping_cart_badge")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    def sort_products(self, value):
        """Sort products selecting a dropdown option (lohi, hilo, az, za)"""
        Select(self.browser.find_element(*self.PRODUCT_SORT)).select_by_value(value)

    def get_products(self):
        """Get all the products web element"""
        products = self.browser.find_elements(*self.PRODUCT_ELEMENTS)
        return products

    def get_products_prices(self):
        """Returns a list of float prices from a list of product elements"""
        products = self.get_products()
        prices = []
        for element in products:
            prices.append(float(element.find_element(*self.PRODUCT_PRICES).text[1:]))
        return prices

    def add_product(self, product):
        product.find_element(*self.ADD_TO_CART_BUTTON).click()

    def add_products_bulk(self, n):
        """Adds 'n' number of products to cart while n <= product elements"""
        products = self.get_products()
        if n <= len(products):
            for product in products[:n]:
                self.add_product(product)

    def get_cart_badge_counter(self):
        return int(self.browser.find_element(*self.CART_BADGE_COUNTER).text)
