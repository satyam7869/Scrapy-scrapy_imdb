import scrapy


class WorldometerSpider(scrapy.Spider):
    name = 'WorldOMeter'
    allowed_domains = ['https://www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/coronavirus']

    def parse(self, response):
        for country in (response.xpath("//td/a/")):
            name=coutry.xpath(".//text()").get()
            link=country.xpath(".//@href").get()

            yield {
                'country_name':name,
                'country_link':link
                }
