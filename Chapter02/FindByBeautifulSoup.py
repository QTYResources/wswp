from bs4 import BeautifulSoup
from pprint import pprint

broken_html = '<ul class=country_or_district><li>Area<li>Population</ul>'
# parse the HTML
soup = BeautifulSoup(broken_html, 'html5lib')
fixed_html = soup.prettify()
ul = soup.find('ul', attrs={'class': 'country_or_district'})
result = ul.find('li') # returns just the first match
pprint(result)
result = ul.find_all('li')  # returns all matches
pprint(result)