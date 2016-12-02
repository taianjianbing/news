# -*- coding: utf-8 -*-
import scrapy


class SohuSpider(scrapy.Spider):
    name = "sohu"
    allowed_domains = ["sohu.com"]
    start_urls = (
        'http://www.sohu.com/',
    )

    def parse(self, response):
        pass
