import scrapy
import scraper_helper as sh
from ..items import CaltranItem


class CaltrannSpider(scrapy.Spider):
    name = 'caltrann'
    allowed_domains = ['dot.ca.gov']
    start_urls = ['https://dot.ca.gov/programs/procurement-and-contracts/ae-contract-information/a-e-executed-contracts']

    def parse(self, response):
        items = CaltranItem()
        tbody = response.xpath("//tbody/tr")
       
        for responses in tbody:
            Contno     = responses.css("td:nth-child(1)::text").extract()
            Contno     = [sh.cleanup(x) for x in Contno]
            Service    = responses.css("td:nth-child(2)::text").extract()
            Service    = [sh.cleanup(x) for x in Service]
            Consultant = responses.css("td~ td+ td,.table p").css("::text").extract()
            Consultant = [sh.cleanup(x) for x in Consultant]

            items['Contno']    = Contno
            items['Service']    = Service
            items['Consultant'] = Consultant

            yield items
            

           



