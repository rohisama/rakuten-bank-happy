import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from rakuten_settings import *
from happy import Happy

PAGEURL = "https://bet.e-shinbun.net/"

class EShinbunBet(Happy):
    @classmethod
    def login(cls):
        cls.open_page(PAGEURL)

        # Click login button
        cls.driver.find_element_by_xpath('//*[@id="hd-main"]/div[1]/div/ul/li[3]/a/img').click()
        cls.sleep()

        # Click "login as Rakuten user" button
        cls.driver.find_element_by_xpath('//*[@id="main_l"]/div[4]/div[2]/div/form/input[6]').click()
        cls.sleep()

        # Fill username and password
        cls.driver.find_element_by_xpath('//*[@id="loginInner_u"]').send_keys(RAKUTEN_ID)
        cls.driver.find_element_by_xpath('//*[@id="loginInner_p"]').send_keys(RAKUTEN_PW)

        cls.driver.find_element_by_xpath('//*[@id="loginInner"]/p[1]/input').click()
        cls.sleep()

        # Skip information window
        cls.driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td/dl/dd/div/a/img').click()
        cls.sleep()

    @classmethod
    def depositting(cls):
        try:
            cls.login()
            
            # Click depositting button
            cls.driver.find_element_by_xpath('//*[@id="racenav"]/div/p[2]/a/img').click()
            cls.sleep()

            # Input depositting price and execute
            cls.driver.find_element_by_id('StatementAmount').send_keys('100')
            cls.driver.find_element_by_id('StatementNotice0').click()
            cls.driver.find_element_by_xpath('//*[@id="conf"]/p[1]/a').click()
            cls.sleep()

            # Fill PIN and execute
            cls.driver.find_element_by_id('UserPassword').send_keys(ESHINBUN_PIN)
            cls.driver.find_element_by_xpath('//*[@id="conf"]/p/a[1]').click()

        except:
            print("Error!!")

        cls.save_screenshot('result/eshinbun_depo_result.png')
        cls.driver.quit()

    @classmethod
    def withdrawal(cls):
        pass
if __name__ == "__main__":
    EShinbunBet.depositting()