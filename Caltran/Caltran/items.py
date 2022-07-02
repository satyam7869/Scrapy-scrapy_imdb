# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CaltranItem(scrapy.Item):
  
     Contno = scrapy.Field()
     Service = scrapy.Field()
     Consultant = scrapy.Field()
    
    
