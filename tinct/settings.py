import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

HUE_BRIDGE_IP = os.environ.get("HUE_BRIDGE_IP")
HUE_USERNAME = os.environ.get("HUE_USERNAME")
