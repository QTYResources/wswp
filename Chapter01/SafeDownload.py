'''
    由于 Python 3.x 已经整合 urllib 和 urllib2 到了 urllib3 模块，因此需要使用下面命令安装 urllib3:
    $ pip3 install urllib3
'''
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url):
    print(f'Downloading: {url}')
    try:
        html = urllib.request.urlopen(url).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error: ', e.reason)
        html = None
    return html

html = download("http://www.baidu.com")
print(html)