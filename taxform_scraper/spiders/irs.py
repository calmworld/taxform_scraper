import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# from taxform_scraper.items import taxform

class IrsSpider(CrawlSpider):
    name = 'irs'
    allowed_domains = ['apps.irs.gov']
    start_urls = [
        'https://apps.irs.gov/app/picklist/list/priorFormPublication.html'
        ]

    rules = [
        Rule(
            LinkExtractor(allow=r'\/[-A-Z0-9+&@#\/%=~_|$?!:,.]'), 
            callback='parse_info', 
            follow=True
        )
    ]
    def parse_info(self, response):
        return {
            'form_number': response.xpath('//option[@value="formNumber"]/text()').get(),
            'form_title': response.xpath('//option[@value="title"]/text()').get(),
            'min_year': response.xpath('//option[@value="currentYearRevDateString"]/text()').get(),
            'max_year': response.xpath('//option[@value="currentYearRevDateString"]/text()').get()
        }
        
