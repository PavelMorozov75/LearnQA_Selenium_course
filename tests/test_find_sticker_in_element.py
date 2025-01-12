from selenium.webdriver.common.by import By

url = 'http://localhost/litecart/en/'
CARDS = 'ul.listing-wrapper li'
CARDS1 = '.product'
STICKER = 'ul.listing-wrapper li .sticker'
STICKER1 = '.sticker'

def test_stickers(driver):
    driver.get(url)
    cards = driver.find_elements(By.CSS_SELECTOR, CARDS1)
    print(len(cards))
    numer = 1
    stickers_count = 0
    for card in cards:
        stickers = card.find_elements(By.CSS_SELECTOR, STICKER1)
        print(stickers)
        if stickers:
            stickers_count+= 1
    print(stickers_count)

        # assert len(stickers) == 1, f"в карточке {numer} : {len(stickers)} стикер(ов) "
        # numer += 1