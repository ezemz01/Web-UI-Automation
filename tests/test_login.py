"""Login tests for the Sauce Demo project"""
import pytest
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Base:
    """Base class that keeps the reference to the web driver. (only one initialization)"""
    pass


class TestLogin:
    
    def test_title(self, driver: WebDriver):
        driver.get("https://www.saucedemo.com/")
        assert driver.title == "Swag Labs"
    
    def test_login_positive(self, driver: WebDriver):
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce", Keys.RETURN)
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    def test_login_negative(self, driver: WebDriver):
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("test")
        driver.find_element(By.ID, "password").send_keys("test", Keys.RETURN)
        assert driver.find_element(By.XPATH, '//h3[@data-test="error"]').is_displayed()

    def test_sort_price(self, driver: WebDriver):
        # Regular login
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce", Keys.RETURN)

        # Select the low to high price filter
        price_filter = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        price_filter.select_by_value("lohi")

        # Find the price of the elements
        price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        # Create a parsed list of prices
        price_list = []
        for element in price_elements:
            price_list.append(float(element.text[1:]))
        assert (price_list == sorted(price_list))
