# -*- coding: utf-8 -*-
# @Time : 2021/2/19 17:39
# @Author : Stanton
# @File : ershoufangScrappy/IpSpider.py
import scrapy


class Spider(scrapy.Spider):
    name = 'ip'
    allowed_domains = []

    def start_requests(self):

        url = 'http://ip.chinaz.com/getip.aspx'

        for i in range(4):
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self,response):
        print(response.text)
