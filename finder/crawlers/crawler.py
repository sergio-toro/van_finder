from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class Crawler:
    def fetch_content(self, url_to_fetch):
        user_headers = {
            'User-Agent': ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/35.0.1916.47 Safari/537.36"
                           )
        }
        req = Request(url_to_fetch, data=None, headers=user_headers)
        response = urlopen(req)
        html = response.read()
        return html
        # return BeautifulSoup(html, "html.parser")
