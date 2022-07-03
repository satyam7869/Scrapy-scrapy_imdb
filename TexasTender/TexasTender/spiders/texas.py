import scrapy
from ..items import TexastenderItem


class TexasSpider(scrapy.Spider):
    name = 'texas'
    allowed_domains = ['gis-txdot.opendata.arcgis.com']
    start_urls = ['https://gis-txdot.opendata.arcgis.com/search?collection=Dataset']

    def parse(self, response):
        items = TexastenderItem()

        title = response.xpath("//div/a[@class='ember-view result-name']/@href").getall()
        dept  = response.xpath("//div[@class='owner-source']/text()").getall()
        desc  = response.xpath("//div[@class='description']/text()").getall()
        typee = response.css("span[data-test='metadata-col-1-item-0']::text").getall()
        lstup = response.css("span[data-test='metadata-col-1-item-1']::text").getall()
        rows  = response.css("span[data-test='metadata-col-2-item-0']::text").getall()
        tags  = response.css("span[data-test='metadata-col-2-item-1']::text").getall()
            
        
        items['title'] = title
        items['dept']  = dept
        items['desc']  = desc
        items['typee'] = typee
        items['rows']  = rows 
        items['lstup'] = lstup
        items['tags']  = tags

        yield items
        

        