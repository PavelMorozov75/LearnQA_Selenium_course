from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
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
SUBMENU_LIST = '#box-apps-menu li li'
SUBMENU_LIST1 = '#box-apps-menu li li'

def test_find_menu_item(driver):
    driver.get(url1)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, BUTTON)))
    driver.find_element(By.XPATH, USERENAME).send_keys(login)
    driver.find_element(By.XPATH, PASSWORD).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, BUTTON).click()
    assert WebDriverWait(driver, 15).until((expected_conditions.presence_of_element_located((By.XPATH,
                                                                                             FIRST_MENU)))),\
        f"незалогин"
    #вариант реализации 1
    menu_items = driver.find_elements(By.CSS_SELECTOR, MENU_ICON)
    count_menu_items = len(menu_items)
    for i in range(1, count_menu_items+1):
        driver.implicitly_wait(1)
        item = driver.find_element(By.XPATH, f"//ul[@id='box-apps-menu']/li[{i}]/a/span[2]").click()
        assert driver.find_element(By.TAG_NAME, "h1"), f"у подпункта {item.text} нет заголовка h1"
        sub_menu_items = driver.find_elements(By.CSS_SELECTOR, SUBMENU_LIST)
        count_submenu_items = len(sub_menu_items)
        for j in range(1, count_submenu_items+1):
            driver.implicitly_wait(1)
            subitem = driver.find_element(By.XPATH, f"//ul[@id='box-apps-menu']/li[{i}]/ul/li[{j}]").click()
            assert driver.find_element(By.TAG_NAME, "h1"), f"у подпункта {subitem.text} нет заголовка h1"

    # вариант реализации 2 с поиском внутри элемента
    n = 1
    while True:
        driver.implicitly_wait(1)
        try:
            item = driver.find_element(By.XPATH, f"//ul[@id='box-apps-menu']/li[{n}]")
        except NoSuchElementException:
            break
        item.click()
        assert driver.find_element(By.TAG_NAME, "h1"), f"у подпункта {item.text} нет заголовка h1"
        driver.implicitly_wait(1)
        item = driver.find_element(By.XPATH, f"//ul[@id='box-apps-menu']/li[{n}]")
        sub_items = item.find_elements(By.XPATH, ".//ul/li")
        if sub_items:
            m = 1
            while m <= len(sub_items):
                item = driver.find_element(By.XPATH, f"//ul[@id='box-apps-menu']/li[{n}]")
                sub_item = item.find_element(By.XPATH, f".//ul/li[{m}]").click()
                assert driver.find_element(By.TAG_NAME, "h1"), f"у подпункта {sub_item.text} нет заголовка h1"
                m += 1
        n += 1







