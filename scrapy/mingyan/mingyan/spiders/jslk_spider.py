# -*- coding: utf-8 -*-
import scrapy

class jslk(scrapy.Spider):
    name = 'jslk1'

    def start_request(self):
        urls = ['http://www.linkwebll.com']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        divs = response.css('.about-content')
        self.log('------------------------------------')
        for each in divs:
            link = each.css('.about-title::text').extract_first().strip()
            author = each.css('.about-inner p span:nth-child(3)::text').extract_first().strip()
            with open('jslk.txt', 'a') as f:
                f.write('链接： %s %s \n' % (link, author))