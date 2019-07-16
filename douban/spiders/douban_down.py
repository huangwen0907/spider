# -*- coding: utf-8 -*-
import scrapy

from douban.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["https://movie.douban.com/"]

    start_urls = [
        "https://movie.douban.com/top250"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="info"]'):
            item = DoubanItem()
            item['title'] = sel.xpath('div[@class="hd"]/a/span/text()').extract()[0]  #此处运行时报错'unindent does not match any outer indentation level',是由于TAB键和空格混搭使用。所以我在此处先消除空格，在tab缩进，就不会报错
            item['star'] = sel.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            print item['title'],item['star']
            yield item