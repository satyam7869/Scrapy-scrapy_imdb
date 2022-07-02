import scrapy
from ..items import TexastenderItem


class TexasSpider(scrapy.Spider):
    name = 'texas'
    allowed_domains = ['gis-txdot.opendata.arcgis.com']
    start_urls = ['https://gis-txdot.opendata.arcgis.com/search?collection=Dataset&modified=1900-06-29%2C2022-06-30']

    def parse(self, response):
        items = TexastenderItem()

        title = response.css(".result-name::text").extract()
        dept  = response.css(".owner-source::text").extract()
        desc  = response.css(".description::text").extract()
        typee = response.css("span::text").extract()
        lstup = response.css("span::text").extract()
        rows  = response.css("span::text").extract()
        tags  = response.css("span::text").extract()
            
        
        items['title'] = title
        items['dept']  = dept
        items['desc']  = desc
        items['typee'] = typee
        items['rows']  = rows 
        items['lstup'] = lstup
        items['tags']  = tags

        yield items
        

        