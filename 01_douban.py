'''
第一个示例：简单的网页爬虫

爬取豆瓣首页
'''

import urllib.request

#网址
url = "http://www.douban.com/"

#请求
request = urllib.request.Request(url)

#爬取结果
response = urllib.request.urlopen(request)

data = response.read()

#设置解码方式
data = data.decode('utf-8')

#打印结果
#print(data)  ## renbin.guo added 
with open("./01_douban.html",'w') as f:
    f.write(data)

#打印爬取网页的各类信息

print('type(response) = %s\n\n'%type(response))
print('response.geturl() = %s\n\n'%response.geturl())
print('response.info() = %s\n\n'%response.info())
print('respense.getcode() = %s\n\n'%response.getcode())
