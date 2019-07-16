# -*- coding: utf-8 -*-
import scrapy
#from douban.items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = "book"     #爬虫名称
    allowed_domains = ["https://movie.douban.com/"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        for sel in response.xpath('//div[@class="info"]'):
            #item = DmozItem()
            title = sel.xpath('div[@class="hd"]/a/span/text()').extract()[0]  #不加[0]会变成Unicode形式
            star= sel.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]  
            print star,title