import scrapy
from ..items import ScrapyImdbItem

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):
      items = ScrapyImdbItem()
      columns=response.css('table[data-caller-name="chart-top250movie"] tbody[class ="lister-list"] tr')
                       
      for col in columns:
            items["title"] =  col.css("td[class='titleColumn'] a::text").extract_first()
            items["year"]  =  col.css("td[class='titleColumn'] span::text").extract_first().strip('()')
            items["rating"]=  col.css("td[class='ratingColumn imdbRating'] strong::text").extract_first()

            yield items
            
                
                

            
 