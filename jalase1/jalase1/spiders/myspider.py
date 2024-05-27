import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["snn.ir"]
    start_urls = ["https://snn.ir"]

    def parse(self, response):
        pass
