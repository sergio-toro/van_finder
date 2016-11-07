from finder.models import Result


def save_results(results):
    for item in results:
        try:
            result = Result.objects.get(provider=item['provider'], identifier=item['identifier'])
        except Result.DoesNotExist:
            result = Result(
                provider=item['provider'],
                identifier=item['identifier'],
            )
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
        result.save()
