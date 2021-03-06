from bs4 import BeautifulSoup
from pprint import pprint

broken_html = '<ul class=country_or_district><li>Area<li>Population</ul>'
# parse the HTML
soup = BeautifulSoup(broken_html, 'html.parser')
fixed_html = soup.prettify()
pprint(fixed_html)