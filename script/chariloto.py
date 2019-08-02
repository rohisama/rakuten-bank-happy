import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from rakuten_settings import *
from random import uniform
from happy import Happy

PAGEURL = "https://www.chariloto.com/"

class Chariloto(Happy):
    @classmethod
    def login(cls):
        cls.open_page(PAGEURL)

        # Inpit user name and Password 
        cls.driver.find_element_by_id('chariloto_id').send_keys(CHARILOTO_ID)
        cls.driver.find_element_by_id('password').send_keys(CHARILOTO_PW)

        # Click "login" button
        cls.driver.find_element_by_xpath('//*[@id="body"]/div[4]/div[1]/div[1]/div[2]/form/button').click()
        cls.sleep()


    @classmethod
    def depositting(cls):
        try:
            # Login
            cls.login()

            # Click depositting button
            cls.driver.find_element_by_xpath('//*[@id="body"]/div[3]/div/div[2]/div[2]/a[3]').click()
            cls.sleep()

            # Input depositting price
            cls.driver.find_element_by_xpath('//*[@id="js-input"]').send_keys("100")

            # Click depositting button
            cls.driver.find_element_by_xpath('//*[@id="new_mypage_bank_statement_deposit_form"]/div/input').click()
            cls.sleep()

            # Input PIN
            cls.driver.find_element_by_xpath('//*[@id="mypage_bank_statement_deposit_form_pincode"]').send_keys(CHARILOTO_PIN)
            cls.sleep()

            # Clicke execute button
            cls.driver.find_element_by_xpath('//*[@id="new_mypage_bank_statement_deposit_form"]/div/input[2]').click()


        except:
            print("Error!!")

        cls.save_screenshot('result/cariloto_depo_result.png')
        cls.driver.quit()

    @classmethod
    def withdrawal(cls):
        try:
            # Login
            cls.login()

            # Click mypage button
            cls.driver.find_element_by_xpath('//*[@id="body"]/div[3]/div/div[2]/div[2]/a[1]').click()
            cls.sleep()

            # Click withdrawal
            cls.driver.find_element_by_xpath('//*[@id="body"]/div[3]/div[2]/section/div[2]/div/ul/li[3]/a').click()
            cls.sleep()

            # Input PIN
            cls.driver.find_element_by_xpath('//*[@id="mypage_bank_statement_withdrawal_form_pincode"]').send_keys(CHARILOTO_PIN)

            # Clicke execute button
            cls.driver.find_element_by_xpath('//*[@id="new_mypage_bank_statement_withdrawal_form"]/div/input').click()

            pass
        except:
            print("Error!!")

        cls.save_screenshot('result/cariloto_withdrawal_result.png')
        cls.driver.quit()

if __name__ == "__main__":
    Chariloto.withdrawal()