# -*- coding: utf-8 -*-
import pymysql
from twisted.enterprise import adbapi
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaidustocksPipeline(object):
    def process_item(self, item, spider):
        try:
            print(item['类型'])
            print(item['价格'])
            print(item['数量'])
            print(item['单价'])
        except:
            print("haaaaaaaa")


    '''
    def open_spider(self, spider):
        self.f = open('BaiduStockInfo.txt', 'w')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)
        except:
            print("haaaaaaaa")
        return item
'''


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


class MysqlPipelineTwo(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):  # 函数名固定，会被scrapy调用，直接可用settings的值
        """
        数据库建立连接
        :param settings: 配置参数
        :return: 实例化参数
        """
        adbparams = dict(
            host=settings['localhost'],
            db=settings['leecx'],
            user=settings['root'],
            password=settings['5201314'],
            cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
        )
        # 连接数据池ConnectionPool，使用pymysql或者Mysqldb连接
        dbpool = adbapi.ConnectionPool('pymysql', **adbparams)
        # 返回实例化参数
        return cls(dbpool)

    def process_item(self, item, spider):
        """
        使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
        """
        query = self.dbpool.runInteraction(self.do_insert, item)  # 指定操作方法和操作数据
        # 添加异常处理
        query.addCallback(self.handle_error)  # 处理异常

    def do_insert(self, cursor, item):
        # 对数据库进行插入操作，并不需要commit，twisted会自动commit
        insert_sql = 'insert into ssss(type,price,num,danjia) values (%s,%s,%s,%s)'
        cursor.execute(insert_sql, (item['类型'], item['价格'], item['数量'], item['单价']))

    def handle_error(self, failure):
        if failure:
            # 打印错误信息
            print(failure)



