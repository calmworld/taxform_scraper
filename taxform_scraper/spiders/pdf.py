# import scrapy

# class PdfSpider(scrapy.Spider):
#     name = 'pdfSpider'
#     start_urls = [
#           'https://apps.irs.gov/app/picklist/list/priorFormPublication.html',
#     ]

#     def parse(self, response):
#         for link in response.css('.LeftCellSpacer').xpath('@href').extract():
#             url = response.url
#             path = response.css('a::text').extract()
#             next_link = response.urljoin(link)
#             yield scrapy.Request(next_link, callback=self.parse_det, meta={'url': url, 'path': path})

#     def parse_det(self, response):

#         def extract_with_css(query):
#             return response.css(query).get(default='').strip()

#         yield {
#             'path':response.meta['path'],
#             'file_urls': [extract_with_css('a::attr(href)')],
#             'url':response.meta['url']
#         }


# from scrapy.crawler import CrawlerProcess

# c = CrawlerProcess({
#     'USER_AGENT': 'Mozilla/5.0',

#     # download files to `FILES_STORE/full`
#     # it needs `yield {'file_urls': [url]}` in `parse()`
#     'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
#     'FILES_STORE': '.',
# })
# c.crawl(PdfSpider)


import scrapy

class PdfSpider(scrapy.Spider):
    name = 'pdfSpider'
    start_urls = [
          'https://apps.irs.gov/app/picklist/list/priorFormPublication.html',
    ]

    def parse(self, response):
        url = response.url
        for link in response.css('table.picklist-dataTable'):
            links = link.css('td.LeftCellSpacer > a::attr("href")').extract()
            for pdfurl in links:
                yield scrapy.Request(pdfurl, callback=self.download_pdf, meta={'url': url, 'path': pdfurl})

    def download_pdf(self, response):
        print(response.url)
        path = response.url.split('/')[-1]
        self.logger.info('Saving PDF %s', path)
        with open(path, 'wb') as f:
            f.write(response.body)