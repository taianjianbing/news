# -*- coding: utf-8 -*-
import scrapy
from news.items import NewsItem

class WySpider(scrapy.Spider):
    name = "wy"
    allowed_domains = ["163.com"]
    start_urls = (
        'http://tech.163.com/',
    )

    def parse(self, response):
        item = NewsItem()
        titledata = response.xpath('//li[@class="list_item"]/a[@class="nl_detail"]/p[descendant-or-self::text()]')
        item['title'] = titledata.xpath('string(.)').extract()
        item['link'] = response.xpath('//li[@class="list_item"]/a/@href').extract()

        return item
