import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("headless")
BUTTON = "//div[starts-with(@class, 'Header' )]/button[1][contains(text(), 'Заказать' )]"
BUTTON1 = "//div[starts-with(@class, 'Header_Nav' )]"
BUTTON2 = "div[class*='Header_Nav'] > button[class*='Button']"
BUTTON3 = "div[class^='Header_Nav'] > button[class*='Button']"


url = 'https://qa-scooter.praktikum-services.ru/'
#browser_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# browser_driver = webdriver.Chrome(ChromeDriverManager().install())
browser_driver = webdriver.Chrome()
print(browser_driver)
browser_driver.get(url)
# elm = browser_driver.find_element(By.CSS_SELECTOR, BUTTON3)
#
# print(elm)
# print(elm.id)

links1 = browser_driver.execute_script("return document.querySelectorAll('div[class^=Header_Nav] > button[class*=Button]')")
# print(links)
browser_driver.quit()