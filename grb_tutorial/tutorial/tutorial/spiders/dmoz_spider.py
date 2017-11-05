# -*- coding: utf-8 -*-
# @Author: guorenbin
# @Date:   2017-11-05 18:27:40
# @Last Modified by:   guorenbin
# @Last Modified time: 2017-11-05 19:04:34
import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    #def parse(self, response):
    #    filename = response.url.split("/")[-2]
    #    print('####response = %s   '%response.url.split("/"))
    #    with open(filename, 'wb') as f:
    #        f.write(response.body)
    #        
    #        
    #def parse(self, response):
    #    for sel in response.xpath('//ul/li'):
    #        title = sel.xpath('a/text()').extract()
    #        link = sel.xpath('a/@href').extract()
    #        desc = sel.xpath('text()').extract()
    #        print('#####tile = %s'%title)
    #        print('#####link = %s'%link)
    #        print('#####desc = %s'%desc)



    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
