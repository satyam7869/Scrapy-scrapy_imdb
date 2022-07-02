import scrapy
from ..items import QuotesItem


class QuoteSpider(scrapy.Spider):

    name = 'Quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        items = QuotesItem()
        all_div = response.css("div.quote")

        for div in all_div:
            title = div.css(".text::text").extract()
            author = div.css(".author::text").extract()
            tag = div.css(".tag::text").extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback =self.parse)    