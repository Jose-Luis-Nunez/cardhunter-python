import undetected_chromedriver as uc
from selenium_stealth import stealth
import time


def search_card():
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.140 Safari/537.36")
    driver = uc.Chrome(options=options)

    stealth(driver,
            languages=["de-DE", "de"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True)

    driver.get('https://www.cardmarket.com/de/Pokemon')
    time.sleep(15)
    driver.save_screenshot('screenshot.png')
    time.sleep(2)
    driver.quit()


search_card()
