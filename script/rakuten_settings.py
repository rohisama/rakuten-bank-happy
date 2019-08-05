import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

RAKUTEN_ID = os.environ.get("RAKUTEN_ID")
RAKUTEN_PW = os.environ.get("RAKUTEN_PW")
RAKUTEN_PIN = os.environ.get("RAKUTEN_PIN")

AUTORACE_ID = os.environ.get("AUTORACE_ID")
AUTORACE_PW = os.environ.get("AUTORACE_PW")
AUTORACE_PIN = os.environ.get("AUTORACE_PIN")

ODDSPARK_ID = os.environ.get("ODDSPARK_ID")
ODDSPARK_PW = os.environ.get("ODDSPARK_PW")
ODDSPARK_PIN = os.environ.get("ODDSPARK_PIN")

KEIRIN_ID = os.environ.get("KEIRIN_ID")
KEIRIN_PW = os.environ.get("KEIRIN_PW")
KEIRIN_PIN = os.environ.get("KEIRIN_PIN")

CHARILOTO_ID = os.environ.get("CHARILOTO_ID")
CHARILOTO_PW = os.environ.get("CHARILOTO_PW")
CHARILOTO_PIN = os.environ.get("CHARILOTO_PIN")

ESHINBUN_PIN = os.environ.get("ESHINBUN_PIN")

BOATRACE_ID = os.environ.get("BOATRACE_ID")
BOATRACE_PW = os.environ.get("BOATRACE_PW")
BOATRACE_VOTE_PW = os.environ.get("BOATRACE_VOTE_PW")
BOATRACE_PIN = os.environ.get("BOATRACE_PIN")

SPAT4_SUBSCRIBER_ID = os.environ.get("SPAT4_SUBSCRIBER_ID")
SPAT4_USER_ID = os.environ.get("SPAT4_USER_ID")
SPAT4_PIN = os.environ.get("SPAT4_PIN")
