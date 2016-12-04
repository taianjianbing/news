# -*- coding: utf-8 -*-
import scrapy
from news.items import NewsItem

class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["sina.com.cn"]
    start_urls = (
        'http://tech.sina.com.cn/',
    )

    def parse(self, response):
        item = NewsItem()
        item['title'] = response.xpath('//div[contains(@class,"news-item")]/h2/a/text()').extract()
        item['link'] = response.xpath('//div[contains(@class,"news-item")]/h2/a/@href').extract()
        return item