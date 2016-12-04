# -*- coding: utf-8 -*-
import scrapy
from news.items import NewsItem

class QqSpider(scrapy.Spider):
    name = "qq"
    allowed_domains = ["qq.com"]
    start_urls = (
        'http://tech.qq.com/',
    )

    def parse(self, response):
        item = NewsItem()
        item['title'] = response.xpath('//h3[@class="f18 l26"]/a/text()').extract()
        item['link'] = response.xpath('//h3[@class="f18 l26"]/a/@href').extract()
        return item

