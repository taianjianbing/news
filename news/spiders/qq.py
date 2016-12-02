# -*- coding: utf-8 -*-
import scrapy


class QqSpider(scrapy.Spider):
    name = "qq"
    allowed_domains = ["qq.com"]
    start_urls = (
        'http://www.qq.com/',
    )

    def parse(self, response):
        pass
