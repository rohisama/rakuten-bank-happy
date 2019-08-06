import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from rakuten_settings import *
from happy import Happy
#from selenium.common.exceptions import NoSuchElementException

PAGEURL="https://www.oddspark.com"

class Oddspark(Happy):
    @classmethod
    def login(cls):
        cls.open_page(PAGEURL)

        # Click depositting/withdrawal button
        cls.driver.find_element_by_xpath('//*[@id="nav2"]/li[6]/a').click()
        cls.sleep()

        # Change window
        handle_array = cls.driver.window_handles
        cls.driver.switch_to.window(handle_array[1])

        # Fill ID & PW
        cls.driver.find_element_by_name('SSO_ACCOUNTID').send_keys(ODDSPARK_ID)
        cls.driver.find_element_by_name('SSO_PASSWORD').send_keys(ODDSPARK_PW)
        cls.sleep()

        # Click login button
        cls.driver.find_element_by_id('btn-login').click()
        cls.sleep()

        try:
            # If the PIN requested, fill it
            cls.driver.find_element_by_name('INPUT_PIN').send_keys(ODDSPARK_PIN)
            cls.driver.find_element_by_xpath('//*[@id="contentS"]/form/div/input').click()
            cls.sleep()
        except:
            print('no pin')
            pass

        try:
            print('close popup')
            cls.sleep()
            cls.driver.find_element_by_xpath('//*[@id="simplemodal-container"]/a').click()
            cls.sleep()      
        except:
            print('close popup error')
            pass
        

    @classmethod
    def depositting(cls):
        try:
            cls.login()
            
            # Click depositting
            cls.driver.find_element_by_xpath('//*[@id="rightAc2"]/ul[1]/li').click()
            cls.sleep()

            # Input depositting price
            cls.driver.find_element_by_name('nyukin').send_keys('1')
            cls.driver.find_element_by_xpath('//*[@id="confirm"]/li[2]/a').click()
            cls.sleep()

            # Fill the PIN
            cls.driver.find_element_by_id('touhyoPassword').send_keys(ODDSPARK_PIN)

            # Click execute button
            cls.driver.find_element_by_xpath('//*[@id="confirm"]/li[2]/a').click()
            cls.sleep()

        except:
            import traceback
            traceback.print_exc()

        cls.save_screenshot('result/oddspark_depo_result.png')
        cls.driver.quit()

    @classmethod
    def withdrawal(cls):
        try:
            cls.login()

            # Click withdrawal
            cls.driver.find_element_by_xpath('//*[@id="rightAc2"]/ul[2]/li/a').click()
            cls.sleep()

            # Fill the PIN
            cls.driver.find_element_by_id('touhyoPassword').send_keys(ODDSPARK_PIN)
            # Click execute button
            cls.driver.find_element_by_xpath('//*[@id="confirm"]/li[2]/a').click()
            cls.sleep()

        except:
            import traceback
            traceback.print_exc()

        cls.save_screenshot('result/oddspark_withdrawal_result.png')
        cls.driver.quit()

if __name__ == "__main__":
    Oddspark.depositting()