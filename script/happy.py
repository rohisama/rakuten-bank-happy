from abc import *
from selenium import webdriver
import time
from random import uniform


class Happy(metaclass = ABCMeta):
    @classmethod
    @abstractmethod
    def login(cls):
        pass

    @classmethod
    @abstractmethod
    def depositting(cls):
        pass

    @classmethod
    @abstractmethod
    def withdrawal(cls):
        pass

    @classmethod
    def open_page(cls, url):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument('--lang=ja')

        cls.driver = webdriver.Chrome(options=options)
        #cls.driver = webdriver.Chrome()
        cls.driver.get(url)
        cls.driver.maximize_window()
        time.sleep(uniform(1, 10))

    @classmethod
    def save_screenshot(cls, path):
        page_width = cls.driver.execute_script('return document.body.scrollWidth')
        page_height = cls.driver.execute_script('return document.body.scrollHeight')
        cls.driver.set_window_size(page_width, page_height)
        time.sleep(2)
        cls.driver.save_screenshot(path)

    @classmethod
    def sleep(cls):
        time.sleep(uniform(1, 10))