from urllib import response
# from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import random
import time

def work():
    # 请改成自己的账户名
    _name = "用户名" 
    # 请改成自己的密码
    _password = "密码"
    cnt = 0
    while(1):
        if(cnt > 3):
            break
        cnt = cnt+1
        time.sleep(random.randint(1, 600))
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        session = requests.session()
        length1 = len(session.get("https://masiro.me/admin").content)
        url = "https://masiro.me/admin/auth/login"
        # print(session.get(url).content)
        # print(session.get(url).content, file=MYFILE)
        soup = BeautifulSoup(session.get(url).content, "html.parser", from_encoding="utf-8")

        links = soup.find_all('input', class_='csrf')
        # print("all of links ", len(links))
        s = str(links[0])
        print(s)
        begin = re.match(".*value=\"", s).end()
        end = re.match(".*", s).end()-3
        # print(begin, " ", end)
        # print( re.match(".*value=", s).end() )
        print("token = ", s[begin: end])
        token = s[begin: end]
        
        input_data = {
            "username" : _name,
            "password" : _password,
            "activationcode" : "",
            "remember" : "1",
            "_token" : str(token)
        }

        session.post("https://masiro.me/admin/auth/login", data=input_data)
        length = len(session.get("https://masiro.me/admin").content)
        if(length >= length1):
            print("Accepted")
            break
        else:
            print("Fail to login")

work()