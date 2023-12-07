from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import random
from datetime import datetime
from datetime import timedelta
import os
import string


url1 = "http://localhost/litecart/admin/login.php"
USERENAME = "//span/input[@name='username']"
PASSWORD = "//span/input[@name='password']"
# FIRST_MENU = "//span[text() ='Appearence']"
CATALOG = "//span[contains(text(), 'Catalog')]"
ADD_NEW_PRODUCT = "//a[contains(text(),  ' Add New Product')]"
BUTTON = 'button'
TAB_GENERAL = "//a[contains(text(),  'General')]"
RADIOBUTTON_STATUS = "//td/label/input[@type='radio']"
NAME = "//input[@name='name[en]']"
CODE = "input[name=code]"
CATEGORIES = "input[data-name=Root]"
PRODUCT_GROUPS = "//input[@name='product_groups[]']"
QUANTITY = "//input[@name='quantity']"
DATEPICKER_VALID_FROM = "//input[@name='date_valid_from']"
DATEPICKER_VALID_TO = "//input[@name='date_valid_to']"
FILE_LOAD = "//input[@type='file']"
INFORMATION_TAB = "//a[contains(text(), 'Information')]"
INFORMATION_TAB_IS_LOADED = "//strong[contains(text(), 'Manufacturer')]"
MANUFACTURER = "select[name=manufacturer_id]"
MANUFACTURER_ITEM1 = "//select[@name='manufacturer_id']/option[contains(text(),'ACME Corp.' )]"
KEYWORDS = "input[name=keywords]"
SHORT_DESCRIPTION = "//input[@name='short_description[en]']"
DESCRIPTION = ".trumbowyg-editor"
HEAD_TITLE = "//input[@name='head_title[en]']"
META_DESCRIPTION = "//input[@name='meta_description[en]']"
PRICES_TAB = "//a[contains(text(), 'Prices')]"
PRICES_TAB_IS_LOADED = "//h2[contains(text(), 'Prices')]"
PURCHASE_PRICE = "input[name=purchase_price]"
SELECT_CURRENCY = "select[name=purchase_price_currency_code]"
USD_CURRENCY = "//select[@name='purchase_price_currency_code']/option[contains(text(), 'US Dollars')]"
GROSS_PRICE_USD = "//input[@name='gross_prices[USD]']"
GROSS_PRICE_EUR = "//input[@name='gross_prices[EUR]']"
ADD_CAMPAIGN = "a#add-campaign"
CAMPAIGNS_START_DATE = "//input[@name='campaigns[new_1][start_date]']"
CAMPAIGNS_END_DATE = "//input[@name='campaigns[new_1][end_date]']"
DISCONT = "//input[@name='campaigns[new_1][percentage]']"
CAMPAIGNS_NEW_USD = "//input[@name='campaigns[new_1][USD]']"
CAMPAIGNS_NEW_EUR = "//input[@name='campaigns[new_1][EUR]']"
BUTTON_SAVE = "button[name=save]"
SAVED_SUCCESS = "//div[@class='notice success' ][contains(text(), ' Changes saved')]"

login = 'admin'
password = 'admin'
keyword = 'abrakada'
price = '15'


def generate_string(length):
    all_symbols = string.ascii_letters
    name = ''.join(random.choice(all_symbols) for _ in range(length))
    return name

driver = webdriver.Chrome()
driver.get(url1)
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, BUTTON)))
driver.find_element(By.XPATH, USERENAME).send_keys(login)
driver.find_element(By.XPATH, PASSWORD).send_keys(password)
driver.find_element(By.CSS_SELECTOR, BUTTON).click()
WebDriverWait(driver, 2).until(lambda d: d.find_element(By.XPATH, CATALOG)).click()
WebDriverWait(driver,2).until(lambda d: d.find_element(By.XPATH, ADD_NEW_PRODUCT)).click()
WebDriverWait(driver,2).until(lambda d: d.find_element(By.XPATH, TAB_GENERAL))
radio_button = driver.find_elements(By.XPATH, RADIOBUTTON_STATUS)
radio_button[0].click()
product_name = f"SUPER DUCK_{generate_string(2)}"
driver.find_element(By.XPATH, NAME).send_keys(product_name)
code = random.randint(10000, 20000)
driver.find_element(By.CSS_SELECTOR, CODE).send_keys(code)
checkbox = driver.find_element(By.CSS_SELECTOR, CATEGORIES)
print(checkbox.get_attribute('checked'))
if not checkbox.get_attribute('checked'):
    checkbox.click()
driver.find_elements(By.XPATH, PRODUCT_GROUPS)[2].click()
driver.find_element(By.XPATH, QUANTITY).clear()
driver.find_element(By.XPATH, QUANTITY).send_keys('1')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'product_foto.png')
driver.find_element(By.XPATH, FILE_LOAD).send_keys(file_path)
time.sleep(1)
driver.find_element(By.XPATH, DATEPICKER_VALID_FROM).send_keys(str(datetime.now().strftime("%d.%m.%Y")))
delta = timedelta(days=15)
driver.find_element(By.XPATH, DATEPICKER_VALID_TO).send_keys(str((datetime.now()+delta).strftime("%d.%m.%Y")))
driver.find_element(By.XPATH, INFORMATION_TAB).click()
WebDriverWait(driver,2).until(lambda d: d.find_element(By.XPATH, INFORMATION_TAB_IS_LOADED))
driver.find_element(By.CSS_SELECTOR, MANUFACTURER).click()
driver.find_element(By.XPATH, MANUFACTURER_ITEM1).click()
driver.find_element(By.CSS_SELECTOR, KEYWORDS).send_keys(generate_string(10))
driver.find_element(By.XPATH, SHORT_DESCRIPTION).send_keys(generate_string(15))
driver.find_element(By.CSS_SELECTOR, DESCRIPTION).send_keys(generate_string(100))
driver.find_element(By.XPATH, HEAD_TITLE).send_keys('DUCK')
driver.find_element(By.XPATH, META_DESCRIPTION).send_keys(generate_string(3))
driver.find_element(By.XPATH, PRICES_TAB).click()
WebDriverWait(driver,2).until(lambda d: d.find_element(By.XPATH, PRICES_TAB_IS_LOADED))
driver.find_element(By.CSS_SELECTOR, PURCHASE_PRICE).clear()
driver.find_element(By.CSS_SELECTOR, PURCHASE_PRICE).send_keys(price)
driver.find_element(By.CSS_SELECTOR, SELECT_CURRENCY).click()
driver.find_element(By.XPATH, USD_CURRENCY).click()
driver.find_element(By.XPATH, GROSS_PRICE_USD).clear()
driver.find_element(By.XPATH, GROSS_PRICE_USD).send_keys(str(int(price)*1.1))
driver.find_element(By.XPATH, GROSS_PRICE_EUR).clear()
driver.find_element(By.XPATH, GROSS_PRICE_EUR).send_keys(str(int(price)*1.3))
driver.find_element(By.CSS_SELECTOR, ADD_CAMPAIGN).click()
driver.find_element(By.XPATH, CAMPAIGNS_START_DATE).send_keys(str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S")))
driver.find_element(By.XPATH, CAMPAIGNS_END_DATE).send_keys(str((datetime.now()+delta).strftime("%Y-%m-%dT%H:%M:%S")))
driver.find_element(By.XPATH,DISCONT).send_keys('5')
driver.find_element(By.XPATH, CAMPAIGNS_NEW_USD).clear()
driver.find_element(By.XPATH, CAMPAIGNS_NEW_USD).send_keys(price)
driver.find_element(By.XPATH, CAMPAIGNS_NEW_EUR).clear()
driver.find_element(By.XPATH, CAMPAIGNS_NEW_EUR).send_keys(str(int(price)*1.2))
driver.find_element(By.CSS_SELECTOR, BUTTON_SAVE).click()
WebDriverWait(driver,2).until(expected_conditions.visibility_of_element_located((By.XPATH, SAVED_SUCCESS)))
driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog')
assert WebDriverWait(driver,2).until(lambda d: d.find_element(By.XPATH, f"//a[contains(text(), '{product_name}')]"))
time.sleep(3)
driver.quit()
