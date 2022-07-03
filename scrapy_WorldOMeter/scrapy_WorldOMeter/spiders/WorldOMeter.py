import scrapy
import scraper_helper as sh
from ..items import ScrapyWorldometerItem


class WorldometerSpider(scrapy.Spider):
    name = 'WorldOMeter'
    allowed_domains = ['https://www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        items = ScrapyWorldometerItem()
        for responses in (response.css('a.mt_a')):    
            name = responses.css("::text").getall()
            for link in response.css("a.mt_a::attr(href)").getall():
                yield scrapy.Request(response.urljoin(link),callback = self.parse)
                link =  response.url + str(responses.css("::attr(href)").getall())

            
            
                items['name']    =  name
                items['link']   =   link 

            
            
            yield items
                
                
