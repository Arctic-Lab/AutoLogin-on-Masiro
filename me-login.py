from urllib import response
# from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import random
import time

def work():
    # 请改成自己的账户名
    _name = "usrname" 
    # 请改成自己的密码
    _password = "password"
    session = requests.session()
    cnt = 0
    while(1):
        if(cnt > 3):
            break
        cnt = cnt+1
        time.sleep(random.randint(1, 600))
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        
        length1 = len(session.get("https://masiro.me/admin").content)
        url = "https://masiro.me/admin/auth/login"
        soup = BeautifulSoup(session.get(url).content, "html.parser", from_encoding="utf-8")

        links = soup.find_all('input', class_='csrf')
        s = str(links[0])
        # print(s)
        begin = re.match(".*value=\"", s).end()
        end = re.match(".*", s).end()-3
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
        session.get('https://masiro.me/admin/checkAnnouncement')
        length = len(session.get("https://masiro.me/admin").content)

        s = str(session.get('https://masiro.me/admin/userCenterShow').content, 'utf-8')
        s = re.findall(r'\u8D44\u5386.+\u5929', s)[0]
        print(s)

        if(length > length1):
            print("Accepted")
            break
        else:
            print("Fail to login")
    

work()
