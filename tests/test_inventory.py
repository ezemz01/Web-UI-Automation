import pytest
from pages.inventory import SauceDemoInventoryPage
from pages.login import SauceDemoLoginPage


class TestInventory:

    @pytest.mark.parametrize("username, password",
                             [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce")])
    @pytest.mark.parametrize("sort_option", ["lohi", "hilo"])
    def test_sort(self, browser, username, password, sort_option):
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

    @pytest.mark.parametrize("username, password",
                             [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce")])
    def test_add_products(self, browser, username, password):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        login_page.login_with_click(username, password)
        inventory_page = SauceDemoInventoryPage(browser)
        inventory_page.add_products_bulk(4)
        assert inventory_page.get_cart_badge_counter() == 4
