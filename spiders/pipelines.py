# -*- coding: utf-8 -*-

from re import compile, IGNORECASE
from finder.models import Result
# from spiders.items import ResultItem
from spiders.settings import SAVE_RESULT
from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ResultPipeline(object):
    def process_item(self, item, spider):
        check = compile(r'(fiat).*(ducato)', IGNORECASE)
        match = check.match(item['title'])

        if not match:
            raise DropItem("Result is not a fiat ducato '%s' => '%s'" % (item['title'], item['url']))

        if not item['price']:
            raise DropItem("Result does not have price '%s' => '%s'" % (item['title'], item['url']))

        try:
            self.save_item(item)
        except Exception as e:
            # raise DropItem("Unexpected error saving item '%s' => '%s'" % (item['title'], item['url']))
            raise DropItem("Unexpected error saving item '%s'" % e)

        return item

    def save_item(self, item):
        not_null_fields = ['province', 'description', 'fuel_type', 'year', 'km']
        for key in not_null_fields:
            item[key] = item[key] if item[key] is not None else ''

        try:
            # Update already-created result
            result = Result.objects.get(provider=item['provider'], identifier=item['identifier'])
            result.url = item['url']
            result.province = item['province']
            result.photo_url = item['photo_url']
            result.description = item['description']
            result.allow_finance = item['allow_finance']
            result.fuel_type = item['fuel_type']
            result.year = item['year']
            result.km = item['km']
            result.title = item['title']
            result.price = item['price']
            if SAVE_RESULT:
                result.save()
        except Result.DoesNotExist:
            if SAVE_RESULT:
                item.save()
