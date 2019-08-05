import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from rakuten_settings import *
from happy import Happy

PAGEURL = "https://www.spat4.jp/keiba/pc"

class Spat4(Happy):
    @classmethod
    def login(cls):
        cls.open_page(PAGEURL)

        # Fill auth information
        cls.driver.find_element_by_id('MEMBERNUMR').send_keys(SPAT4_SUBSCRIBER_ID)
        cls.driver.find_element_by_id('MEMBERIDR').send_keys(SPAT4_USER_ID)
        cls.driver.find_element_by_xpath('/html/body/div/div[1]/form/a/span/div').click()
        cls.sleep()
        try:
            cls.driver.find_element_by_id('goKaisai').click()
            cls.sleep()
        except:
            print('skip page')
            pass

    @classmethod
    def depositting(cls):
        try:
            cls.login()

            # Click depositting button
            cls.driver.find_element_by_xpath('/html/body/form/div/div[2]/div/ul/li[4]/input').click()
            cls.sleep()
            
            # Change window
            handle_array = cls.driver.window_handles
            cls.driver.switch_to.window(handle_array[1])

            # Input depositting price
            cls.driver.find_element_by_id('ENTERR').send_keys("100")
            cls.driver.find_element_by_xpath('//*[@id="nyukinForm"]/div/input').click()
            cls.sleep()

            # Fill PIN and execute
            cls.driver.find_element_by_id('MEMBERPASSR').send_keys(SPAT4_PIN)
            cls.driver.find_element_by_name('EXEC').click()

        except:
            print("Error!!")

        cls.save_screenshot('result/spat4_depo_result.png')
        cls.driver.quit()

    @classmethod
    def withdrawal(cls):
        try:
            cls.login()

            # Click withdrawal button
            cls.driver.find_element_by_xpath('/html/body/form/div/div[2]/div/ul/li[5]/input').click()
            cls.sleep()

            cls.driver.find_element_by_xpath('//*[@id="seisanForm"]/div/input').click()
            cls.sleep()

            # Fill PIN and execute
            cls.driver.find_element_by_id('MEMBERPASSR').send_keys(SPAT4_PIN)
            cls.driver.find_element_by_name('EXEC').click()

        except:
            print("Error!!")

        cls.save_screenshot('result/spat4_withdrawal_result.png')
        cls.driver.quit()

if __name__ == "__main__":
    Spat4.depositting()