import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from rakuten_settings import *

class Boatrace:

    URL = "https://ib.mbrace.or.jp/"
    @classmethod
    def login(cls):
        pass

    @classmethod
    def depositting(cls):
        try:
            cls.login()
            pass

        except:
            print("Error!!")

    @classmethod
    def withdrawal(cls):
        try:
            cls.login()
            pass
        except:
            print("Error!!")

if __name__ == "__main__":
    pass