import requests
from bs4 import BeautifulSoup
import argparse


class GoogleSearchScraper:
    def __init__(self, headers=None):
        self.url = 'https://www.google.com/search?q='

        if not headers:
            self.headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/116.0.0.0 Safari/537.36'
            }
        else:
            self.headers = headers

    def get_results(self, query: str, k: int):
        r = requests.get(self.url + query, headers=self.headers)
        assert r.status_code == 200

        soup = BeautifulSoup(r.text, 'html.parser')
        results = set()

        for a in soup.find('div', id='search').find_all('a'):
            try:
                href = a['href']
                assert isinstance(href, str)

                if href.startswith('http') and 'www.google.com' not in href:
                    if len(results) < k:
                        results.add(href.strip())
                    else:
                        return list(results)
            except Exception as e:
                print(f"[ERROR] {e}")
                continue

        if len(results) > 0:
            return list(results)

        return None


def main():
    parser = argparse.ArgumentParser(description="Google Search Scraper")
    parser.add_argument("query", type=str, help="The search query")
    parser.add_argument("-k", "--count", type=int, default=100, help="Number of search results to fetch")

    args = parser.parse_args()

    search = GoogleSearchScraper()
    search_results = search.get_results(query=args.query, k=args.count)

    if search_results:
        print(f"Top {args.count} Results: {search_results}")
    else:
        print("No results found.")


if __name__ == '__main__':
    main()
