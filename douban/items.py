# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    pass

class DoubanItem(scrapy.Item):
        # define the fields for your item here like:
        # name = scrapy.Field()
        title=scrapy.Field()   #用来存储豆瓣电影标题
        star=scrapy.Field()    #用来存储豆瓣电影评分