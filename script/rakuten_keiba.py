import time
import chromedriver_binary
from selenium import webdriver

from rakuten_settings import *

class RakutenKeiba:
    @classmethod
    def depositting(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")

        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

        # Open Rakuten-keiba web page
        driver.get('https://keiba.rakuten.co.jp/')

        try:
            # Click "depositting" button
            driver.find_element_by_id('noBalanceStatus').click()

            # Waiting for open the new tab page
            time.sleep(20)

            # Change tab
            handle_array = driver.window_handles
            driver.switch_to.window(handle_array[1])

            # Inpit user name and Password 
            driver.find_element_by_id('loginInner_u').send_keys(RAKUTEN_ID)
            driver.find_element_by_id('loginInner_p').send_keys(RAKUTEN_PW)

            # Click "login" button
            driver.find_element_by_css_selector('#loginInner > p:nth-child(3) > input').click()

            # Input depositting price
            driver.find_element_by_id('depositingInputPrice').send_keys('100')
            driver.find_element_by_id('depositingInputButton').click()

            # Input PIN
            driver.find_element_by_css_selector('#depositingConfirmForm > div > table:nth-child(3) > tbody > tr > td > div.inputArea > input.tealeaf_masking.definedNumber').send_keys(RAKUTEN_PIN)
            driver.find_element_by_id('depositingConfirmButton').click()

        except:
            print("Error!!")

        driver.save_screenshot('rakutekeiba_results.png')

        driver.quit()

if __name__ == "__main__":
    RakutenKeiba.depositting()