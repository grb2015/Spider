'''
第一个示例：简单的网页爬虫

爬取豆瓣首页



 renbin.guo added :
  ###　疑问，1 .这里decode之后不就成了unicode吗?write不能写unicode啊?不然 TypeError: 'str' does not support the buffer interface
  ###  		 2. 必须open时候必须wb,不然  error :  must be str, not bytes
'''

import urllib.request

#网址
url = "http://www.douban.com/"

#请求
request = urllib.request.Request(url)

#爬取结果
response = urllib.request.urlopen(request)

data = response.read()

#设置解码方式  这里不需要解码为unicode,不然write会出错
#data = data.decode('utf-8')

#打印结果
#print(data)  ## renbin.guo added 
with open("./01_douban.html",'wb') as f:    ###　疑问，这里decode之后不就成了unicode吗?write不能写unicode啊?
    f.write(data)							###  解答 ： 'wb'的话可以写bytes 即uft-8等			
    										###  而如果是'w' 则必须写str 即 unicode,这时候就需要data.decode('utf-8')
'''
	这里也可以
data = data.decode('utf-8')	
with open("./01_douban.html",'wb') as f:
f.write(data)	

'''

    										
data = data.decode('utf-8')			### 同样，这里因为print(str)参数为str 所以需要unicode
print(data)
#打印爬取网页的各类信息

print('type(response) = %s\n\n'%type(response))
print('response.geturl() = %s\n\n'%response.geturl())
print('response.info() = %s\n\n'%response.info())
print('respense.getcode() = %s\n\n'%response.getcode())
