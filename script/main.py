import time
from rakuten_keiba import RakutenKeiba
from chariloto import Chariloto
from autorace import Autorace
from oddspark import Oddspark
from boatrace import Boatrace

def depositting():
    RakutenKeiba.depositting()
    Autorace.depositting()
    Chariloto.depositting()
    Oddspark.depositting()
    Boatrace.depositting()


def withdrawal():
    Autorace.withdrawal()
    Chariloto.withdrawal()
    Oddspark.withdrawal()
    Boatrace.withdrawal()
    


print("start depositting")
depositting()
time.sleep(600)
print("start withdrawal")
withdrawal()

