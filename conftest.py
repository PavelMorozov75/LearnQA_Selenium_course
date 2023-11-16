import pytest
from selenium import webdriver
@pytest.fixture()
def driver():
    browser_driver = webdriver.Chrome()
    yield browser_driver
    browser_driver.quit()