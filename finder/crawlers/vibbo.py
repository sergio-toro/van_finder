from re import findall, search, IGNORECASE
from .crawler import Crawler


class VibboCrawler(Crawler):
    def __init__(self):
        self.results = []
        self.base_url = "http://www.vibbo.com"

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
        for item in content.select_one("#list_ads_table_container").find_all('.list_ads_row'):
            result = self.get_result(item)
            matches = search(r'fiat.+ducato', result.title, IGNORECASE)
            if matches:
                self.results.append(result)

    def get_max_page(self, content):
        last_link = content.select_one(".center-pagination .result_container_right a")
        max_page = findall(r'&o=(\d+)$', last_link.get('href'))[0]

        return int(max_page)

    def get_result(self, item):
        url = item.select_one('a.subjectTitle').get('title')
        price_item = item.select_one(".subjectPrice").get_text()
        price = findall(r"([0-9\.]+)", price_item)[0]

        attributes = item.select_one("p.show_attributes").get_text()
        km = findall(r'([\d\.]+ - [\d\.]+)', attributes)[0]
        year = findall(r'año ([\d]+)', attributes)[0]

        return {
            "provider": "vibbo",
            "identifier": item.get('id'),
            "title": item.select_one('a.subjectTitle').get('title'),
            "photo_url": item.select_one('img.lazy').get('src'),
            "province": item.select_one(".zone").get_text(),
            "fuel_type": None,
            "km": km,
            "year": year,
            "price": int(price.replace('.', '')),
            "description": '',
            "allow_finance": None,
            "url": self.base_url + url,
        }

    def get_content(self, page=1):
        url_to_fetch = self.base_url + ("/motor-de-segunda-mano-toda-espana-profesionales/fiat-ducato.htm?o=%d" % page)
        return super().fetch_content(url_to_fetch)
