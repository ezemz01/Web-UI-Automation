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

    def test_title(self, browser):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        assert login_page.title() == "Swag Labs"

    @pytest.mark.parametrize("username, password",
                             [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce")])
    def test_login_with_enter_positive(self, browser, username, password):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        login_page.login_with_enter(username, password)
        assert login_page.get_current_url() == "https://www.saucedemo.com/inventory.html"
        # driver.find_element(By.ID, "user-name").send_keys(username)
        # driver.find_element(By.ID, "password").send_keys(password, Keys.RETURN)
        # assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    @pytest.mark.parametrize("username, password", [("locked_out_user", "secret_sauce")])
    def test_login_negative(self, browser, username, password):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        login_page.login_with_click(username, password)
        errorbox = login_page.get_errorbox_element()
        assert errorbox.is_displayed()
        assert errorbox.text == "Epic sadface: Sorry, this user has been locked out."
