# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FdotItem(scrapy.Item):
    # define the fields for your item here like:
    district = scrapy.Field()
    contactID = scrapy.Field()
    status = scrapy.Field()
    begin = scrapy.Field()
    projectID = scrapy.Field()
    desc = scrapy.Field()
    workmix = scrapy.Field()
    county = scrapy.Field()
    vendorname = scrapy.Field()
