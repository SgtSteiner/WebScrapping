import re
import requests
from bs4 import BeautifulSoup


def download(url, user_agent="wswp", num_retries=2, proxies=None):
    print("Downloading:", url)
    headers = {"User-Agent": user_agent}
    try:
        resp = requests.get(url, headers=headers, proxies=proxies)
        html = resp.text
        if resp.status_code >= 400:
            print("Download error:", resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                return download(url, num_retries=num_retries - 1)
    except requests.exceptions.RequestException as e:
        print("Download error:", e)
        html = None
    return html


def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall("<loc>(.*?)</loc>", sitemap)
    for link in links:
        soup = BeautifulSoup(download(link), "lxml")
        for lk in soup.find_all('a'):
            print(lk.get('href'))


crawl_sitemap('https://www.panel.es/page-sitemap.xml')



