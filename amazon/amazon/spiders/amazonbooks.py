import scrapy
from ..items import AmazonItem

class AmazonbooksSpider(scrapy.Spider):
    name = 'amazonbooks'
    page_number = 2
    allowed_domains = ['www.amazon.in']
    start_urls = [
        'https://www.amazon.in/s?k=amazon+store+book&adgrpid=136672682136&hvadid=595899011230&hvdev=c&hvlocphy=9040183&hvnetw=g&hvqmt=e&hvrand=4080644923417940523&hvtargid=kwd-799749580504&hydadcr=23637_1876856&tag=googinhydr1-21&ref=pd_sl_65cvo5ea55_e']

    def parse(self, response):
        items =AmazonItem()

        items['title']  = response.css(".a-size-medium::text").extract()
        items['author'] = response.css(".a-color-secondary .a-size-base+ .a-size-base").css("::text").extract()
        items['rating'] = response.css(".aok-align-bottom::text").extract()
        items['typee']  = response.css(".a-spacing-mini.a-color-base .a-text-bold").css("::text").extract()
        items['price']  = response.css(".s-price-instructions-style .a-price-whole").css("::text").extract()

        yield items

        next_page = "https://www.amazon.in/s?k=amazon+store+book&page="+str(AmazonbooksSpider.page_number)+"&adgrpid=136672682136&hvadid=595899011230&hvdev=c&hvlocphy=9040183&hvnetw=g&hvqmt=e&hvrand=4080644923417940523&hvtargid=kwd-799749580504&hydadcr=23637_1876856&qid=1656705904&ref=sr_pg_"+str(AmazonbooksSpider.page_number)

        if AmazonbooksSpider.page_number <=20 :
            AmazonbooksSpider.page_number+=1
            yield response.follow(next_page, callback =self.parse)    

        
