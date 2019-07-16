# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class DoubanPipeline(object):
#     def process_item(self, item, spider):
#         return item


# class DoubanBookPipeline(object):
#     def process_item(self, item, spider):
#         info = item['content'].split(' / ')
#         item['name'] = item['name']
#         item['price'] = info[-1]
#         item['edition_year'] = info[-2]
#         item['publisher'] = info[-3]
#         return item


import sys 
reload(sys) 
sys.setdefaultencoding('utf8') 

class DoubanPipeline(object):
    def __init__(self):
        self.file=open('douban_top250.txt',mode='wb')


    def process_item(self, item, spider):
        line='the top250 movie list:'

        for i in range(1,len(item['star'])-1):
            title=item['title']
            star=item['star']
            line=line+'  '+title+'  '
            line=line+star+'\n'

        self.file.write(line)

    def close_spider(self,spider):
        self.file.close()