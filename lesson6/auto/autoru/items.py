# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


def cleaner_photo(values):
    return f'http:{values}'

def str_to_int_ignore_letters(s):
  return int(''.join(c for c in s if c.isdigit()))

def cleaner_price(values):
    price = values.replace("\xa0", '')
    return str_to_int_ignore_letters(values)

class AutoruItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    model = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(cleaner_price))
    year = scrapy.Field(output_processor=TakeFirst())
    color = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(cleaner_photo))
    url = scrapy.Field()
