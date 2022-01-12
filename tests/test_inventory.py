import pytest
from pages.inventory import SauceDemoInventoryPage
from pages.login import SauceDemoLoginPage


# from selenium.webdriver.remote.webelement import WebElement


class TestInventory:

    @pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
    @pytest.mark.parametrize("sort_option", ["lohi", "hilo"])
    def test_sort_lohi(self, browser, username, password, sort_option):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        login_page.login_with_enter(username, password)
        inventory_page = SauceDemoInventoryPage(browser)
        inventory_page.sort_products(sort_option)
        prices = inventory_page.get_products_prices()
        if sort_option == "lohi":
            assert prices == sorted(prices)
        elif sort_option == "hilo":
            assert prices == sorted(prices, reverse=True)
        else:
            raise Exception(f"Invalid parameter: {sort_option}")
