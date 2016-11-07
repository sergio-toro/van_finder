from django.http import HttpResponse

import json
from finder.crawlers import VehiculosIndustrialesCrawler, VibboCrawler
from finder.libraries import save_results


def create(request):
    # crawler = VehiculosIndustrialesCrawler()
    # results = crawler.get_results()
    # save_results(results)

    crawler = VibboCrawler()
    results = crawler.get_content()
    # results = crawler.get_results()
    # save_results(results)

    return HttpResponse(results)
    # return HttpResponse(
    #     "<pre>" +
    #     json.dumps(results, indent=4) +
    #     "</pre>"
    # )
