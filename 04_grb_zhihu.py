# -*- coding: utf-8 -*-
# @Author: guorenbin
# @Date:   2017-11-04 19:20:00
# @Last Modified by:   guorenbin
# @Last Modified time: 2017-11-04 21:40:30

## 参考：https://github.com/injetlee/Python/blob/master/login_zhihu.py   稍作改动
import requests,time
import urllib.request
from bs4 import BeautifulSoup
url = 'https://www.zhihu.com/login/email'
def get_captcha(data):
    with open('captcha.gif','wb') as fb:
        fb.write(data)
    return input('captcha')

def login(username,password,oncaptcha):
    sessiona = requests.Session()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    xyz = sessiona.get('https://www.zhihu.com/#signin',headers=headers).content
    print('xyz = %s'%xyz)
    _xsrf = BeautifulSoup(xyz,'html.parser').find('input',attrs={'name':'_xsrf'}).get('value')
    print(_xsrf)
    captcha_content = sessiona.get('https://www.zhihu.com/captcha.gif?r=%d&type=login'%(time.time()*1000),headers=headers).content
    data = {
        "_xsrf":_xsrf,
        "email":username,
        "password":password,
        "remember_me":True,
        "captcha":oncaptcha(captcha_content)
    }
    resp = sessiona.post('https://www.zhihu.com/login/email',data,headers=headers).content
    print(resp)

    ### 登录之后，要验证是否是登录了，可以访问settting页面
    data = sessiona.get('https://www.zhihu.com/settings',headers=headers)
    da = data.content.decode('utf-8')  ### 获取到的是utf-8类型,而f.write需要是str类型，python中str是unicode,所以需要把bytes类型转为unicode
    print(da)
    with open("./04_grb_zhihu.html",'w') as f:
    	f.write(da)
    return resp 

if __name__ == "__main__":
    login('your_email','your_password',get_captcha)


