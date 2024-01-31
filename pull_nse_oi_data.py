
#====== Importing Libraries ================
import os
import time
import json
import requests
from datetime import datetime

#====== script constants ===================

url = "https://www.nseindia.com/api/quote-derivative?symbol=NIFTY"

# url for bank nifty : "https://www.nseindia.com/api/quote-derivative?symbol=BANKNIFTY"

path = r"E:\Option chain\json\nifty50"  ## folder path where data will be saved

st = 918  # start time 
en = 1535  # end time

time_h = int(datetime.today().strftime(r"%H%M"))
time_sleep = 60  ## number of seconds between each data pull

#========== script functions ===============
def DATE_CALC():
    if ((datetime.today().strftime('%A')=="Saturday") or (datetime.today().strftime('%A')=="Sunday") ):
         exit()
    else:
        pass

def PULL_JSON_FILE(folderPath,url):
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
         'accept-language':'en-US,en;q=0.9,bn;q=0.8','accept-encoding':'gzip, deflate, br'}
    try:
        r=requests.get(url,headers=headers,timeout=30).json()
    except requests.exceptions.Timeout:
        print("Timed out")
    currentTime = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    fileLoc = os.path.join(str(folderPath),currentTime+'.json')
    json.dump( r, open( fileLoc, 'w' ) )
    print("file: ",fileLoc)
    return r

#============= main code =======================

DATE_CALC()

while time_h <= en:
  try:
    if time_h >= 918:
      currentTime = datetime.now().strftime("%H:%M:%S")
      print(currentTime)
      r = PULL_JSON_FILE(path,url)
      time_h = int(datetime.today().strftime(r"%H%M"))
      time.sleep(time_sleep)
    else:
      time_h = int(datetime.today().strftime(r"%H%M"))
      print(time_h)
      time.sleep(time_sleep)
  except:
    pass
      
