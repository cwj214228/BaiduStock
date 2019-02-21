# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

from BaiduStocks.items import BaidustocksItem


class StocksSpider(scrapy.Spider):
    name = "5173"
    start_urls = ['http://s.5173.com/dnf-0-f10pkw-qrekgd-0-bx1xiv-0-0-0-a-a-a-a-a-0-itemprice_asc-0-0.shtml']


    def parse(self, response):
        #首先定义了需要解析网页获取的数据的队列，分别是：商品、价钱、数量和单价。
        goods_list=[]
        price_list=[]
        UnitPrice_list=[]

        #使用了xpath语法，根据标签快速定位想要获取的内容，速度比BeautifulSoup要快
        goods_list=response.xpath('.//div[@class="sin_pdlbox"]/ul[1]/li[1]/h2/a/text()').extract()
        price_list=response.xpath('.//div[@class="sin_pdlbox"]/ul[2]/li[1]/strong/text()').extract()
        UnitPrice_list=response.xpath('.//div[@class="sin_pdlbox"]/ul[4]/li[1]/b/text()').extract()

        data=BaidustocksItem()

        for i,j,l in zip(goods_list,price_list,UnitPrice_list):
            data['goods_list']=i
            data['price_list']=j
            data['UnitPrice_list']=l
            yield data



