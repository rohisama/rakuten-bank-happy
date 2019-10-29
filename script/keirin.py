import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from rakuten_settings import *
from happy import Happy

PAGEURL = "https://keirin.jp/pc/login"

class Keirin(Happy):
    @classmethod
    def login(cls):
        cls.open_page(PAGEURL)

        # Change window size
        cls.driver.set_window_size(1200, 1000)

        # Fill ID and Password
        cls.driver.find_element_by_id('txtnetVotingAutId').send_keys(KEIRIN_ID)
        cls.driver.find_element_by_id('txtnetVotingPass').send_keys(KEIRIN_PW)
        
        # Click login button
        cls.driver.execute_script("window.scrollTo(0, 300);")
        cls.driver.find_element_by_id('btnlogin').click()
        cls.sleep()

    @classmethod
    def depositting(cls):
        try:
            cls.login()
            
            # Sclool window
            cls.driver.execute_script("window.scrollTo(100, 500);")
            cls.driver.find_element_by_xpath('//*[@id="balance"]/table/tbody/tr/td[1]/button').click()
            cls.sleep()

            # Input depositting price and click button
            cls.driver.find_element_by_id('UNQ_orexpandText_12').send_keys('1')
            cls.driver.find_element_by_id('UNQ_orbutton_36').click()
            cls.sleep()

            # Fill the PIN and click execute button            
            cls.driver.find_element_by_id('UNQ_pfInputText_14').send_keys(KEIRIN_PIN)
            cls.driver.find_element_by_id('UNQ_orbutton_18').click()
            cls.sleep()

        except:
            f_path = "result/keirin_depo_error.png"
            cls.save_screenshot(f_path)
            cls.report_to_slack("error!", f_path)

        cls.save_screenshot('result/keirin_depo_result.png')
        cls.driver.quit()

    @classmethod
    def withdrawal(cls):
        try:
            cls.login()

            # Sclool window
            cls.driver.execute_script("window.scrollTo(100, 500);")
            cls.driver.find_element_by_xpath('//*[@id="balance"]/table/tbody/tr/td[3]/button').click()
            cls.sleep()

            # Click button
            cls.driver.execute_script("window.scrollTo(100, 500);")
            cls.driver.find_element_by_id('UNQ_orbutton_36').click()
            cls.sleep()

            # Fill the PIN and click execute button            
            cls.driver.find_element_by_id('UNQ_orexpandText_11').send_keys(KEIRIN_PIN)
            cls.driver.find_element_by_id('UNQ_orbutton_18').click()
            cls.sleep()

        except:
            f_path = "result/keirin_withdrawal_error.png"
            cls.save_screenshot(f_path)
            cls.report_to_slack("error!", f_path)

        cls.save_screenshot('result/keirin_withdrawal_result.png')
        cls.driver.quit()

if __name__ == "__main__":
    Keirin.depositting()