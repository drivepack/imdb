# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']

    rules = (
        Rule(LinkExtractor(restrict_css='h3.lister-item-header a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_css="div[class='nav'] div[class='desc']>a"))
    )

    def parse_item(self, response):
        yield {
            'title': response.css('div.sc-80d4314-1.fbQftq > h1::text').get(), # Alt + Shift + down arrow to duplicate code line
            'year': response.css('div.sc-80d4314-1.fbQftq div > ul > li:nth-child(1) > span::text').get(),
            'duration': response.css('div.sc-80d4314-1.fbQftq > div > ul > li:nth-child(3)::text').getall(),
            'genre': response.css('.sc-16ede01-3.bYNgQ.ipc-chip.ipc-chip--on-baseAlt span::text').get(),
            'rating': response.css('div.sc-db8c1937-0.eGmDjE.sc-2a827f80-12.gOJseW div > div:nth-child(1) > a > div > div > div.sc-7ab21ed2-0.fAePGh > div.sc-7ab21ed2-2.kYEdvH > span.sc-7ab21ed2-1.jGRxWM::text').get(),
            'movie_url': response.url,

        }
