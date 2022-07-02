# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TexastenderItem(scrapy.Item):
    # define the fields for your item here like:
     title = scrapy.Field()
     dept  = scrapy.Field()
     desc  = scrapy.Field()
     typee = scrapy.Field()
     rows  = scrapy.Field()
     lstup = scrapy.Field()
     tags = scrapy.Field()

    
