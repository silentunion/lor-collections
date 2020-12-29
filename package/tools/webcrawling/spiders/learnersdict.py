# -*- coding: utf-8 -*-
import scrapy


class LearnersdictSpider(scrapy.Spider):
    name = 'learnersdict'
    allowed_domains = ['learnersdictionary.com']
    start_urls = ['https://learnersdictionary.com/3000-words/alpha/a']

    

    def parse(self, response):
        urls = self.get_other_pages(response)
        for u in urls:
            absolute_next_page_url = response.urljoin(u)
            yield scrapy.Request(url=absolute_next_page_url, callback=self.parse_items)

    def parse_items(self, response):
        items = response.xpath('//*[contains(@class,"words")]/li/a/text()').extract()

        for item in items:
            word = item.strip()

            if len(word) > 0:
                word = word.split(' ', 1)[0]
                with open('words.txt', 'a') as f:
                    f.write(word + "\n")

        next_page = response.xpath('//a[@class="button next"]/@href').get()
        print('next_page: ', next_page)
        if next_page:
            absolute_next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=absolute_next_page_url, callback=self.parse_items)


    def get_other_pages(self, response):        
        urls = response.xpath('//*[contains(@class,"selected")]/a/@href').extract()
        return urls

