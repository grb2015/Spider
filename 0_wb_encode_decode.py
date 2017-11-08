# -*- coding: utf-8 -*-
# @Author: guorenbin
# @Date:   2017-11-08 22:05:29
# @Last Modified by:   guorenbin
# @Last Modified time: 2017-11-08 22:06:06


##error  TypeError: a bytes-like object is required, not 'str'
## 解释 : wb打开的时候,需要写入的是字节流,所以必须先把unicode的a转为字节编码
a = '中文'
with open("4.txt",'wb') as f:
	f.write(a)

## ok 
a = '中文'
a=a.encode('utf-8')
with open("4.txt",'wb') as f:
	f.write(a)


## --------如果是用w打开一个文件-----------则需要写入的是字符串,即unicode类型。

## error   TypeError: write() argument must be str, not bytes   
a = '中文'
a=a.encode('utf-8')  ## w 打开一个文件，需要写入字符串类型，即unicode类型，所以这里不应该转化
with open("4.txt",'w') as f:
	f.write(a)

## ok 
a = '中文'
with open("4.txt",'w') as f:
	f.write(a)
