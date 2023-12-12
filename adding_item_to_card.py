from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from datetime import datetime
from datetime import timedelta


url = "http://localhost/litecart/en/"
ITEMS = ".products .product"
HOME = "//a[contains(text(), 'Home')]"
SELECT = "//select[@name]"
SELECT_ITEMS = "select[name] option[value]"
BUTTON_ADD = "//button[contains(text(), 'Add To Cart')]"
COUNTER = "span.quantity"
CHECKOUT = "//a[contains(text(), 'Checkout »')]"
CUSTOMER_DETAILS = "//h2[contains(text(), 'Customer Details')]"
PRODUCTS_LINE = ".shortcuts li a"
REMOVE_BUTTON = "[name=remove_cart_item]"
ITEM_IN_TABLE = "tr td.item"
PRODUCT_NAME = "a >strong"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(1)

attempt = 1
while attempt <= 3:
   driver.find_elements(By.CSS_SELECTOR, ITEMS)[0].click()
   # counter_elm = driver.find_element(By.CSS_SELECTOR, COUNTER)
   cont_products_before = int(driver.find_element(By.CSS_SELECTOR, COUNTER).get_attribute('textContent'))
   # print(cont_products_before)
   WebDriverWait(driver,1).until(lambda d: d.find_element(By.XPATH, HOME))
   if len(driver.find_elements(By.XPATH, SELECT)) > 0:
       driver.find_element(By.XPATH, SELECT).click()
       driver.find_elements(By.CSS_SELECTOR,SELECT_ITEMS)[1].click()
   driver.find_element(By.XPATH, BUTTON_ADD).click()
   cont_products_after = cont_products_before
   stoptime = datetime.now() + timedelta(seconds=1)
   while cont_products_after == cont_products_before and datetime.now() <= stoptime:
       cont_products_after = int(driver.find_element(By.CSS_SELECTOR, COUNTER).get_attribute('textContent'))
   # print(cont_products_after)
   assert cont_products_after == cont_products_before + 1
   driver.get(url)
   attempt+=1
driver.find_element(By.XPATH,CHECKOUT).click()
WebDriverWait(driver,1).until(lambda d: d.find_element(By.XPATH, CUSTOMER_DETAILS))
products_in_cart = driver.find_elements(By.CSS_SELECTOR, PRODUCTS_LINE)
# print(len(products_in_cart))
if len(products_in_cart) > 0:
   products_in_cart[0].click()
for i in range(len(products_in_cart)):
   name = driver.find_element(By.CSS_SELECTOR, PRODUCT_NAME).text
   elm_in_table = driver.find_element(By.XPATH, f"//tr/td[contains(text(), '{name}')]")
   print(name)
   driver.find_element(By.CSS_SELECTOR, REMOVE_BUTTON).click()
   WebDriverWait(driver,2).until(expected_conditions.staleness_of(elm_in_table))
# time.sleep(2)
driver.quit()

