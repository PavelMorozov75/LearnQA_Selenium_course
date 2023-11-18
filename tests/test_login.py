from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url1 = "http://localhost/litecart/admin/login.php"
BUTTON = 'button'
USERENAME = "//span/input[@name='username']"
PASSWORD = "//span/input[@name='password']"
FIRST_MENU = "//span[text() ='Appearence']"
login = 'admin'
password = 'admin'

def test_login_to_admin(driver):
    driver.get(url1)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, BUTTON)))
    driver.find_element(By.XPATH, USERENAME).send_keys(login)
    driver.find_element(By.XPATH, PASSWORD).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, BUTTON).click()
    assert WebDriverWait(driver, 15).until((expected_conditions.presence_of_element_located((By.XPATH, FIRST_MENU))))
