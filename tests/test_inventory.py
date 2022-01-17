import pytest
from pages.inventory import SauceDemoInventoryPage
from pages.login import SauceDemoLoginPage


class TestInventory:
    """Homepage / Inventory page Test Suite"""

    @pytest.mark.parametrize("username, password",
                             [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce")])
    def test_sort_low_to_high(self, browser, username, password):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        login_page.login_with_enter(username, password)
        inventory_page = SauceDemoInventoryPage(browser)
        inventory_page.sort_products("lohi")
        prices = inventory_page.get_products_prices()
        assert prices == sorted(prices)

    @pytest.mark.parametrize("username, password",
                             [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce")])
    def test_sort_high_to_low(self, browser, username, password):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        login_page.login_with_enter(username, password)
        inventory_page = SauceDemoInventoryPage(browser)
        inventory_page.sort_products("hilo")
        prices = inventory_page.get_products_prices()
        assert prices == sorted(prices, reverse=True)

    @pytest.mark.parametrize("username, password",
                             [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce")])
    def test_add_products(self, browser, username, password):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        login_page.login_with_click(username, password)
        inventory_page = SauceDemoInventoryPage(browser)
        inventory_page.add_products_bulk(4)
        assert inventory_page.get_cart_badge_counter() == 4

    @pytest.mark.parametrize("username, password",
                             [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce")])
    def test_logout(self, browser, username, password):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        inventory_page = SauceDemoInventoryPage(browser)

        login_page.login_with_enter(username, password)
        inventory_page.logout()
        assert login_page.get_current_url().endswith("saucedemo.com/")

    @pytest.mark.parametrize("username, password",
                             [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce")])
    def test_logout(self, browser, username, password):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        inventory_page = SauceDemoInventoryPage(browser)

        login_page.login_with_enter(username, password)
        inventory_page.logout()
        assert login_page.get_current_url().endswith("saucedemo.com/")

    # test checkout positive
        # login
        # add products to cart
        # go to cart page
        # checkout
            # fill first name, last name, zip code
            # continue
            # finish payment
    # test checkout without items
    # test checkout with one item
    # test checkout with more than one item
    # test checkout without filling form
