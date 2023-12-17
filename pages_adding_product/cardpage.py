from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class CardPage:


    CUSTOMER_DETAILS = (By.XPATH, "//h2[contains(text(), 'Customer Details')]")
    PRODUCTS_LINE = (By.CSS_SELECTOR, ".shortcuts li a")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "[name=remove_cart_item]")
    ITEM_IN_TABLE = (By.CSS_SELECTOR, "tr td.item")
    PRODUCT_NAME = (By.CSS_SELECTOR, "a >strong")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def weit_is_opend(self):
        self.wait.until(lambda d: d.find_element(*CardPage.CUSTOMER_DETAILS))

    def get_progucts_in_card(self):
        return self.driver.find_elements(*CardPage.PRODUCTS_LINE)

    def click_on_firs_product_in_card(self):
        if len(self.get_progucts_in_card()) > 0:
            self.get_progucts_in_card()[0].click()

    def delete_all_products(self):
        for i in range(len(self.get_progucts_in_card())):
            name = self.driver.find_element(*CardPage.PRODUCT_NAME).text
            elm_in_table = self.driver.find_element(By.XPATH, f"//tr/td[contains(text(), '{name}')]")
            self.driver.find_element(*CardPage.REMOVE_BUTTON).click()
            self.wait.until(expected_conditions.staleness_of(elm_in_table))



