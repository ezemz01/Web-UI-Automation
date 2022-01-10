"""Collection of fixtures to use across tests"""
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
 

#@pytest.fixture(params=["chrome", "firefox"], scope="class")
#def driver_init(request) -> WebDriver:
#    if request.param == "chrome":
#        web_driver = webdriver.Chrome()
#    if request.param == "firefox":
#        web_driver = webdriver.Firefox()
#    web_driver.maximize_window()
#    request.cls.driver = web_driver
#    yield
#    web_driver.close()
#    web_driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def driver(browser) -> WebDriver:

    browser_list = ["firefox", "chrome"]

    if browser in browser_list:
        web_driver = getattr(webdriver, str(browser).capitalize())()
    else:
        web_driver = webdriver.Firefox()
    yield web_driver
    web_driver.close()
    web_driver.quit()
