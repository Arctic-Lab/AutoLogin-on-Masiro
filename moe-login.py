from urllib import response
# from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import random
import time

def work():
    # 请改成自己的账户名
    _name = "账户名" 
    # 请改成自己的密码
    _password = "密码"
    cnt = 0
    while(1):
        if(cnt > 3):
            break
        cnt = cnt+1
        # time.sleep(random.randint(1, 600))
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        session = requests.session()
        length1 = len(session.get("https://masiro.moe").content)
        url = "https://masiro.moe"
        soup = BeautifulSoup(session.get(url).content, "html.parser", from_encoding="utf-8")

        handlekey = str(soup.find('input', {'name':'handlekey'})['value'])
        
        input_data = {
            "fastloginfield": "username",
            "username" : _name,
            "password" : _password,
            "quickforward" : "yes",
            "handlekey" : handlekey
        }
        print(input_data)
        session.post("https://masiro.moe/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1", data=input_data)
        length = len(session.get("https://masiro.moe").content)
        print(length, "  ", length1)
        if(length > length1):
            print("Accepted")
            break
        else:
            print("Fail to login")

work()