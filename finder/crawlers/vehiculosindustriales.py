from .crawler import Crawler


class VehiculosIndustrialesCrawler(Crawler):
    def __init__(self):
        self.results = []
        self.base_url = "http://vehiculosindustriales.coches.net"

    def get_results(self):
        content = self.get_content()
        if not content:
            return None

        # Process first page
        self.process_results(content)

        # Determine last page based on first page content
        max_page = self.get_max_page(content)

        # Get the rest of the pages
        for page in range(2, max_page):
            content = self.get_content(page)
            if content:
                self.process_results(content)

        return self.results

    def process_results(self, content):
        for link in content.select_one("#gridRows").find_all('a'):
            self.results.append(self.get_result(link))

    def get_max_page(self, content):
        pagination = content.select_one("#more_pages")
        max_page = 1
        for page_item in pagination.find_all('a'):
            page = page_item.get_text()
            if page and int(page) > max_page:
                max_page = int(page)
        return max_page

    def get_result(self, item):
        url = item.get('href')
        price_item = item.select_one(".precio").get_text()
        price = super().re_findone(r"([0-9\. €]+)", price_item)
        photo = item.select_one('.xfoto .p')

        if photo:
            photo = super().re_findone(r"\('(.+)'\)", photo.get('style'))

        return {
            "provider": "vehiculosindustriales",
            "identifier": super().re_findone(r"-(\d+)\.htm", url),
            "title": item.get('title'),
            "photo_url": (self.base_url + photo) if photo else None,
            "province": item.select_one(".provincia").get_text(),
            "fuel_type": item.select_one(".combustible").get_text(),
            "km": item.select_one(".km").get_text(),
            "year": item.select_one(".anio").get_text(),
            "price": price,
            "description": '',
            "allow_finance": bool(item.select_one(".precio .finan_grid")),
            "url": url,
        }

    def get_content(self, page=1):
        url_to_fetch = self.base_url + ("/furgonetas-segunda-mano/fiat/ducato?pg=%d" % page)
        return super().fetch_content(url_to_fetch)
