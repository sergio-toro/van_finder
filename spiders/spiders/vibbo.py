# -*- coding: utf-8 -*-
import scrapy

from spiders.items import ResultItem


BASE_URL = 'http://www.vibbo.com/fiat-ducato-de-segunda-mano-toda-espana/'
# BASE_URL = 'http://www.vibbo.com/motor-de-segunda-mano-toda-espana-profesionales/fiat-ducato.htm'


class VibboSpider(scrapy.Spider):
    name = "vibbo"
    start_urls = [
        BASE_URL
    ]

    def parse(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        # from scrapy.utils.response import open_in_browser
        # open_in_browser(response)

        for result in response.css("#hl .list_ads_row"):
            yield self.get_result(result)

        next_page = response.css(".paginationNextLink::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)

    def get_result(self, result):
        price = result.css(".subjectPrice::text").re_first(r"([0-9\.]+)")

        def get_text(css_selector):
            return result.css(css_selector + ' ::text').extract_first().strip()

        result = ResultItem(
            provider="vibbo",
            identifier=result.css('::attr(id)').extract_first(),
            title=result.css('a.subjectTitle::attr(title)').extract_first().strip(),
            photo_url=result.css('img.lazy::attr(title)').extract_first(),
            province=get_text(".zone a"),
            fuel_type='',
            km=result.css(".infoBottom").re_first(r'([\d\.]+ - [\d\.]+)'),
            year=result.css(".infoBottom").re_first(r'span> (\d+)'),
            price=int(price.replace('.', '')) if price else None,
            description='',
            allow_finance=None,
            url=result.css('::attr(href)').extract_first(),
        )

        return result
