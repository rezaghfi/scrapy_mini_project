import scrapy
from scrapy.crawler import CrawlerProcess

class Pagination(scrapy.Spider):
    name = 'pagination'
    start_urls = []
    
    custom_settings = {
        'DOWNLOAD_DELAY': 0,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1
    }
    
    def __init__(self):
        url = 'https://snn.ir/fa/allnews?page='
        page =1
        while True:
            self.start_urls.append(url + str(page))
            page = page + 1
        
    def parse(self, response):
        next_page = response.css("a.pager_next_list::attr(href)").get()
        if next_page is not None:
            print('response url:', response.url)
        else:
            print("end")

# run scraper
process = CrawlerProcess()
process.crawl(Pagination)
process.start()