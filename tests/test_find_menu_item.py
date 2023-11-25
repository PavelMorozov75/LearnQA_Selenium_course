from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

url1 = "http://localhost/litecart/admin/login.php"
BUTTON = 'button'
USERENAME = "//span/input[@name='username']"
PASSWORD = "//span/input[@name='password']"
FIRST_MENU = "//span[text() ='Appearence']"
login = 'admin'
password = 'admin'
MENU_ICON = '#box-apps-menu li span.fa-stack:nth-child(1)'
# MENU_LIST = '#box-apps-menu li'
MENU_LIST = '#box-apps-menu li span.name'
SUBMENU_LIST = '#box-apps-menu li li span'

def test_find_menu_item(driver):
    driver.get(url1)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, BUTTON)))
    driver.find_element(By.XPATH, USERENAME).send_keys(login)
    driver.find_element(By.XPATH, PASSWORD).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, BUTTON).click()
    assert WebDriverWait(driver, 15).until((expected_conditions.presence_of_element_located((By.XPATH,
                                                                                             FIRST_MENU)))),\
        f"незалогин"

    menu_items = driver.find_elements(By.CSS_SELECTOR, MENU_ICON)
    print(len(menu_items))
    for item in menu_items:
        item.click()
        time.sleep(3)
        sub_menu_items = driver.find_elements(By.CSS_SELECTOR, SUBMENU_LIST)
        if len(sub_menu_items) > 0:
            for subitem in sub_menu_items:
                subitem.click()
                time.sleep(2)
                assert driver.find_element(By.TAG_NAME, "h1"), f"у подпункта {subitem.text} нет заголовка h1"
        else:
            assert driver.find_element(By.TAG_NAME, "h1"), f"у пункта {item.text} нет заголовка h1"



    '''while True:
        try:
            driver.find_element(By.CSS_SELECTOR, MENU_LIST).click()
            time.sleep(2)
            while True:
                try:
                    driver.find_element(By.CSS_SELECTOR, SUBMENU_LIST).click()
                    time.sleep(2)
                    assert driver.find_element(By.TAG_NAME, "h1")
                    break
                except:
                    break
        except: break'''




