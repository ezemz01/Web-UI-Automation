"""Login tests for the Sauce Demo project"""
import pytest
# from time import sleep
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select

from pages.login import SauceDemoLoginPage


class TestLogin:
    # maybe add config as parameter and use to parametrize input
    
    # def test_title(browser, ):
    #     driver.get("https://www.saucedemo.com/")
    #     assert drivesr.title == "Swag Labs"

    @pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce")])
    def test_login_with_enter_positive(self, browser, username, password):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        login_page.login_with_enter(username, password)
        assert login_page.get_current_url() == "https://www.saucedemo.com/inventory.html"
        #driver.find_element(By.ID, "user-name").send_keys(username)
        #driver.find_element(By.ID, "password").send_keys(password, Keys.RETURN)
        #assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    @pytest.mark.parametrize("username, password", [("locked_out_user", "secret_sauce")])
    def test_login_negative(self, browser, username, password):
        login_page = SauceDemoLoginPage(browser)
        login_page.load()
        login_page.login_with_click(username, password)
        errorbox = login_page.get_errorbox_element()
        assert errorbox.is_displayed()
        assert errorbox.text == "Epic sadface: Sorry, this user has been locked out."

    # def test_sort_price(self, driver: WebDriver):
    #     # Regular login
    #     driver.get("https://www.saucedemo.com/")
    #     driver.find_element(By.ID, "user-name").send_keys("standard_user")
    #     driver.find_element(By.ID, "password").send_keys("secret_sauce", Keys.RETURN)
    #
    #     # Select the low to high price filter
    #     price_filter = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    #     price_filter.select_by_value("lohi")
    #
    #     # Find the price of the elements
    #     price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    #     # Create a parsed list of prices
    #     price_list = []
    #     for element in price_elements:
    #
    #         price_list.append(float(element.text[1:]))
    #     assert (price_list == sorted(price_list))
