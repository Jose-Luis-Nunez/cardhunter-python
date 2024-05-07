import undetected_chromedriver as uc

import time


def search_card():
    driver = uc.Chrome(headless=True,use_subprocess=False)

    # options = uc.ChromeOptions()
    # options.headless = True
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--disable-gpu')
    #
    # driver = uc.Chrome(options=options)

    driver.get('https://www.cardmarket.com/de/Pokemon')

    time.sleep(4)
    driver.save_screenshot('screenshot.png')
    time.sleep(2)

    driver.quit()


search_card()
