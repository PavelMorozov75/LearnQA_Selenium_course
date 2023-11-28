from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from copy import deepcopy
import time


base_url = 'http://localhost/litecart/admin/?app=countries&doc=countries'
BUTTON = 'button'
USERENAME = "//span/input[@name='username']"
PASSWORD = "//span/input[@name='password']"
countries_list = 'form[name=countries_form] td:nth-child(5) a'
zones_list = 'form[name=countries_form] td:nth-child(6) '
login = 'admin'
password = 'admin'
# zones_level2 = 'td input[name*=name][type=hidden]'
zones_level22 = '#table-zones td:nth-child(3)'

def test_sort_countries(driver):
    driver.get(base_url)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, BUTTON)))
    driver.find_element(By.XPATH, USERENAME).send_keys(login)
    driver.find_element(By.XPATH, PASSWORD).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, BUTTON).click()
    time.sleep(3)
    countries_text =[]
    countries = driver.find_elements(By.CSS_SELECTOR, countries_list)
    for country in countries:
        countries_text.append(country.text)
    countries_text_template = deepcopy(countries_text)
    countries_text_template.sort()
    for i in range(len(countries_text_template)):
        assert countries_text_template[i] == countries_text[i], (f"в строке {i+1} страна {countries_text[i]},"
                                                                 f"а надо {countries_text_template[i]}")

def test_sort_zones(driver):
    driver.get(base_url)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, BUTTON)))
    driver.find_element(By.XPATH, USERENAME).send_keys(login)
    driver.find_element(By.XPATH, PASSWORD).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, BUTTON).click()
    time.sleep(3)
    countries_with_many_zones_text =[]
    countries = driver.find_elements(By.CSS_SELECTOR, countries_list)
    count_zones = driver.find_elements(By.CSS_SELECTOR, zones_list)
    for j in range(len(countries)):
        if count_zones[j].text != '0':
           countries_with_many_zones_text.append(countries[j].text)
    print(countries_with_many_zones_text)

    for country in countries_with_many_zones_text:
        driver.find_element(By.XPATH, f"//a[text()='{country}']").click()
        time.sleep(2)
        zones = driver.find_elements(By.CSS_SELECTOR, zones_level22)
        zones = zones[:len(zones)-1]
        zone_list = []
        for zone in zones:
            zone_list.append(zone.text)
        print(zone_list)
        zone_list_template = deepcopy(zone_list)
        zone_list_template.sort()
        for i in range(len(zone_list_template)):
            assert zone_list_template[i] == zone_list[i], (f"В строке {i+1} зона {zone_list[i]},"
                                                           f"а должна быть {zone_list_template[i]}")
        driver.back()





