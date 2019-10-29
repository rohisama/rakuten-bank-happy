import time
import os
from rakuten_keiba import RakutenKeiba
from chariloto import Chariloto
from autorace import Autorace
from oddspark import Oddspark
from boatrace import Boatrace
from spat4 import Spat4
from e_shinbun_bet import EShinbunBet
from keirin import Keirin
from slackbot.slackclient import SlackClient
from slackbot_settings import *

slack_client = None

def depositting():
    RakutenKeiba.depositting()
    Autorace.depositting()
    Chariloto.depositting()
    Oddspark.depositting()
    Boatrace.depositting()
    Spat4.depositting()
    EShinbunBet.depositting()
    Keirin.depositting()


def withdrawal():
    Autorace.withdrawal()
    Chariloto.withdrawal()
    Oddspark.withdrawal()
    Boatrace.withdrawal()
    Spat4.withdrawal()
    EShinbunBet.withdrawal()
    Keirin.withdrawal()

def send_message_to_slack(msg):
    try:
        slack_client = get_slack_client()
        time.sleep(5)
        slack_client.rtm_send_message(SLACK_CHANNEL, msg)
    except:
        print("error")
        pass

def get_slack_client():
    return SlackClient(API_TOKEN) if slack_client is None else slack_client

print("start depositting")
send_message_to_slack("start rakuten-bank automation")
depositting()
time.sleep(600)
print("start withdrawal")
withdrawal()
send_message_to_slack("finish rakuten-bank automation")
