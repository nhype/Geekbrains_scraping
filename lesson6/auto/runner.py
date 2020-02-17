from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from autoru import settings
from autoru.spiders.myautoru import MyautoruSpider

if __name__ == '__main__':
  crawler_settings = Settings()
  crawler_settings.setmodule(settings)
  process = CrawlerProcess(settings = crawler_settings)
  process.crawl(MyautoruSpider, mark='BMW')
  process.start()
