import re
import scrapy
from infospider.items import viewItem


class viewSpider(scrapy.Spider):
    name = "viewspider"
    start_urls = ["http://www.view.sdu.edu.cn"]

    def parse(self, response):
        item = viewItem()
        re_tag = re.compile(r'<[^>]+>')
        re_line = re.compile(r'\t|\n|\r')
        title = response.xpath('//div[@class="news_tit"]/h3').extract_first()
        content = response.xpath('//div[@class="news_content"]').extract_first()
        item['url'] = response.url
        if title is not None and content is not None:
            item['title'] = re_tag.sub('', re_line.sub('', title))
            item['content'] = re_tag.sub('', re_line.sub('', content))
            yield item

        next_urls = response.xpath('//a/@href').extract()
        for next_url in next_urls:
            url = response.urljoin(next_url)
            if next_url is not None and re.search('http://www.view.sdu.edu.cn/[0-9A-Za-z]*', url):
                yield scrapy.Request(url, callback=self.parse)
