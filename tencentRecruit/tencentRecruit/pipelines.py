# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


## bug : 得到的json文件编码是unicode竟然


import scrapy
from scrapy import signals
import json, codecs

class TencentrecruitPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingTencentPipeline(object):
	def __init__(self):
		#self.file = codecs.open('tencent.json','w',encoding='utf-8')
		self.file = codecs.open('tencent.json','w')
		
	def process_item(self,item,spider):
		print("#### positionLink = %s"%item["positionLink"])
		item["positionLink"] = item["positionLink"].decode()  ##这里原来为bytes类型，必须要转为unicode (str) 不然 TypeError: Object of type 'bytes' is not JSON serializable

		print('##### item = %s'%item)
		print('##### type item  = %s'%type(item))   ### time is a class type
		item2 = dict(item)
		print('#####2 item = %s'%item2)
		print('#####2 type item  = %s'%type(item2)) 
		#item['positionLink'].decode()
		line = json.dumps(item2)

		#line = json.dumps(item,ensure_ascii=False)+'\n\n'
		self.file.write(line)
		return item

	def spider_closed(self,spider):
		self.file.close()
