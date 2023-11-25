import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture()
def driver():
    # caps = webdriver.DesiredCapabilities.CHROME.copy()
    # caps['unexpectedAlertBehaviour'] = "dismiss"
    # browser_driver = webdriver.Chrome(desired_capabilities=caps)
    # options = Options()
    # options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    # browser_driver = webdriver.Firefox(executable_path=r'C:\WebDriver\bin\geckodriver.exe', options=options)
    # browser_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # browser_driver = webdriver.Chrome(ChromeDriverManager().install())
    browser_driver = webdriver.Chrome()
    yield browser_driver
    browser_driver.quit()