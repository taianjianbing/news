# -*- coding: utf-8 -*-
import scrapy


class HuanqiuSpider(scrapy.Spider):
    name = "huanqiu"
    allowed_domains = ["huanqiu.com"]
    start_urls = (
        'http://www.huanqiu.com/',
    )

    def parse(self, response):
        pass
