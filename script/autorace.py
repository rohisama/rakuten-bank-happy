import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from rakuten_settings import *

class Autorace:
    @classmethod
    def login(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")

        #driver = webdriver.Chrome()
        cls.driver = webdriver.Chrome(options=options)

        # Open Rakuten-keiba web page
        cls.driver.get('https://pc.autoinet.jp/')
        time.sleep(1)

        # Inpit user name and Password 
        cls.driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[1]/div/table/tbody/tr/td/form/table/tbody/tr[1]/td/input').send_keys(AUTORACE_ID)
        cls.driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[1]/div/table/tbody/tr/td/form/table/tbody/tr[2]/td/input').send_keys(AUTORACE_PW)

        # Click "login" button
        cls.driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[1]/div/table/tbody/tr/td/form/div/input[1]').click()
        time.sleep(1)

        # Input PIN
        cls.driver.find_element_by_xpath('/html/body/form[1]/div[1]/table/tbody/tr[2]/td/input[3]').send_keys(AUTORACE＿PIN)

    @classmethod
    def depositting(cls):
        try:
            cls.login()

            # Click depositting
            cls.driver.find_element_by_xpath('/html/body/form[1]/div[3]/table/tbody/tr/td[1]/input').click()
            time.sleep(1)

            # Input depositting price
            cls.driver.find_element_by_xpath('/html/body/form/div[1]/table/tbody/tr/td/input').send_keys('1')
            cls.driver.find_element_by_xpath('/html/body/form/div[2]/input').click()

            time.sleep(2)
            Alert(cls.driver).accept()
            time.sleep(2)

        except:
            print("Error!!")

        cls.driver.save_screenshot('autorace_depo_result.png')
        cls.driver.quit()

    @classmethod
    def withdrawal(cls):
        try:
            cls.login()
            # Click out
            cls.driver.find_element_by_xpath('/html/body/form[1]/div[3]/table/tbody/tr/td[2]/input').click()
            time.sleep(1)

            # get price
            price = cls.driver.find_element_by_xpath('/html/body/form/div[3]/center/table/tbody/tr[2]/td/font').get_attribute("textContent")
            print(price)

            num = re.sub(r"\D", "", price)
            print(num)

            # Input output price
            cls.driver.find_element_by_xpath('/html/body/form/div[1]/table/tbody/tr/td/input').send_keys(num)
            cls.driver.find_element_by_xpath('/html/body/form/div[2]/input').click()

            time.sleep(2)
            Alert(cls.driver).accept()
            time.sleep(2)

        except:
            print("Error!!")

        cls.driver.save_screenshot('autorace_withdrawal_result.png')
        cls.driver.quit()

if __name__ == "__main__":
    Autorace.depositting()