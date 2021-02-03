# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Form(scrapy.Item):
    # define the fields for your item here like:
    form_number = scrapy.Field()
    form_title = scrapy.Field()
    min_year = scrapy.Field()
    max_year = scrapy.Field()
