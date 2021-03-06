import re
import itertools
from lxml.html import fromstring
import urllib.request
from urllib import robotparser
from urllib.parse import urljoin
from urllib.error import URLError, HTTPError, ContentTooShortError
from CsvCallback import CsvCallback

def download(url, user_agent='wswp', num_retries=2, charset='utf-8'):
    print('Downloading: ', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error: ', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)
    return html

def link_crawler(start_url, link_regex, robtos_url=None, user_agent='wswp', max_depth=4, scrape_callback=None):
    """
    Crawl from the given start URL following links matched by link_regex
    """
    crawl_queue = [start_url]
    # keep track which URL's have seen before
    seen = {}
    data = []
    if not robtos_url:
        robtos_url = '{}/robots.txt'.format(start_url)
    rp = get_robots_parser(robtos_url)
    while crawl_queue:
        url = crawl_queue.pop()
        # check url passes robots.txt restrictions
        if rp.can_fetch(user_agent, url):
            depth = seen.get(url, 0)
            if depth == max_depth:
                print('Skipping %s due to depth' %url)
                continue
            html = download(url, user_agent=user_agent)
            if not html:
                continue
            if scrape_callback:
                data.extend(scrape_callback(url, html) or [])
            # filter for links matching our regular expression
            for link in get_links(html):
                # check if link matches expected regex
                if re.match(link_regex, link):
                    abs_link = urljoin(start_url, link)
                    # check if have already seen this link
                    if abs_link not in seen:
                        seen[abs_link] = depth + 1
                        print("link: ", abs_link)
                        crawl_queue.append(abs_link)
        else:
            print('Blocked by robots.txt: ', url)

def get_links(html):
    """
    Return a list of links from html
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']""", re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

def get_robots_parser(robots_url):
    " Return the robots parser object using the robots_url "
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp

def scrape_callback(url, html):
    fields = ('area', 'population', 'iso', 'country_or_district', 'capital',
    'continent', 'tld', 'currency_code', 'currency_name',
    'phone', 'postal_code_format', 'postal_code_regex',
    'languages', 'neighbours')
    if re.search('/view/', url):
        tree = fromstring(html)
        all_rows = [
            tree.xpath('//tr[@id="places_%s__row"]/td[@class="w2p_fw"]' % field)[0].text_content()
            for field in fields
        ]
        print(url, all_rows)

link_crawler('http://example.python-scraping.com', '/places/default/(index|view)/', max_depth=2, scrape_callback=CsvCallback())