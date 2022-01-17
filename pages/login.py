"""Login page of the Sauce Demo webpage"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.inventory import SauceDemoInventoryPage

class SauceDemoLoginPage:
    URL = "https://www.saucedemo.com/"

    # Locators
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    ERROR_MESSAGE = (By.XPATH, '//h3[@data-test="error"]')
    PRICE_FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def get_current_url(self):
        return self.browser.current_url

    def title(self):
        return self.browser.title

    def login_with_enter(self, username, password):
        self.browser.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(password, Keys.RETURN)

    def login_with_click(self, username, password):
        self.browser.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.browser.find_element(By.ID, "password").send_keys(password)
        self.browser.find_element(By.ID, "login-button").click()

    def get_errorbox_element(self):
        return self.browser.find_element(*self.ERROR_MESSAGE)
