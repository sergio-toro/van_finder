import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Crawler:
    def fetch_content(self, url_to_fetch):
        response = urlopen(url_to_fetch)
        html = response.read()
        return BeautifulSoup(html, "html.parser")

    def re_findone(self, regex, string_to_test):
        return re.findall(regex, string_to_test)[0]
