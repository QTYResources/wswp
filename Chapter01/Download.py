'''
    由于 Python 3.x 已经整合 urllib 和 urllib2 到了 urllib3 模块，因此需要使用下面命令安装 urllib3:
    $ pip3 install urllib3
'''
import urllib.request

def download(url):
    return urllib.request.urlopen(url).read()

result = download('http://www.baidu.com')
print(result)