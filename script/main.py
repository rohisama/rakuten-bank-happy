import time
from rakuten_keiba import RakutenKeiba
from chariloto import Chariloto
from autorace import Autorace

def depositting():
    RakutenKeiba.depositting()
    Autorace.depositting()
    Chariloto.depositting()


def withdrawal():
    Autorace.withdrawal()
    Chariloto.withdrawal()


print("start depositting")
depositting()
time.sleep(600)
print("start withdrawal")
withdrawal()

