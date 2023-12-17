from selenium.webdriver.common.by import By
class MainPage:

    mainpage_url = "http://localhost/litecart/en/"
    ITEMS = (By.CSS_SELECTOR, ".products .product")
    HOME = (By.XPATH, "//a[contains(text(), 'Home')]")
    SELECT = (By.XPATH, "//select[@name]")
    SELECT_ITEMS = (By.CSS_SELECTOR, "select[name] option[value]")
    BUTTON_ADD = (By.XPATH, "//button[contains(text(), 'Add To Cart')]")
    COUNTER = (By.CSS_SELECTOR, "span.quantity")
    CHECKOUT = (By.XPATH, "//a[contains(text(), 'Checkout »')]")

    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(driver, 10)

    def open_mainpage(self):
        self.driver.get(MainPage.mainpage_url)
        return self
    def click_on_first_product(self):
        self.driver.find_elements(*MainPage.ITEMS)[0].click()
    def get_count_products_in_card(self):
        return int(self.driver.find_element(*MainPage.COUNTER).get_attribute('textContent'))

    def check_maipage_is_opend(self):
        assert self.driver.current_url == MainPage.mainpage_url, f"не открылась главная страница"

    def go_to_cardpage(self):
        self.driver.find_element(*MainPage.CHECKOUT).click()




