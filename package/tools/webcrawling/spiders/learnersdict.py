# -*- coding: utf-8 -*-
import scrapy


class LearnersdictSpider(scrapy.Spider):
    name = 'learnersdict'
    allowed_domains = ['www.learnersdictionary.com']
    start_urls = ['https://learnersdictionary.com/3000-words/alpha/a']

    def parse(self, response):
        items = response.xpath('//*[contains(@class,"words")]/li/a/text()').extract()

        for item in items:
            word = item.strip()

            if len(word) > 0:
                word = word.split(' ', 1)[0]
                yield {"word": word}
            

