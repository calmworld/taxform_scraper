
import scrapy
from taxform_scraper.items import MyPdf

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