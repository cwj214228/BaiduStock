# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidustocksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    goods_list = scrapy.Field()
    price_list = scrapy.Field()
    num_list = scrapy.Field()
    UnitPrice_list = scrapy.Field()
    pass
