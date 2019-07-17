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


# 巨潮公告
class GonggaoItem(scrapy.Item):
    # id
    announcementId = scrapy.Field()
    # name
    secName = scrapy.Field()
    # code
    secCode = scrapy.Field()
    # 公告title
    announcementTitle = scrapy.Field()
    # 公告全文
    announcementDetail = scrapy.Field()
    # timestamp
    announcementTime = scrapy.Field()
    # 重要度描述typedesc
    announcementTypeName = scrapy.Field()
    # 重要度important
    important = scrapy.Field()
    # pdfURL
    adjunctUrl = scrapy.Field()
    # createtime
    createtime = scrapy.Field()