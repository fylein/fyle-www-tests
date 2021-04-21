import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get_hub_url():
  return os.environ.get('HUB_URL')