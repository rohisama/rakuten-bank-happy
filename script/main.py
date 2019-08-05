import time
from rakuten_keiba import RakutenKeiba
from chariloto import Chariloto
from autorace import Autorace
from oddspark import Oddspark
from boatrace import Boatrace
from spat4 import Spat4
from e_shinbun_bet import EShinbunBet
from keirin import Keirin

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


print("start depositting")
depositting()
time.sleep(600)
print("start withdrawal")
withdrawal()

