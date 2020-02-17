# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import pymongo


class AutoruPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient("mongodb+srv://geekbrains:T1cWWlPDNSy281hK@cluster0-oq9cq.azure.mongodb.net/test?retryWrites=true&w=majority")
        db = client.geekbrains
        self.collection = db.vacancies_bd

    def process_item(self, item, spider):
        self.collection.insert_one(item)
        return item

class AutoruPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    request = scrapy.Request(img)
                    yield request
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item
