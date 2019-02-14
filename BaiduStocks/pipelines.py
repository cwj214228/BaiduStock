# -*- coding: utf-8 -*-
import pymysql
from twisted.enterprise import adbapi
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MysqlPipeline(object):
    """
    同步操作
    """
    def __init__(self):
        # 建立连接
        #数据库的地址，账号，密码，数据库的名字
        self.conn = pymysql.connect('localhost', 'root', '5201314', 'leecx',charset='utf8')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # sql语句
        # 执行插入数据到数据库操作
        self.cursor.execute("insert into ssss(type,price,num,danjia) values (%s,%s,%s,%s)",
                            (item['类型'], item['价格'], item['数量'], item['单价']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()


