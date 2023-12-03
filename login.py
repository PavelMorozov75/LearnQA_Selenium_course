import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from selenium.webdriver.support.ui import Select
import random

base_url = 'http://localhost/litecart/en/login'
LOGIN_NEW_CUSTOMER_UP = "//a[contains(text(), 'New customers click here')]"
H1_TITLE = "//h1[contains(text(), 'Create Account')]"
FIRST_NAME = "input[name=firstname]"
LAST_NAME = "input[name=lastname]"
ADDRESS1 = "input[name=address1]"
POSTCODE = "input[name=postcode]"
CITY = "input[name=city]"
EMAIL = "input[name=email]"
PHONE = "input[name=phone]"
DESIRED_PASSWORD = "input[name=password]"
CONFIRMED_PASSWORD = "input[name=confirmed_password]"
BUTTON_CTEATE_ACCOUNT = "button[name=create_account]"
SELECT = "select[name=country_code]"
ACCOUNT_CREATED = "//div[contains(text(), ' Your customer account has been created.')]"
LOGOUT = "//a[contains(text(), 'Logout')]"
LOGOUT_SUCCESS = "//div[contains(text(), ' You are now logged out.')]"
BUTTON_LOGIN = "button[name=login]"
LOGGED_AS = "//div[contains(text(), 'You are now logged in as')]"

driver = webdriver.Chrome()
driver.get(base_url)
WebDriverWait(driver,1).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                        LOGIN_NEW_CUSTOMER_UP))).click()
WebDriverWait(driver,1).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                      H1_TITLE)))
faker = Faker()
faker.locate = 'en'
name = faker.first_name()
last_name = faker.last_name()
email = faker.ascii_free_email()
phone = "+7212-555-7575"
address = faker.street_address()
city = faker.city()
postcode = faker.postcode()
password = random.randint(10000, 20000)
driver.find_element(By.CSS_SELECTOR, FIRST_NAME).send_keys(name)
driver.find_element(By.CSS_SELECTOR, LAST_NAME).send_keys(last_name)
driver.find_element(By.CSS_SELECTOR, ADDRESS1).send_keys(address)
driver.find_element(By.CSS_SELECTOR, POSTCODE).send_keys(postcode)
driver.find_element(By.CSS_SELECTOR, CITY).send_keys(city)
select = Select(driver.find_element(By.CSS_SELECTOR, SELECT))
select.select_by_visible_text("United States")
driver.find_element(By.CSS_SELECTOR, EMAIL).send_keys(email)
driver.find_element(By.CSS_SELECTOR, PHONE).send_keys(phone)
driver.find_element(By.CSS_SELECTOR, DESIRED_PASSWORD).send_keys(password)
driver.find_element(By.CSS_SELECTOR, CONFIRMED_PASSWORD).send_keys(password)
driver.find_element(By.CSS_SELECTOR, BUTTON_CTEATE_ACCOUNT).click()
WebDriverWait(driver,2).until(expected_conditions.visibility_of_element_located((By.XPATH, ACCOUNT_CREATED)))
driver.find_element(By.XPATH, LOGOUT).click()
WebDriverWait(driver,2).until(expected_conditions.visibility_of_element_located((By.XPATH, LOGOUT_SUCCESS)))
driver.find_element(By.CSS_SELECTOR, EMAIL).send_keys(email)
driver.find_element(By.CSS_SELECTOR, DESIRED_PASSWORD).send_keys(password)
driver.find_element(By.CSS_SELECTOR, BUTTON_LOGIN).click()
WebDriverWait(driver,2).until(expected_conditions.visibility_of_element_located((By.XPATH, LOGGED_AS)))
driver.find_element(By.XPATH, LOGOUT).click()
# WebDriverWait(driver,2).until(expected_conditions.visibility_of_element_located((By.XPATH, LOGOUT_SUCCESS)))
wait = WebDriverWait(driver, 1).until(lambda d: d.find_element(By.XPATH, LOGOUT_SUCCESS))
time.sleep(3)
driver.quit()



