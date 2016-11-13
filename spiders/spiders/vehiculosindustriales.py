# -*- coding: utf-8 -*-
import scrapy

from spiders.items import ResultItem

# from scrapy.shell import inspect_response
# from scrapy.utils.response import open_in_browser

BASE_URL = 'http://vehiculosindustriales.coches.net'
SEARCH_URL = '/furgonetas-segunda-mano/fiat/ducato'


class VehiculosindustrialesSpider(scrapy.Spider):
    name = "vehiculosindustriales"
    start_urls = [
        BASE_URL + SEARCH_URL
    ]

    def parse(self, response):

        # inspect_response(response, self)
        # open_in_browser(response)

        for result in response.css("#gridRows a"):
            yield self.get_result(result)

        current_page = int(response.css('#more_pages span::text').extract_first())
        next_page = current_page + 1
        max_page = 1
        for link in response.css('#more_pages a'):
            page = link.css('::text').extract_first()
            if page and int(page) > max_page:
                max_page = int(page)

        if next_page <= max_page:
            next_page_url = BASE_URL + SEARCH_URL + "?pg=%d" % next_page
            yield scrapy.Request(next_page_url, callback=self.parse)

    def get_result(self, result):
        price = result.css(".precio").re_first(r"([0-9\.]+)")

        def get_text(css_selector):
            return result.css(css_selector + ' ::text').extract_first()

        result = ResultItem(
            provider="vehiculosindustriales",
            identifier=result.css('::attr(href)').re_first(r"-(\d+)\.htm"),
            title=result.css('::attr(title)').extract_first(),
            photo_url=result.css('.xfoto .p::attr(style)').re_first(r"\('(.+)\/.+\/'\)"),
            province=get_text(".provincia"),
            fuel_type=get_text(".combustible"),
            km=get_text(".km"),
            year=get_text(".anio"),
            price=int(price.replace('.', '')),
            description='',
            allow_finance=bool(result.css(".precio .finan_grid")),
            url=BASE_URL + result.css('::attr(href)').extract_first(),
        )

        return result
