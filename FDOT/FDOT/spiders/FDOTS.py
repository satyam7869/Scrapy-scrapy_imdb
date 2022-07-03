import scrapy
from ..items import FdotItem


class FdotsSpider(scrapy.Spider):
    name = 'FDOTS'
    page =2
    allowed_domains = ['scoc.fdot.gov']
    start_urls = ['https://scoc.fdot.gov/#/active/1']

    def parse(self, response):
        items = FdotItem()

        items['district']  = response.css("td.DISTRICT::text").getall()
        items['contactID'] = response.css("td:nth-child(3)::text").extract()
        items['status']    = response.css("td:nth-child(4)::text").extract()
        items['begin']     = response.css("td:nth-child(5)::text").extract()
        items['projectID'] = response.css("td:nth-child(6)::text").extract()
        items['desc']      = response.css("td:nth-child(7)::text").extract()
        items['workmix']   = response.css("td:nth-child(8)::text").extract()
        items['county']    = response.css("td:nth-child(9)::text").extract()
        items['vendorname'] = response.css("td:nth-child(10)").css(" a::text").extract()

        yield items

        next_page = 'https://scoc.fdot.gov/#/active/'+str(FdotsSpider.page)

        if FdotsSpider.page <=130 :
            FdotsSpider.page+=1
            yield response.follow(next_page, callback =self.parse)  

        
