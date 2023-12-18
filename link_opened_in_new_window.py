import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


base_url = 'http://localhost/litecart/admin/'
countries_url = "http://localhost/litecart/admin/?app=countries&doc=countries"
BUTTON = 'button'
USERENAME = "//span/input[@name='username']"
PASSWORD = "//span/input[@name='password']"
COUNTRIES_LIST = 'form[name=countries_form] td:nth-child(5) a'
STATUS = "//strong[contains(text(), 'Status')]"
EXTERNAL_LINK = ".fa-external-link"
login = 'admin'
password = 'admin'

driver = webdriver.Chrome()

def check_is_not_in():
    return len(driver.find_elements(By.CSS_SELECTOR, BUTTON)) > 0
def login_in():
    driver.find_element(By.XPATH, USERENAME).send_keys(login)
    driver.find_element(By.XPATH, PASSWORD).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, BUTTON).click()

driver.get(base_url)
if check_is_not_in():
    login_in()

driver.get(countries_url)
driver.find_elements(By.CSS_SELECTOR, COUNTRIES_LIST)[0].click()
WebDriverWait(driver,1).until(lambda d: d.find_element(By.XPATH, STATUS))
esternal_links = driver.find_elements(By.CSS_SELECTOR, EXTERNAL_LINK)
first_window = driver.current_window_handle
assert len(driver.window_handles) == 1
for elm in esternal_links:
    elm.click()
    WebDriverWait(driver,3).until(expected_conditions.number_of_windows_to_be(2))
    assert len(driver.window_handles) == 2
    driver.switch_to.window([w for w in driver.window_handles if w != first_window][0])
    time.sleep(1)
    driver.close()
    driver.switch_to.window(first_window)
    time.sleep(1)










