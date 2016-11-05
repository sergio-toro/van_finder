# from django.shortcuts import render
from django.http import HttpResponse

import json

from finder.crawlers import VehiculosIndustrialesCrawler
from finder.models import Result


# Create your views here.
def index(request):
    parser = VehiculosIndustrialesCrawler()
    results = parser.get_results()
    for item in results:
        Result.objects.update_or_create(
            title=item['title'],
            fuel_type=item['fuel_type'],
            year=item['year'],
            km=item['km'],
            provider=item['provider'],
            identifier=item['identifier'],
            url=item['url'],
            photo_url=item['photo_url'],
            description=item['description'],
            allow_finance=item['allow_finance'],
        )

    return HttpResponse(
        "<pre>" +
        json.dumps(results, indent=4) +
        "</pre>"
    )
