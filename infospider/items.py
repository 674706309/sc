# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class viewItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()


class ipItem(scrapy.Item):
    type = scrapy.Field()
    url = scrapy.Field()
    port = scrapy.Field()
