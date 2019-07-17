# -*- coding: utf-8 -*-
# 巨潮个股公告 spider
# @dbaoxiang
# www.cninfo.com.cn
# 2018-08年报读取及提取pdf的主要内容
import scrapy
import json
import random
import logging
import pdfminer
import io
import os

import sys   #reload()之前必须要引入模块

from datetime import datetime
from scrapy import Selector, FormRequest
from GonggaoSpider2019.items import GonggaoItem  
from urllib import urlopen
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
num_dir = 0

for x in range(2008, 2019):     #此选择需要下载的年份参数，注意：（2008，2018）代表下载2008-2017年的数据
    s = x+1
    print(x)
    print(s)
    class GonggaoSpider(scrapy.Spider):
        sys.path

        # name = "GonggaoSpider2019"
        start_urls = ["http://www.cninfo.com.cn"]
        name = "GonggaoSpider2019"
        allowed_domains = ['www.cninfo.com.cn']
        headers = {
        }

        reload(sys)
        sys.setdefaultencoding('utf-8')

        # custom_settings = {
        #     'ITEM_PIPELINES': {
        #         'sgrcrscrapy.pipelines.JsonWriterPipeline.JsonWriterPipeline': 300,
        #         'sgrcrscrapy.pipelines.MongoGongGaoPipeline.MongoGongGaoPipeline': 400,
        #     }
        # }
        
        # custom_settings = {
        #     'ITEM_PIPELINES': {
        #         # 'GonggaoSpider2019.pipelines.JsonWriterPipeline': 300,
        #         #  'GonggaoSpider2019.pipelines.TutorialPipeline': 300,

        #         # 'Gonggaospider2019Pipeline.pipelines.MongoGongGaoPipeline.MongoGongGaoPipeline': 400,
        #     }
        # }

        # custom_settings = {
        #     'ITEM_PIPELINES': {
        #     'GonggaoSpider2019.pipelines.Gonggaospider2019Pipeline': 300,
        #     }
        # }
        
        print(x)
        print(str(x) + '.txt')
        print(str(s) + '-01-01 ~ ' + str(s) + '-08-31')
        print('stock' + str(x) + '/')
        s = x+1
        def start_requests(self):
            url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'      #代表爬取数据对应的网址
            # url = 'http://www.cninfo.com.cn/cninfo-new/announcement/query'
            # url = 'http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice-sse#'
            # url = 'view-source:http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice-sse#'

            requests = []
            f = open("output.json",'w')
            # stocklist = json.load(f)
            # f = open('stock/'+ str(x) + '.txt')
            # stocklist = []
            # for line in f.readlines():
            #     #print(line,end = '')
            #     line = line.replace('\n', '')
            #     stocklist.append(line)
            # f.close()
            # print(stocklist)

            stocklist = ['000001','000002','0000003','000004']
            random.shuffle(stocklist)
            for data in stocklist:
                formdata = {"stock": data,
                            "searchkey": "",
                            "category": "category_ndbg_szsh",
                            "pageNum": "1",
                            "pageSize": "30",
                            "column": "szse_main",
                            "tabName": "fulltext",
                            "sortName": "",
                            "sortType": "",
                            "limit": "",
                            "seDate": str(s)+"-01-01 ~ "+ str(s) +"-08-31",
                            }

                #specailTips2018-05-11=1204931590|1204931583; JSESSIONID=E7EFBC77F7AE2905A623F3EA46753541
                request = FormRequest(url,
                                      callback=self.parse_item,
                                      formdata=formdata,
                                      headers=self.headers)
                tex = open('data.txt', 'a+')
                #print(request, file=tex)
                tex.close()
                requests.append(request)
            return requests

        def readPDF(self, pdfFile):
            print(pdfFile)
            logging.propagate = False
            logging.getLogger().setLevel(logging.ERROR)
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            laparams = LAParams()
            device = TextConverter(rsrcmgr, retstr, laparams=laparams)

            # PDFPageInterpreter(rsrcmgr, device, pdfFile)
            PDFPageInterpreter(rsrcmgr, device)

            device.close()

            content = retstr.getvalue()
            retstr.close()
            return content

        def parse_item(self, response):

            print("fuck text before .............................")
            print(response.text)
            print("fuck text after .............................")
            print(response.status)

            datas = json.loads(response.text)["announcements"]
            print("$$$$$$$$$$$$$" * 100)
            print(datas)
            if datas:
                    for linerecord in datas:
                        print("next \n")
                        print("#####"*100)
                        print(linerecord)
                        item = GonggaoItem()
                        item['announcementId'] = linerecord['announcementId']
                        item['secCode'] = str(linerecord['secCode'])
                        item['secName'] = linerecord['secName']
                        item['announcementTitle'] = linerecord['announcementTitle']


                        item['announcementTime'] = datetime. \
                            fromtimestamp((linerecord['announcementTime'] / 1000)). \
                            strftime('%Y-%m-%d %H:%M:%S')
                        item['announcementTypeName'] = linerecord['announcementTypeName']
                        item['important'] = linerecord['important']
                        # item['adjunctUrl'] = 'http://www.cninfo.com.cn/' + linerecord['adjunctUrl']
                        item['adjunctUrl'] = 'http://static.cninfo.com.cn/' + linerecord['adjunctUrl']
                        item['createtime'] = datetime.now().isoformat()
                        print item['adjunctUrl']
                        pdfFile = urlopen(item['adjunctUrl'])                        
                        
                        item['announcementDetail'] = self.readPDF(pdfFile)
                        item['announcementDetail'] = pdfFile.readlines()
                        # item['announcementDetail'] = pdfFile.readlines()
                        pdfFile.close()
                        print(",..,.,.,.,.,.,.,.,..,.,.,.,")
                        # print(item['announcementDetail'])
                        print("$$$$$$$$$$$$$$$$$$$$")
                        print(item)
                        if 'ST' in item['secName']:
                            pass
                        elif '摘要' in item['announcementTitle']:
                            pass
                        elif '更正' in item['announcementTitle']:
                            pass
                        elif '修订' in item['announcementTitle']:
                            pass
                        else:
                            global num_dir
                            num_dir = num_dir + 1
                            with open(str(num_dir) + '.txt', "w+") as wf:    #爬取出来的文件对应存放的位置
                                wf.write(str(item['announcementDetail']))
                                yield item

            else:
                print("pass parse_item")
                pass
