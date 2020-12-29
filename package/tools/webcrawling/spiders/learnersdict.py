# -*- coding: utf-8 -*-
import scrapy


class LearnersdictSpider(scrapy.Spider):
    name = 'learnersdict'
    allowed_domains = ['learnersdictionary.com']
    start_urls = ['http://learnersdictionary.com/']

    def parse(self, response):
        pass
