# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import redis
import json


class FirstScrapyPipeline:
    conn = None

    def open_spider(self, spider):
        print('爬虫开始')
        self.conn = redis.Redis(host='127.0.0.1', port=6379)  #链接redis数据库

    # 该方法可以接受爬虫文件传输的item对象，并进行处理
    def process_item(self, item, spider):
        # 取出item中存储的数据值
        data = {
            'title': item['title'],
            'href': item['href']
        }
        json_data = json.dumps(data)
        # 持久化存储
        self.conn.lpush('data', json_data)
        return item

    def close_spider(self, spider):
        print('爬虫结束')
