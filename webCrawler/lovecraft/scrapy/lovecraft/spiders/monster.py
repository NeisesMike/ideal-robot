# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector

class MonsterSpider(CrawlSpider):
    name = 'monster'
    allowed_domains = ['hplovecraft.com']
    start_urls = ['http://hplovecraft.com/writings/texts/fiction/a.aspx',
                  'http://hplovecraft.com/writings/texts'
    ]

    storyRule = '/html/body/font/center/div/table/tbody/tr/td/font/div/ul/ul/li'

    rules = (
        Rule(
            LinkExtractor(
                allow=r'^https?://hplovecraft.com/writings/texts/.*',
            ),
            callback="parse_item",
            follow=True
        ),
    )
    
    def parse_item(self, response):
        print('Processing..' + response.url)

    def parse(self, response):
        print('Standard Parse Processing..' + response.url)
        interlinks = response.xpath('//div/ul/ul/li/a/@href')
        final = interlinks.extract()
        print(final)
        pass

