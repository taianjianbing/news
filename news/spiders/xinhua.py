# -*- coding: utf-8 -*-
import scrapy


class XinhuaSpider(scrapy.Spider):
    name = "xinhua"
    allowed_domains = ["news.cn"]
    start_urls = (
        'http://www.news.cn/',
    )

    def parse(self, response):
        pass
