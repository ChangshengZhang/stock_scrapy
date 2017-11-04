#!/usr/bin/python
# -*- coding: utf-8 -*-
# File Name: stock_spider.py
# Author: Changsheng Zhang
# mail: zhangcsxx@gmail.com
# Created Time: Wed Oct 18 20:35:57 2017

#########################################################################

import scrapy
from scrapy.selector import Selector
from stock.items import StockItem
import datetime

class StockSpider(scrapy.Spider):

    name = 'stock'
    allowed_domains = ["hkexnews.hk"]
    start_urls = ['http://www.hkexnews.hk/sdw/search/mutualmarket.aspx?t=hk']

    def parse(self,response):
        
        td = datetime.date.today().strftime('%Y%m%d')
        f = open("holding_data/"+td+".csv","w")
	f.write("stock_id ;stock_name; holding_num; holding_perc \n")
        for sel in response.xpath("//tr").extract():
            
            item = StockItem() 
            info = Selector(text = sel).xpath("//td/text()").extract()
            if len(info) !=4:
                continue

            a = info[0].split("\r\n")[1]
            b = info[1].split("\r\n")[1]
            c = info[2].split("\r\n")[1]
            d = info[3].split("\r\n")[1]
            
            f.write(a+";"+b+";"+c+";"+d+"\n")
        f.close()
