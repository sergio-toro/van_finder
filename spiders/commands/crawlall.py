from scrapy.commands import ScrapyCommand
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


class Command(ScrapyCommand):

    requires_project = True
    excludes = []

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def run(self, args, opts):
        settings = get_project_settings()
        crawler_process = CrawlerProcess(settings)

        for spider_name in crawler_process.spider_loader.list():
            if spider_name in self.excludes:
                continue
            spider_cls = crawler_process.spider_loader.load(spider_name)
            crawler_process.crawl(spider_cls)
        crawler_process.start()
