import scrapy
import scraper_helper as sh


class GreatbooksSpider(scrapy.Spider):
    name = 'greatbooks'
    allowed_domains = ['www.thegreatestbooks.org']
    start_urls = ['https://thegreatestbooks.org/']

    def parse(self, response):
        all_div = response.css("div.col")
        for div in all_div:
            title  = div.css("a::text").extract()
            title  = [sh.cleanup(x) for x in title]

            yield {'title':title}
            
      
