import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule         
from sqlalchemy import create_engine, insert
from Model import page_table

class UrlSpiderSpider(CrawlSpider):
    name = "url_spider"
    allowed_domains = ["snn.ir"]
    start_urls = ["https://snn.ir"]
    le1 = LinkExtractor(allow='/news/')
    rules = (Rule(le1, callback="parse_item", follow=True),)

    def parse_item(self, response):
      engine = create_engine("postgresql://postgres:1@localhost:5432/website_content")
      text = str(response.xpath('//text()').getall())
      url = response.url
      path = url.replace("https://snn.ir",'')
      html = response.text
      stmt = insert(page_table).values(url=url, path=path, html=html, text=text)
      with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
      yield{
          'path': path, 
          'url': url,
          'html': html,
          'text': text,               
      }

    def insert_db(data):   
      # اتصال به پایگاه داده
      conn = psycopg2.connect(
          dbname="webcont_html",
          user="postgres",
          password="1",
          host="localhost"
      )
      cur = conn.cursor()

      # داده‌هایی که می‌خواهید به پایگاه داده اضافه کنید
      data = [
          ('John', 'Doe'),
          ('Jane', 'Smith'),
          ('Alice', 'Brown')
      ]

      # Query برای انجام batch insert
      query = "INSERT INTO table_name (column1, column2) VALUES %s"

      # انجام batch insert
      psycopg2.extras.execute_values(cur, query, data)

      # Commit تغییرات
      conn.commit()

      # بستن cursor و اتصال
      cur.close()
      conn.close()

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(UrlSpiderSpider)
    process.start()