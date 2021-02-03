import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from taxform_scraper.items import Form

class IrsSpider(CrawlSpider):
    name = 'irs'
    allowed_domains = ['apps.irs.gov']
    start_urls = [
        'https://apps.irs.gov/app/picklist/list/priorFormPublication.html'
        ]

    rules = [
        Rule(
            LinkExtractor(allow=r'\/[a-zA-Z0-9_]'), 
            callback='parse_info', 
            follow=True
        )
    ]
    def parse_info(self, response):
        form = Form()
        form['form_number']= response.xpath('normalize-space(//td[@class="LeftCellSpacer"])').get()
        form['form_title']= response.xpath('normalize-space(//td[@class="MiddleCellSpacer"]/text())').get()
        form['min_year']= response.xpath('normalize-space(//td[@class="EndCellSpacer"])').get()
        form['max_year']= response.xpath('normalize-space(//td[@class="EndCellSpacer"])').get()
        return form
