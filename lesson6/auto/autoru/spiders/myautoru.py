# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from autoru.items import AutoruItem
from scrapy.loader import ItemLoader

class MyautoruSpider(scrapy.Spider):
    name = 'myautoru'
    allowed_domains = ['auto.ru']

    def __init__(self, mark):
        self.start_urls = [f'https://auto.ru/moskva/cars/{mark}/used/?sort=fresh_relevance_1-desc']

    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//a[contains(@class, 'ListingPagination-module__next')]/@href").extract_first()
        yield response.follow(next_page, callback=self.parse)
        car_links = response.xpath("//a[@class='Link ListingItemTitle-module__link']/@href").extract()
        for link in car_links:
            yield response.follow(link, callback=self.parse_cars)


    def parse_cars(self, response:HtmlResponse):
        loader = ItemLoader(item=AutoruItem(), response=response)
        loader.add_xpath('model', "//div[contains(@class, '__line_1')]/div[1]/text()") #first
        loader.add_xpath('price', "//div[@class='Price-module__caption ltgTX0yu2uc9Rq7KJvEtp__priceCaption']/span/text()") #first
        loader.add_xpath('year', "//a[@class='Link CardInfo__link_black']/text()") #first
        loader.add_xpath('color', "//li[@class='CardInfo__row CardInfo__row_color']/span[2]/text()") #first
        loader.add_xpath('photos', "//img[@class='image-gallery-image']/@src")
        loader.add_value('url', response.url)
        yield loader.load_item()
