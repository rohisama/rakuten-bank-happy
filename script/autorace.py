import time
import chromedriver_binary
import re
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from rakuten_settings import *
from happy import Happy

PAGEURL = "https://pc.autoinet.jp/"

class Autorace(Happy):
    @classmethod
    def login(cls):
        cls.open_page(PAGEURL)

        # Inpit user name and Password 
        cls.driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[1]/div/table/tbody/tr/td/form/table/tbody/tr[1]/td/input').send_keys(AUTORACE_ID)
        cls.driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[1]/div/table/tbody/tr/td/form/table/tbody/tr[2]/td/input').send_keys(AUTORACE_PW)

        # Click "login" button
        cls.driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[1]/div/table/tbody/tr/td/form/div/input[1]').click()
        cls.sleep()

        # Input PIN
        cls.driver.find_element_by_xpath('/html/body/form[1]/div[1]/table/tbody/tr[2]/td/input[3]').send_keys(AUTORACE＿PIN)

    @classmethod
    def depositting(cls):
        try:
            cls.login()

            # Click depositting
            cls.driver.find_element_by_xpath('/html/body/form[1]/div[3]/table/tbody/tr/td[1]/input').click()
            cls.sleep()

            # Input depositting price
            cls.driver.find_element_by_xpath('/html/body/form/div[1]/table/tbody/tr/td/input').send_keys('1')
            cls.driver.find_element_by_xpath('/html/body/form/div[2]/input').click()

            cls.sleep()
            Alert(cls.driver).accept()
            cls.sleep()

        except:
            f_path = "result/autorace_depo_error.png"
            cls.save_screenshot(f_path)
            cls.report_to_slack("error!", f_path)

        cls.save_screenshot('result/autorace_depo_result.png')
        cls.driver.quit()

    @classmethod
    def withdrawal(cls):
        try:
            cls.login()
            # Click out
            cls.driver.find_element_by_xpath('/html/body/form[1]/div[3]/table/tbody/tr/td[2]/input').click()
            cls.sleep()

            # get price
            price = cls.driver.find_element_by_xpath('/html/body/form/div[3]/center/table/tbody/tr[2]/td/font').get_attribute("textContent")
            print(price)

            num = re.sub(r"\D", "", price)
            print(num)

            # Input output price
            cls.driver.find_element_by_xpath('/html/body/form/div[1]/table/tbody/tr/td/input').send_keys(num)
            cls.driver.find_element_by_xpath('/html/body/form/div[2]/input').click()

            cls.sleep()
            Alert(cls.driver).accept()
            cls.sleep()
        except:
            f_path = "result/autorace_withdrawal_error.png"
            cls.save_screenshot(f_path)
            cls.report_to_slack("error!", f_path)

        cls.save_screenshot('result/autorace_withdrawal_result.png')
        cls.driver.quit()

if __name__ == "__main__":
    Autorace.depositting()