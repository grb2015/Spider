'''
批量下载豆瓣首页的图片

采用伪装浏览器的方式爬取豆瓣网站首页的图片，保存到指定路径文件夹下
'''

#导入所需的库
import urllib.request,socket,re,sys,os

#定义文件保存路径
targetPath = "./03_dbImages/"

def saveFile(path):
    #检测当前路径的有效性
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)

    #设置每个图片的路径
    pos = path.rindex('/')
    t = os.path.join(targetPath,path[pos+1:])
    return t

#用if __name__ == '__main__'来判断是否是在直接运行该.py文件


# 网址
url = "https://www.douban.com/"
headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '                            'Chrome/51.0.2704.63 Safari/537.36'
           }

req = urllib.request.Request(url=url, headers=headers)

res = urllib.request.urlopen(req)

data = res.read()


## renbin.guo added 2017-11-04  begin
data = data.decode('utf-8')
with open("./03_image.html",'w') as f:
    f.write(data)

## renbin.guo added 2017-11-04  end

##  renbin.guo add comment  2017-11-04
#   关于这里的正则表达式：
#   1.原文中是[^s] 这里感觉用错了,需要转义\s
#   2.(r'(https:[^\s]*?(jpg|png|gif))'的意义:
#       它会匹配以https:开头 ,中间不含空格, 且以jpg,png,gif 结尾的字符串(url)
#       a.这里[^\s]表示https: ~ jpg直接不能有空格,[^\s]*表示https:~jpg之间有任意多个非空格字符。可以用.*代替[^\s]*试试，这样的就会包含空格的url，
#       b.这里的?表示惰性匹配，如果不加它，则jpg也可能被[^\s]匹配。可以去掉看看效果
#       
#
#
#
#   3.这里有两个圆括号,第一个圆括号得到的一个变量即link,第二个圆括号(jpg|png|gif)得到一个图片类型的变量t 
#                                                     但是如果你说不想要图片类型,不要第二组括号可以吗?即:(https:[^\s]*?jpg|png|gif )'                                                               
#                                                     因为它是一个集合表达式,正则的语法决定了一定要。所以这里的圆括号是一举两用了,而且
#                                                     不得不收集第二个参数。
#   
#                                                       
#   
###  renbin.guo end 
for link,t in set(re.findall(r'(https:[^\s]*?(jpg|png|gif))', str(data))):
    print(link)
#    print(t)
    try:
        urllib.request.urlretrieve(link,saveFile(link))
    except:
        print('失败')
