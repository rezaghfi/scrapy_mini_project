import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class UrlSpiderSpider(CrawlSpider):
    name = "url_spider"
    allowed_domains = ["snn.ir"]
    start_urls = ["https://snn.ir"]
    le1 = LinkExtractor()
    rules = (Rule(le1, callback="parse_item", follow=True),)

    def parse_item(self, response):
        items = response.xpath('//text()').getall()
        for i in items:
            yield{
                'text': items,
                '***url': response.url
            }
            

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(UrlSpiderSpider)
    process.start()