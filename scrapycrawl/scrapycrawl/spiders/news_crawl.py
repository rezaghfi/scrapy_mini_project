import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapycrawl.items import NewsItem


class NewsCrawlSpider(CrawlSpider):
    name = "news_crawl"
    # crawl just search in this allowed_domains pages
    allowed_domains = ["snn.ir"]
    start_urls = ["https://snn.ir"]

    # rule for news pages in domain
    le_news_details = LinkExtractor(allow=r"https://snn.ir/")
    rules = (Rule(le_news_details, callback="parse_item", follow=True),)

    def parse_item(self, response):
        
        news = NewsItem()

        news['url'] = response.url
        news['path'] = news['url'].replace("https://snn.ir", "")
        news['html'] = response.text
        news['text'] = str(response.xpath("//text()").getall()) 
        
        yield news

