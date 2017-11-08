'''
program: csdn博文爬虫
function: 实现对我的csdn主页所有博文的日期、主题、访问量、评论个数信息爬取

version: python 3.5.1
time: 2016/05/29
author: yr


renbin.guo added :  
    1.  但是有个疑问，d转为str后为什么[]不见了 ? line28
    2.   write写的内容必须为bytes
'''

import urllib.request,re,time,random,gzip

#定义保存文件函数
def saveFile(data,i):
    #path = "E:\\projects\\Spider\\05_csdn\\papers\\paper_"+str(i+1)+".txt"
    path = "./05/paper_"+str(i+1)+".txt"   ## both linux and windows is  ok 
    file = open(path,'wb')
    page = '当前页：'+str(i+1)+'\r\n'
    #file.write(page.encode('gbk'))       
    file.write(page.encode('utf-8'))       ### write 写 必须写bytes类型的, 这里page现在是str类型，即是unicode，所以需要转为bytes类型。可以选择gbk，也可以utf-8
    #将博文信息写入文件(以utf-8保存的文件声明为gbk)
    for d in data:  
       # d = str(d)+'\n'   ## linux 
        d = str(d)+'\r\n'  #   这里的d是一个list，所以需要转为str才可以进行write    但是有个疑问，d转为str后为什么[]不见了。比如 ['Mich', 'Bob', 'Tra']转为str后
                                          ## 应该还是['Mich', 'Bob', 'Tra'] 为什么中括号不见了 ?
        file.write(d.encode('utf-8'))   ### 同样的道理,d现在是一个str,所以需要转为bytes
        #file.write(d.encode('gbk'))  
    file.close()

#解压缩数据uft
def ungzip(data):
    try:
        #print("正在解压缩...")
        data = gzip.decompress(data)
        #print("解压完毕...")
    except:
        print("未经压缩，无需解压...")
    return data

#CSDN爬虫类
class CSDNSpider:
    def __init__(self,pageIdx=1,url="http://blog.csdn.net/fly_yr/article/list/1"):
        #默认当前页
        self.pageIdx = pageIdx
        self.url = url[0:url.rfind('/') + 1] + str(pageIdx)
        self.headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Host": "blog.csdn.net"
        }

    #求总页数
    def getPages(self):
        req = urllib.request.Request(url=self.url, headers=self.headers)
        res = urllib.request.urlopen(req)

        # 从我的csdn博客主页抓取的内容是压缩后的内容，先解压缩
        data = res.read()
        data = ungzip(data)
        data = data.decode('utf-8')

        pages = r'<div.*?pagelist">.*?<span>.*?共(.*?)页</span>'
        #link = r'<div.*?pagelist">.*?<a.*?href="(.*?)".*?</a>'
        # 计算我的博文总页数
        pattern = re.compile(pages, re.DOTALL)
        pagesNum = re.findall(pattern, data)[0]
        return pagesNum

    #设置要抓取的博文页面
    def setPage(self,idx):
        self.url = self.url[0:self.url.rfind('/')+1]+str(idx)

    #读取博文信息
    def readData(self):
        ret=[]
        #str = r'<dl.*?list_c clearfix">.*?date_t"><span>(.*?)</span><em>(.*?)</em>.*?date_b">(.*?)</div>.*?'+\
         #     r'<a.*?set_old">(.*?)</a>.*?<h3.*?list_c_t"><a href="(.*?)">(.*?)</a></h3>.*?'+\
          #    r'<div.*?fa fa-eye"></i><span>\((.*?)\)</span>.*?fa-comment-o"></i><span>\((.*?)\)</span></div>'
          #


        req = urllib.request.Request(url=self.url, headers=self.headers)
        res = urllib.request.urlopen(req)

        # 从我的csdn博客主页抓取的内容是压缩后的内容，先解压缩

        data = res.read()
        data = ungzip(data)
        data = data.decode('utf-8')

        re_str =[]
        ### str_title = r'<span class="link_title"><a href=.*?">\r\n\s*(.*?)\s*?</a>'  todo1 ：获取标题的那里会有换行和空格,如果要去掉，可以用这一行的正则表达式
        ###     这几句正则表达式，但是看起来就复杂一些了。这里的\s代表空格,\r\n代表换行. \s*就是匹配任意多的空格 ?为惰性匹配。
        re_str.append(r'<span class="link_title"><a href=.*?">(.*?)</a>')   ## tile
        re_str.append(r'<span class="link_postdate">(.*?)</span>')          ## date
        re_str.append(r'阅读</a>(.*?)</span>')                               ## read count
        re_str.append(r'评论</a>(.*?)</span>')                               ## comment count 
        re_str.append(r'<span class="link_title"><a href="(.*?)">')         ###  artile link
        #print(re_str)

        #patterns = []
        #for i in range(5):
        #    patterns.append(re.compile(re_str[i],re.DOTALL))
        #print(patterns)

        #record = []
        #for i in range(4):
        #    record[i] = re.findall(patterns[i],data)
        #    print(record[i])
        
        pattern_tile = re.compile(re_str[0],re.DOTALL)
        #print('patterns_title = %s'%pattern_tile)
        titles = re.findall(pattern_tile,data)   ## 这里获取当前页的文章标题的List
       # print(titles)
        #
        #
        pattern_date= re.compile(re_str[1],re.DOTALL) 
        dates = re.findall(pattern_date,data)
       # print(dates)

        pattern_read = re.compile(re_str[2],re.DOTALL)
        reads = re.findall(pattern_read,data)
       # print(reads)

        pattern_comment= re.compile(re_str[3],re.DOTALL)
        comments = re.findall(pattern_comment,data)
       #print(comments)

        pattern_link = re.compile(re_str[4],re.DOTALL)
        links = re.findall(pattern_link,data)
        #print(links)


        for i  in range(len(titles)):  ### 将上面获取的List合并
            ret.append(titles[i] +  dates[i]+ '\r\n'+'read count :'+reads[i]+ '\r\n'+\
                'comment count:' +comments[i]+'\r\n'+'http://blog.csdn.net'+links[i]+'\r\n\r\n\r\n')
        for i in range(5):
            print(ret[i])
       # print('#####ret = %s'%ret)



       # f =  open("./05_test.txt",'w')
       # for title in titles:
       #     f.write(title)
       # for date in dates:
        #    print(date)
        #print(titles)
       # print(dates)
       # for i in range(len(titles)):
        #    titles[i] = titles[i]+dates[i]
       # for title in titles:
        #    print(title)

            #ret.append(item[0]+'年'+item[1]+'月'+item[2]+'日'+'\t'+item[3]+'\n标题：'+item[5]
            #           +'\n链接：http://blog.csdn.net'+item[4]
             #          +'\n'+'阅读：'+item[6]+'\t评论：'+item[7]+'\n')
            #ret.append(item)
        return  ret

#定义爬虫对象
cs = CSDNSpider()
#求取
pagesNum = int(cs.getPages())


for idx in range(pagesNum):
    cs.setPage(idx)
    print("当前页：",idx+1)
    #读取当前页的所有博文，结果为list类型
    papers = cs.readData()
    print('#####papers = %s'%papers)
    saveFile(papers,idx)





