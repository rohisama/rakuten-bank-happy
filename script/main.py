import time
from rakuten_keiba import RakutenKeiba
from autorace import Autorace


def depositting():
    RakutenKeiba.depositting()
    Autorace.depositting()


def withdrawal():
    Autorace.withdrawal()


print("start depositting")
depositting()
time.sleep(10)
print("start withdrawal")
withdrawal()

