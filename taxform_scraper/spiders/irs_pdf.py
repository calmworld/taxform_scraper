# import scrapy
# from scrapy.http import Request

# class IrsPdfSpider(scrapy.Spider):
#     name = 'irs_pdf'
#     allowed_domains = ['apps.irs.gov']
#     start_urls = ['https://apps.irs.gov/app/picklist/list/priorFormPublication.html']

#     def parse_pdf(self, response):
#         return {
#             'file': response.xpath('//a[@href=".pdf"]/@href').get()
#         }
    
    # def save_pdf(self, response):
    #     path = response.url.split('/')[-1]
    #     self.logger.info('saving PDF %s', path)
    #     with open(path, 'wb') as f:
    #         f.write(response.body)

# ########################################################

import scrapy

class MySpider(scrapy.Spider):

    name = 'myspider'

    start_urls = [
          'https://apps.irs.gov/app/picklist/list/priorFormPublication.html',
    ]

    def parse(self, response):

        for link in response.css('.LeftCellSpacer').xpath('@href').extract():
             url = response.url
             path = response.css('td.LeftCellSpacer a::text').extract()
             next_link = response.urljoin(link)
             yield scrapy.Request(next_link, callback=self.parse_det, meta={'url': url, 'path': path})

    def parse_det(self, response):

        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'path':response.meta['path'],
            'file_urls': [extract_with_css('a::attr(href)')],
            'url':response.meta['url']
        }


from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # # save in file as CSV, JSON or XML
    # 'FEED_FORMAT': 'csv',     # csv, json, xml
    # 'FEED_URI': 'output.csv', # 

    # download files to `FILES_STORE/full`
    # it needs `yield {'file_urls': [url]}` in `parse()`
    'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
    'FILES_STORE': '.',
})
c.crawl(MySpider)
c.start()