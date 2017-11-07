# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import scrapy
from scrapy import signals
import json, codecs

class TencentrecruitPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingTencentPipeline(object):
	def __init__(self):
		self.file = codecs.open('tencent.json','w',encoding='utf-8')
		
	#def process_item(self,item,spider):
		#line = json.dumps(dict(item),ensure_ascii=False)+'\n\n'
		#self.file.write(line)
	#	print('#########  process_item item = %s ,type(item)=%s\n'%(item,type(item)))
		#item=item.decode('utf-8')  ### 显然这里item是一个类的实例，所以无法调用decode

		#item['name']= item['name'].decode('utf-8')  ### 而这里，类的成员name 和 positionLink本身就是str了，所以可以直接写文件，不需要decode 
		#itme['positionLink'] = itme['positionLink'].decode('utf-8')  
		#self.file.write(item)  ## 这样不行，因为item是一个类实例，write接受的是一个字符串的参数,所以要转为字符串.
	#	self.file.write(str(item))
	#	return item
	def process_item(self,item,spider):
		print('######### 1  process_item item = %s ,type(item)=%s\n'%(item,type(item)))
		item = dict(item)
		print('#########  2 process_item item = %s ,type(item)=%s\n'%(item,type(item)))
		line = json.dumps(item,ensure_ascii=False)+'\n\n'
		self.file.write(line)
		return item

	def spider_closed(self,spider):
		self.file.close()
