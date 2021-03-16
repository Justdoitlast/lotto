import numpy as np
import random
import math
import schedule
import time
import datetime
import requests

#!/usr/local/bin/python
# -- coding: utf-8 --

import requests

def send_lotto2():
    url = 'https://notify-api.line.me/api/notify'
    token = "sAYp5lGYaFRXn6JoE3hBHMmuYu2IRiOSsyKOgWvNwAX"
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

    msg = digit2lotto_()

    r = requests.post(url, headers=headers , data = {'message':msg})
def send_lotto6():
    url = 'https://notify-api.line.me/api/notify'
    token = "sAYp5lGYaFRXn6JoE3hBHMmuYu2IRiOSsyKOgWvNwAX"
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

    msg = digit6lotto_()

    r = requests.post(url, headers=headers , data = {'message':msg})


def digit2lotto_():
    lotto = ''
    for _ in range(2):
        lotto += str(random.randint(0,9))
    get_lotto = 'เลขท้าย 2 ตัว : %s' %lotto
    return get_lotto

def digit6lotto_():
    lottery = ''
    for _ in range(6):
        lottery += str(random.randint(0,9))
    get_lotto= 'รางวัลที่ 1 : %s' %lottery
    return get_lotto

# schedule.every(5).seconds.do(job)

schedule.every().days.at("12:40").do(send_lotto2)
schedule.every().days.at("12:41").do(send_lotto6)

while True:
    schedule.run_pending()
    time.sleep(1)