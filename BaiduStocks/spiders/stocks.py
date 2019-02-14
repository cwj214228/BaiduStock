# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup



class StocksSpider(scrapy.Spider):
    name = "stocks"
    start_urls = ['http://s.5173.com/dnf-0-f10pkw-qrekgd-0-bx1xiv-0-0-0-a-a-a-a-a-0-itemprice_asc-0-0.shtml']


    def parse(self, response):
        ndict={}
        tplt = "{0:{4}^10}\t\t{1:^10}\t{2:^10}\t{3:^10}"
        print(tplt.format("商品", "价格", "数量", "单价", chr(12288)))
        soup =BeautifulSoup(response.body,'html.parser')
        for div in soup.find_all('div', 'sin_pdlbox'):
            h2s = div('li')
            ndict['类型']=h2s[0].a.string
            ndict['价格']=h2s[4].strong.string
            ndict['数量']=h2s[5].string
            ndict['单价']=h2s[6].b.string
            yield ndict



    '''def parse_stock(self, response):
        infoDict = {}
        stockInfo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name').extract()[0]
        keyList = stockInfo.css('dt').extract()
        valueList = stockInfo.css('dd').extract()
        for i in range(len(keyList)):
            key = re.findall(r'>.*</dt>', keyList[i])[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>', valueList[i])[0][0:-5]
            except:
                val = '--'
            infoDict[key] = val

        infoDict.update(
            {'股票名称': re.findall('\s.*\(', name)[0].split()[0] + \
                     re.findall('\>.*\<', name)[0][1:-1]})
        yield infoDict'''


