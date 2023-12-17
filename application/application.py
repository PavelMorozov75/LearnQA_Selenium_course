from pages_adding_product.mainpage import MainPage
from pages_adding_product.productpage import ProductPage
from pages_adding_product.cardpage import CardPage
from selenium import webdriver

class Application():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.card_page = CardPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_product_to_card(self, count=3):
        self.main_page.open_mainpage()
        self.main_page.check_maipage_is_opend()
        attempt = 1
        while attempt <= count:
            self.main_page.click_on_first_product()
            self.product_page.weit_until_page_load()
            self.product_page.check_and_set_select()
            # if self.product_page.check_product_has_select():
            #     self.product_page.set_select()
            self.product_page.press_add_to_card_button()
            self.product_page.weit_change_count_priduct_in_cart()
            self.main_page.open_mainpage()
            self.main_page.check_maipage_is_opend()
            attempt += 1


    def get_count_product_in_card(self):
        return self.main_page.get_count_products_in_card()

    def delete_products_from_card(self):
        self.main_page.go_to_cardpage()
        self.card_page.weit_is_opend()
        self.card_page.click_on_firs_product_in_card()
        self.card_page.delete_all_products()
        self.main_page.open_mainpage()



