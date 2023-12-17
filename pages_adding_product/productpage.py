from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime
from datetime import timedelta
from selenium.common.exceptions import TimeoutException
from pages_adding_product.mainpage import MainPage

class ProductPage(MainPage):


    HOME = (By.XPATH, "//a[contains(text(), 'Home')]")
    SELECT = (By.XPATH, "//select[@name]")
    SELECT_ITEMS = (By.CSS_SELECTOR, "select[name] option[value]")
    BUTTON_ADD = (By.XPATH, "//button[contains(text(), 'Add To Cart')]")

    '''def __int__(self, driver):
        self.driver = driver
        self.weit = WebDriverWait(driver, 2)'''

    '''def __init__(self, driver):
        super().__init__(self)
        self.driver = driver
        self.wait = WebDriverWait(driver, 2)'''

    def weit_until_page_load(self):
        WebDriverWait(self.driver, 2).until(lambda d: d.find_element(*ProductPage.HOME))

    def check_product_has_select(self):
        return len(self.driver.find_elements(*ProductPage.SELECT)) > 0
    def check_and_set_select(self):
        if self.check_product_has_select():
            self.driver.find_element(*ProductPage.SELECT).click()
            self.driver.find_elements(*ProductPage.SELECT_ITEMS)[1].click()
    def press_add_to_card_button(self):
        self.driver.find_element(*ProductPage.BUTTON_ADD).click()
    def weit_change_count_priduct_in_cart(self, timeout=1):
        cont_products_before = self.get_count_products_in_card()
        cont_products_after = cont_products_before
        stoptime = datetime.now() + timedelta(seconds=timeout)
        while cont_products_after == cont_products_before and datetime.now() <= stoptime:
            cont_products_after = self.get_count_products_in_card()
        if cont_products_before == cont_products_after:
            raise TimeoutException
        else:
            return True



