'''
批量下载豆瓣首页的图片(公司无法上豆瓣，则爬的csdn)

采用伪装浏览器的方式爬取豆瓣网站首页的图片，保存到指定路径文件夹下
'''

#导入所需的库
import urllib.request,socket,re,sys,os

#定义文件保存路径
targetPath = "/root/python_spider/"   ### 这里要注意，不存在python_spider可以创建。但是不能多级不存在。比如/root/python_spider/03/ 如果python_spider都不存在，则下面的urllib.request.urlretrieve(link,saveFile(link)) 就会失败。

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
url = "http://www.csdn.net/"
headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '                            'Chrome/51.0.2704.63 Safari/537.36'
           }

req = urllib.request.Request(url=url, headers=headers)

res = urllib.request.urlopen(req)

data = res.read()
## renbin.guo added  begin
#with open(targetPath,"wb") as f:
#    f.write(data)
### renbin.guo added end


#for link,t in set(re.findall(r'(http:*(jpg|png|gif))', str(data))):
#for link in re.findall(r'src="(.+?\.[a-z]{3})" ' , str(data)):
#pattern = re.compile(r'src="(http.+?)".*?',re.S)
pattern = re.compile(r'src="(http.+?)"',re.S)
### renbin.guo added  要注意,这里的双引号 "是原来网页中的，()里面的东西就是返回的字符串。 但是也r'src="(.+?)"'也可以
                                                        ### 网页中的原文<img src="http://images.csdn.net/20171026/头条3s.jpg">
                                                        ### 另外, '.+?'的意思是至少有一个任意字符,并且不采用贪婪匹配(?的作用)。

for link in re.findall(pattern , str(data)):

    print(link)
    try:
        urllib.request.urlretrieve(link,saveFile(link))
    except:
        print('失败')
