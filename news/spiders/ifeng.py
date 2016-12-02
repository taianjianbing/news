# -*- coding: utf-8 -*-
import scrapy


class IfengSpider(scrapy.Spider):
    name = "ifeng"
    allowed_domains = ["ifeng.com"]
    start_urls = (
        'http://www.ifeng.com/',
    )

    def parse(self, response):
        pass
