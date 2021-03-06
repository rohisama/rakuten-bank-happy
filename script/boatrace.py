import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from rakuten_settings import *
from happy import Happy

PAGEURL = "https://ib.mbrace.or.jp/"

class Boatrace(Happy):

    @classmethod
    def login(cls):
        cls.open_page(PAGEURL)

        # Input auth information
        cls.driver.find_element_by_id('memberNo').send_keys(BOATRACE_ID)
        cls.driver.find_element_by_id('pin').send_keys(BOATRACE_PIN)
        cls.driver.find_element_by_id('authPassword').send_keys(BOATRACE_PW)

        # Click login button
        cls.driver.find_element_by_id('loginButton').click()
        cls.sleep()

        # Change window
        handle_array = cls.driver.window_handles
        cls.driver.switch_to.window(handle_array[1])

        # When information pop-up is displayed, close it
        if (len(cls.driver.find_elements(value='newsoverviewDisp')) != 0):
            cls.driver.find_element_by_id('isAllread').click()
            cls.driver.find_element_by_id('newsoverviewdispCloseButton').click()
        else:
            print("continue")
            


    @classmethod
    def depositting(cls):
        try:
            cls.login()

            # Click depositting button
            cls.driver.find_element_by_id('gnavi01').click()
            cls.sleep()
            cls.driver.find_element_by_id('charge').click()
            cls.sleep()
            
            # Input depositting price
            cls.driver.find_element_by_id('chargeInstructAmt').send_keys("1")

            # Input auth password
            cls.driver.find_element_by_id('chargeBetPassword').send_keys(BOATRACE_VOTE_PW)

            # Click execute button
            cls.driver.find_element_by_id('executeCharge').click()
            cls.sleep()

            # Click ok
            cls.driver.find_element_by_id('ok').click()
            cls.sleep()

        except:
            f_path = "result/boatrace_depo_error.png"
            cls.save_screenshot(f_path)
            cls.report_to_slack("error!", f_path)
        
        cls.save_screenshot('result/boatrace_depo_result.png')
        cls.driver.quit()

    @classmethod
    def withdrawal(cls):
        try:
            cls.login()    

            # Click withdrawal button
            cls.driver.find_element_by_id('gnavi01').click()
            cls.sleep()
            cls.driver.find_element_by_id('account').click()
            cls.sleep()

            # Input auth password
            cls.driver.find_element_by_id('accountBetPassword').send_keys(BOATRACE_VOTE_PW)

            # Click execute button
            cls.driver.find_element_by_id('executeAccount').click()
            cls.sleep()

            # Click ok
            cls.driver.find_element_by_id('ok').click()
            cls.sleep()

        except:
            f_path = "result/boatrace_withdrawal_error.png"
            cls.save_screenshot(f_path)
            cls.report_to_slack("error!", f_path)
        
        cls.save_screenshot('result/boatrace_withdrawal_result.png')
        cls.driver.quit()

if __name__ == "__main__":
    Boatrace.depositting()
    time.sleep(300)
    Boatrace.withdrawal()
