from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from copy import deepcopy
import time

BUTTON = 'button'
USERENAME = "//span/input[@name='username']"
PASSWORD = "//span/input[@name='password']"
login = 'admin'
password = 'admin'
baseurl = 'http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones'
COUNTRYES = '[name=geo_zones_form] td:nth-child(3) a'
ZONES = 'td select[name*=zone_code]'
ZONES1 = 'td select[name*=zone_code] option[selected]'

def test_geozones(driver):
    driver.get(baseurl)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, BUTTON)))
    driver.find_element(By.XPATH, USERENAME).send_keys(login)
    driver.find_element(By.XPATH, PASSWORD).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, BUTTON).click()
    time.sleep(2)
    countries_text = []
    countries = driver.find_elements(By.CSS_SELECTOR, COUNTRYES)
    for j in range(len(countries)):
        countries_text.append(countries[j].text)
    print(countries_text)
    for country in countries_text:
        driver.find_element(By.XPATH, f"//a[text()='{country}']").click()
        zones = driver.find_elements(By.CSS_SELECTOR, ZONES1)
        print(len(zones))
        zones_text = []
        for zona in zones:
            zones_text.append(zona.text)
        print(zones_text)
        zones_text_template = deepcopy(zones_text)
        zones_text_template.sort()
        for i in range(len(zones_text_template)):
            assert zones_text_template[i] == zones_text[i], (f"В строке {i + 1} зона {zones_text[i]},"
                                                           f"а должна быть {zones_text_template[i]}")
        driver.back()



