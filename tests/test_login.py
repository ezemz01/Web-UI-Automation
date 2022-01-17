"""Login tests for the Sauce Demo project"""
import pytest
from pages.login import SauceDemoLoginPage
# from time import sleep
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select


class TestLogin:
    # maybe add config as parameter and use to parametrize input

    PAGE_TITLE = "Swag Labs"
    HOMEPAGE_PATH = "inventory.html"
    ERRORMSG_LOCKED_USER = "Epic sadface: Sorry, this user has been locked out."
    ERRORMSG_INVALID_USER = "Epic sadface: Username and password do not match any user in this service"

    def test_title(self, browser):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        assert login_page.title() == self.PAGE_TITLE

    @pytest.mark.parametrize("username, password",
                             [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce")])
    def test_login_with_enter_positive(self, browser, username, password):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        login_page.login_with_enter(username, password)
        assert login_page.get_current_url().endswith(self.HOMEPAGE_PATH)

    @pytest.mark.parametrize("username, password", [("locked_out_user", "secret_sauce")])
    def test_login_negative_locked(self, browser, username, password):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        login_page.login_with_click(username, password)
        errorbox = login_page.get_errorbox_element()
        assert errorbox.is_displayed()
        assert errorbox.text == self.ERRORMSG_LOCKED_USER

    @pytest.mark.parametrize("username, password", [("test", "test")])
    def test_login_negative_invalid(self, browser, username, password):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        login_page.login_with_click(username, password)
        errorbox = login_page.get_errorbox_element()
        assert errorbox.is_displayed()
        assert errorbox.text == self.ERRORMSG_INVALID_USER
