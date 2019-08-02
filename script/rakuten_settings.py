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

