from urllib import robotparser

rp = robotparser.RobotFileParser()
rp.set_url('http://example.python-scraping.com/robots.txt')
rp.read()
url = 'http://example.python-scraping.com'
user_agent = 'BadCrawler'
result = rp.can_fetch(user_agent, url)
print('BadCrawler fetch: ', result)
user_agent = 'GoodCrawler'
result = rp.can_fetch(user_agent, url)
print('GoodCrawler fetch: ', result)