import re
import scrapy
from infospider.items import ipItem

class viewSpider(scrapy.Spider):
    name = "ipspider"
    start_urls = ["http://www.xicidaili.com/nt/"]

    def parse(self, response):
        pass