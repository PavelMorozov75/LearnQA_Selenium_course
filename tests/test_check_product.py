from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

NAME_MAIN_PAGE = '#box-campaigns .name'
REGULAR_PRICE_MAIN_PAGE = '#box-campaigns .regular-price'
CAMPAIGN_PRICE_MAINPAGE = '#box-campaigns .campaign-price'
NAME_PROGUCT_PAGE = 'h1.title'
REGULAR_PRICE_PRODUCT_PAGE = '.regular-price'
CAMPAIGN_PRICE_PRODUCT_PAGE = '.campaign-price'

baseurl = 'http://localhost/litecart/en/'

def test_check_product(driver, browser_name):
    # browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("chrome")
    elif browser_name == "firefox":
        print('firefox')
    driver.get(baseurl)
    time.sleep(2)
    name_main_page = driver.find_elements(By.CSS_SELECTOR, NAME_MAIN_PAGE)[0]
    regular_price_main_page = driver.find_elements(By.CSS_SELECTOR, REGULAR_PRICE_MAIN_PAGE)[0]
    campaign_price_main_page = driver.find_elements(By.CSS_SELECTOR, CAMPAIGN_PRICE_MAINPAGE)[0]
    name_main_page_text = name_main_page.text
    regular_price_main_page_text = regular_price_main_page.text
    campaign_price_main_page_text = campaign_price_main_page.text
    print(name_main_page.text)
    print(regular_price_main_page.text)
    print(campaign_price_main_page.text)
    regular_price_color_mp = regular_price_main_page.value_of_css_property('color')
    print(regular_price_color_mp)
    if browser_name == "chrome":
        print(regular_price_color_mp.replace('rgba(', '').replace(')', '').split(',')[:3])
        R = regular_price_color_mp.replace('rgba(', '').replace(')', '').split(',')[:3][0].strip()
        G =  regular_price_color_mp.replace('rgba(', '').replace(')', '').split(',')[:3][1].strip()
        B = regular_price_color_mp.replace('rgba(', '').replace(')', '').split(',')[:3][2].strip()
        assert R == G == B
    elif browser_name == "firefox":
        print(regular_price_color_mp.replace('rgb(', '').replace(')', '').split(',')[:3])
        R = regular_price_color_mp.replace('rgb(', '').replace(')', '').split(',')[:3][0].strip()
        G = regular_price_color_mp.replace('rgb(', '').replace(')', '').split(',')[:3][1].strip()
        B = regular_price_color_mp.replace('rgb(', '').replace(')', '').split(',')[:3][2].strip()
        assert R == G == B
    regular_price_color_style_mp = regular_price_main_page.value_of_css_property('text-decoration-line')
    assert regular_price_color_style_mp == 'line-through'
    print(regular_price_color_style_mp)
    compaingn_price_color_mp = campaign_price_main_page.value_of_css_property('color')
    if browser_name == "chrome":
        print(compaingn_price_color_mp.replace('rgba(', '').replace(')', '').split(',')[:3])
        G = compaingn_price_color_mp.replace('rgba(', '').replace(')', '').split(',')[:3][1].strip()
        B = compaingn_price_color_mp.replace('rgba(', '').replace(')', '').split(',')[:3][2].strip()
        assert G == B == '0'
    elif browser_name == "firefox":
        print(compaingn_price_color_mp.replace('rgb(', '').replace(')', '').split(',')[:3])
        G = compaingn_price_color_mp.replace('rgb(', '').replace(')', '').split(',')[:3][1].strip()
        B = compaingn_price_color_mp.replace('rgba', '').replace(')', '').split(',')[:3][2].strip()
        assert G == B == '0'
    compaingn_price_font_weight_mp = campaign_price_main_page.value_of_css_property('font-weight')
    print(compaingn_price_font_weight_mp)
    if browser_name == "chrome":
        print(compaingn_price_font_weight_mp)
        assert compaingn_price_font_weight_mp == '700'
    elif browser_name == "firefox":
        print(compaingn_price_font_weight_mp)
        assert compaingn_price_font_weight_mp == '900'
    regular_price_font_size_mp = float(regular_price_main_page.value_of_css_property('font-size').rstrip('px'))
    compaingn_price_font_size_mp = float(campaign_price_main_page.value_of_css_property('font-size').rstrip('px'))
    print(regular_price_font_size_mp)
    print(compaingn_price_font_size_mp)
    assert compaingn_price_font_size_mp > regular_price_font_size_mp
    name_main_page.click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     NAME_PROGUCT_PAGE)))
    name_product_page = driver.find_element(By.CSS_SELECTOR, NAME_PROGUCT_PAGE)
    name_product_page_text = name_product_page.text
    assert name_main_page_text == name_product_page_text
    regular_price_product_page = driver.find_element(By.CSS_SELECTOR, REGULAR_PRICE_PRODUCT_PAGE)
    regular_price_product_page_text = regular_price_product_page.text
    assert regular_price_main_page_text == regular_price_product_page_text
    compaign_price_product_page = driver.find_element(By.CSS_SELECTOR, CAMPAIGN_PRICE_PRODUCT_PAGE)
    compaign_price_product_page_text = compaign_price_product_page.text
    assert campaign_price_main_page_text == compaign_price_product_page_text
    regular_price_color_pp = regular_price_product_page.value_of_css_property('color')
    if browser_name == "chrome":
        print(regular_price_color_pp.replace('rgba(', '').replace(')', '').split(',')[:3])
        R = regular_price_color_pp.replace('rgba(', '').replace(')', '').split(',')[:3][0].strip()
        G = regular_price_color_pp.replace('rgba(', '').replace(')', '').split(',')[:3][1].strip()
        B = regular_price_color_pp.replace('rgba(', '').replace(')', '').split(',')[:3][2].strip()
        assert R == G == B
    elif browser_name == "firefox":
        print(regular_price_color_pp.replace('rgb(', '').replace(')', '').split(',')[:3])
        R = regular_price_color_pp.replace('rgb(', '').replace(')', '').split(',')[:3][0].strip()
        G = regular_price_color_pp.replace('rgb(', '').replace(')', '').split(',')[:3][1].strip()
        B = regular_price_color_pp.replace('rgb(', '').replace(')', '').split(',')[:3][2].strip()
        assert R == G == B
    regular_price_color_style_pp = regular_price_product_page.value_of_css_property('text-decoration-line')
    assert regular_price_color_style_pp == 'line-through'
    compaign_price_product_page = driver.find_element(By.CSS_SELECTOR, CAMPAIGN_PRICE_PRODUCT_PAGE)
    compaingn_price_color_pp = compaign_price_product_page.value_of_css_property('color')
    if browser_name == "chrome":
        print(compaingn_price_color_pp.replace('rgba(', '').replace(')', '').split(',')[:3])
        G = compaingn_price_color_pp.replace('rgba(', '').replace(')', '').split(',')[:3][1].strip()
        B = compaingn_price_color_pp.replace('rgba(', '').replace(')', '').split(',')[:3][2].strip()
        assert G == B == '0'
    elif browser_name == "firefox":
        print(compaingn_price_color_pp.replace('rgb(', '').replace(')', '').split(',')[:3])
        G = compaingn_price_color_pp.replace('rgb(', '').replace(')', '').split(',')[:3][1].strip()
        B = compaingn_price_color_pp.replace('rgb(', '').replace(')', '').split(',')[:3][2].strip()
        assert G == B == '0'
    compaingn_price_font_weight_pp = compaign_price_product_page.value_of_css_property('font-weight')
    print(compaingn_price_font_weight_pp)
    if browser_name == "chrome":
        print(compaingn_price_font_weight_pp)
        assert compaingn_price_font_weight_pp == '700'
    elif browser_name == "firefox":
        print(compaingn_price_font_weight_pp)
        assert compaingn_price_font_weight_pp == '700'
    regular_price_font_size_pp = float(regular_price_product_page.value_of_css_property('font-size').rstrip('px'))
    compaingn_price_font_size_pp = float(compaign_price_product_page.value_of_css_property('font-size').rstrip('px'))
    print(regular_price_font_size_pp)
    print(compaingn_price_font_size_pp)
    assert compaingn_price_font_size_pp > regular_price_font_size_pp













