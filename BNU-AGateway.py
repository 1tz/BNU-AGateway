#coding:utf-8
import urllib2
import urllib
import re

username = "引号内填写学号"
password = "引号内填写密码"

def check():
    try:
        urllib2.urlopen('http://gw.bnu.edu.cn', timeout=0.02)
        return True
    except urllib2.URLError as err:
        print '网络连接失败，请检查网络连接'
        return False

def force_logout():
    postData_logout = {
        "action": "logout",
        "username": username,
        "password": password,
        "ajax": "1"
    }
    postData_logout = urllib.urlencode(postData_logout)
    posturl_logout = "http://172.16.202.201:802/include/auth_action.php"
    header_logout = {
        "User-Agen": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36",
        "Referer": "http://gw.bnu.edu.cn:803/srun_portal_phone.php?ac_id=1&"
    }
    request_logout = urllib2.Request(posturl_logout, postData_logout, header_logout)

def login():
    posturl = "http://gw.bnu.edu.cn:803/srun_portal_phone.php?ac_id=1&"
    header = {
        "User-Agen": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36",
        "Referer": "http://gw.bnu.edu.cn:803/srun_portal_phone.php?ac_id=1&"
    }
    postData = {
        "action": "login",
        "ac_id": "1",
        "user_ip": "",
        "nas_ip": "",
        "user_mac": "",
        "url": "",
        "username": username,
        "password": password,
        "save_me": "1"
    }
    postData = urllib.urlencode(postData)
    request = urllib2.Request(posturl, postData, header)
    content = urllib2.urlopen(request).read()
    if content.find("成功") != -1:
        print '登录成功'
        return
    elif content.find("用尽") != -1:
        print '没救了，充钱吧'
        return
    else:
        force_logout()
        request = urllib2.Request(posturl, postData, header)
        content = urllib2.urlopen(request).read()
        print '全部下线，登录成功'
        return

if check():
    login()
