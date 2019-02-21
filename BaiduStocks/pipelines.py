# -*- coding: utf-8 -*-
import pymysql
import xlsxwriter
import time
from twisted.enterprise import adbapi
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MysqlPipeline(object):
    def open_spider(self, spider):
        self.workbook = xlsxwriter.Workbook('d:/'+time.strftime("%Y-%m-%d")+'.xlsx')  # 创建一个Excel文件
        self.worksheet = self.workbook.add_worksheet()  # 创建一个sheet
        self.num0=0

    def process_item(self, item, spider):
        self.num0 = self.num0 + 1
        row = 'A' + str(self.num0)
        data = [item['goods_list'], item['price_list'], item['UnitPrice_list'], time.strftime("%Y-%m-%d")]
        self.worksheet.write_row(row, data)
        return item

    def close_spider(self, spider):
        self.workbook.close()



    """
    同步操作
    """
    '''
    def open_spider(self,spider):
        # 建立连接
        #数据库的地址，账号，密码，数据库的名字
        self.conn = pymysql.connect('localhost', 'root', '5201314', 'leecx',charset='utf8')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # sql语句
        # 执行插入数据到数据库操作
        self.cursor.execute("insert into ssss(type,price,num,danjia) values (%s,%s,%s,%s)",
                            (item['goods_list'], item['price_list'], item['num_list'], item['UnitPrice_list']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()
'''

