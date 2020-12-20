import time
import os

import requests


URL = os.environ['URL']

while True:
  r = requests.get(URL)
  print(r.text)
  time.sleep(60)
