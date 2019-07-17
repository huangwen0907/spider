# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys 
reload(sys) 
sys.setdefaultencoding('utf8') 
num_dir =1

class Gonggaospider2019Pipeline(object):
    def __init__(self):
        global num_dir
        self.file=open(str(num_dir)+'.txt',mode='wb')
        num_dir  = num_dir +1
       

    def process_item(self, item, spider):
        title = item['announcementTitle'] + '\n'
        global num_dir
        num_dir = num_dir+1
        self.file=open(str(num_dir) +'.txt',mode='w+')
        self.file.write(title)
        # for i in range(1,len(item['announcementDetail'])):
        self.file.write(item['announcementDetail'])
        
        
    def close_spider(self,spider):
        self.file.close()
