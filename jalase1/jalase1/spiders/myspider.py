import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["snn.ir"]
    start_urls = ["https://snn.ir/fa/allnews"]

    def parse(self, response):
        news = response.css('div.cat_item_main')
        for new in news:
            yield {
                'url': "https://www.snn.ir"+new.css('div.cat_item_title a').attrib['href'],
                'path': new.css('a.cat_item_img').attrib['href'],
                'html': '',
                'text':''
            }

        next_page = response.css("a.pager_next_list::attr(href)").get()

        if next_page is not None:
            next_page_url = "https//www.snn.ir" + next_page
            yield response.follow(next_page_url, callback=self.parse)
