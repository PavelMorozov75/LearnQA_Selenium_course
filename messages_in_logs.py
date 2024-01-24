from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


base_url = 'http://localhost/litecart/admin/'
catalog_url = "http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1"

BUTTON = 'button'
USERENAME = "//span/input[@name='username']"
PASSWORD = "//span/input[@name='password']"
CATALOG = "//h1[contains(text(), 'Catalog')]"
ELEMENTS_IN_TABLE = ".dataTable a"
ELEMENTS_IN_TABLE1 = "//table [@class='dataTable']/tbody/tr[@class='row']/ td/a"
ELEMENTS_IN_TABLE2 = "//table [@class='dataTable']/tbody/tr/td[3]/a"
ELEMENTS_IN_TABLE2_STRONG = "//table [@class='dataTable']/tbody/tr/td[3]/strong/a"
ELEMENTS_IN_TABLE22 = "//table [@class='dataTable']/tbody/tr[@class='row']/td[3]/a"# все элементы
ELEMENTS_IN_TABLE33 = "//table [@class='dataTable']/tbody/tr[@class='row' or @class='row semi-transparent']//td[3]/a"


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

driver.get(catalog_url)
WebDriverWait(driver,2).until(lambda d: d.find_element(By.XPATH, CATALOG))

products = driver.find_elements(By.XPATH, ELEMENTS_IN_TABLE33)
products_count = len(products)
for i in range(5, products_count + 4):
    driver.implicitly_wait(1)
    elm = driver.find_elements(By.XPATH, f"//table [@class='dataTable']/tbody/tr[{i}]/td[3]/a")
    if len(elm) > 0:
        elm[0].click()
        for j in driver.get_log('browser'):
            print(f"При клике на товар {i-5}  сообщения в логах браузера {j}")
        driver.back()
driver.quit()


