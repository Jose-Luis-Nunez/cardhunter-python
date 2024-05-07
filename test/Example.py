import undetected_chromedriver as uc

import time


def search_card():
    options = uc.ChromeOptions()

    driver = uc.Chrome(options=options)

    driver.get('https://www.cardmarket.com/de/Pokemon')

    time.sleep(4)
    driver.save_screenshot('screenshot.png')
    time.sleep(2)

    driver.quit()

search_card()
