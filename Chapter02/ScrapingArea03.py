import re
import requests
from lxml.html import fromstring, tostring

def download(url, user_agent='wswp', num_retries=2, proxies=None):
    print('Downloading: ', url)
    headers = {'User-Agent': user_agent}
    try:
        resp = requests.get(url, headers=headers, proxies=proxies)
        html = resp.text
        if resp.status_code >= 400:
            print('Download error:', resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)
    except requests.exceptions.RequestException as e:
        print('Download error: ', e.reason)
        html = None
    return html

url = 'http://example.python-scraping.com/places/default/view/Albania-3'
html = download(url)
tree = fromstring(html)
td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
area = td.text_content()
print(area)
