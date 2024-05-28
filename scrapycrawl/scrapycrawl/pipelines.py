# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapycrawlPipeline:
    def process_item(self, item, spider):
        return item

class SavingToPostgresPipeline(object):

    def __init__(self):
        self.create_connection()


    def create_connection(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="website_content",
            user="postgres",
            password="1")
        self.curr =self.conn.cursor()

    def process_item(self, item, spider):
        self.store_in_db(item)
        #we need to return the item below as scrapy expects us to!
        return item

    def store_in_db(self, item):
        try:
            self.curr.execute(""" insert into pages(path, url, html, text) values (%s,%s,%s, %s)""", (
                item["path"],
                item["url"],
                item["html"],
                item["text"]
            ))
        except BaseException as e:
            print(e)
        self.conn.commit()