"""Collection of fixtures to use across tests"""
import pytest
from selenium import webdriver
# from selenium.webdriver.remote.webdriver import WebDriver
import json


@pytest.fixture
def config(scope='session'):
    with open('../config.json') as config_file:
        config = json.load(config_file)
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    # assert isinstance(config['implicit_wait'], int)
    # assert config['implicit_wait'] > 0
    yield config

@pytest.fixture
def browser(config):
    try:
        b = getattr(webdriver, config['browser'])()
    except ValueError:
        print(f"Browser '{config['browser']}' is not supported.")
        raise
    yield b
    b.quit()

# def pytest_addoption(parser):
#     parser.addoption('--browser')
# @pytest.fixture
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture
# def driver(browser) -> WebDriver:
#
#     browser_list = ["firefox", "chrome"]
#
#     if browser in browser_list:
#         web_driver = getattr(webdriver, str(browser).capitalize())()
#     else:
#         web_driver = webdriver.Firefox()
#     yield web_driver
#     web_driver.close()
#     web_driver.quit()
