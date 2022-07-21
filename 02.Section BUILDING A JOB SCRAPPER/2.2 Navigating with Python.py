# 2.2 Navigating with Python

# requests => python 요청을 만드는 기능을 모아둔 싸이트

# python urllib => 파이선에서 기본적으로 제공하는 urls 정보 추출 (import urllib)

import os
import requests


def finishgame():
  print("Do you wnat to start over? y/n")
  continued = input()
  if continued == 'y':
    os.system('clear')
    startgame()
  elif continued == 'n':
    print('anonymous bye!')
  else:
    print("That's not a valid answer")
    finishgame()


def startgame():
  print("Welcom to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")
  urls = input()
  if urls == '':
    print('please write url')
    startgame()
  else:
    url = urls.split(',')
    for el in url:
      try: 
        if 'https://' not in el:
          el = 'https://' + el.strip()
          result = requests.get(el)
          res_code = result.status_code
          
          if int(res_code) == 200:
            print(el + " is UP!")
      except: 
        print(el + " is DOWN!")
  finishgame()

startgame()

