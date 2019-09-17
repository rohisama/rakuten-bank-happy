import subprocess
import sys
import os
from abc import *
from selenium import webdriver
import time
from random import uniform
from slackbot.slackclient import SlackClient
from slackbot_settings import *
from slackbot.slackclient import SlackClient
from slackbot_settings import *

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
        try:
            page_width = cls.driver.execute_script('return document.body.scrollWidth')
            page_height = cls.driver.execute_script('return document.body.scrollHeight')
            cls.driver.set_window_size(page_width, page_height)
            time.sleep(2)
            cls.driver.save_screenshot(path)
        except:
            import traceback
            traceback.print_exc()

    @classmethod
    def sleep(cls):
        time.sleep(uniform(5, 15))

    @classmethod
    def image_to_text(cls, img_path):
        command = ["tesseract", img_path, "tmp"]

        subprocess.run(command)

        with open("tmp.txt", mode="r") as f:
            txt = f.readline()
 
        os.remove(img_path)
        os.remove("tmp.txt")
        return txt

    @classmethod
    def report_to_slack(cls, msg, file_path):
        try:
            slack_client = SlackClient(API_TOKEN)
            classname = cls.__class__.__name__
            slack_client.rtm_send_message(SLACK_CHANNEL, f"[{classname}] : {msg}")
            slack_client.upload_file(SLACK_CHANNEL, "image", file_path, None)
        except:
            pass

if __name__ == "__main__":
    img_path = "draw.jpg"
    print(Happy.image_to_text(img_path))